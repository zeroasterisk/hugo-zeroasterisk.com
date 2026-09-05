---
title: "Agent Plugins Package Your Skills, Tools, and More"
date: 2026-08-06
description: "Google's new vendor-neutral standard for packaging Agent Skills and MCP servers into portable, interoperable AI tools"
tags: ["ai", "google", "agent-plugins", "mcp", "developer-tools", "cross-post", "2026"]
type: "posts"
canonical_url: "https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/"
external_source: "Google Developers Blog"
crosspost: true
---

# Agent Plugins Package Your Skills, Tools, and More

**Originally published on [Google Developers Blog](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/)** - *August 6, 2026*

Google has announced Agent Plugins 1.0.0, a new vendor-neutral directory specification backed by major tech companies including Google, Amazon, and Microsoft. This standard aims to package Agent Skills and MCP (Model Context Protocol) servers into portable, interoperable units.

## Key Highlights

The specification standardizes the manifest (`plugin.json`) and utilizes a fixed directory layout, eliminating the need for developers to maintain separate wrappers or configurations to support different AI coding agents and IDEs.

**What this means for AI developers:**
- **Portability**: Build once, deploy anywhere across different AI platforms
- **Interoperability**: No more platform-specific agent configurations  
- **Standardization**: Clear specification for packaging agent capabilities
- **Industry backing**: Supported by major cloud providers

Google has officially joined as a Core Maintainer and rolled out support in the Agents CLI and Data Agent Kit, allowing developers to start building and distributing interoperable plugins today.

This is particularly relevant for my work at Google on agent memory systems and the broader agentic runtime ecosystem we're building.

---

*Read the full article with technical details and implementation examples: [Agent Plugins package your skills, tools, and more](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/) on Google Developers Blog*