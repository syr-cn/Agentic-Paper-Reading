# 01.me 文章阅读笔记

## 0) Metadata
- **Title:** From Memory to Cognition: How AI Agents Can Deliver Truly Personalized Services
- **Alias:** 01me-User-Memory-Cognition
- **Author / Org:** 01.me
- **Type:** Blog / Technical Talk Notes
- **Date:** 2025-10
- **Link:** https://01.me/en/2025/10/user-memory-for-ai-agent/
- **Tags:** user-memory, personalization, context-aware-retrieval, evaluation, proactive-agent
- **My rating:** ★★★☆☆
- **Read depth:** normal

## 1) TL;DR
- 把 Agent Memory 分成三层能力：基础召回 → 跨会话检索 → 主动服务。
- 强调“用户偏好学习”比“事实记忆”难很多，核心难点是上下文依赖与过度泛化。
- 推荐双层记忆架构：结构化 JSON 卡片（常驻）+ context-aware RAG（按需检索）。
- 给出评测框架：Rubric + LLM-as-judge，覆盖事实准确、召回完整、幻觉惩罚等维度。

## 2) 关键价值
- 对 Memory 的工程拆解很实用：表示（notes/json）- 检索（RAG/结构化索引）- 评测（rubric）。
- 观点与我们方向高度一致：主动服务是“存储+检索+推理”协同涌现，而非独立魔法模块。

## 3) 可迁移点
- 可迁移 1：给 memory 建立 Level-1/2/3 评测集，避免“看起来聪明”但不可验证。
- 可迁移 2：重要事实走结构化卡片，长尾细节走检索，降低上下文污染。
- 可迁移 3：对偏好学习显式区分“一次行为”与“稳定偏好”。

## 4) 局限
- 更偏系统设计经验总结，严格学术对照不足。
- 文中大量 case 需要统一 benchmark 才能横向比较不同方法。

## 5) Next Actions
- [ ] 给现有 agent 增加 L1/L2/L3 memory 能力打分表。
- [ ] 补一版 context-aware retrieval 的对照实验。
