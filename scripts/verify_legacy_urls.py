#!/usr/bin/env python3
"""
Comprehensive Legacy URL Verification Script

Tests all legacy URLs from the merged code.zeroasterisk.com content
and verifies proper 301 redirects are in place.
"""

import requests
import sys
import json
from urllib.parse import urlparse, urljoin
import time

class LegacyURLVerifier:
    def __init__(self):
        self.main_domain = "https://zeroasterisk.com"
        self.legacy_domain = "https://code.zeroasterisk.com" 
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'URL-Verifier/1.0 (zeroasterisk.com migration)'
        })
        
        # URL patterns to test
        self.test_urls = [
            # Code site legacy URLs (should 301 to main site)
            "https://code.zeroasterisk.com/",
            "https://code.zeroasterisk.com/2017/09/2017-09-06-how-to-learn/",
            "https://code.zeroasterisk.com/2017/07/playing-with-elixir-is-just-fun/", 
            "https://code.zeroasterisk.com/2017/06/meteor-and-elixir-part-one-a-rocky-courtship/",
            "https://code.zeroasterisk.com/2017/05/meteor-1.5-bundle-optimization-examples/",
            "https://code.zeroasterisk.com/tags/elixir/",
            "https://code.zeroasterisk.com/tags/meteor/",
            
            # Main site URLs (should work directly)
            f"{self.main_domain}/",
            f"{self.main_domain}/posts/",
            f"{self.main_domain}/personal/",
            f"{self.main_domain}/2017/09/2017-09-06-how-to-learn/",
            f"{self.main_domain}/2017/07/playing-with-elixir-is-just-fun/", 
            f"{self.main_domain}/2017/06/meteor-and-elixir-part-one-a-rocky-courtship/",
            f"{self.main_domain}/tags/elixir/",
            f"{self.main_domain}/tags/meteor/",
            f"{self.main_domain}/tags/2017/",
            f"{self.main_domain}/pages/about/",
            
            # Search and other key pages
            f"{self.main_domain}/search/",
            f"{self.main_domain}/sitemap.xml",
            f"{self.main_domain}/robots.txt",
        ]
        
    def check_url(self, url, expect_redirect=False, target_domain=None):
        """Check a single URL and return results"""
        try:
            # Follow redirects but capture the chain
            response = self.session.get(url, allow_redirects=True, timeout=10)
            
            result = {
                'url': url,
                'status_code': response.status_code,
                'final_url': response.url,
                'redirect_chain': [],
                'success': False,
                'error': None
            }
            
            # Check redirect chain
            if response.history:
                for resp in response.history:
                    result['redirect_chain'].append({
                        'status': resp.status_code,
                        'location': resp.headers.get('Location', '')
                    })
            
            # Validate based on expectations
            if expect_redirect:
                if response.history and any(r.status_code in [301, 302, 307, 308] for r in response.history):
                    if target_domain and target_domain in response.url:
                        result['success'] = True
                    elif not target_domain:
                        result['success'] = True
                else:
                    result['error'] = f"Expected redirect but got direct response"
            else:
                if response.status_code == 200:
                    result['success'] = True
                else:
                    result['error'] = f"Expected 200 but got {response.status_code}"
                    
            return result
            
        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'status_code': None,
                'final_url': None,
                'redirect_chain': [],
                'success': False,
                'error': str(e)
            }

    def verify_all_urls(self):
        """Verify all URLs and return results"""
        print("🔍 Starting Legacy URL Verification")
        print("=" * 60)
        
        results = {
            'main_site_urls': [],
            'legacy_redirects': [],
            'failed_urls': [],
            'summary': {
                'total_tested': 0,
                'successful': 0,
                'failed': 0
            }
        }
        
        for url in self.test_urls:
            print(f"\n📍 Testing: {url}")
            
            # Determine test type
            is_legacy = 'code.zeroasterisk.com' in url
            expect_redirect = is_legacy
            target_domain = 'zeroasterisk.com' if is_legacy else None
            
            result = self.check_url(url, expect_redirect, target_domain)
            results['summary']['total_tested'] += 1
            
            if result['success']:
                results['summary']['successful'] += 1
                status = "✅"
                if is_legacy:
                    results['legacy_redirects'].append(result)
                    print(f"{status} REDIRECT: {result['status_code']} → {result['final_url']}")
                else:
                    results['main_site_urls'].append(result)
                    print(f"{status} DIRECT: {result['status_code']}")
            else:
                results['summary']['failed'] += 1
                results['failed_urls'].append(result)
                status = "❌"
                print(f"{status} FAILED: {result['error']}")
                
            # Show redirect chain if present
            if result['redirect_chain']:
                for i, redirect in enumerate(result['redirect_chain']):
                    print(f"    {i+1}. {redirect['status']} → {redirect['location']}")
                    
            time.sleep(0.5)  # Rate limiting
        
        return results

    def print_summary(self, results):
        """Print a comprehensive summary"""
        print("\n" + "=" * 60)
        print("📊 LEGACY URL VERIFICATION SUMMARY")
        print("=" * 60)
        
        summary = results['summary']
        print(f"📋 Total URLs Tested: {summary['total_tested']}")
        print(f"✅ Successful: {summary['successful']}")
        print(f"❌ Failed: {summary['failed']}")
        print(f"📈 Success Rate: {summary['successful']/summary['total_tested']*100:.1f}%")
        
        if results['failed_urls']:
            print(f"\n🚨 FAILED URLs ({len(results['failed_urls'])}):")
            for result in results['failed_urls']:
                print(f"   ❌ {result['url']}")
                print(f"      Error: {result['error']}")
                
        if results['legacy_redirects']:
            print(f"\n🔄 Legacy Redirects Working ({len(results['legacy_redirects'])}):")
            for result in results['legacy_redirects']:
                print(f"   ✅ {result['url']} → {result['final_url']}")
                
        print(f"\n🌍 Main Site URLs Working ({len(results['main_site_urls'])}):")
        for result in results['main_site_urls'][:5]:  # Show first 5
            print(f"   ✅ {result['url']}")
        if len(results['main_site_urls']) > 5:
            print(f"   ... and {len(results['main_site_urls']) - 5} more")
            
        # Generate Cloudflare redirect rules
        self.generate_cloudflare_rules(results)
        
    def generate_cloudflare_rules(self, results):
        """Generate Cloudflare redirect rules for any missing redirects"""
        print(f"\n📝 CLOUDFLARE REDIRECT RULES")
        print("=" * 60)
        
        failed_code_urls = [r for r in results['failed_urls'] 
                           if 'code.zeroasterisk.com' in r['url']]
        
        if not failed_code_urls:
            print("✅ All code.zeroasterisk.com URLs are already redirecting properly!")
            return
            
        print("🔧 Required Cloudflare Page Rules:")
        print("\nAdd these page rules in Cloudflare Dashboard:")
        print("(Settings → Rules → Page Rules)")
        
        rules = [
            {
                'pattern': 'code.zeroasterisk.com/*',
                'action': '301 Redirect',
                'target': 'https://zeroasterisk.com/$1'
            },
            {
                'pattern': 'code.zeroasterisk.com',
                'action': '301 Redirect', 
                'target': 'https://zeroasterisk.com/'
            }
        ]
        
        for i, rule in enumerate(rules, 1):
            print(f"\nRule #{i}:")
            print(f"  Pattern: {rule['pattern']}")
            print(f"  Action: {rule['action']}")
            print(f"  Target: {rule['target']}")
            
        print(f"\n📖 Alternative: Use Cloudflare Bulk Redirects")
        print("(Rules → Redirect Rules → Create rule)")
        print("Expression: (http.host eq \"code.zeroasterisk.com\")")
        print("Action: Dynamic redirect")
        print("Expression: concat(\"https://zeroasterisk.com\", http.request.uri.path)")
        print("Status code: 301")

def main():
    verifier = LegacyURLVerifier()
    results = verifier.verify_all_urls()
    verifier.print_summary(results)
    
    # Exit with error code if any tests failed
    if results['summary']['failed'] > 0:
        print(f"\n⚠️  {results['summary']['failed']} URLs failed verification")
        sys.exit(1)
    else:
        print(f"\n🎉 All {results['summary']['total_tested']} URLs verified successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()