# 01.me 文章阅读笔记

## 0) Metadata
- **Title:** Creation Notes for “Distillation”
- **Alias:** 01me-Distillation-Notes
- **Type:** Blog / Creation Notes
- **Link:** https://01.me/en/2026/03/novel-distillation-notes/
- **My rating:** ★★★★☆
- **Read depth:** normal
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 2 = 4

## 1) Core Insight
- 这篇不是技术论文，但给出一个对 agent 研究非常实用的方法论：**高质量产出来自“上下文资产 + 外部反思循环（Writer-Reviewer）”的系统设计，而不是一次性 prompt。**

## 2) Interesting Observations
- “Context is everything”：作者把 blog + 可穿戴对话记录作为长期语义资产，显著提高生成深度。
- 强制外部 reviewer loop 比“请仔细检查”这类 prompt 更可靠，核心是架构级反思而非口头要求。
- 文中提出“蒸馏同质化 → 相关失效（correlated failures）”风险链，对我们做 memory/retrieval 去同质化有直接启发。
- 双层对齐视角：物理/事实层修好后，价值判断层问题仍存在（factual correctness ≠ value correctness）。

## 3) Evidence / Claims
- 内容基于作者创作过程复盘与行业观察，属于高价值经验文，不是可复现实验论文。
- 明确描述了多轮写作-评审-修订 loop 的时间分配与收益来源。

## 4) Why It Matters for Your Work
- 对你当前方向（agent memory + continual learning）有直接映射：
  - 记忆系统要重视“上下文积累”与“可检索组织”；
  - 训练/推理流程应显式引入外部 critique/review 闭环；
  - 评测上要分开 factual correctness 与 value correctness。

## 5) Actionable Next Step
- [ ] 在现有 agent pipeline 增加硬性 Draft→Critique→Rewrite→Gate 环。
- [ ] 增加“异构检索/异构评估头”对照，缓解同质化导致的相关失效。
- [ ] 记忆卡片 schema 增加“来源类型（blog/meeting/audio）+ 置信度 + 冲突标签”。

## 6) Why not higher score
- 不是更高分的原因：启发很强，但本质是经验性文章，缺系统化可复现实证。
