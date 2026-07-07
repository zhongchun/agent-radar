# AI Agent Open Source Project Trends — July 7, 2026

## Executive Summary

The AI agent ecosystem is in a massive growth phase as of mid-2026. Key themes observed:
- **Agent Skills** is the dominant new paradigm — skill-based tooling for coding agents (Claude Code, Cursor, Codex) is exploding
- **Meta-harnesses** that orchestrate multiple coding agents (Omnigent, Peerd) are emerging
- **Loop Engineering** as a discipline for designing repeatable agent workflows
- **Security/Red-teaming** agents for autonomous security testing
- Chinese AI agent ecosystem is thriving (Xiaomi's MiMo, Qwen-AgentWorld, baoyu-design)
- LangChain.js v1.5.2 and LangChain Python v1.3.11 show maturity

---

## 1. Major Framework Stars & Status (as of July 7, 2026)

| Project | Stars | Latest Release | Date |
|---------|-------|---------------|------|
| **AutoGPT** | 185,423 | autogpt-platform-beta-v0.6.65 | 2026-06-25 |
| **Dify** | 148,078 | v1.15.0 | 2026-06-25 |
| **LangChain** | 141,218 | v1.3.11 (Py), v1.5.2 (JS) | 2026-06-22 |
| **addyosmani/agent-skills** | 72,083 | — | 2026-07-07 |
| **MetaGPT** | 69,250 | v0.8.1 | 2024-04-22 (STALE) |
| **AutoGen (MS)** | 59,558 | python-v0.7.5 | 2025-09-30 (STALE) |
| **CrewAI** | 55,100 | v1.15.1 | 2026-06-27 |
| **Agno** | 41,038 | v2.7.1 | 2026-07-07 |
| **smolagents** | 28,236 | v1.26.0 | 2026-05-29 |
| **PydanticAI** | 18,259 | v2.5.1 | 2026-07-07 |

### Key Observations
- **Agno** (v2.7.1, released 2026-07-07) is actively developed with frequent releases — positioned as "the programming language for agentic software"
- **PydanticAI** (v2.5.1, 2026-07-07) rapidly iterating — "AI Agent Framework, the Pydantic way"
- **CrewAI** (v1.15.1, 2026-06-27) — active development on role-playing agent orchestration
- **MetaGPT** and **AutoGen** appear stalled — no recent releases in 2026
- **LangChain** renamed to "The agent engineering platform" — evolving beyond chains
- **addyosmani/agent-skills** (72K stars!) — the defining project of the agent-skills paradigm

---

## 2. Trending New Projects (June-July 2026)

### Hottest New Entrants

| Project | Stars | Category | Description |
|---------|-------|----------|-------------|
| **DietrichGebert/ponytail** | 76,884 | Agent Philosophy | AI agents think like the laziest senior dev |
| **XiaomiMiMo/MiMo-Code** | 11,587 | AI Coding | Models and Agents Co-Evolve (Xiaomi) |
| **langchain-ai/openwiki** | 9,006 | Agent Docs | CLI for agent documentation |
| **omnigent-ai/omnigent** | 6,636 | Meta-Harness | Orchestrate Claude Code, Codex, Cursor, Pi |
| **cobusgreyling/loop-engineering** | 6,408 | Loop Engineering | Patterns for loop engineering with AI coding agents |
| **BuilderIO/skills** | 3,512 | Agent Skills | Skills for coding agents |
| **vercel/eve** | 3,300 | Agent Framework | The Framework for Building Agents (Vercel) |
| **elder-plinius/T3MP3ST** | 3,279 | Red Teaming | Autonomous multi-agent offensive-security |
| **Forward-Future/loopy** | 2,534 | Loop Engineering | Practical AI-agent loops |
| **JimLiu/baoyu-design** | 2,467 | Agent Skill | Claude Design as local Agent Skill |
| **cloudflare/security-audit-skill** | 2,335 | Agent Skill | Multi-phase security audits |
| **davidondrej/skills** | 1,790 | Agent Skills | Personal agent skills collection |
| **tigicion/dao-code** | 1,610 | Terminal Agent | Open-source terminal coding agent for DeepSeek-V4 |
| **synthetic-sciences/openscience** | 1,324 | AI Science | Open-source AI workbench for scientific research |
| **Forsy-AI/agent-apprenticeship** | 1,292 | Agent Learning | Agents complete tasks, improve iteratively, accumulate experience |
| **larlarua/AutoCVE** | 1,077 | Security | Agent-driven automated CVE discovery |
| **shepherd-agents/shepherd** | 1,041 | Observability | Reversible, Git-like agent execution traces |

---

## 3. Agent Skills Ecosystem (2026 Trend)

The "Agent Skills" paradigm is the defining trend of mid-2026 — reusable skill packages for AI coding agents:

| Skill Project | Stars | Purpose |
|--------------|-------|---------|
| **addyosmani/agent-skills** | 72,083 | Production-grade engineering skills for AI coding agents |
| **BuilderIO/skills** | 3,512 | General-purpose coding agent skills |
| **cloudflare/security-audit-skill** | 2,335 | Multi-phase security audit automation |
| **JimLiu/baoyu-design** | 2,467 | Claude Design as local Agent Skill |
| **modiqo/skillspec** | 904 | Agent skills followable, testable, and provable |
| **Kulaxyz/self-learning-skills** | 856 | Self-improving skill harvesting golden paths |
| **amElnagdy/guard-skills** | 971 | Guard skills to catch AI-generated failure modes |
| **isjiamu/gzh-design-skill** | 994 | Markdown to WeChat article HTML |
| **majidmanzarpour/threejs-game-skills** | 796 | Agent skills for Three.js browser games |

---

## 4. Emerging Categories

### Meta-Harnesses & Orchestrators
- **omnigent-ai/omnigent** (6,636 stars) — Framework for orchestrating multiple coding agents under unified policies
- **NotASithLord/peerd** (327 stars) — Browser-native agent harness

### Loop Engineering
- **cobusgreyling/loop-engineering** (6,408 stars) — Patterns for designing agent loops
- **Forward-Future/loopy** (2,534 stars) — Library of practical agent loops
- **ksimback/looper** (626 stars) — Visual loop designer for Claude Code

### Security & Red Teaming
- **elder-plinius/T3MP3ST** (3,279 stars) — Autonomous multi-agent red teaming
- **larlarua/AutoCVE** (1,077 stars) — Agent-driven CVE discovery
- **visa/visa-vulnerability-agentic-harness** (654 stars) — Visa's vulnerability testing
- **badchars/darknet-mcp-server** (198 stars) — 66-tool MCP server for dark web intelligence

### Agent Observability & Traceability
- **shepherd-agents/shepherd** (1,041 stars) — Reversible Git-like execution traces
- **superloglabs/superlog** (996 stars) — AI agents that self-heal software

---

## 5. PyPI Package Status

| Package | Version | Date | Notes |
|---------|---------|------|-------|
| **agno** | 2.7.1 | 2026-07-07 | Latest release TODAY |
| **pydantic-ai** | 2.5.1 | 2026-07-07 | Latest release TODAY |
| **crewai** | 1.15.1 | 2026-06-27 | Active |
| **crewai-tools** | 1.15.1 | 2026-06-27 | Aligned with crewai |
| **smolagents** | 1.26.0 | 2026-05-29 | HuggingFace |
| **langchain** | 1.3.11 | 2026-06-22 | Active (recent releases: 1.3.9–1.3.11) |
| **autogen-agentchat** | 0.7.5 | 2025-09-30 | STALE — no 2026 release |

---

## 6. npm/JavaScript Agent Frameworks

| Package | Version | Description |
|---------|---------|-------------|
| **langchain** | 1.5.2 | TypeScript LangChain bindings |
| **@langchain/core** | 1.2.1 | Core LangChain.js abstractions |
| **@langchain/openai** | 1.5.3 | OpenAI integrations |
| **@voltagent/core** | 2.8.1 | VoltAgent Core — JS AI agent framework |
| **@cnrai/pave** | 0.11.30 | PAVE — Personal AI Virtual Environment |
| **cray-code** | 1.3.6 | MCP, Skills, and Sub-agent support |
| **@open1s/jsbos** | 2.3.6 | BrainOS — multi-language agent framework |
| **@iqai/adk** | 0.8.5 | TypeScript-native agent framework |
| **kernl** | 0.12.7 | Modern AI agent framework |
| **@looopy-ai/core** | 3.1.3 | RxJS-based AI agent framework |
| **@tailored-ai/cli** | 0.1.9 | Lightweight framework for local LLMs |

---

## 7. Chinese AI Agent Ecosystem

| Project | Stars | Description |
|---------|-------|-------------|
| **XiaomiMiMo/MiMo-Code** | 11,587 | Xiaomi's Models+Agents co-evolution |
| **QwenLM/Qwen-AgentWorld** | 790 | Language World Models for General Agents |
| **lyra81604/zhengxi-views** | 1,180 | Fund manager research Agent Skill |
| **ziqihe10-droid/xuefeng-agent** | 893 | College admission AI advisor |
| **isjiamu/gzh-design-skill** | 994 | WeChat article design skill |
| **orange2ai/renwei-writing** | 907 | Chinese writing style agent |
| **alchaincyf/fanbox** | 899 | Vibe coding cockpit |
| **shy3130/tickflow-stock-panel** | 1,862 | A-share quant trading workbench with LLM |
| **Karovia/fullstack-ai-agent-roadmap** | 282 | 110 tutorials, 580K chars, CN roadmap |

---

## 8. Key Takeaways

1. **Agent Skills is the dominant paradigm** — reusable, installable skill packages for AI coding agents; addyosmani/agent-skills has 72K stars
2. **Agno and PydanticAI are the fastest-moving frameworks** — both released updates TODAY (July 7, 2026)
3. **MetaGPT and AutoGen appear abandoned or stalled** — no releases in 2026
4. **Loop Engineering** emerging as a new discipline for designing repeatable agent workflows
5. **Meta-harnesses** (Omnigent) that orchestrate multiple agent runtimes are rising
6. **LangChain rebranded** from "building LLM applications" to "the agent engineering platform"
7. **Chinese ecosystem** vibrant with Xiaomi's MiMo, Qwen-AgentWorld, and many agent skills
8. **Security** (red teaming, CVE discovery, vulnerability testing) is a growing agent use-case
9. **Vercel entering** the agent framework space with "eve"
10. **Browser-native agents** (Peerd) represent a new deployment paradigm
11. **ponytail** (76K stars) shows viral interest in making agents "lazy" — writing less code
12. **OpenWiki** by LangChain (9K stars) — automated agent documentation is a new category

---

*Report generated: July 8, 2026 | Data sourced from GitHub API, PyPI, npm registry*
