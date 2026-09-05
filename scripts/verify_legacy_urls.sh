#!/usr/bin/env bash
set -euo pipefail

echo "🔍 Legacy URL Verification Script"
echo "=================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0
MISSING_REDIRECTS=()

# Test function
test_url() {
    local url="$1"
    local expect_redirect="${2:-false}"
    local target_domain="${3:-}"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    echo -e "\n📍 Testing: ${BLUE}$url${NC}"
    
    # Get response with redirect chain
    local response=$(curl -s -w "HTTPSTATUS:%{http_code};REDIRECT:%{redirect_url};FINALURL:%{url_effective}" -L "$url" --connect-timeout 10 --max-time 15 || echo "HTTPSTATUS:000;REDIRECT:;FINALURL:")
    
    local http_code=$(echo "$response" | grep -o "HTTPSTATUS:[0-9]*" | cut -d: -f2)
    local final_url=$(echo "$response" | grep -o "FINALURL:.*" | cut -d: -f2-)
    
    if [[ "$http_code" == "000" ]]; then
        echo -e "   ${RED}❌ FAILED${NC}: Connection failed"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        return 1
    fi
    
    if [[ "$expect_redirect" == "true" ]]; then
        # Check if we got redirected to the target domain
        if [[ -n "$target_domain" && "$final_url" == *"$target_domain"* ]]; then
            echo -e "   ${GREEN}✅ REDIRECT${NC}: $http_code → $final_url"
            PASSED_TESTS=$((PASSED_TESTS + 1))
            return 0
        elif [[ "$final_url" != "$url" ]]; then
            echo -e "   ${GREEN}✅ REDIRECT${NC}: $http_code → $final_url"
            PASSED_TESTS=$((PASSED_TESTS + 1))
            return 0
        else
            echo -e "   ${RED}❌ NO REDIRECT${NC}: Expected redirect but got direct response"
            FAILED_TESTS=$((FAILED_TESTS + 1))
            MISSING_REDIRECTS+=("$url")
            return 1
        fi
    else
        # Direct response expected
        if [[ "$http_code" == "200" ]]; then
            echo -e "   ${GREEN}✅ SUCCESS${NC}: $http_code"
            PASSED_TESTS=$((PASSED_TESTS + 1))
            return 0
        else
            echo -e "   ${RED}❌ FAILED${NC}: Expected 200 but got $http_code"
            FAILED_TESTS=$((FAILED_TESTS + 1))
            return 1
        fi
    fi
}

echo -e "\n🌍 Testing main site URLs..."

# Test main site URLs (should work directly)
test_url "https://zeroasterisk.com/" false
test_url "https://zeroasterisk.com/posts/" false
test_url "https://zeroasterisk.com/personal/" false
test_url "https://zeroasterisk.com/pages/about/" false
test_url "https://zeroasterisk.com/search/" false
test_url "https://zeroasterisk.com/sitemap.xml" false

echo -e "\n🔄 Testing legacy code.zeroasterisk.com redirects..."

# Test legacy code.zeroasterisk.com URLs (should redirect to main site)
test_url "https://code.zeroasterisk.com/" true "zeroasterisk.com"
test_url "https://code.zeroasterisk.com/2017/09/2017-09-06-how-to-learn/" true "zeroasterisk.com"
test_url "https://code.zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/" true "zeroasterisk.com"
test_url "https://code.zeroasterisk.com/2017/06/meteor-and-elixir-part-one-a-rocky-courtship/" true "zeroasterisk.com"
test_url "https://code.zeroasterisk.com/2017/05/meteor-1.5-bundle-optimization-examples/" true "zeroasterisk.com"
test_url "https://code.zeroasterisk.com/tags/elixir/" true "zeroasterisk.com"
test_url "https://code.zeroasterisk.com/tags/meteor/" true "zeroasterisk.com"

echo -e "\n📊 Testing key migrated content URLs..."

# Test that the migrated content is accessible on main site
test_url "https://zeroasterisk.com/2017/09/2017-09-06-how-to-learn/" false
test_url "https://zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/" false
test_url "https://zeroasterisk.com/2017/06/meteor-and-elixir-part-one-a-rocky-courtship/" false
test_url "https://zeroasterisk.com/tags/elixir/" false
test_url "https://zeroasterisk.com/tags/meteor/" false
test_url "https://zeroasterisk.com/tags/2017/" false

echo -e "\n" 
echo "================================================================"
echo "📊 LEGACY URL VERIFICATION SUMMARY"
echo "================================================================"

SUCCESS_RATE=$(( PASSED_TESTS * 100 / TOTAL_TESTS ))

echo -e "📋 Total URLs Tested: ${TOTAL_TESTS}"
echo -e "✅ Successful: ${GREEN}${PASSED_TESTS}${NC}"
echo -e "❌ Failed: ${RED}${FAILED_TESTS}${NC}"
echo -e "📈 Success Rate: ${SUCCESS_RATE}%"

if [[ ${#MISSING_REDIRECTS[@]} -gt 0 ]]; then
    echo -e "\n🚨 URLs Missing Redirects:"
    for url in "${MISSING_REDIRECTS[@]}"; do
        echo -e "   ${RED}❌${NC} $url"
    done
    
    echo -e "\n🔧 REQUIRED CLOUDFLARE REDIRECT RULES"
    echo "======================================"
    echo -e "${YELLOW}Configure these in Cloudflare Dashboard → Rules → Redirect Rules:${NC}"
    echo ""
    echo "Rule Name: Redirect code.zeroasterisk.com to main site"
    echo "Expression: (http.host eq \"code.zeroasterisk.com\")"
    echo "Action: Dynamic redirect"
    echo "Expression: concat(\"https://zeroasterisk.com\", http.request.uri.path)"
    echo "Status code: 301"
    echo ""
    echo -e "${YELLOW}Alternative Page Rule (Legacy method):${NC}"
    echo "Pattern: code.zeroasterisk.com/*"
    echo "Setting: Forwarding URL → 301 Permanent Redirect"
    echo "Destination: https://zeroasterisk.com/\$1"
    
else
    echo -e "\n${GREEN}🎉 All legacy redirects are working correctly!${NC}"
fi

echo -e "\n📝 Next Steps:"
if [[ ${#MISSING_REDIRECTS[@]} -gt 0 ]]; then
    echo "1. Configure Cloudflare redirects as shown above"
    echo "2. Wait 2-3 minutes for DNS propagation"
    echo "3. Re-run this script to verify redirects"
    echo "4. Test a few URLs manually in browser"
    exit 1
else
    echo "✅ All URLs verified - legacy redirect setup is complete!"
    echo "✅ SEO preservation successful"
    echo "✅ User experience maintained for bookmarked URLs"
    exit 0
fi