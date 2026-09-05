#!/usr/bin/env python3
"""
Simple content migration script for zeroasterisk.com unified site
"""

import os
import re
from datetime import datetime
from pathlib import Path

def parse_frontmatter_simple(content):
    """Simple frontmatter parser without yaml dependency"""
    if content.startswith('---') or content.startswith('+++'):
        delimiter = content[:3]
        parts = content.split(delimiter, 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            body = parts[2].strip()
            
            # Parse key-value pairs
            frontmatter = {}
            for line in fm_text.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"\'')
                    
                    if key == 'tags' or key == 'categories':
                        # Handle list format
                        if value.startswith('[') and value.endswith(']'):
                            items = [item.strip().strip('"\'') for item in value[1:-1].split(',') if item.strip()]
                            frontmatter[key] = items
                        elif value:
                            frontmatter[key] = [value]
                        else:
                            frontmatter[key] = []
                    else:
                        frontmatter[key] = value
            
            return frontmatter, body
    return {}, content

def categorize_content(title, tags, categories):
    """Determine if content should go to posts or personal"""
    text = f"{title.lower()} {' '.join(tags).lower()} {' '.join(categories).lower()}"
    
    personal_keywords = ['family', 'anita', 'penelope', 'personal', 'life', 'parenting', 'wedding', 'baby', 'kids']
    if any(keyword in text for keyword in personal_keywords):
        return 'personal'
    
    return 'posts'

def migrate_post(source_path, target_base_dir):
    """Migrate a single post"""
    try:
        with open(source_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        frontmatter, body = parse_frontmatter_simple(content)
        
        title = frontmatter.get('title', source_path.stem.replace('-', ' ').title())
        date_str = frontmatter.get('date', '')
        
        # Extract date
        try:
            if 'T' in date_str:
                date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00').split('+')[0].split('-')[0:3] + [date_str.split('T')[0]])
            elif len(date_str) >= 10:
                date_obj = datetime.strptime(date_str[:10], '%Y-%m-%d')
            else:
                # Use filename date if available
                filename = source_path.name
                date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
                if date_match:
                    date_obj = datetime.strptime(date_match.group(1), '%Y-%m-%d')
                else:
                    date_obj = datetime.fromtimestamp(source_path.stat().st_mtime)
        except:
            date_obj = datetime.fromtimestamp(source_path.stat().st_mtime)
        
        date = date_obj.strftime('%Y-%m-%d')
        
        tags = frontmatter.get('tags', [])
        categories = frontmatter.get('categories', [])
        
        if isinstance(tags, str):
            tags = [tags]
        if isinstance(categories, str):
            categories = [categories]
        
        content_type = categorize_content(title, tags, categories)
        
        # Create safe slug
        slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
        slug = re.sub(r'\s+', '-', slug).strip('-')[:50]  # Limit length
        if not slug:
            slug = source_path.stem[:50]
        
        # Create frontmatter
        new_frontmatter = f"""---
title: "{title}"
date: {date}
tags: {tags}
type: "{content_type}"
---

"""
        
        # Write to new location
        target_path = target_base_dir / content_type / f"{date}-{slug}.md"
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(new_frontmatter + body)
        
        print(f"Migrated: {source_path.name} -> {content_type}/")
        return True
        
    except Exception as e:
        print(f"Error migrating {source_path}: {e}")
        return False

def main():
    unified_dir = Path("/home/node/zeroasterisk-unified")
    content_dir = unified_dir / "content"
    
    # Clean existing generated posts (keep the manually written ones)
    generated_posts = [
        "headroom-context-compression.md",
        "agent-memory-systems-at-scale.md", 
        "playing-with-elixir.md"
    ]
    
    for post_file in generated_posts:
        for content_type in ['posts', 'personal']:
            for existing_file in (content_dir / content_type).glob(f"*{post_file}"):
                existing_file.unlink()
                print(f"Removed generated file: {existing_file}")
    
    print("Starting migration of all your real posts...")
    
    main_site = Path("/home/node/original-main-site/content/post")
    code_site = Path("/home/node/original-code-site/content/post")
    
    total_migrated = 0
    
    if main_site.exists():
        print(f"Migrating from main site: {main_site}")
        for md_file in main_site.glob('*.md'):
            if migrate_post(md_file, content_dir):
                total_migrated += 1
    
    if code_site.exists():
        print(f"Migrating from code site: {code_site}")
        for md_file in code_site.glob('*.md'):
            if migrate_post(md_file, content_dir):
                total_migrated += 1
    
    print(f"Migration complete! Migrated {total_migrated} posts.")

if __name__ == '__main__':
    main()