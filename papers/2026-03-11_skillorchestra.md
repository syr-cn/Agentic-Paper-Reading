# SkillOrchestra 阅读笔记

## 0) Metadata
- **Title:** SkillOrchestra: Learning to Route Agents via Skill Transfer
- **Alias:** SkillOrchestra
- **Venue / Status:** arXiv 2602.19672
- **Links:** Abs https://arxiv.org/abs/2602.19672 | PDF https://arxiv.org/pdf/2602.19672 | Code https://github.com/jiayuww/SkillOrchestra
- **My rating:** ★★★☆☆
- **Read depth:** skim
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = 3

## 1) Core Insight
- 用“技能需求”做路由比 query-level 粗路由更可解释，也更易做性能-成本平衡。

## 2) Interesting Observations
- skill transfer 可显著降低路由学习成本。
- 路由器学的是“任务需要什么能力”，而不是“这个问题像谁”。
- 在多 benchmark 上收益稳定，但更偏系统工程收益。

## 3) Evidence / Method
- skill-aware routing + transfer，在 10 个 benchmark 报告优于多种 orchestrator。

## 4) Why It Matters for Your Work
- 对你后续多 agent/多工具编排很实用，特别是成本约束下路由。

## 5) Actionable Next Step
- 在你现有流程记录“skill demand 特征”，做轻量路由器原型。

## 6) Why not higher score
- 不是更高分的原因：observation 有启发，但机制层分析深度一般。
