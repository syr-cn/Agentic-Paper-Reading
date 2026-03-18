# SkillOrchestra 阅读笔记

## 0) Metadata
- **Title:** SkillOrchestra: Learning to Route Agents via Skill Transfer
- **Alias:** SkillOrchestra
- **Venue / Status:** arXiv 2602.19672
- **Links:**
  - HTML: https://arxiv.org/html/2602.19672v1
  - PDF: https://arxiv.org/pdf/2602.19672
  - Code: https://github.com/jiayuww/SkillOrchestra
- **Read depth:** skim
- **My rating (★☆☆☆☆~★★★★★):** ★★★☆☆ (3/5)

## 1) TL;DR
- 关注 compound AI 的路由编排，反对粗粒度 query-level routing。
- 用显式 skill 建模 agent 的能力与成本，再做性能-成本权衡路由。
- 在 10 个 benchmark 上，相比 RL orchestrator 报告最高 +22.5%，学习成本显著下降（700x/300x）。

## 2) Notes
- 技能视角用于路由是亮点：解释性和 sample efficiency 都更强。
