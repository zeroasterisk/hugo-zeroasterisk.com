# Legacy URL Redirect Setup - code.zeroasterisk.com → zeroasterisk.com

## 🎯 **CRITICAL ISSUE FOUND**

The verification shows that **code.zeroasterisk.com is NOT redirecting** to the main site. This means:
- **SEO Impact**: Search engine rankings for code.zeroasterisk.com content are lost
- **User Experience**: Bookmarks and external links to code.zeroasterisk.com return 404s
- **Content Duplication**: Two sites serving different versions of the same content

## 🚨 **IMMEDIATE ACTION REQUIRED: Configure Cloudflare Redirects**

### Option 1: Redirect Rules (Recommended)

**Go to:** Cloudflare Dashboard → Your Domain → Rules → Redirect Rules

**Click:** Create rule

**Rule Configuration:**
```
Rule name: Redirect code.zeroasterisk.com to main site
When incoming requests match: Custom filter expression
Expression: (http.host eq "code.zeroasterisk.com")

Then:
Type: Dynamic redirect  
Expression: concat("https://zeroasterisk.com", http.request.uri.path)
Status code: 301 - Permanent Redirect
Preserve query string: Yes
```

### Option 2: Page Rules (Legacy Method)

**Go to:** Cloudflare Dashboard → Your Domain → Rules → Page Rules

**Create Rule 1:**
```
Pattern: code.zeroasterisk.com/*
Setting: Forwarding URL
Status: 301 - Permanent Redirect  
Destination: https://zeroasterisk.com/$1
```

**Create Rule 2:**
```
Pattern: code.zeroasterisk.com  
Setting: Forwarding URL
Status: 301 - Permanent Redirect
Destination: https://zeroasterisk.com/
```

### Option 3: Bulk Redirects (For Many URLs)

**Go to:** Cloudflare Dashboard → Your Domain → Rules → Redirect Rules → Bulk Redirects

**Upload CSV with format:**
```
source_url,target_url,status
code.zeroasterisk.com,https://zeroasterisk.com/,301
code.zeroasterisk.com/*,https://zeroasterisk.com/$1,301
```

## 📋 **Post-Configuration Steps**

1. **Wait 2-3 minutes** for DNS propagation
2. **Test manually:**
   ```bash
   curl -I https://code.zeroasterisk.com/
   # Should show: Location: https://zeroasterisk.com/
   
   curl -I https://code.zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/
   # Should show: Location: https://zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/
   ```
3. **Re-run verification script:** `./scripts/verify_legacy_urls.sh`

## 🔍 **URLs That Need Redirects**

Based on the merged content, these legacy URLs should redirect:

### High-Priority Redirects (SEO Critical)
- `https://code.zeroasterisk.com/` → `https://zeroasterisk.com/`
- `https://code.zeroasterisk.com/2017/09/2017-09-06-how-to-learn/` → `https://zeroasterisk.com/2017/09/2017-09-06-how-to-learn/`
- `https://code.zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/` → `https://zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/`
- `https://code.zeroasterisk.com/2017/06/meteor-and-elixir-part-one-a-rocky-courtship/` → `https://zeroasterisk.com/2017/06/meteor-and-elixir-part-one-a-rocky-courtship/`
- `https://code.zeroasterisk.com/2017/05/meteor-1.5-bundle-optimization-examples/` → `https://zeroasterisk.com/2017/05/meteor-1.5-bundle-optimization-examples/`

### Tag Pages
- `https://code.zeroasterisk.com/tags/elixir/` → `https://zeroasterisk.com/tags/elixir/`  
- `https://code.zeroasterisk.com/tags/meteor/` → `https://zeroasterisk.com/tags/meteor/`

### Universal Pattern
- `https://code.zeroasterisk.com/{anything}` → `https://zeroasterisk.com/{anything}`

## 📊 **Current Status**

✅ **Main Site**: All zeroasterisk.com URLs working (200 responses)  
✅ **Content Migration**: All merged content accessible on main site  
❌ **Legacy Redirects**: code.zeroasterisk.com not redirecting (NEEDS FIXING)  
✅ **Tag Fix**: Meteor tag added to relevant posts and deploying

## ⚡ **Expected Results After Configuration**

Once Cloudflare redirects are configured:
- **SEO Preservation**: Search engines will transfer rankings
- **User Experience**: All bookmarks and external links work seamlessly  
- **Analytics**: Traffic consolidated to main domain
- **Maintenance**: Single site to maintain instead of two

## 🔗 **Test URLs After Configuration**

Run these manually to verify:
```bash
# Should redirect with 301
curl -I https://code.zeroasterisk.com/
curl -I https://code.zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/

# Should work directly with 200  
curl -I https://zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/
curl -I https://zeroasterisk.com/tags/meteor/
```

---

**⚠️ PRIORITY: Configure Cloudflare redirects immediately to preserve SEO and user experience!**