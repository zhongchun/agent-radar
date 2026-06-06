# Agent Radar

AI Agent 领域每日雷达 —— 自动抓取、聚合、总结最新动态

> Daily radar for the AI Agent ecosystem — tracking news, open-source projects, and trends automatically.

## 做什么

每天自动扫描以下信息源，生成一份简洁的 AI Agent 日报：

- **新闻动态** — 主流科技媒体、博客、Twitter/X 上关于 AI Agent 的最新报道
- **开源项目** — GitHub Trending、Hugging Face 上新出现的 Agent 框架/工具/论文复现
- **论文速递** — arXiv 上最新的 Agent 相关论文
- **产品发布** — 各大 AI 公司（OpenAI、Anthropic、Google 等）的 Agent 产品更新

输出格式：

```
Agent Radar 日报 · 2026-06-06
═══════════════════════════════
🔔 新闻  |  3 条
⭐ 开源  |  5 个
📄 论文  |  2 篇
🚀 产品  |  1 个
═══════════════════════════════
[详细摘要...]
```

## 路线图

- [ ] 数据源对接（GitHub API / arXiv API / RSS / X API）
- [ ] 去重 & 排序（按热度/话题/时效）
- [ ] LLM 摘要生成
- [ ] 日报渲染输出（Markdown / Feishu 文档 / 终端）
- [ ] 定时调度（每日自动运行）
- [ ] 历史归档 & 趋势回顾

## 技术栈

| 层 | 技术 |
|----|------|
| 数据采集 | GitHub API, arXiv API, RSS, X API |
| 数据处理 | Python, SQLite |
| AI 摘要 | LLM API (DeepSeek / OpenAI) |
| 输出分发 | Markdown, Feishu Lark, 终端 |
| 调度 | cron / Hermes Agent Cronjob |

## 使用

```bash
# TODO: 克隆后安装依赖
pip install -r requirements.txt

# TODO: 运行一次扫描
python -m agent_radar.scan

# TODO: 每日自动运行
python -m agent_radar.daily
```

## License

MIT © 2026 bermaker
