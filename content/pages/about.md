---
title: "About"
description: "Member of Technical Staff / Technical Product Manager at Google, focused on agent security, governance, capabilities, quality, and evaluation"
type: "page"
aliases: ["/about/"]
---

# About Alan Blount

I'm a **Member of Technical Staff / Technical Product Manager** at Google in Boulder, Colorado, working on the Gemini Enterprise Agent Platform (formerly Vertex AI). I spent about 20 years as a software engineer before moving into product. I help developers build agents they can trust in production.

My day-to-day covers A2A, ADK, Agent Engine, MCP, grounding/RAG, memory, and Agent Ops. Before that I worked on Google's Payments Smart Router, an ML multi-armed-bandit optimization and analytics system. Before Google, I was a tech lead and full-stack developer, helping startups grow into successful small companies since ~2001.

## Areas of Focus

### Security & Governance

Agents are a new kind of principal. To be useful they need autonomy and tools, and every capability you give them adds risk. I work on making that trade-off explicit and enforceable:

- **Agent identity**: each agent gets its own verifiable identity (e.g. SPIFFE), separate from the user who invoked it and the developer who built it, with least-privilege permissions so a compromised agent has a small blast radius.
- **Policy & authorization**: constraining access to tools, data, sub-agents, and remote agents, enforced at the API/gateway layer for MCP and A2A traffic.
- **Defense in depth**: deterministic guardrails outside the model, plus reasoning-based defenses (guard models, plan review) against prompt injection, data poisoning, and data leakage.
- **Governance at fleet scale**: a central control plane instead of "agent sprawl". Every user→agent, agent→tool, agent→agent, and agent→model call is authenticated, authorized, logged, and auditable.
- **Execution isolation**: sandboxes for agent-generated code, where network egress is often a bigger attack surface than the hypervisor.

### Capabilities, Quality & Evaluation

Agents are probabilistic by design, so `assert output == expected` isn't enough. I care about measuring whether agents (and software in general) actually work:

- **Capabilities**: knowing what each level of agent can do, from a single connected problem-solver to multi-agent systems and self-evolving agents, and scoping systems to match.
- **Agent Ops**: the next step after DevOps and MLOps. Metrics-driven development, go/no-go deployment gates, and A/B-style KPIs tied to real outcomes (goal completion, cost per task, latency, user satisfaction).
- **Evaluation**: LM-as-judge quality scoring, trajectory evals, and human feedback that feeds back into automated test sets.
- **Observability**: OpenTelemetry traces that answer *why* an agent did what it did.
- **Deterministic verification first**: wherever possible, check results with code instead of opinion.
- **Tokenomics**: routing work between fast and deep models by task ROI, not habit.

## Writing & Publications

- **[Introduction to Agents](https://www.kaggle.com/whitepaper-introduction-to-agents)** whitepaper (lead author, with Antonio Gulli, Shubham Saboo, Michael Zimmermann, and Vladimir Vuskovic). Day 1 of the [Kaggle × Google 5-Day AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-agents) (Nov 2025, [1.5M+ learners](https://blog.google/innovation-and-ai/technology/developers-tools/ai-agents-intensive-recap/)). It covers agent taxonomy, architecture, Agent Ops, agent identity, policy, and governance. I was also a guest on the [Day 1 livestream](https://www.youtube.com/live/ZaUcqznlhv8).
- The full 5-day series:
  1. [Introduction to Agents](https://www.kaggle.com/whitepaper-introduction-to-agents)
  2. [Agent Tools & Interoperability with MCP](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp)
  3. [Context Engineering: Sessions & Memory](https://www.kaggle.com/whitepaper-context-engineering-sessions-and-memory)
  4. [Agent Quality](https://www.kaggle.com/whitepaper-agent-quality)
  5. [Prototype to Production](https://www.kaggle.com/whitepaper-prototype-to-production)
- [Google Developers Blog articles](https://developers.googleblog.com/en/search/?author=Alan+Blount) on ADK, A2A, MCP, AG-UI, and Agent Plugins
- [Agentic AI Foundation (AAIF) blog](https://aaif.io/author/alan-blount)
- Google Cloud Tech articles on X: [agent sandboxes](https://x.com/GoogleCloudTech/status/2094598332131709078) (with Ryan Ismert) and [Fable 5.1 + Gemini 3.8 Flash model routing](https://x.com/GoogleCloudTech/status/2099507349828350285)

## Talks

- [Agents and MCP @ Google Scale](https://www.youtube.com/watch?v=jCJ3LfqyHy4), MCP Dev Summit NA 2026 (with Vaibhav Katkade)
- [How Google Built the A2A Protocol](https://www.youtube.com/watch?v=aW4jovr7Rys), Patchwork: Syncing on AI Standards (2026)

## Open Source & Community

- **Creator of Headroom**: context compression for AI applications that reduces token costs by 70%
- **Agent protocols & runtimes**: A2A, ADK, MCP, plus OpenClaw, Scion, Flue, and ax
- **zeroasterisk on GitHub**: developer tools and AI-related projects
- **Mentoring**: free coding bootcamps, universities, conferences, and meetups

## Technical Philosophy

- **Research-driven development**: understand the problem before building solutions
- **Iterative prototyping**: quick feedback loops and continuous improvement
- **Deterministic verification**: prefer programmatic checks over subjective evaluation
- **Platform-native solutions**: build with the grain of existing systems
- **Trust is the product**: building an agent is easy; trusting it is hard

## Personal Side

When I'm not working on AI systems, you'll find me:
- **Parenting**: raising kids with my wife Anita in Boulder
- **Teaching**: helping kids balance screen time with productive projects
- **Learning**: always exploring new technologies and methodologies
- **Writing**: documenting experiences both technical and personal

## Boulder, Colorado

I love living in Boulder. It's the perfect blend of tech innovation and outdoor adventure, with incredible access to hiking, biking, and the mountains, plus a thriving tech community.

## Connect

I'm always interested in discussing:
- Agent security, identity, and governance
- Agent quality, evaluation, and Agent Ops
- Agent interoperability (A2A, MCP) and memory
- The intersection of technology and parenting

Find me on [GitHub](https://github.com/zeroasterisk), [X/Twitter](https://x.com/zeroasterisk), or [LinkedIn](https://linkedin.com/in/alanblount).
