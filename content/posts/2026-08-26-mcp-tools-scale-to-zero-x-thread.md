---
title: "Give Your Agents Tools That Scale Down to Zero or Up to Infinity"
date: 2026-08-26
description: "A deep-dive thread on the stateless MCP transport: why sessions were a hidden tax, and how to deploy tools that scale to zero on Cloud Run"
tags: ["ai", "google", "mcp", "cloud-run", "google-cloud", "developer-tools", "cross-post", "2026"]
type: "posts"
canonical_url: "https://x.com/GoogleCloudTech/status/2092757828511379468"
external_source: "Google Cloud Tech (X/Twitter)"
crosspost: true
---

# Give Your Agents Tools That Scale Down to Zero or Up to Infinity

**Originally shared by [Google Cloud Tech on X](https://x.com/GoogleCloudTech/status/2092757828511379468)** - *August 26, 2026*. By @zeroasterisk and @Saboo_Shubham_.

An agent is only as capable as its tools, and in production those tools run as Model Context Protocol (MCP) servers. Every other layer of your stack scales to zero when it goes idle — until last month, a single MCP session pinned every tool call to one container.

## Key Points

- **Sessions were an unadvertised tax**: round-robin load balancing broke older, stateful MCP servers with `400 Session Not Found` errors.
- **The 2026-07-28 spec makes every tool call self-describing**: SEP-2575 and SEP-2567 delete the `initialize` handshake and the `Mcp-Session-Id` header, moving identity into inline `_meta`.
- **Tool containers can finally scale to zero**: deploy stateless MCP tools to Cloud Run with `--min-instances=0` and retire the Redis session cluster.
- **Wiring stateless tools into ADK takes six lines of Python**: point `McpToolset` at a `StreamableHTTPConnectionParams` URL — no session choreography required.
- **Stateless is the transport, not your application**: long-running work gets an explicit task handle via the Tasks extension instead of hiding state in a socket.

## Why This Matters

This is the companion field report to my [Google Developers Blog post on scaling AI agent infrastructure](/2026/08/scaling-ai-agent-infrastructure-mcp-stateless/) — the same story, with the exact `curl` reproduction steps, the ADK wiring code, and the Cloud Run deploy command. SDK betas for the 2026-07-28 spec are live for Go (v1.7.0), Python (`mcp[cli]==2.0.0b1`), and TypeScript.

---

*View the original thread: [Google Cloud Tech on X](https://x.com/GoogleCloudTech/status/2092757828511379468)*
