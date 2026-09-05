#!/usr/bin/env bash

# Script to retrieve Cloudflare API token from GCP Secret Manager and configure redirects
# Run this script with proper authentication to access secrets

echo "🔑 Retrieving Cloudflare API Token from GCP Secret Manager"
echo "======================================================="

# List all secrets and find Cloudflare-related ones
echo "🔍 Step 1: Finding Cloudflare secrets..."
gcloud secrets list --format="value(name)" | grep -i cloudflare

echo -e "\n📋 Available secrets (all):"
gcloud secrets list --format="table(name,createTime)" | head -20

echo -e "\n🎯 Looking for specific patterns..."
CLOUDFLARE_SECRET=$(gcloud secrets list --format="value(name)" | grep -iE "(cloudflare|cf-api|cf_api)")

if [[ -n "$CLOUDFLARE_SECRET" ]]; then
    echo "✅ Found Cloudflare secret: $CLOUDFLARE_SECRET"
    
    echo -e "\n🔐 Step 2: Retrieving secret value..."
    CF_API_TOKEN=$(gcloud secrets versions access latest --secret="$CLOUDFLARE_SECRET")
    
    if [[ -n "$CF_API_TOKEN" ]]; then
        echo "✅ API token retrieved successfully (${#CF_API_TOKEN} characters)"
        
        echo -e "\n🚀 Step 3: Configuring redirects..."
        export CF_API_TOKEN
        cd /home/node/production-migration
        ./scripts/setup_cloudflare_redirects.sh
    else
        echo "❌ Failed to retrieve API token"
        exit 1
    fi
else
    echo "❌ No Cloudflare secret found"
    echo ""
    echo "Please check these commands manually:"
    echo "  gcloud secrets list | grep -i cloudflare"
    echo "  gcloud secrets list | grep -i cf"
    echo "  gcloud secrets list | grep -i api"
    echo ""
    echo "Or use manual configuration: see URGENT_REDIRECT_SETUP.md"
fi