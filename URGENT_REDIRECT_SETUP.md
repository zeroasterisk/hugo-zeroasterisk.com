# 🚨 IMMEDIATE ACTION: Configure code.zeroasterisk.com Redirects

## Option A: Automated Script (Recommended if you have API access)

1. **Get your Cloudflare API Token:**
   - Go to https://dash.cloudflare.com/profile/api-tokens
   - Click "Create Token" 
   - Use "Edit zone DNS" template or "Custom token"
   - Permissions: Zone.Zone:Read, Zone.DNS:Edit
   - Zone: Include → zeroasterisk.com

2. **Run the automated script:**
   ```bash
   cd /home/node/production-migration
   chmod +x scripts/setup_cloudflare_redirects.sh
   
   export CF_API_TOKEN=your_api_token_here
   ./scripts/setup_cloudflare_redirects.sh
   ```

## Option B: Manual Configuration (5 minutes)

### Via Cloudflare Dashboard:

1. **Go to:** https://dash.cloudflare.com
2. **Select:** zeroasterisk.com domain
3. **Navigate to:** Rules → Redirect Rules
4. **Click:** Create rule

**Rule Configuration:**
```
Rule name: Redirect code subdomain to main site

When incoming requests match:
- Field: Hostname
- Operator: equals  
- Value: code.zeroasterisk.com

Then:
- Type: Dynamic redirect
- Expression: concat("https://zeroasterisk.com", http.request.uri.path)
- Status code: 301 - Permanent Redirect
- Preserve query string: ✓ Enabled
```

5. **Click:** Deploy

### Expected Result:
- `https://code.zeroasterisk.com/` → `https://zeroasterisk.com/` (301)
- `https://code.zeroasterisk.com/any/path` → `https://zeroasterisk.com/any/path` (301)

## Test After Configuration (2-3 minutes for propagation):

```bash
curl -I https://code.zeroasterisk.com/
# Should show: HTTP/2 301 + Location: https://zeroasterisk.com/

curl -I https://code.zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/  
# Should show: HTTP/2 301 + Location: https://zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/
```

## Verify Success:
```bash
cd /home/node/production-migration
./scripts/verify_legacy_urls.sh
```

---

**⚠️ This is CRITICAL for SEO - configure now to prevent ranking loss!**