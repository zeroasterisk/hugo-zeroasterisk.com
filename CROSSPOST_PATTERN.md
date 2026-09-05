# Cross-Posting Pattern for zeroasterisk.com

## Overview

This site implements a "Brief Summary + Canonical Link" pattern for cross-linking external publications. This approach:

- ✅ **SEO-friendly**: Uses canonical tags to credit original source
- ✅ **Respectful**: Provides summary rather than full content copy
- ✅ **Value-added**: Includes personal commentary and perspective
- ✅ **Clear attribution**: Visual indicators show cross-posted content

## Implementation Pattern

### Frontmatter Structure
```yaml
---
title: "Article Title"
date: YYYY-MM-DD  
description: "Brief description"
tags: ["relevant", "tags", "cross-post"]
type: "posts"
canonical_url: "https://original-source.com/article"
external_source: "Publication Name"
crosspost: true
---
```

### Content Structure
1. **Attribution line**: "Originally published on [Source]"
2. **Brief summary**: 2-3 sentences capturing key points  
3. **Personal commentary**: Your perspective/relevance to your work
4. **Call-to-action**: Link to read full original

### Visual Treatment

**Homepage Cards:**
- Blue left border for cross-posts
- 📄 icon + source indicator
- All standard post elements (tags, dates, etc.)

**Individual Post Pages:**
- Prominent cross-post notice at top
- Canonical URL notice
- Blue left border on content
- Footer with link to original
- Canonical meta tags in `<head>`

## SEO Considerations

- ✅ Canonical link points to original source
- ✅ Brief excerpts qualify as fair use
- ✅ Clear attribution prevents duplicate content issues
- ✅ Personal commentary adds unique value

## Examples Implemented

1. **Google Developers Blog**: "Agent Plugins package your skills, tools, and more"
   - Technical standard announcement
   - Personal relevance to Google AI work added

2. **Google Cloud Tech (X/Twitter)**: "5 things every AI engineer should know about agent sandboxes"
   - Social media post format
   - Expanded with personal context

## Future Cross-Posts

Use this pattern for:
- Google blog posts you contribute to
- Industry articles you're quoted in
- Conference talks/presentations
- Open source project announcements
- Technical papers with your involvement

## File Naming Convention
`YYYY-MM-DD-descriptive-slug.md` (matches publication date when possible)