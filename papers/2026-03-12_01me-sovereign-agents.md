# 01.me 文章阅读笔记

## 0) Metadata
- **Title:** Sovereign Agents: In-Depth Research on Clawdbot/OpenClaw
- **Alias:** 01me-Sovereign-Agents
- **Author / Org:** 01.me
- **Type:** Blog / System Research Report
- **Date:** 2026-01
- **Link:** https://01.me/en/2026/01/clawdbot-openclaw-analysis/
- **Tags:** sovereign-agent, local-first, memory-system, multi-tool-agent, security
- **My rating (★☆☆ / ★★☆ / ★★★):** 4.8
- **Read depth:** normal

## 1) TL;DR
- 文章提出“主权 Agent”三要素：数据主权、算力主权、控制主权。
- 将通用 Agent 能力拆为 Deep Research + Computer Use + Coding，并强调 Coding Agent 是核心底座。
- 重点分析 OpenClaw 架构：多通道网关、工具策略、Markdown 记忆层、执行沙箱。
- 同时强调安全现实：prompt injection、供应链插件风险、端口暴露，建议 Docker + HITL + 审计。

## 2) 关键价值
- 对“本地优先 + 可审计 memory（Markdown + Git）”的论证非常契合我们当前路线。
- 对 Agent 体系工程化拆分清晰，适合直接映射到我们自己的系统模块。

## 3) 可迁移点
- 可迁移 1：memory 使用“可读可改可版本化”优先于黑盒向量仓。
- 可迁移 2：工具权限采用多层策略级联（profile/provider/agent/channel/sandbox）。
- 可迁移 3：高风险动作默认 HITL 审批，形成“可用但可控”的执行边界。

## 4) 局限
- 文章带较强立场（开放/主权），部分市场结论偏叙事驱动。
- 架构性能与安全收益的量化数据仍有限。

## 5) Next Actions
- [ ] 给现有系统补一版工具权限级联表与默认 deny 策略。
- [ ] 增加 prompt injection 演练清单和审计回放流程。
