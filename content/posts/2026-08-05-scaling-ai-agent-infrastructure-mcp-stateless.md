---
title: "Scaling AI Agent Infrastructure with the MCP Stateless Updates"
date: 2026-08-05
description: "The 2026-07-28 Model Context Protocol spec drops session state for a stateless core, unlocking seamless horizontal scaling"
tags: ["ai", "google", "mcp", "model-context-protocol", "cloud-run", "developer-tools", "cross-post", "2026"]
type: "posts"
canonical_url: "https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/"
external_source: "Google Developers Blog"
crosspost: true
---

# Scaling AI Agent Infrastructure with the MCP Stateless Updates

**Originally published on [Google Developers Blog](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/)** - *August 5, 2026*, co-authored with Kurtis Van Gent.

The 2026-07-28 Model Context Protocol (MCP) spec removes protocol-level sessions in favor of a stateless core. Every tool call is now self-describing, which unlocks seamless horizontal scaling and lets tool servers run on standard HTTP routing infrastructure — no more sticky sessions, no more Redis clusters just to remember which pod holds a session.

## Why This Matters

I co-authored this piece after hitting the session-affinity wall firsthand while deploying MCP servers across Google's cloud infrastructure — sticky sessions and idle warm pods just to hold onto an `Mcp-Session-Id` header. The 2026-07-28 spec (SEP-2575 and SEP-2567) deletes that handshake, moves identity into inline `_meta`, and lets tool containers scale to zero on Cloud Run. This directly shapes how we design agent tool infrastructure — see also the companion breakdown in the [X thread linked below](#related-post).

---

*Read the full article: [Scaling AI Agent Infrastructure with the MCP Stateless updates](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/) on Google Developers Blog*
