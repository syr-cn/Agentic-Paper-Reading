# SkillOrchestra 阅读笔记

## 0 Metadata
- **Title:** SkillOrchestra: Learning to Route Agents via Skill Transfer
- **Alias:** SkillOrchestra
- **Venue / Status:** arXiv 2602.19672
- **Links:** Abs https://arxiv.org/abs/2602.19672 | PDF https://arxiv.org/pdf/2602.19672 | Code https://github.com/jiayuww/SkillOrchestra
- **My rating:** ★★★☆☆
- **Read depth:** skim
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = 3

## 1 一句话 Why-read
- 用“技能需求”做路由比 query-level 粗路由更可解释，也更易做性能-成本平衡。

## 2 CRGP
### C — Context
- 用“技能需求”做路由比 query-level 粗路由更可解释，也更易做性能-成本平衡。

### R — Related work
- - skill transfer 可显著降低路由学习成本。

### G — Research gap
- 待补证据（需从原文引言补充明确 gap 描述）

### P — Proposal
- - skill-aware routing + transfer，在 10 个 benchmark 报告优于多种 orchestrator。

## 3 Figure 区
- 待补证据（建议补 1 张方法图或主结果图）
- 可定位链接：- **Links:** Abs https://arxiv.org/abs/2602.19672 | PDF https://arxiv.org/pdf/2602.19672 | Code https://github.com/jiayuww/SkillOrchestra

## 4 Experiments
### 4.1 Experimental setup
- skill-aware routing + transfer，在 10 个 benchmark 报告优于多种 orchestrator。

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 原文摘要 | 原文未给出可提取数字 | 原文未给出可提取数字 | 原文未给出可提取数字 |

### 4.3 Analysis
- **现象：** skill transfer 可显著降低路由学习成本。
  **解释（作者）：** 待补证据。
  **【标注】（我的判断，可选）：** 待补证据。

## 5 Why it matters for our work
- 对你后续多 agent/多工具编排很实用，特别是成本约束下路由。

## 6 Actionable next step
- 在你现有流程记录“skill demand 特征”，做轻量路由器原型。

## 7 评分解释
- 维持原评分倾向，不做无根据上调。
- 不是更高分的原因：observation 有启发，但机制层分析深度一般。
