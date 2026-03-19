# AutoSkill 阅读笔记

## 0) Metadata
- **Title:** Experience-Driven Lifelong Learning via Skill Self-Evolution
- **Alias:** AutoSkill
- **Authors / Org:** Yutao Yang*, Junsong Li*, Qianjun Pan*, Bihao Zhan, Yuxuan Cai, Lin Du, Jie Zhou†, Kai Chen†, Qin Chen, Xin Li, Bo Zhang, Liang He（ECNU + Shanghai AI Lab）
- **Venue / Status:** arXiv 2603.01145（cs.AI，preprint）
- **Date:** 2026-03
- **Links:**
  - Abs: https://arxiv.org/abs/2603.01145
  - PDF: https://arxiv.org/pdf/2603.01145
  - Code: https://github.com/ECNU-ICALK/AutoSkill
- **Tags:** lifelong-learning, agent-memory, skill-evolution, personalization, training-free
- **My rating:** ★★★☆☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = 3

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：** 将“长期记忆”从文本片段提升为可版本化、可复用的技能工件（SKILL.md），以 training-free 方式实现跨会话个性化持续演化。

## 2) CRGP 拆解（必填）
### C — Context
- 长期个性化 agent 的核心问题不是“记住更多上下文”，而是“如何沉淀可复用行为模式”。

### R — Related work
- 传统 memory/RAG 多以片段检索为主，难形成可维护的行为策略资产。

### G — Research gap
- 缺少一种不改底座参数、可在线更新、可解释且可编辑的技能化终身学习层。

### P — Proposal
- 提出 AutoSkill：
  - 在线循环：rewrite → hybrid retrieval（dense+BM25）→ skill 注入生成；
  - 后台循环：技能抽取 → 邻域检索 → judge（add/merge/discard）→ merge 版本递增；
  - 关键约束：抽取证据优先来自用户 query，降低模型自回声污染。

## 3) Figure 区（至少 1 张）
- Figure 2（SkillBank 总体统计，N=1858）
- 论文链接（可定位图表）：https://arxiv.org/pdf/2603.01145

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- **Training setting:** training-free（不更新LLM参数）
- **Data:** WildChat-1M，筛选 >8 turns
- **Split:** zh/en × GPT-3.5/GPT-4 四子集
- **Output:** 四个 SkillBank 子库并统计技能演化

### 4.2 Main result table（可提取数字）
| Item | Value |
|---|---:|
| SkillBank 总技能数（Fig.2） | 1858 |
| 英文 GPT-3.5 子集 conversations | 10,243 |
| 英文 GPT-3.5 子集 messages | 267,681 |
| 英文 GPT-3.5 子集 skills | 631 |
| 中文 GPT-4 子集 conversations | 1,145 |
| 中文 GPT-4 子集 messages | 36,834 |
| 中文 GPT-4 子集 skills | 224 |

### 4.3 Analysis experiments（现象+解释）
- **现象：** 技能分布集中在编程/写作等高频需求。  
  **解释（作者）：** 技能抽取受真实交互频次驱动，高频任务优先沉淀。

- **现象：** 技能演化速率不均（如 `professional_text_rewrite` 迭代到 v0.1.34）。  
  **解释（作者）：** 高频触发 + 反馈密集的技能更快发生 merge 更新。

- **现象：** 同一 schema 可承载风格技能与流程技能。  
  **解释（作者）：** 统一 SKILL.md 表征提高了跨任务可复用性。

### 4.4 缺失项（明确标注）
- 与主流 baseline 的严格定量对比：**原文未给出可提取数字**。
- 任务级指标（成功率/满意度/长期一致性）：**原文未给出可提取数字**。
- 关键消融（去掉 rewrite/judge/merge）：**原文未给出可提取数字**。

## 5) Why it matters for our work
- **Agent memory:** 把记忆对象化为“行为技能资产”，更适合长期可维护系统。  
- **Long-context:** 通过技能压缩历史，避免单纯拉长上下文带来的噪声和成本。  
- **Multimodal RL（迁移潜力）：** 可把 tool/GUI/vision 轨迹进一步技能化，形成可解释 options 库。

## 6) Actionable next step
- [ ] 先做 training-free sidecar（rewrite + retrieve + async extract）接入当前 agent。
- [ ] 做 A/B：AutoSkill 风格技能库 vs 纯 summary-memory/RAG-memory。
- [ ] 设计多模态技能 schema（trigger / constraints / procedure / failure patterns）。

## 7) 评分解释（必填）
- **质量分 1/2：** 系统完整且工程可落地，但缺强基线和任务级量化。  
- **Observation 分 1/2：** 技能工件化视角有价值，但反直觉证据仍偏弱。  
- **总分 3/5：** 工程启发强，学术实证中等。  
- **为什么不是更高分：** 缺少系统化benchmark对照与显著性分析。
