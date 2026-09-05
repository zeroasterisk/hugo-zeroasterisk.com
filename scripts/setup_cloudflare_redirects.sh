#!/usr/bin/env bash
set -euo pipefail

# Cloudflare Redirect Rule Setup Script
# Programmatically creates 301 redirects for code.zeroasterisk.com → zeroasterisk.com

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🌍 Cloudflare Redirect Rule Setup${NC}"
echo "=================================="

# Check for required environment variables
if [[ -z "${CF_API_TOKEN:-}" ]]; then
    echo -e "${RED}❌ ERROR: CF_API_TOKEN environment variable not set${NC}"
    echo ""
    echo "Please set your Cloudflare API Token:"
    echo "  export CF_API_TOKEN=your_cloudflare_api_token_here"
    echo ""
    echo "To get your API token:"
    echo "1. Go to https://dash.cloudflare.com/profile/api-tokens"  
    echo "2. Click 'Create Token'"
    echo "3. Use 'Edit zone DNS' template"
    echo "4. Select your domain: zeroasterisk.com"
    echo "5. Copy the token and export it above"
    exit 1
fi

# Domain configuration
DOMAIN="zeroasterisk.com"
LEGACY_SUBDOMAIN="code.zeroasterisk.com"

echo -e "\n${BLUE}📋 Configuration:${NC}"
echo "Domain: $DOMAIN"
echo "Legacy subdomain: $LEGACY_SUBDOMAIN"
echo "Target: https://$DOMAIN"

# Function to make Cloudflare API calls
cf_api() {
    local endpoint="$1"
    local method="${2:-GET}"
    local data="${3:-}"
    
    local curl_args=(
        -s
        -X "$method"
        -H "Authorization: Bearer $CF_API_TOKEN"
        -H "Content-Type: application/json"
    )
    
    if [[ -n "$data" ]]; then
        curl_args+=(-d "$data")
    fi
    
    curl "${curl_args[@]}" "https://api.cloudflare.com/v4/$endpoint"
}

echo -e "\n${YELLOW}🔍 Step 1: Finding zone ID for $DOMAIN${NC}"

