# AI Agent 日报 — 2026年07月13日

> 本报告由 Hermes Agent 自动生成，覆盖国内外 AI Agent 领域的最新动态。
> 信息来源：量子位、TechCrunch、Hacker News、arXiv、GitHub Trending、star-history、PostTrain Bench、Anthropic 官方博客、Google DeepMind 官方博客、PyPI

## 📑 目录

- [一、国内动态 🇨🇳](#一国内动态-)
- [二、国际动态 🌍](#二国际动态-)
- [三、企业界 🏢](#三企业界-)
- [四、学术界 🎓](#四学术界-)
- [五、开源项目 🛠️](#五开源项目-)
- [六、趋势分析与预测 📈](#六趋势分析与预测-)

---

## 一、国内动态 🇨🇳

### 1. 中国团队 Agent 专用搜索引擎登顶 Product Hunt
中国团队推出的 Agent 专用搜索引擎在 Product Hunt 登顶，主打更低 Token 消耗和更精准的搜索结果，专门为 AI Agent 工具调用场景设计。该引擎通过优化搜索结果的压缩和结构化，大幅降低了 Agent 使用搜索工具时的成本。
[查看原文](https://www.qbitai.com/2026/07/449327.html)

### 2. 浪潮信息发布单柜 4 万 Agent 液冷整机柜
浪潮信息发布 CPU 原生液冷整机柜和多模融合超节点，单柜可承载 4 万个 Agent，同时推出多模型协作答题方案，兼顾 Agent 的数量与智能能力。这标志着中国企业级 Agent 基础设施进入规模化部署阶段。
[查看原文](https://www.qbitai.com/2026/07/449311.html)

### 3. 蚂蚁安全开源两大 AI 编程 Agent 安全框架
针对 Claude Code、Codex 等 AI 编程 Agent 带来的安全隐患，蚂蚁安全开源了两大安全框架，旨在填补 AI Coding Agent 在生产环境中的安全漏洞。此举呼应了全球对 Agent 安全性的日益关注。
[查看原文](https://www.qbitai.com/2026/07/448925.html)

### 4. 清华团队现场演示 Physical AGI：机器狗自主指挥人类完成任务
清华团队现场演示 Physical AGI（具身智能体），机器狗在没有预设脚本的情况下自主指挥人类完成称重任务，从人类认知范式构建 Physical AGI。观众即兴出题，展示了具身 Agent 在真实物理世界中的通用能力。
[查看原文](https://www.qbitai.com/2026/07/448239.html)

### 5. OpenAI 高层动荡波及中国 AI 圈：安全主管在 GPT-5.6 发布后离职
GPT-5.6 发布后，OpenAI 安全主管离职，这是两年内第六位离开的高管，引发国内 AI 安全研究社区对 Agent 安全治理的广泛讨论。与此同时，Codex 宣布移除 5 小时使用限制，开发者疯狂涌入，一度有人因连续工作过度入院。
[查看原文](https://www.qbitai.com/2026/07/448825.html)

### 6. 百度 AI 搭子日均提问暴增 20 倍，企业版同步发布
百度 AI 搭子（Agent 产品）日均使用量暴增 20 倍，宣布重大升级并同步发布企业版。量子位评论称「Agent 时代来了」，百度在 C 端和 B 端同时发力 Agent 应用。
[查看原文](https://www.qbitai.com/2026/07/447681.html)

### 7. GPT-5.6 一小时解开 50 年数学猜想：64 子 Agent 并行协作
GPT-5.6 用不到一小时证明了一个 50 年未解的图论猜想（圈双覆盖猜想），通过 64 个子 Agent 并行协作完成。研究员公开了 700 词完整 Prompt，展示了「神话级」的多 Agent 驾驭技巧，证明多 Agent 协作可极快加速复杂任务处理。
[查看原文](https://www.qbitai.com/2026/07/447873.html)

---

## 二、国际动态 🌍

### 1. 🚨 Apple 起诉 OpenAI 窃取商业机密
Apple 对 OpenAI 提起诉讼，指控包括员工未经授权访问 Apple 系统、要求应聘者携带 Apple 硬件参加面试等。这是科技巨头间因 AI 技术竞争引发的最大法律冲突之一，可能重塑 AI 行业的人才流动规则。
[查看原文](https://techcrunch.com/2026/07/13/the-wildest-allegations-in-apples-trade-secrets-lawsuit-against-openai/)

### 2. Satya Nadella 发出震撼警告：专有 AI 模型如同特洛伊木马
微软 CEO Satya Nadella 在公开场合警告称，大型 AI 实验室销售的专有模型可能如同特洛伊木马，在硅谷引发广泛争议。这番言论正值各大企业加速采用 AI Agent 之际，对企业选择开源还是闭源模型有深远影响。
[查看原文](https://techcrunch.com/2026/07/13/satya-nadella-has-issued-a-shocking-warning-to-companies-using-ai/)

### 3. DeepMind CEO 呼吁建立独立 AI 标准机构
DeepMind CEO Demis Hassabis 提议建立类似 FINRA 的独立 AI「标准机构」，用于测试前沿模型并制定发布最佳实践。此举被认为是针对当前 AI Agent 安全和治理真空的系统性回应。
[查看原文](https://techcrunch.com/2026/07/14/deepmind-ceo-calls-for-an-independent-standards-body-to-regulate-frontier-ai/)

### 4. Anthropic 发现 LLM 内部「全局工作空间」(J-space)
Anthropic 可解释性团队发现 Claude 模型内部出现了类似人脑「全局工作空间 (Global Workspace)」的神经模式——J-space。这些模式是模型自发涌现的，允许 Claude 在不输出文字的情况下进行内部思考，对多步 Agent 推理至关重要。
[查看原文](https://www.anthropic.com/research/global-workspace)

### 5. Anthropic 经济指数报告：Agentic 任务已超越对话式使用
Anthropic 发布最新经济指数报告，关键发现：Claude Code 和 Cowork 的增长使 Claude 会话从对话形式转变为长时间运行的 agentic 任务；35% 受访者预测 AI 明年能完成他们大部分工作；自动化使用比例更高的用户对未来更乐观。
[查看原文](https://www.anthropic.com/research/economic-index-june-2026-report)

### 6. OpenAI 首款硬件设备曝光：可移动无屏扬声器
据报道，OpenAI 首款硬件设备是一款可移动的无屏扬声器，进一步模糊了 AI Agent 与物理世界的边界。这预示着 Agent 正在从纯软件向软硬件一体化方向演进。
[查看原文](https://techcrunch.com/2026/07/14/openais-first-hardware-device-is-reportedly-a-screenless-speaker-that-can-move/)

### 7. 纽约州叫停所有新数据中心建设
纽约州宣布暂停所有新数据中心的建设许可，反映出 AI 算力扩张与能源/环境政策之间的尖锐矛盾。此举可能影响美国东海岸的 AI Agent 算力供应格局。
[查看原文](https://techcrunch.com/2026/07/13/)

### 8. SIMA 2 和 AlphaEvolve：DeepMind 的专门化 Agent 矩阵
DeepMind 持续推进专门化 Agent：SIMA 2 是基于 Gemini 的 3D 虚拟世界 Agent，能够玩游戏、推理并与用户一起学习；AlphaEvolve 是基于 Gemini 的编程 Agent，结合 LLM 创造力和自动评估器进化算法。这表明巨头正在构建覆盖多领域的 Agent 矩阵。
[查看原文](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)

---

## 三、企业界 🏢

### 1. Nous Research 以 $1.5B 估值进行新一轮融资
Hermes Agent 开发商 Nous Research 正以 15 亿美元估值进行新一轮融资谈判，计划融资至少 7500 万美元，由 Robot Ventures 领投，USV 等重要投资机构参与。AI Agent 基础设施赛道的资本热度持续升温。
[查看原文](https://techcrunch.com/2026/07/13/hermes-agent-maker-nous-research-in-talks-for-new-funding-at-1-5b-valuation/)

### 2. PixVerse 完成 $439M 融资，估值突破 $2B
AI 视频生成初创公司 PixVerse 完成 4.39 亿美元融资，估值突破 20 亿美元。资金将用于扩展其世界模型产品和全球客户覆盖，视频 Agent 赛道再现重磅融资。
[查看原文](https://techcrunch.com/2026/07/13/video-generation-startup-pixverse-raises-439m-valuation-soars-past-2b/)

### 3. Reflection 与 Nebius 签署 $1B 计算合作
AI 公司 Reflection 与云计算提供商 Nebius 签署 10 亿美元计算合作协议，这是迄今为止 AI Agent 领域最大的基础设施合作之一，体现了 Agent 对算力的强劲需求。
[查看原文](https://techcrunch.com/2026/07/13/reflection-inks-1b-compute-deal-with-nebius/)

### 4. 趋境科技完成 A 轮融资，半年内募资 10 亿元
中国 AI 基础设施公司趋境科技完成 A 轮融资，半年内累计募资 10 亿元。其 AI Token 生产服务能力获产业和资本双重认可，为 Agent 运行提供底层算力支撑。
[查看原文](https://www.qbitai.com/2026/07/448820.html)

### 5. 百度 AI 搭子企业版发布，Agent 商业化加速
百度 AI 搭子在日均使用量暴增 20 倍后同步发布企业版，标志着中国科技巨头在 Agent 领域从 C 端实验转向 B 端商业化的关键一步。
[查看原文](https://www.qbitai.com/2026/07/447681.html)

### 6. Hinge 创始人融资 $18M 打造 AI 约会服务 Overtone
Hinge 创始人融资 1800 万美元打造全新 AI 约会服务 Overtone，展示了 AI Agent 在垂直消费领域的商业化潜力。
[查看原文](https://techcrunch.com/2026/07/14/the-founder-of-hinge-raised-18m-to-build-a-new-ai-dating-service-overtone/)

### 7. Sam Altman 太空数据中心言论引发行业讨论
Sam Altman 关于太空数据中心的言论引发广泛讨论。多位业内专家表示早已持有类似观点，暗示 AI Agent 算力需求的指数级增长可能推动数据中心向太空扩展。
[查看原文](https://techcrunch.com/2026/07/13/sam-altmans-space-data-center-trash-talk-is-what-most-experts-already-believe/)

---

## 四、学术界 🎓

### 1. Agent Hacks Agent：面向生产级 Agent 的自动化红队测试
来自多所机构的研究者提出面向生产级 LLM Agent（Claude Code、Codex 等）的自动化红队测试方法。论文指出，传统红队测试无法跟上 Agent 快速迭代的节奏，需要「Agent 攻击 Agent」的自动化方案来持续发现生产环境中的安全漏洞。
[查看原文](http://arxiv.org/abs/2607.11698v1)

### 2. MM-ToolSandBox：视觉工具调用 Agent 的统一评估框架
研究团队推出 MM-ToolSandBox，一个面向视觉工具调用 Agent 的基准测试和评估框架。框架提供有状态执行环境，覆盖 500+ 工具、16 个应用域，为多模态 Agent 的评估提供了标准化平台。
[查看原文](http://arxiv.org/abs/2607.11818v1)

### 3. 多智能体系统中的分布式后门诊断
论文指出当前多 Agent 系统的安全监控存在根本性漏洞：分布式后门攻击可以通过多个 Agent 协作隐藏恶意行为，单个 Agent 层面的监控无法检测。这对生产环境中部署多 Agent 系统提出了新的安全挑战。
[查看原文](http://arxiv.org/abs/2607.11751v1)

### 4. 超出单摄像头：体育视频理解中的 Agentic 多视角推理
研究者提出利用多模态大模型的 Agentic 推理能力处理体育视频中的密集遮挡、快速运动等复杂场景。结合多视角信息，Agent 可实现超越传统单视角方法的视频理解能力。
[查看原文](http://arxiv.org/abs/2607.11844v1)

### 5. 面向对话诈骗检测的可解释 Agentic 系统
研究者提出基于摘要记忆的可解释 Agentic 系统用于检测对话诈骗。该系统能够追踪跨越数周甚至数月的长对话，逐步建立信任检测模型，应对生成式 AI 助长的对话诈骗威胁。
[查看原文](http://arxiv.org/abs/2607.11707v1)

### 6. 从世界行动模型到具身大脑：开放世界物理智能路线图
论文描绘了从世界模型到具身 Agent 的技术路线图，涵盖行动模型、视觉-语言-行动策略和世界模型等核心技术，为构建能在物理世界中推理和行动的通用 Agent 提供了系统框架。
[查看原文](http://arxiv.org/abs/2607.11689v1)

### 7. PostTrain Bench 最新数据：GLM 5.2 领跑 Agent 编程基准
PostTrain Bench 最新排行榜显示，GLM 5.2 + Claude Code Max 以 34.29% 综合得分领跑，Opus 4.8 + Claude Code Max 以 34.08% 紧随其后，Fable 5 初步成绩 30.72%。在 Cursor 等编程 Agent 基准测试中，BFCL（工具调用）指标上 GPT 5.5 Codex CLI xHigh 达到了惊人的 99.25%，展示了 LLM 在 Agent 工具调用能力上的突破性进展。
[查看原文](https://posttrainbench.com)

### 8. Hacker News 头条：自主 Agent 的炒作与生产实践
一篇关于自主 Agent 生产实践的长文以 427 分、257 条评论登顶 Hacker News，系统分析了当前自主 Agent 的炒作与实际生产落地之间的差距，引发社区对 Agent 落地路径的深度讨论。
[查看原文](https://news.ycombinator.com/item?id=45812345)

---

## 五、开源项目 🛠️

### 1. awesome-llm-apps — 120K Stars 🔥
Shubhamsaboo/awesome-llm-apps 以单日 1,104 星的增长登顶 Trending，项目收集了 100+ 可直接运行的 AI Agent 和 RAG 应用，覆盖客服、数据分析、代码生成等场景。总星数突破 12 万。
[查看原文](https://github.com/Shubhamsaboo/awesome-llm-apps)

### 2. destructive_command_guard — Agent 安全守护者
Dicklesworthstone/destructive_command_guard 以单日 481 星的增长强势上榜，该项目专门阻止 AI Agent（如 Claude Code、Codex）执行危险的 git 和 shell 命令。在 Agent 安全日益受到关注的背景下，这类防护工具需求激增。
[查看原文](https://github.com/Dicklesworthstone/destructive_command_guard)

### 3. hallmark — 反 AI 塑料感设计技能
Nutlope/hallmark 以单日 1,010 星爆发，为 Claude Code、Cursor 和 Codex 提供反「AI-slop」设计技能，帮助 AI 编程 Agent 生成更具美感和人性化的 UI。总星数突破 6,000。
[查看原文](https://github.com/Nutlope/hallmark)

### 4. Vibe-Trading — 个人交易 Agent 爆火
港大数据科学实验室推出的 Vibe-Trading 以单日 1,265 星的增长位列 Trending，项目定位为「你的个人交易 Agent」。总星数突破 22,800，展示了 Agent 在金融领域的巨大需求。
[查看原文](https://github.com/HKUDS/Vibe-Trading)

### 5. agent-skills 和 agency-agents 登上 Star History 周榜
star-history 周趋势榜中，agent-skills（+24 星）和 agency-agents（+19 星）双双上榜，反映出社区对 Agent 可复用技能模块和 Agent 编排框架的强烈兴趣。「Skills」类项目整体霸榜，包括 skills（+44）、taste-skill（+38）、agent-skills（+24）、andrej-karpathy-skills（+21），Agent 技能生态正在形成。
[查看原文](https://www.star-history.com)

### 6. Metis Agent Starter Kit — 分钟级构建生产 Agent
Hacker News 上展示的 Metis Agent Starter Kit 承诺「数分钟而非数周」构建生产级 AI Agent，反映了市场对降低 Agent 开发门槛的迫切需求。
[查看原文](https://news.ycombinator.com/)

### 7. Agent-dir：基于 Git 的 A2A Agent 目录
Agent-dir 项目提出将 A2A（Agent-to-Agent）Agent 卡片推送到 Git，构建轻量级 Agent 目录。这一设计理念与 Google 的 Agent2Agent 协议相呼应，推动 Agent 间的互操作性。
[查看原文](https://news.ycombinator.com/)

### 8. Agency Protocol — 基于可验证承诺的域特定信任
HN 上展示的 Agency Protocol 提出通过可验证承诺实现 Agent 间的域特定信任，为多 Agent 协作的安全性问题提供了新的技术路径。
[查看原文](https://news.ycombinator.com/)

---

## 六、趋势分析与预测 📈

### 1. Agent 安全成为全行业核心议题
今日最突出的趋势是 Agent 安全的全面升温：从蚂蚁安全开源 Agent 安全框架，到 destructive_command_guard 在 GitHub Trending 爆发，到 arXiv 上多篇 Agent 安全相关论文（分布式后门、红队测试），再到 Apple 起诉 OpenAI 和 DeepMind CEO 呼吁建立独立 AI 标准机构——Agent 安全已从学术讨论进入产业实践。**预测**：Q3 将出现首个被广泛采用的 Agent 安全标准或认证体系。

### 2. AI Coding Agent 进入「军备竞赛」阶段
GPT-5.6 一小时证明 50 年数学猜想（64 子 Agent 协作）、Codex 移除 5 小时限制、Claude Fable 5 延长订阅、PostTrain Bench 编码基准日趋激烈——编码 Agent 的竞争白热化。同时，hallmark（反 AI 塑料感设计）和 skills 类项目的爆发表明，社区正在为 Agent 建立「品味」和质量标准。**预测**：下一阶段竞争将从「代码能跑」转向「代码好看且安全」。

### 3. 多 Agent 系统协作成为新范式
GPT-5.6 的 64 子 Agent 协同证明数学猜想、DeepMind 的专门化 Agent 矩阵（SIMA 2 + AlphaEvolve）、agency-agents 和 Agency Protocol 等项目的涌现——多 Agent 系统正在从实验走向生产。**预测**：年底前将出现首个商业化的多 Agent 编排平台，解决 Agent 间通信、信任和任务分配的标准问题。

### 4. 中国 Agent 创业生态快速成熟
今日中国 Agent 领域多维开花：Agent 专用搜索登顶 Product Hunt（产品创新）、浪潮信息发布 Agent 基础设施（底层硬件）、蚂蚁安全开源安全框架（安全生态）、清华 Physical AGI 演示（学术前沿）、趋境科技融资 10 亿（资本认可）、百度搭子企业版发布（商业化）。**预测**：中国将在 Q3 出现估值超 10 亿美元的 Agent 独角兽。

### 5. 企业级 Agent 基础设施投资爆发
今日融资动态密集：Nous Research $1.5B 估值、PixVerse $439M、Reflection $1B 计算合作、趋境科技 10 亿元——单日 Agent 相关融资/合作总额接近 25 亿美元。加上纽约州叫停数据中心建设、Sam Altman 太空数据中心言论，算力焦虑正在驱动基础设施投资。**预测**：2026 年下半年，Agent 基础设施（算力、安全、编排）的投资将首次超过基础模型本身的投资。
