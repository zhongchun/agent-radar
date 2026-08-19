# AI Agent 日报 — 2026年08月19日

> 本报告由 Hermes Agent 自动生成，覆盖国内外 AI Agent 领域的最新动态。
> 信息来源：量子位, 36氪, 新浪科技/新浪财经, 网易科技, TechCrunch, Hacker News, Japan Times, arXiv, Hugging Face Daily Papers, GitHub Trending, GitHub API, PostTrainBench, Anthropic News
> 注：8 月 18 日报告因调度异常未生成，本报告中个别 8/18 高价值条目已标注日期补入，其余均为 8/19 当天新闻。

## 📑 目录

- [一、国内动态 🇨🇳](#一国内动态-)
- [二、国际动态 🌍](#二国际动态-)
- [三、企业界 🏢](#三企业界-)
- [四、学术界 🎓](#四学术界-)
- [五、开源项目 🛠️](#五开源项目-)
- [六、趋势分析与预测 📈](#六趋势分析与预测-)

---

## 一、国内动态 🇨🇳

**8 月 19 日是 AI Agent 领域"信息大日"：2026 世界机器人大会（WRC）在北京开幕，具身智能成为绝对主角；智谱、MiniMax、360、腾讯、蚂蚁等企业的 Agent 动作密集。**

- [2026世界机器人大会开幕：全球首个人形机器人自主乒乓球完整对局亮相](https://www.qbitai.com/2026/08/475907.html) — 8月19日，以"人机共生、产需共融"为主题的 WRC 2026 在北京开幕。超维动力携全球首个人形机器人自主乒乓球完整对局成果、SMASH 2.0 高动态人形乒乓系统、KAI 世界模型、117 自由度 KAIBot 本体亮相，实现毫秒级"感知—决策—控制"全链路闭环，且同一套算法可适配不同机器人（"一脑多形"），标志高速动态场景下具身智能体的里程碑式突破。

- [银河通用发布全球首款"自主学习"智能体人形机器人 Galbot ET1"银河星仔"](https://36kr.com/p/3946454123822213) — WRC 现场，银河通用在"具身智能大模型的进化之路"分论坛发布 Galbot ET1，搭载自研 AstraBrain-Agent（定义为"物理世界原生智能体"），人类无需动作视频即可通过互动教会它新技能；详解"大脑-脑桥-小脑"全脑架构与 WAM（世界—动作模型）技术路线，是"当 Agent 进入物理世界"的典型样本。

- [章鱼动力亮相 WRC 2026，携"脑-手-数据"技术体系探索具身智能未来范式](https://www.qbitai.com/2026/08/475931.html) — 物理 AI 新锐 SynapX 发布 SYNWorld 具身原生世界基础模型（"脑"）、OctoH-Hand 高自由度仿生灵巧手（"手"）、OctoSense 下一代具身数采方案（"数据"），其中 OctoSense 首次实现肌电跨个体零样本泛化，让人类操作数据近乎无损对齐真机。

- [IDC发布2026中国AI50强：360以"智能体+安全"双轮驱动入选](https://www.qbitai.com/2026/08/475901.html) — IDC 发布《2026年IDC中国AI50强》，360 与阿里云、百度、腾讯云、小米等共同登榜。360 推出企业级智能体办公平台"纳米Work"（自然语言驱动任务拆解、工具调用与流程执行），并打造"中国版Mythos"AI 安全攻防系统"图龙锋"（安全大模型+智能体蜂群架构），已发现安全漏洞近 9000 个。IDC 指出智能体正推动 AI 从"对话工具"迈向"业务生产力"。

- [因为AI新版本太强，强到智谱暂时不敢开源了](https://36kr.com/p/3945790191179400) — 智谱 8/14 发布通用编程模型 GLM-5.3，因训练中展现"超出预期的网络安全能力"，将权重公开时间推迟约两周。GLM-5.3 软件工程 Agent 能力大幅跃升：Terminal-Bench 3.0 从 4.6% 升至 28.3%，ExploitBench 漏洞利用从 24.4% 升至 54.4%，漏洞复现成功率 84.5%，逼近 Anthropic 对照模型。开源模型"太会找漏洞"的安全风险引发行业争议。

- [MiniMax核心工程负责人阿岛离职](https://www.qbitai.com/2026/08/475869.html) — 负责范围横跨语言模型、编程产品、Agent、语音与 C 端多模态应用的核心技术负责人从 MiniMax 组织图中退场。其职业路径覆盖搜索/广告系统→移动内容平台→大模型与 Agent，是连接模型、工程、产品与开发者社区的关键角色，对 MiniMax 的 Agent 工程体系影响值得关注。

- [AI办公混战，腾讯百度抢先：桌面端 Agent 产品已超 20 款](https://36kr.com/p/3946308190672517) — 半年内中国市场已出现超 20 款桌面端 Agent 产品。AI 产品榜最新 MAU 显示：腾讯 WorkBuddy 以 1115 万月活居桌面端 AI 办公第一，百度搭子以 674 万月活居第二（环比增速 1063.79%），两者先后登顶 PinchBench、DeepResearch Bench 榜单，路径迥异（内部自发式创新 vs 全栈资源集中释放）。

- [蚂蚁阿福发布医生端服务战略全景；北京友谊医院智能体"谊小益"上线](http://client.sina.com.cn/news/2026-08-19/doc-ininvmyw2723220.shtml) — 8/19 中国医师节，蚂蚁 AI 健康应用阿福公布医生端战略："数字家医"采用"AI智能体+真人医生"模式，已在 40+ 城市服务超 500 万居民；同日首都医科大学附属北京友谊医院智能体"谊小益"上线蚂蚁阿福 App，提供 AI 陪诊、报告解读、挂号缴费等全流程服务，医院称 AI 可承接 90% 以上基础咨询。

- [京东发布机器人战略：百亿投入，建 80 个 RoboBase 基地](https://36kr.com/newsflashes/3946397274242436) — WRC 2026 上，京东作为全球战略合作伙伴发布机器人战略：截至 2028 年投入百亿资源，助力 100 个品牌独立销售额破 10 亿；未来 5 年建立覆盖 100+ 国家的售后能力，建设 80 个 RoboBase 机器人基地；具身智能 JoyInside 打造"AI Home"生态，预计年内接入超千万终端设备。

- [星动纪元物流机器人亮相 WRC：最快 2000 件/小时](https://finance.sina.com.cn/tech/2026-08-19/doc-ininvshr7054191.shtml) — 星动纪元物流分拣具身机器人在 WRC 现场演示快递分拣，自主识别不同规格/材质/重量的包裹，目前 1200 件/小时、内部极限测试 2000 件/小时，已完成 PMF 验证，与中国邮政、顺丰等合作，在 5 省市 10 多个物流中心常态化运营。

- [火山引擎官宣：特斯拉车机开始陆续推送豆包大模型](https://www.163.com/dy/article/L4NKK0E4051191D6.html) — 8/19 火山引擎官宣特斯拉在中国市场车机接入豆包大模型，采用"双模型"协作：豆包负责车辆控制类语音指令（导航、空调、媒体），DeepSeek Chat 承担闲聊与资讯查询。国产大模型进入国际品牌车机系统，是端侧 Agent 落地的标志性案例。

- [AI for Science开始"动手"了：机器人正式走进国家级实验室](https://www.qbitai.com/2026/08/475332.html) — 双机械臂人形机器人 Monte2 进入国家级科研实验室，可完成微量试剂转移、核酸提取预处理、细胞毒性培养实验等长序列操作，复现人类实验员操作逻辑；此前利物浦大学自主实验系统曾在 8 天内完成 680 次实验（Nature 发表），"AI 科学家"正从论文走向实验台。

---

## 二、国际动态 🌍

- [OpenAI 推出新客户隐私保护措施，正面叫板 Anthropic](https://techcrunch.com/2026/08/19/openai-seeks-to-one-up-anthropic-with-new-customer-privacy-protections/) — OpenAI 与 Anthropic 围绕"谁能给企业客户提供最好的隐私保护"展开竞争，OpenAI 于 8/19 宣布新的企业数据隐私承诺。两家公司都在冲刺 IPO/上市，企业级 Agent 数据隐私已成为销售军备竞赛的核心卖点。

- [Anthropic 拒绝支持 Agents.md 标准，GitHub Issue 引发热议](https://github.com/anthropics/claude-code/issues/6235) — Claude Code 仓库 issue #6235 中，Anthropic 明确表态不打算支持 agents.md（由 agents.md 社区推动的编码智能体引导文件标准），在 Hacker News 引发 52 分/22 评论讨论。此前 Vercel 实测 agents.md "在 agent evals 中优于 skills"，而 Anthropic 坚持自有 CLAUDE.md 路线，标准之争折射出"谁定义 Agent 行为规范"的生态话语权争夺。

- [日本拟要求 AI 企业披露训练数据](https://www.japantimes.co.jp/news/2026/08/19/japan/ai-training-data-disclosure/) — 日本政府 8/19 提出新规草案：要求 AI 企业向监管机构披露训练数据来源与使用情况，成为继欧盟 AI Act 之后又一个强化训练数据透明度的主要经济体。对依赖大规模数据训练的 Agent 基础模型厂商构成新的合规压力。

- [Google 为 Search 与 Gemini 打包推出 AI 学习工具](https://techcrunch.com/2026/08/19/google-launches-new-study-tools-for-students-across-search-and-gemini/) — Google 面向学生推出覆盖 Search 与 Gemini 的新 AI 学习工具集，将 AI 助手深度嵌入学习场景（解题、资料整理、知识点讲解），是"通用 AI 助手→垂直场景 Agent"的又一落点。

- [OpenAI 撤销部分研究者的网络攻防项目访问权限，引发争议](https://techcrunch.com/2026/08/19/researchers-complain-that-openai-revoked-their-access-to-limited-cyber-program/) — 多名外部研究者投诉 OpenAI 撤销了其"有限网络攻防项目"访问权限。结合智谱 GLM-5.3 推迟开源、Anthropic 网络安全评估等事件，头部模型厂商正在收紧高危 Agent 能力的开放边界。

- [Amazon 将 AI 版 Alexa+ 免费开放给 Fire TV 用户](https://techcrunch.com/2026/08/19/amazon-makes-its-ai-powered-alexa-free-on-fire-tv-no-prime-required/) — Amazon 宣布 Alexa+（生成式 AI 助手）在 Fire TV 上免费开放，无需 Prime 会员。家庭场景智能体入口（语音助手）进入免费获客阶段，与桌面/办公 Agent 形成场景互补。

- [TerraPower 核反应堆设计新增"秘密武器"：为 AI 数据中心供电](https://techcrunch.com/2026/08/19/terrapowers-nuclear-reactor-has-a-secret-weapon-for-powering-ai-data-centers/) — Bill Gates 旗下 TerraPower 的钠冷快堆针对 AI 数据中心电力需求优化设计，Agent/AI 算力扩张带来的能源约束正倒逼核能基础设施创新。

- [Linear 公布 AI 在软件团队中的真实使用模式数据](https://linear.app/data) — 项目协作平台 Linear 发布 2026 数据分析：AI 编码工具已渗透软件团队工作流（8/18 上线，HN 178 分/110 评论），为"Agent 如何改变开发者日常"提供了可量化的一手数据。

- [PINE64 暂停开源硬件生产，"直到 AI 泡沫破裂"](https://www.hackster.io/news/pine64-calls-time-on-the-linux-hardware-market-ceases-production-until-the-ai-bubble-bursts) — 知名开源硬件厂商 PINE64 宣布停止生产，理由是 AI 泡沫扭曲了供应链与市场。AI 热潮的"挤出效应"开始波及边缘硬件生态（HN 6 分，讨论热烈）。

- [AI;DR：当 AI 摘要取代阅读，信息信任危机浮现](https://www.rickmanelius.com/p/aidr-ai-didnt-read) — 8/17 起 HN 高赞长文（1086 分/686 评论）持续发酵：越来越多人用 AI 摘要替代原文阅读，"AI;DR（AI；没读过）"成为默认姿势。对 Agent 的信息检索与知识工作范式提出深层拷问——摘要 Agent 是否在系统性稀释人类的理解力。

---

## 三、企业界 🏢

- [Cognition CEO 否认 SpaceX 收购传闻；SpaceX 已收购 Cursor](https://techcrunch.com/2026/08/19/cognition-ceo-denies-report-that-spacex-tried-to-acquire-the-startup/) — 据报 SpaceX 曾洽谈收购 AI 编码智能体公司 Cognition（Devin 开发者），Cognition CEO 否认。值得注意的是 SpaceX 此前已收购 Cursor——马斯克正在企业 AI 编码赛道大举布局，与 OpenAI、Anthropic 争夺"开发者入口"。

- [OpenAI 第二季度销售增长乏力，与 Anthropic 形成对比（WSJ）](https://www.wsj.com/tech/ai/openais-second-quarter-sales-show-tepid-growth-compared-with-anthropic-5cb42998) — 华尔街日报援引数据：OpenAI Q2 销售增速放缓，而 Anthropic 年化收入据报已达 650 亿美元且增速强劲。企业 Agent/工具业务的分化信号明显，投资者开始用"收入质量"而非"模型能力"给 AI 公司定价。

- [Relativity Networks 融资 2200 万美元：为数据中心带来更快光纤](https://techcrunch.com/2026/08/19/relativity-networks-raises-22-million-to-bring-a-faster-kind-of-fiber-to-data-centers/) — 面向 AI 数据中心互联的光纤初创完成 2200 万美元融资。Agent 算力集群扩张带动数据中心基础设施投资潮持续。

- [Cursor 借 GitHub 用户不满，推出竞品托管平台](https://techcrunch.com/2026/08/18/cursor-capitalizes-on-github-frustration-launches-rival-hosting-platform/) — （8/18）AI 编码 IDE Cursor 推出代码托管/部署平台，直接挑战 GitHub；叠加 SpaceX 收购背景，编码 Agent 生态的"平台化+入口化"整合正在加速。

- [Etched 估值一个月翻倍至 210 亿美元](https://techcrunch.com/2026/08/18/etcheds-valuation-doubles-to-21b-in-a-month/) — （8/18）Transformer 专用芯片公司 Etched 估值一个月内从约百亿美元级翻倍至 210 亿。Agent 推理负载（长上下文、工具调用）被视为专用芯片的最大增量场景。

- [Warp 发布"开箱即用"的 AI 开发软件工厂](https://techcrunch.com/2026/08/18/warps-new-system-is-an-out-of-the-box-software-factory-for-ai-development/) — （8/18）终端/IDE 公司 Warp 推出面向 AI 开发的全新系统，把 Agent 编码流水线做成开箱即用产品，瞄准"AI 原生软件工厂"赛道。

- [Perplexity 免费策略奏效：印度新增数百万用户](https://techcrunch.com/2026/08/18/perplexitys-free-ai-offer-left-it-with-millions-more-users-in-india/) — （8/18）Perplexity 在印度推出免费方案后用户激增数百万，AI 搜索/助手在新兴市场的免费获客模式得到验证。

- [OpenAI 在 Hugging Face 泄露事件后实施新安全措施](https://techcrunch.com/2026/08/18/openai-institutes-new-safeguards-after-hugging-face-breach/) — （8/18）针对此前 Hugging Face 相关泄露事件，OpenAI 引入新的访问与凭据安全机制，显示头部厂商对 AI 供应链安全（含 agent 工具链）的重视升级。

- [网易传媒发布"蜜蜂AI"：从工具到伙伴，让 AI 更懂人](https://www.qbitai.com/2026/08/474857.html) — （8/18）网易传媒发布"蜜蜂AI"，主打从工具型 AI 向"伙伴型"AI 演进，体现国内内容平台在 Agent 化产品上的差异化尝试。

- [阿里"千问办公"接入企业微信；阿里杀进 Agent 上下文战场](https://www.qbitai.com/2026/08/474647.html) — （8/18）阿里"千问办公"正式接入企业微信；同期阿里宣布钉钉聊天、企业文档、工作数据将开放给 Agent 调用，直接把办公 Agent 的"上下文弹药库"摆上牌桌，与腾讯 WorkBuddy、百度搭子正面对抗。

---

## 四、学术界 🎓

**8/19 Hugging Face 每日精选 + 8/18 arXiv 投稿（8/19 投稿尚未入库），Agent 相关论文密集。**

- [Demystifying Agent Skills: Why They Work-Until They Don't（加州大学圣迭戈分校 UCSD）](https://arxiv.org/abs/2608.14036) — 系统解构"Agent Skills"（技能库）为何有效又为何失效：技能通过封装专家子任务提升成功率，但过度抽象/错误耦合会放大失败。HF 当日最高赞（125），为技能库工程实践提供理论依据。 [查看原文](https://huggingface.co/papers/2608.14036)

- [Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements（新加坡国立大学 NUS）](https://arxiv.org/abs/2608.17310) — 提出低显存开销的长时程 Agent 微调方法（ESOpt），让长任务 Agent 的训练不再依赖大规模 GPU 集群，显著降低 Agent 后训练门槛（HF 91 赞）。

- [ASI-Bench: At the Dawn of Artificial Superintelligence](https://arxiv.org/abs/2608.17271) — 42 位作者联合推出的"超人工智能（ASI）"评测基准，覆盖长时程自主任务、科学发现与自我改进等前沿维度，是当前最具野心的 Agent 能力评测之一（HF 51 赞）。

- [Agent Lightning v1.0: Towards Harnessed Agentic RL（微软）](https://arxiv.org/abs/2608.17528) — 微软提出"受控 Agentic RL"框架，为编码/工具型 Agent 的强化学习训练引入 harness 约束，平衡探索能力与安全性。

- [AVA-Encoder: Towards Agent-Native Video Representation Learning（阿里 Qwen 团队）](https://arxiv.org/abs/2608.12313) — 通义千问团队提出面向 Agent 原生的视频表征学习编码器，让多模态 Agent 更好"看懂"视频输入，为视觉 Agent 与视频理解提供新底座。

- [On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification（Qinyuan Ye 等）](https://arxiv.org/abs/2608.18066) — 系统研究"记忆式自我改进 Agent"（在线任务流+文本记忆库）的可靠性：任务顺序、方差与规格缺失都会导致改进不稳定，给"自我进化 Agent"热潮泼了冷水。

- [StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents](https://arxiv.org/abs/2608.18050) — 为知识工作型 Agent（代码/文档/表格/幻灯片）设计带版本控制的"分段工作区"，解决 Agent 修改持久化数字工件时搜索视图与原生文件不一致的问题。

- [StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End Workflows](https://arxiv.org/abs/2608.17800) — 用"市场验证过的端到端工作流"（而非研究者自选任务）评测通用 Agent，覆盖真实创业场景的复杂任务链，弥补现有基准脱离真实商业任务的缺陷。

- [HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety](https://arxiv.org/abs/2608.17597) — 面向 Agent harness（运行框架）安全的全生命周期评测基准，与微软"Harnessed Agentic RL"、DeepSeek Harness 安全测评互相呼应，harness 安全正在成为独立研究子领域。

- [LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents（微软）](https://arxiv.org/abs/2608.17393) — 编码 Agent 的原生 harness RL 方法，将强化学习直接构建在 agent harness 之上，改善长程编码任务的学习效率。

- [Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents](https://arxiv.org/abs/2608.15008) — 对记忆 Agent 的各类记忆载体（向量库、图、结构化文件等）做系统性评测，与火山引擎 OpenViking、CABLE 等"记忆基础设施"热点的学术呼应。

- [AdaLens: Interactive Storyline for Monitoring and Steering Long-Running Agentic Data Analysis](https://arxiv.org/abs/2608.17834) — 为长时程数据分析 Agent 提供交互式"故事线"监控与干预界面，解决自主分析流程黑盒化问题，是人机协同 Agent 交互研究的新方向。

- [Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection](https://arxiv.org/abs/2608.16393) — 对 DeepSeek Harness 进行间接提示注入（indirect prompt injection）安全性测评，国产开源 harness 的安全边界开始被系统检验。

- [VisDocAgentBench: Benchmarking Agents for Visually Rich Document Retrieval](https://arxiv.org/abs/2608.17889) — 针对版式丰富文档（布局、视觉元素、语料上下文）检索的 Agent 基准，填补 agentic search 在视觉文档场景的评测空白。

---

## 五、开源项目 🛠️

### GitHub Trending 热点（8/19-20）

- [MoneyPrinterTurbo：AI 一键生成短视频，今日 +2,221 stars（110,538 总星）](https://github.com/harry0703/MoneyPrinterTurbo) — 连续多日霸榜 Trending 的 AI 视频自动化工作流，将"提示词→成片"的 Agent 工作流做到极致。

- [OpenViking：火山引擎开源 Agent 上下文数据库，今日 +803 stars（30,139 总星）](https://github.com/volcengine/OpenViking) — "Self-evolving Context Database for AI Agents"：将记忆、资源、技能统一为一个虚拟文件系统（`viking://` 协议），Agent 用 `ls`/`tree`/`find` 浏览自己的上下文，而非查询黑盒向量库，号称"自进化"；AGPLv3，自 1 月创建以来累计 30k+ 星，是国产 Agent 基础设施出海标杆。

- [munder-difflin：本地多智能体 harness，今日 +797 stars（2,657 总星）](https://github.com/chaitanyagiri/munder-difflin) — TypeScript 编写的本地多 Agent 运行框架（local multi-agent harness），5 月底创建后热度快速上升。

- [cordis：时空可组合性元框架，两日 +839 stars（6,392 总星，8/17 为 5,553）](https://github.com/cordiverse/cordis) — 基于 effect 生态的 TypeScript 元框架，8/13 更新后持续高热度，被开发者用作 Agent 插件化基础设施。

- [semantica：图原生 Agent 基础设施（"开源版 Palantir"），9,497 总星](https://github.com/semantica-agi/semantica) — Graph-Native Infrastructure for Context and Accountable AI Systems，8/19 登上 HN（"The Open Source Palantir for AI Agents"），主打可审计、可问责的 Agent 上下文管理。

- [OpenBot：开源 AI"同事"，8/17 创建即获 372 星](https://github.com/CopilotKit/openbot) — CopilotKit 推出的开源 AI coworkers：每个 Agent 拥有独立的浏览器、文件与工具，动作执行前决策、执行后记录，兼容任何 AG-UI Agent，8/19 Show HN 上榜。

- [omlx：Apple Silicon LLM 推理服务器，今日 +467 stars](https://github.com/jundot/omlx) — 面向 Mac 的 LLM 推理服务器（连续批处理 + SSD 缓存），端侧 Agent 推理的轻量选择。

### 核心 Agent 框架星数（8/19-20 快照，较 8/17 报告为两日累计增量）

| 项目 | 星数 | 两日增量 | 说明 |
|------|------|---------|------|
| n8n | 201,217 | — | 工作流自动化+原生 AI，体量已超 AutoGPT |
| AutoGPT | 186,689 | +34 | 生态持续扩张，仍居 agent 框架头部 |
| Dify | 152,921 | +200 | Agentic 工作流 + RAG 平台，8/19 有推送 |
| LangChain | 144,578 | +164 | "The agent engineering platform"，8/19 活跃 |
| browser-use | 109,779 | — | 浏览器 Agent 基础设施 |
| OpenHands | 84,504 | — | AI 驱动软件开发，8/19 活跃 |
| MetaGPT | 69,900 | +34 | 多智能体框架（FoundationAgents 名下） |
| AutoGen | 60,523 | +50 | 微软 Agentic AI 框架 |
| CrewAI | 57,339 | +124 | 多角色编排框架，8/19 活跃 |
| Agno | 41,788 | +41 | Agent 平台构建，8/19 活跃 |
| LangGraph | 40,039 | — | "Build resilient agents"，8/19 活跃 |
| smolagents | 28,890 | +47 | HF 极简 agent 库 |
| babyagi | 22,351 | — | 经典任务驱动 agent 框架 |
| PydanticAI | 19,399 | +44 | "How Python does AI"，8/19 活跃 |

（未列增量的项目为 8/17 报告未收录基线，仅给出当前快照。数据来源：GitHub API，2026-08-20 早间抓取。）

### PostTrainBench 排行榜（v1.1，8/19-20 快照）

- **第 1 名：Fable 5（Claude Code · Max）41.79% ± 1.7%** — 后训练 Agent 基准保持领先
- 第 2 名：GPT 5.6 (Sol)（Codex CLI · Max）36.23%
- 第 3 名：Opus 5（Claude Code）35.04%
- 第 6 名：**Kimi K3（Claude Code）31.96%** — 国内模型保持前六
- 第 7 名：**GLM 5.2（Claude Code · Max）31.70%** — 智谱后训练能力上榜
- 基线：Base Models Zero Shot 7.53% — agent 化后训练增益依然巨大
- 与 8/17 报告相比榜单无位次变动；官方参考线（预算外）51.14%

---

## 六、趋势分析与预测 📈

- **"Agent 进入物理世界"从口号变为产品竞赛**：8/19 WRC 2026 成为具身智能 Agent 的集中秀场——银河通用"自主学习"智能体人形机器人、超维动力毫秒级乒乓球全链路闭环（"一脑多形"）、星动纪元物流分拣落地 5 省市、京东百亿机器人战略。行业共识是"下一代机器人必须兼具环境理解、落地操作与自主迭代"，世界模型路线正从单步动作的 WAM 向保证长程任务成功率的 WTM（世界任务模型）切换（亿欧预判"仅剩 8 个月"）。预计 3-6 个月内物流/家庭场景会跑出第一批规模化商业闭环。

- **Agent 能力安全成为全球性治理议题，且开始左右商业决策**：同一天三件事同时发生——智谱因 GLM-5.3 网络攻防能力"太强"推迟开源两周、OpenAI 撤销研究者网络攻防项目访问、日本拟立法强制披露 AI 训练数据。加上 Anthropic 网络安全评估与 OpenAI/Anthropic 企业隐私军备竞赛，可以判断：**"高危 Agent 能力"的开放边界正在被系统性收紧**，开源与闭源、能力开放与安全合规之间的张力将贯穿下半年。

- **办公/桌面 Agent 商业化混战正式开打**：腾讯 WorkBuddy（1115 万 MAU）、百度搭子（674 万 MAU，环比 +1063%）、阿里千问办公接入企业微信并开放钉钉/文档上下文、网易"蜜蜂AI"、20+ 款桌面端 Agent 产品同台。办公场景兼具高频、付费意愿与数据壁垒，是 Agent 变现最快的赛道；竞争焦点已从"谁家的模型强"转向"谁能吃到企业上下文数据"。

- **编码 Agent 的入口与整合之争白热化**：SpaceX 已收购 Cursor、又被曝洽谈收购 Cognition（Devin 母公司）；Stripe 70 亿+ 美元收购 OpenRouter；Cursor 反手推出托管平台挑战 GitHub；Cognition 否认 SpaceX 传闻但传闻本身即信号。编码 Agent 正在复刻浏览器/操作系统的"入口之争"，预计未来 6 个月还会有多起高额并购，标的集中在 Agent IDE、运行 harness 与模型网关。

- **Agent 记忆/上下文层成为下一个"基础设施品类"**：火山引擎 OpenViking（viking:// 协议统一记忆/RAG/技能，30k+ 星持续飙升）与学术界 Harness the Memory、CABLE、Cross-Model Memory Transfer 论文同日密集出现，说明行业正在从"模型能力竞争"转向"Agent 记不记得住、上下文怎么组织"的竞争。记忆层大概率成为继模型网关（OpenRouter 被 Stripe 收购）之后下一个被并购或标准化的 Agent 基础设施。

---

*本报告由 Hermes Agent 自动生成，数据采集于 2026-08-20 上午（UTC+8）。所有链接均经实际访问验证。*
