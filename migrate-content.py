#!/usr/bin/env python3
"""
Content migration script for zeroasterisk.com unified site
Migrates content from the old split repositories into the new organized structure
"""

import os
import re
import yaml
from datetime import datetime
from pathlib import Path

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content"""
    # Handle both --- and +++ for frontmatter delimiters
    if content.startswith('---') or content.startswith('+++'):
        delimiter = content[:3]
        parts = content.split(delimiter, 2)
        if len(parts) == 3:
            try:
                frontmatter = yaml.safe_load(parts[1].strip())
                body = parts[2].strip()
                return frontmatter if frontmatter else {}, body
            except yaml.YAMLError:
                print(f"Warning: Could not parse YAML frontmatter for a post. Skipping... ")
                return {}, content
    return {}, content

def categorize_content(frontmatter, title, tags, categories):
    """Determine if content should go to posts or personal"""
    
    text_to_check = f"{title.lower()} {' '.join(tags).lower()} {' '.join(categories).lower()}"
    
    # Personal keywords
    personal_keywords = ['family', 'personal', 'anita', 'penelope', 'life', 'parenting', 'wedding', 'baby']
    if any(keyword in text_to_check for keyword in personal_keywords):
        return 'personal'
    
    # Default to posts for all other content (technical, general, etc.)
    return 'posts'

def migrate_post(source_path, target_base_dir):
    """Migrate a single post to the new structure"""
    
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, body = parse_frontmatter(content)
    
    if not frontmatter:
        print(f"Skipping {source_path} due to unparsable frontmatter.")
        return

    title = frontmatter.get('title', source_path.stem.replace('-', ' ').title())
    date_str = str(frontmatter.get('date', ''))
    
    # Attempt to parse date, default to file modification time if not found or invalid
    try:
        # Common formats for Hugo/WordPress frontmatter
        if re.match(r'^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}[+-Z]\\d{2}:\\d{2}$', date_str):
            date_obj = datetime.fromisoformat(date_str)
        elif re.match(r'^\\d{4}-\\d{2}-\\d{2}$', date_str):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        elif re.match(r'^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}$', date_str):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        else:
            date_obj = datetime.fromtimestamp(source_path.stat().st_mtime)
    except (ValueError, TypeError):
        date_obj = datetime.fromtimestamp(source_path.stat().st_mtime)
        print(f"Warning: Using file modification date for {source_path.name}")

    date = date_obj.strftime('%Y-%m-%d')
    
    tags = frontmatter.get('tags', [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(',') if t.strip()]
    
    categories = frontmatter.get('categories', [])
    if isinstance(categories, str):
        categories = [c.strip() for c in categories.split(',') if c.strip()]
    
    # Ensure tags and categories are lists of strings
    tags = [str(t) for t in tags if t is not None]
    categories = [str(c) for c in categories if c is not None]

    # Determine content type (posts or personal)
    content_type = categorize_content(frontmatter, title, tags, categories)
    
    # Create slug from title, ensuring it's URL-friendly
    slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
    slug = re.sub(r'\s+', '-', slug).strip('-')
    if not slug: # Fallback if title leads to empty slug
        slug = source_path.stem

    # Prepare new frontmatter
    new_frontmatter_data = {
        'title': title,
        'date': date,
        'description': frontmatter.get('description', frontmatter.get('summary', '')),
        'tags': sorted(list(set(tags))), # Ensure unique and sorted tags
        'type': content_type
    }
    
    # Convert description to string if it's not already (e.g. if it's a NoneType)
    if not isinstance(new_frontmatter_data['description'], str):
        new_frontmatter_data['description'] = str(new_frontmatter_data['description'])

    # Construct new frontmatter string
    new_frontmatter_str = "---\n"
    for key, value in new_frontmatter_data.items():
        if key == 'tags':
            new_frontmatter_str += f"{key}: {yaml.dump(value, default_flow_style=True).strip()}\n"
        else:
            new_frontmatter_str += f"{key}: {value}\n"
    new_frontmatter_str += "---\n\n"
    
    # Write to new location
    target_path = target_base_dir / content_type / f"{date}-{slug}.md"
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_frontmatter_str + body)
    
    print(f"Migrated: {source_path.name} -> {content_type}/{date}-{slug}.md")

def main():
    """Main migration function"""
    script_dir = Path(__file__).parent
    unified_dir = script_dir
    content_dir = unified_dir / 'content'
    
    original_main_site_path = Path("/home/node/original-main-site/content/post")
    original_code_site_path = Path("/home/node/original-code-site/content/post")
    
    print("Starting content migration...")
    
    # Migrate posts from original-main-site
    if original_main_site_path.exists():
        for md_file in original_main_site_path.rglob('*.md'):
            migrate_post(md_file, content_dir)
    else:
        print(f"Warning: {original_main_site_path} not found. Skipping main site migration.")

    # Migrate posts from original-code-site
    if original_code_site_path.exists():
        for md_file in original_code_site_path.rglob('*.md'):
            migrate_post(md_file, content_dir)
    else:
        print(f"Warning: {original_code_site_path} not found. Skipping code site migration.")

    print("Content migration complete!")

if __name__ == '__main__':
    main()