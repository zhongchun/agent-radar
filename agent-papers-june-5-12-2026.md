# Latest AI Agent Academic Papers — Week of June 5–12, 2026

> Searched: arXiv (queries: "LLM agent", "multi-agent", "agentic", "agent framework"), HuggingFace Daily Papers, Papers With Code.

---

## 1. Agentic Environment Engineering for Large Language Models: A Survey
- **arXiv:** [2606.12191](https://arxiv.org/abs/2606.12191)
- **Authors:** Jiachun Li, Zhuoran Jin, Tianyi Men, Yupu Hao, Kejian Zhu et al. (Chinese Academy of Sciences)
- **Date:** June 10, 2026
- **Contribution:** A comprehensive 63-page survey on environment modeling, synthesis, evaluation, and application for LLM agents. Systematically categorizes how agent environments are engineered, from sandbox construction to dynamic world simulation.
- **Source:** arXiv + HuggingFace Daily Papers (56 upvotes)

## 2. Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution
- **arXiv:** [2606.10917](https://arxiv.org/abs/2606.10917)
- **Authors:** Xucong Wang, Ziyu Ma, Shidong Yang, Tongwen Huang, Pengkun Wang, Yong Wang, Xiangxiang Chu
- **Date:** June 9, 2026
- **Contribution:** Introduces a dual-role self-play mechanism where an LLM agent iteratively acts as both executor and critic, bootstrapping its own capabilities without human feedback. Achieves significant improvements on complex reasoning and tool-use tasks through self-evolution.
- **Source:** arXiv + HuggingFace Daily Papers (73 upvotes)

## 3. Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts
- **arXiv:** Available on HuggingFace Daily Papers (Jun 10)
- **Authors:** Microsoft Research
- **Date:** June 10, 2026
- **Contribution:** Proposes a method for improving LLM agents by optimising the agent harness (prompt, tool configuration, orchestration logic) through retrospective preference learning over multiple trajectory rollouts, rather than fine-tuning the base model.
- **Source:** HuggingFace Daily Papers (52 upvotes)

## 4. SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research
- **arXiv:** Available on HuggingFace Daily Papers (Jun 10)
- **Authors:** SearchSwarm team
- **Date:** June 10, 2026
- **Contribution:** A multi-agent framework where a coordinator LLM dynamically delegates sub-tasks to specialist agents for deep research. Introduces "delegation intelligence" — the ability to decide what, when, and to whom to delegate during long-horizon investigative tasks.
- **Source:** HuggingFace Daily Papers (49 upvotes)

## 5. Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents
- **arXiv:** [2606.11688](https://arxiv.org/abs/2606.11688)
- **Authors:** Youwang Deng
- **Date:** June 10, 2026
- **Contribution:** Treats agent honesty as a first-class metric distinct from capability. Presents Autopilot, a verifiable anti-fabrication system that bounds what an unattended long-horizon agent may claim at termination, preventing silent false-success reporting.
- **Source:** arXiv

## 6. OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents
- **arXiv:** [2606.12341](https://arxiv.org/abs/2606.12341)
- **Authors:** Jin Xie, Songze Li
- **Date:** June 10, 2026
- **Contribution:** Formalizes privacy leakage in LLM agents through inference-leakage budgets. Proposes OCELOT, a framework that quantifies and bounds how much PII an agent can leak across trust boundaries when reading personal files and calling external tools.
- **Source:** arXiv

## 7. From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents
- **arXiv:** [2606.09863](https://arxiv.org/abs/2606.09863)
- **Authors:** Laksh Advani
- **Date:** June 6, 2026
- **Contribution:** A systematic study of "false success" — where LLM agents confidently assert task completion despite environmental evidence of failure. Analyzes 9,876 trajectories from 8 model families across two benchmarks, revealing this as a pervasive failure mode.
- **Source:** arXiv

## 8. Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops
- **arXiv:** [2606.08960](https://arxiv.org/abs/2606.08960)
- **Authors:** Ziqian Zhong, Ivgeni Segal, Ivan Bercovich, Shashwat Saxena, Kexun Zhang, Aditi Raghunathan
- **Date:** June 7, 2026
- **Contribution:** Introduces the hacker-fixer loop: alternating adversarial LLM agents that hack verifiers (bypassing task requirements) and fix verifiers (patching discovered exploits), producing exploit-resistant evaluation benchmarks without manual patching.
- **Source:** arXiv

## 9. Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs
- **arXiv:** [2606.10322](https://arxiv.org/abs/2606.10322)
- **Authors:** Saeid Jamshidi, Amin Nikanjam, Arghavan Moradi Dakhel, Kawser Wazed Nafi, Foutse Khomh
- **Date:** June 8, 2026
- **Contribution:** Proposes GT-MCP, a controller-driven multi-agent method that treats context management as a closed-loop dynamical process. Three heterogeneous LLM agents coordinate through a game-theoretic trust function that evaluates causal consistency for robust reasoning.
- **Source:** arXiv

## 10. 3SPO: State-Score-Supervised Policy Optimization for LLM Agents
- **arXiv:** [2606.09961](https://arxiv.org/abs/2606.09961)
- **Authors:** Yu Han, Kailing Li, Yang Jiao, Yulin Dai, Yuqian Fu, Linhai Zhuo, Tianwen Qian
- **Date:** June 8, 2026
- **Contribution:** A reinforcement learning method for LLM agents that operates at the sub-trajectory level rather than waiting for full trajectory completion. Uses state-score supervision to provide denser reward signals, enabling more sample-efficient policy optimization for long-horizon tasks.
- **Source:** arXiv

## 11. Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation
- **arXiv:** [2606.10749](https://arxiv.org/abs/2606.10749)
- **Authors:** Yuchen Ling, Shengcheng Yu, Zhenyu Chen, Chunrong Fang
- **Date:** June 9, 2026
- **Contribution:** A systematic taxonomy of security threats unique to LLM agents (distinct from static LLM security). Covers threat surfaces across planning, tool invocation, memory, and external actions, with a survey of attack vectors and defense mechanisms.
- **Source:** arXiv

## 12. HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning
- **arXiv:** [2606.10507](https://arxiv.org/abs/2606.10507)
- **Authors:** Juncheng Diao, Zhicong Lu, Peiguang Li, Yongwei Zhou, Changyuan Tian, Qingbin Li, Rongxiang Weng, Jingang Wang, Xunliang Cai
- **Date:** June 9, 2026
- **Contribution:** End-to-end training method that teaches LLM agents hierarchical subgoal decomposition and information compression. Agents learn to summarize completed progress into compact representations, enabling effective reasoning over arbitrarily long horizons.
- **Source:** arXiv

## 13. Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems
- **arXiv:** [2606.08661](https://arxiv.org/abs/2606.08661)
- **Authors:** Kuncan Wang, Ziting Wang, Peizhuo Lv, Haoyang Li, Guoliang Li, Gao Cong, Wei Dong
- **Date:** June 7, 2026
- **Contribution:** Identifies new security vulnerabilities at the intersection of database systems and LLM agents. Categorizes failure modes across data resources, database execution, and agent reasoning that neither database security nor general LLM-agent security literature captures alone.
- **Source:** arXiv

## 14. From Player to Master: Enhancing Test-Time Learning of LLM Agents via RL over Memory
- **arXiv:** [2606.08656](https://arxiv.org/abs/2606.08656)
- **Authors:** Yishuo Cai, Xingyu Guo, Xuancheng Huang, Jinhua Du, Can Huang, Wenxuan Huang, Wenhan Ma, Yuyang Hu, Aohan Zeng, Jie Tang, Xu Sun
- **Date:** June 7, 2026
- **Contribution:** Uses reinforcement learning to teach LLM agents how to update their own memory at test time. Instead of hand-designed memory update rules, the agent learns an optimal memory-writing policy that maximally improves future task performance.
- **Source:** arXiv

---

## Notable Mentions

- **Agents' Last Exam** (UC Berkeley, Jun 3) — A comprehensive benchmark for evaluating frontier AI agents. 281 upvotes on HF.
- **SkillOpt: Executive Strategy for Self-Evolving Agent Skills** (Microsoft Research, May 22) — Agent learns to optimize its own skill library. 226 upvotes on HF.
- **Claw-SWE-Bench** (TokenRhythm, Jun 11) — Benchmark for evaluating OpenClaw-style agent harnesses on coding tasks. 55 upvotes on HF.
- **Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents** (arXiv:2606.09483, Jun 8) — Dual-process memory architecture inspired by cognitive science.

---

*Report generated June 12, 2026. Sources: arXiv, HuggingFace Daily Papers, Papers With Code.*
