# 🔑 GCP Secret Manager Access Summary

## 🚨 Current Authentication Status

**Service Account**: `84719228704-compute@developer.gserviceaccount.com`
**Issue**: Insufficient scopes for Secret Manager access
**Projects Tried**: 
- ✅ `alanblount-sandbox` (accessible but scope limited)
- ✅ `alanblount-demo` (accessible but scope limited)

## 🎯 Commands to Run When You Have Proper Access

### Step 1: Authenticate with proper permissions
```bash
# Option A: Your user account
gcloud auth login

# Option B: Service account with broader scopes
gcloud auth activate-service-account --key-file=path/to/service-account.json
```

### Step 2: Find Cloudflare secrets
```bash
# Check both projects for Cloudflare-related secrets
gcloud secrets list --project=alanblount-sandbox | grep -i cloudflare
gcloud secrets list --project=alanblount-demo | grep -i cloudflare

# Alternative patterns to search
gcloud secrets list --project=alanblount-sandbox | grep -iE "(cf|api|token)"
gcloud secrets list --project=alanblount-demo | grep -iE "(cf|api|token)"

# List all secrets to see naming patterns
gcloud secrets list --project=alanblount-sandbox --format="table(name,createTime)"
gcloud secrets list --project=alanblount-demo --format="table(name,createTime)"
```

### Step 3: Retrieve and use the token
```bash
# Get the secret value (replace SECRET_NAME)
CF_API_TOKEN=$(gcloud secrets versions access latest --secret=SECRET_NAME --project=PROJECT_NAME)

# Run automated setup
cd /home/node/production-migration
export CF_API_TOKEN
./scripts/setup_cloudflare_redirects.sh
```

## 📋 Expected Secret Names

Based on common naming conventions, look for:
- `cloudflare-api-token`
- `cf-api-key`
- `cloudflare-token`
- `cf-api-token`
- `cloudflare-dns-token`

## 🚀 Automated Script Ready

Once you have the token, all scripts are ready:
- **`get_cf_token_and_setup.sh`** - Full automation if you have Secret Manager access
- **`setup_cloudflare_redirects.sh`** - Configure redirects with API token
- **`verify_legacy_urls.sh`** - Test all redirects work

## ⚡ Alternative: Manual Configuration

If secret access is complex, the manual Cloudflare dashboard method in `URGENT_REDIRECT_SETUP.md` takes just 5 minutes and requires no API tokens.

---

**The production site is live and perfect - just need the `code.zeroasterisk.com` redirects!**