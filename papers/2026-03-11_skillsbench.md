# SkillsBench 阅读笔记

## 0) Metadata
- **Title:** Benchmarking How Well Agent Skills Work Across Diverse Tasks
- **Alias:** SkillsBench
- **Venue / Status:** arXiv 2602.12670
- **Links:** Abs https://arxiv.org/abs/2602.12670 | PDF https://arxiv.org/pdf/2602.12670
- **My rating:** ★★★★☆
- **Read depth:** skim
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 2 = 4

## 1) Core Insight
- 真正价值在于把“技能有效性”从主观印象变成可验证评测：很多自生成技能并不带来收益，curated 技能才稳定有效。

## 2) Interesting Observations
- curated skills 平均提升显著，但 self-generated skills 平均几乎无收益。
- 2-3 个聚焦技能常优于“超长技能文档”。
- 小模型 + 高质量技能可逼近大模型无技能表现，说明 skill quality 是一级杠杆。

## 3) Evidence / Method
- 86 任务、11 领域，配 deterministic verifiers 的统一评测框架。

## 4) Why It Matters for Your Work
- 直接告诉你该投资源在“技能质量与评测协议”，而非盲目扩技能数量。

## 5) Actionable Next Step
- 用 SkillsBench 思路给你的 skill 库做 quality gate（新增技能先过 verifier）。

## 6) Why not higher score
- 不是更高分的原因：核心在评测框架，方法创新侧相对有限。