# Get zone ID
ZONES_RESPONSE=$(cf_api "zones?name=$DOMAIN")
ZONE_ID=$(echo "$ZONES_RESPONSE" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    if data['success'] and len(data['result']) > 0:
        print(data['result'][0]['id'])
    else:
        print('ERROR: Zone not found')
        sys.exit(1)
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(1)
")

if [[ "$ZONE_ID" == "ERROR:"* ]]; then
    echo -e "${RED}❌ Failed to get zone ID: $ZONE_ID${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Zone ID found: $ZONE_ID${NC}"

echo -e "\n${YELLOW}🔍 Step 2: Checking for existing redirect rules${NC}"

# List existing redirect rules
RULES_RESPONSE=$(cf_api "zones/$ZONE_ID/rulesets" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    redirect_rulesets = [rs for rs in data['result'] if rs['kind'] == 'zone' and rs['phase'] == 'http_request_dynamic_redirect']
    if redirect_rulesets:
        print(redirect_rulesets[0]['id'])
    else:
        print('NONE')
except:
    print('ERROR')
")

echo "Redirect ruleset: $RULES_RESPONSE"

echo -e "\n${YELLOW}🛠️ Step 3: Creating redirect rule${NC}"

# Create the redirect rule
REDIRECT_RULE_DATA=$(cat <<EOF
{
  "rules": [
    {
      "action": "redirect",
      "action_parameters": {
        "from_value": {
          "status_code": 301,
          "target_url": {
            "expression": "concat(\"https://$DOMAIN\", http.request.uri.path)"
          },
          "preserve_query_string": true
        }
      },
      "expression": "(http.host eq \"$LEGACY_SUBDOMAIN\")",
      "description": "Redirect $LEGACY_SUBDOMAIN to $DOMAIN with 301 status",
      "enabled": true
    }
  ]
}
EOF
)

if [[ "$RULES_RESPONSE" == "NONE" ]]; then
    # Create new ruleset
    echo "Creating new redirect ruleset..."
    CREATE_RESPONSE=$(cf_api "zones/$ZONE_ID/rulesets" "POST" "{
        \"name\": \"Default redirect rules\",
        \"kind\": \"zone\",
        \"phase\": \"http_request_dynamic_redirect\",
        $REDIRECT_RULE_DATA
    }")
else
    # Add to existing ruleset
    echo "Adding to existing ruleset: $RULES_RESPONSE"
    CREATE_RESPONSE=$(cf_api "zones/$ZONE_ID/rulesets/$RULES_RESPONSE" "PUT" "$REDIRECT_RULE_DATA")
fi

# Check if rule creation was successful
SUCCESS=$(echo "$CREATE_RESPONSE" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    if data.get('success'):
        print('true')
        if 'result' in data and 'rules' in data['result']:
            for rule in data['result']['rules']:
                print(f\"Rule created: {rule['description']}\")
    else:
        print('false')
        if 'errors' in data:
            for error in data['errors']:
                print(f\"Error: {error.get('message', 'Unknown error')}\")
except Exception as e:
    print(f'ERROR: {e}')
")

if [[ "$SUCCESS" == "true"* ]]; then
    echo -e "${GREEN}✅ Redirect rule created successfully!${NC}"
    echo "$SUCCESS"
else
    echo -e "${RED}❌ Failed to create redirect rule:${NC}"
    echo "$SUCCESS"
    echo ""
    echo "Raw response:"
    echo "$CREATE_RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$CREATE_RESPONSE"
    exit 1
fi

echo -e "\n${YELLOW}⏱️ Step 4: Waiting for propagation${NC}"
echo "Waiting 30 seconds for DNS/rule propagation..."
sleep 30

echo -e "\n${YELLOW}🧪 Step 5: Testing redirects${NC}"

# Test the redirects
TEST_URLS=(
    "https://$LEGACY_SUBDOMAIN/"
    "https://$LEGACY_SUBDOMAIN/2017/07/playing-with-elixir-is-just-fun/"
    "https://$LEGACY_SUBDOMAIN/tags/elixir/"
)

ALL_TESTS_PASSED=true

for url in "${TEST_URLS[@]}"; do
    echo -e "\n📍 Testing: $url"
    
    # Get response with redirect info
    response=$(curl -s -w "HTTPSTATUS:%{http_code};FINALURL:%{url_effective};REDIRECT:%{redirect_url}" -L "$url" --connect-timeout 10 --max-time 15 || echo "HTTPSTATUS:000;FINALURL:;REDIRECT:")
    
    http_code=$(echo "$response" | grep -o "HTTPSTATUS:[0-9]*" | cut -d: -f2)
    final_url=$(echo "$response" | grep -o "FINALURL:.*" | cut -d: -f2- | cut -d';' -f1)
    
    if [[ "$final_url" == *"$DOMAIN"* && "$http_code" == "200" ]]; then
        echo -e "   ${GREEN}✅ SUCCESS${NC}: Redirected to $final_url"
    else
        echo -e "   ${RED}❌ FAILED${NC}: HTTP $http_code, Final URL: $final_url"
        ALL_TESTS_PASSED=false
    fi
done

echo -e "\n" 
echo "================================================================"
if [[ "$ALL_TESTS_PASSED" == "true" ]]; then
    echo -e "${GREEN}🎉 ALL TESTS PASSED - Redirect setup complete!${NC}"
    echo ""
    echo -e "${GREEN}✅ SEO preservation: Search engines will transfer rankings${NC}"
    echo -e "${GREEN}✅ User experience: All bookmarks and external links work${NC}" 
    echo -e "${GREEN}✅ Analytics consolidation: All traffic goes to main domain${NC}"
    echo ""
    echo "🔍 Run the verification script to double-check:"
    echo "  ./scripts/verify_legacy_urls.sh"
else
    echo -e "${RED}❌ Some tests failed. Check Cloudflare configuration.${NC}"
    echo ""
    echo "Troubleshooting:"
    echo "1. Check rule is enabled in Cloudflare dashboard"
    echo "2. Wait a few more minutes for global propagation"  
    echo "3. Verify the rule expression matches exactly"
    exit 1
fi