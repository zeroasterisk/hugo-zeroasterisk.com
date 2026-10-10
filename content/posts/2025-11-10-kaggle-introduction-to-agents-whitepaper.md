---
title: "Introduction to Agents (Kaggle 5-Day AI Agents Intensive Whitepaper)"
date: 2025-11-10
description: "Lead-authored Day 1 whitepaper of the Kaggle x Google 5-Day AI Agents Intensive: agent taxonomy, architecture, Agent Ops, identity, policy, and governance."
tags: ["ai", "agents", "whitepaper", "kaggle", "security", "governance", "evaluation", "cross-post", "2025"]
type: "posts"
canonical_url: "https://www.kaggle.com/whitepaper-introduction-to-agents"
external_source: "Kaggle"
crosspost: true
---

# Introduction to Agents

**Lead author, with Antonio Gulli, Shubham Saboo, Michael Zimmermann, and Vladimir Vuskovic, on [Kaggle](https://www.kaggle.com/whitepaper-introduction-to-agents)**, *November 2025*

Day 1 of the [Kaggle × Google 5-Day AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-agents), which reached [1.5M+ learners](https://blog.google/innovation-and-ai/technology/developers-tools/ai-agents-intensive-recap/). It is written for developers, architects, and product leaders moving from proof-of-concept to production-grade agents:

- **Taxonomy**: Level 0 (core reasoning) → Level 4 (self-evolving systems)
- **Architecture**: Model ("brain"), Tools ("hands"), Orchestration ("nervous system")
- **Agent Ops**: LM-as-judge quality, metrics-driven go/no-go, OpenTelemetry traces, human feedback
- **Security**: the utility vs. risk trade-off, defense in depth, agents as a new class of principal (SPIFFE identity), least-privilege policies
- **Governance**: a central gateway/control plane instead of agent sprawl
- **Interop**: agents with humans, agents, and money (A2A, AP2)

I also joined the [Day 1 livestream](https://www.youtube.com/live/ZaUcqznlhv8) as a guest.

## The Full Series

1. [Introduction to Agents](https://www.kaggle.com/whitepaper-introduction-to-agents) ([podcast](https://www.youtube.com/watch?v=zTxvGzpfF-g))
2. [Agent Tools & Interoperability with MCP](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp) ([podcast](https://www.youtube.com/watch?v=Cr4NA6rxHAM))
3. [Context Engineering: Sessions & Memory](https://www.kaggle.com/whitepaper-context-engineering-sessions-and-memory) ([podcast](https://www.youtube.com/watch?v=FMcExVE15a4))
4. [Agent Quality](https://www.kaggle.com/whitepaper-agent-quality) ([podcast](https://www.youtube.com/watch?v=LFQRy-Ci-lk))
5. [Prototype to Production](https://www.kaggle.com/whitepaper-prototype-to-production) ([podcast](https://www.youtube.com/watch?v=8Wyt9l7ge-g))

## Why This Matters

Building a prototype is easy. Making it secure, high-quality, and reliable is the hard part. Success doesn't come from the first prompt. It comes from engineering rigor across the whole system: tool contracts, error handling, context management, and comprehensive evaluation.

---

*Read the whitepaper: [Kaggle](https://www.kaggle.com/whitepaper-introduction-to-agents)*
