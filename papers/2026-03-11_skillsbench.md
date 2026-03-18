# SkillsBench 阅读笔记（重写版）

## 0) Metadata
- **Title:** Benchmarking How Well Agent Skills Work Across Diverse Tasks
- **Alias:** SkillsBench
- **Venue / Status:** arXiv 2602.12670 (v3)
- **Links:**
  - Abs: https://arxiv.org/abs/2602.12670
  - PDF: https://arxiv.org/pdf/2602.12670
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 2 = 4

---

## 1) 一句话：为什么值得读（key claim + key observation）
**这篇最值得读的点是：它首次用大规模、可验证（deterministic verifier）的评测把“skills 到底有没有用”从经验争论变成可测事实；最有意思 observation 是**：
- curated skills 平均显著增益（+16.2pp），
- 但 self-generated skills 平均无增益（约 -1.3pp），
说明“模型会用技能 ≠ 模型会写出高质量技能”。

---

## 2) 用 CRGP 拆解 Introduction

### C — Context（研究背景）
- LLM agent 已经从“文本生成器”进化到真实多步任务执行体（CLI/工具链/环境交互）。
- 问题是：基础模型有通用能力，但缺少面向具体工作流的 procedural knowledge。
- skills（指令+模板+资源+校验逻辑）成为推理时增强 agent 的主流路线，而且生态增长很快（社区技能库大量涌现）。

### R — Related Work（相关工作）
- 现有 agent benchmark（论文中点名的一系列）主要回答：
  - “模型在任务 X 上有多强？”
- 但没有回答：
  - “技能 Y 对任务 X 到底贡献了多少？”
- 即：大家在评“裸模能力”，没有系统评“技能增益”。

### G — Gap（研究缺口）
- 缺少一个把 skills 当作**一等评测对象**的 benchmark。
- 缺少可比较的 protocol 去回答这几个关键问题：
  1) skills 相比 no-skills 的真实增益有多大？
  2) 哪些 skill 设计（长度、数量、内容粒度）真正有效？
  3) 什么时候 skills 反而有害？

### P — Proposal（本文方案）
- 提出 **SkillsBench**：84/86 个任务（论文主表按 84）覆盖 11 个领域。
- 每任务三条件评测：
  1) no-skills
  2) curated skills
  3) self-generated skills（部分配置）
- 使用 deterministic verifier + 全轨迹日志。
- 在 7 个 model-harness 配置上跑 7308 条有效轨迹，给出首个系统实证。

---

## 3) 实验拆解（设定 + 主表 + 分析性实验）

## 3.1 实验设定（Experimental Setup）

### 任务与协议
- 84 个任务，11 个 domain。
- 每任务在 no-skills / with curated skills / self-generated skills 三条件下评估。
- 主要指标：
  - Pass Rate
  - Normalized Gain（文中给公式）

### 模型与 agent harness（7 配置）
- Claude Code × Claude Opus 4.5 / 4.6 / Sonnet 4.5 / Haiku 4.5
- Gemini CLI × Gemini 3 Pro / 3 Flash
- Codex CLI × GPT-5.2

### 评测规模
- 7308 条有效 trajectory（pass/fail/timeout，排除基础设施错误）。

---

## 3.2 主结果表（Main Table）

### 结论 A：curated skills 平均有效
- Across 7 配置：
  - no-skills 平均 24.3%
  - with curated skills 平均 40.6%
  - **平均绝对提升 +16.2pp**（论文主结论）

### 结论 B：self-generated skills 平均无效
- 在支持 self-generated 的配置上：
  - 平均约 21.0%，相对 no-skills **约 -1.3pp**
- 典型例子：Codex+GPT-5.2 有明显退化（文中约 -5.6pp）。

### 结论 C：最佳配置与“提升最大”配置不同
- 最高 with-skills pass rate：Gemini CLI + Gemini 3 Flash（48.7%）
- 提升最大之一：Claude Code + Opus 4.5（从 22.0 到 45.3，+23.3pp）

> 这点很重要：
> **绝对性能最好 ≠ skills 增益最大**，两者反映的是不同能力面。

---

## 3.3 分析性实验（Analysis / Ablation-like Findings）

### (1) Domain 差异非常大
- Healthcare：+51.9pp
- Manufacturing：+41.9pp
- Software Engineering：+4.5pp
- Mathematics：+6.0pp

解释：
- 预训练覆盖不足、流程知识更专业的领域，skills 增益更大。

### (2) 任务级并非“全涨”
- 16/84 任务出现负增益。
- 说明 skills 可能引入冲突指令、无关负担或上下文污染。

### (3) Skills 数量存在最佳区间
- 2~3 个 skills 最优（+18.6pp）
- 4+ skills 增益明显下降（+5.9pp）

### (4) Skills 复杂度不是越全越好
- detailed / compact 最有效（约 +18.8 / +17.1pp）
- comprehensive 反而可能伤害表现（文中报告负增益）

### (5) 模型尺度补偿效应
- 小模型 + 好 skills 可能超过大模型无 skills。
- 这是工程上非常有价值的成本结论。

---

## 4) 我的评分解释 + 对我们研究的价值

## 4.1 为什么是 ★★★★☆（不是 5 星）

按你当前标准（1+2+2）：
- **基础 1**：默认。
- **质量 1/2**：
  - 优点：评测规模大、协议清晰、可复验、分析维度丰富。
  - 扣分：核心贡献主要是 benchmark/measurement，不是方法机制创新；另外主文对“为何某些任务负增益”的因果拆解仍可更深入。
- **Observation 2/2**：
  - 提供了多个高价值、反直觉且可迁移 observation：
    1) self-generated 无效；
    2) 2~3 skills 最优；
    3) comprehensive 可能有害；
    4) 小模型可借 skills 补偿。

因此总分 **4/5** 合理。

---

## 4.2 对我们研究有什么用（直接可行动）

### 用处 1：把“写技能”变成“测技能”
- 你的 pipeline 里可以直接引入 SkillsBench 风格三条件：
  - no-skills / curated / self-generated
- 不再凭直觉说“这个 skill 应该有用”。

### 用处 2：建立 quality gate
- 新增 skill 必须先过 verifier + A/B 才能入库。
- 重点盯负增益任务，建立“skill 回滚/降权”机制。

### 用处 3：控制 skill 数量与文档长度
- 默认优先 2~3 个聚焦 skill，而不是大而全 skill bundle。
- 这会直接降低上下文污染和 token 浪费。

### 用处 4：服务你当前的 token 成本优化
- 小模型 + 高质量 skills 的补偿效应，与你今天关心的 token 成本问题直接耦合。
- 可把“模型升级”与“技能优化”放到同一成本-性能坐标上做决策。

---

## 5) 给你的下一步建议（可直接执行）
- 在 `SYRs-Memory-Paper-Reading` 里新增一个 mini protocol：
  1) 每篇 skill 型论文提炼 1~3 个可执行 skill
  2) 对同一任务跑 no-skill / curated / self-generated
  3) 记录 pass rate + token + wall-clock
- 先从你最常用的 5 个任务开始，做一个“技能真实收益看板”。

---

## 6) Why not higher score
- 不是更高分的原因：尽管 observation 质量很高，但其核心是 benchmark 贡献；若后续补上更强因果分析（例如系统地解释何时/为何 skills 导致负迁移），可接近 5 星。
