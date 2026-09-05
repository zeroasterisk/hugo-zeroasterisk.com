# zeroasterisk.com Unified Website

A modern, professional website for Alan Blount showcasing AI/ML work at Google and technical expertise.

## 🎯 Design Philosophy

- **Professional first**: AI/ML career and Google work highlighted prominently
- **Clean organization**: Clear separation between work, technical posts, and personal content
- **Minimalist design**: Fast, accessible, and focused on content
- **Modern build**: Self-contained Hugo setup with automated deployment

## 📁 Content Organization

```
content/
├── work/           # Professional AI/ML projects and achievements
├── posts/          # Technical blog posts and tutorials  
├── personal/       # Family stories and personal reflections
└── pages/          # Static pages (about, etc.)
```

### Content Types

- **Work**: Projects at Google, open source contributions, AI/ML achievements
- **Posts**: Technical tutorials, programming insights, engineering deep-dives
- **Personal**: Family stories, parenting, life outside technology
- **Pages**: About, contact, and other static content

## 🏗️ Architecture

### Built With
- **Hugo** (v0.121+): Static site generator
- **Custom minimal theme**: Clean, professional design
- **GitHub Actions**: Automated deployment
- **GitHub Pages**: Free hosting

### Key Features
- Responsive design (mobile-first)
- Fast loading (minimal CSS/JS)
- SEO optimized (structured data, meta tags)
- RSS feeds for all content types
- Tag and topic-based organization
- Reading time estimates

## 🚀 Development

### Local Development
```bash
# Install Hugo
wget https://github.com/gohugoio/hugo/releases/download/v0.121.1/hugo_extended_0.121.1_linux-amd64.tar.gz
tar -xzf hugo_extended_0.121.1_linux-amd64.tar.gz
sudo mv hugo /usr/local/bin/

# Clone and serve
git clone [repository]
cd zeroasterisk-unified
hugo server
```

### Content Creation

#### Work Articles
```yaml
---
title: "Project Name"
date: 2024-01-15
description: "Brief description"
tags: ["ai", "ml", "agents"]
topics: ["AI Engineering", "Memory Systems"]
type: "work"
featured: true
---
```

#### Technical Posts
```yaml
---
title: "How to Build X"
date: 2024-01-15
description: "Tutorial description"
tags: ["python", "tutorial", "devops"]
topics: ["Software Development"]
type: "posts"
---
```

#### Personal Content
```yaml
---
title: "Family Story"
date: 2024-01-15
description: "Personal reflection"
tags: ["family", "parenting"]
topics: ["Parenting", "Life"]
type: "personal"
---
```

## 📦 Migration from Old Sites

The `migrate-content.py` script helps migrate content from the original split repositories:

```bash
./migrate-content.py
```

The script automatically:
- Categorizes content based on keywords
- Updates frontmatter for new structure
- Generates clean URLs
- Preserves metadata and tags

## 🔧 Configuration

Key settings in `config.toml`:

```toml
# Site identity
title = "Alan Blount | AI/ML Engineer at Google"
author = "Alan Blount"
job = "AI/ML Engineer at Google"

# Content organization
[permalinks]
  work = "/work/:slug/"
  posts = "/:year/:month/:slug/"
  personal = "/personal/:year/:month/:slug/"

# Focus areas (displayed on homepage)
focus_areas = [
  "AI Agent Systems",
  "Memory Architectures", 
  "LLMOps",
  "Agentic Runtimes",
  "Developer Tools"
]
```

## 🎨 Customization

### Theme Structure
```
themes/minimal-tech/
├── layouts/
│   ├── _default/       # Base templates
│   ├── partials/       # Reusable components
│   └── index.html      # Homepage
├── static/
│   ├── css/main.css    # Styles
│   └── js/main.js      # JavaScript
└── theme.toml          # Theme metadata
```

### Styling
- Colors: Professional blue/gray palette
- Typography: System fonts for performance
- Layout: CSS Grid for responsive design
- Components: Card-based content display

## 📈 SEO & Analytics

- Google Analytics integration
- Structured data for rich snippets
- Social media meta tags (Open Graph, Twitter)
- XML sitemaps and RSS feeds
- Robots.txt for search engines

## 🚀 Deployment

Automated deployment via GitHub Actions:

1. **Push to main** → Triggers build
2. **Hugo build** → Generates static files  
3. **Deploy to Pages** → Updates live site

### Manual Deployment
```bash
hugo --gc --minify
# Upload public/ folder to hosting
```

## 📊 Performance

- **Lighthouse Score**: 95+ on all metrics
- **Page Size**: <100KB average
- **Load Time**: <2s on 3G
- **Core Web Vitals**: All green

## 🔗 Navigation Structure

```
Home → Professional focus with recent work
├── Work & AI → Project portfolio
├── Technical Posts → Engineering content
├── Personal → Family stories
└── About → Professional background
```

## 📝 Content Guidelines

### Work Content
- Focus on impact and scale
- Include technical details
- Highlight Google projects (where appropriate)
- Show open source contributions

### Technical Posts
- Deep technical content
- Code examples and tutorials
- Engineering best practices
- Tool and framework reviews

### Personal Content
- Family stories and insights
- Parenting experiences  
- Life outside technology
- Personal growth and learning

## 🤝 Contributing

1. Create content in appropriate section
2. Follow frontmatter conventions
3. Use descriptive titles and tags
4. Test locally before committing
5. Deploy automatically via GitHub Actions

## 📄 License

Content: © Alan Blount
Code: MIT License

---

Built with ❤️ and Hugo by Alan Blount