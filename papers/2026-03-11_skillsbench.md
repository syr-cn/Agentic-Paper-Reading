# SkillsBench 阅读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** Benchmarking How Well Agent Skills Work Across Diverse Tasks
- **Alias:** SkillsBench
- **Authors / Org:** Xiangyi Li 等（大规模协作团队）
- **Venue / Status:** arXiv 2602.12670v3（2026）
- **Date:** 2026-03-11（笔记重写：2026-03-19）
- **Links:**
  - Abs: https://arxiv.org/abs/2602.12670
  - HTML: 原文无可用 arXiv HTML 页面
  - PDF: https://arxiv.org/pdf/2602.12670
  - Code: 原文正文未给出统一代码仓库直链（仅可见 benchmark/框架描述）
- **Tags:** agent-skill, benchmark, harness-eval, long-context, procedural-knowledge
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 2 = 4

---

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：**这篇工作的核心价值是把“Skill 本身”而不是“裸模型”设为评测对象，在 84 个任务、7 个 agent-model 配置、7308 条轨迹上定量证明：**人工精选 skills 平均 +16.2pp**，而 **self-generated skills 平均 -1.8% normalized gain（对应 pass rate 还下降）**，说明“会用 skill ≠ 会写 skill”。

---

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- LLM agent 从单轮生成走向多步执行（CLI、工具调用、容器环境）。
- 现实中越来越多团队用 Skills（`SKILL.md` + 资源文件）在推理时补 procedural knowledge。
- 但此前基准主要评估模型/agent 的总体能力，不直接评估 skill 增益。

### R — Related work
- 现有 benchmark（如 execution-based agent benchmarks）强调“任务是否做成”，较少单独估计“skills 是否带来净收益”。
- 常见增强范式（prompt/RAG/tools）与 Skills 在“可移植+程序化操作指南”维度不同，但缺系统量化对比。

### G — Research gap
- 缺统一协议回答：**同一任务、同一 agent，给 skill 到底提升多少？**
- 缺 failure taxonomy：为什么有些任务会被 skill 反向伤害。
- 缺跨 harness 的稳定结论（不同 CLI 可能 skill 使用行为不同）。

### P — Proposal
- 提出 SkillsBench：**86 个任务（其中 84 个纳入评测）**，覆盖 **11 个 domain**，配 deterministic verifier。
- 三种条件：No Skills / Curated Skills / Self-Generated Skills（Gemini CLI 不支持 self-gen）。
- 在 7 个 model-harness 配置上运行，得到 **7308 条有效轨迹**，报告 pass rate 与 normalized gain。

---

## 3) Figure 区（至少 1 张）
- 图1（方法总览）：`figs/pipeline.pdf`（构建-筛选-评测三阶段）
- 图2（性能-成本）：`figs/pareto_cost_vs_performance.pdf`
- 图3（task-level uplift 热力图）：`figs/heatmap_skills_uplift.pdf`

> 注：原文有一处数字不一致：pipeline 图注写“+12.66pp”，而主结果表/正文结论是“+16.2pp”。以主结果表（84任务评测）为主。

---

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- **任务/数据：**
  - 总任务数 86；因 `mhc-layer-impl`（需 GPU）和 `fix-visual-stability`（verifier timeout）排除，**评测任务 84**。
  - 覆盖 **11 个 domain**。
  - 难度分层：Core 17（19.8%）、Extended 43（50.0%）、Extreme 26（30.2%）。
- **模型/agent 配置（7）**：
  - Claude Code × {Opus 4.5, Opus 4.6, Sonnet 4.5, Haiku 4.5}
  - Gemini CLI × {Gemini 3 Pro, Gemini 3 Flash}
  - Codex CLI × {GPT-5.2}
- **条件：**
  1) No Skills  
  2) Curated Skills  
  3) Self-Generated Skills（仅 Claude/Codex，Gemini 不支持）
- **运行规模：**
  - **7308 valid trajectories**。
  - 运行策略：主条件每 task **5 runs**；self-gen 每 task **3 runs**。
- **评测指标：**
  - 主指标：Pass Rate（按任务平均再跨任务平均，固定分母 84）。
  - 辅助：Normalized gain  
    \( g = \frac{pass_{skill}-pass_{vanilla}}{1-pass_{vanilla}} \)
  - 置信区间：95% bootstrap CI（**1000 resamples**）。
  - 统计显著性检验：**原文未给出可提取的 p 值 / 显著性检验结果**。

### 4.2 Main result table（必填）
| Setting (Harness × Model) | Baseline No Skills | Proposed Curated Skills | Delta (pp) |
|---|---:|---:|---:|
| Gemini CLI × Gemini 3 Flash | 31.3% | 48.7% | +17.4 |
| Claude Code × Opus 4.5 | 22.0% | 45.3% | +23.3 |
| Codex CLI × GPT-5.2 | 30.6% | 44.7% | +14.1 |
| Claude Code × Opus 4.6 | 30.6% | 44.5% | +13.9 |
| Gemini CLI × Gemini 3 Pro | 27.6% | 41.2% | +13.6 |
| Claude Code × Sonnet 4.5 | 17.3% | 31.8% | +14.5 |
| Claude Code × Haiku 4.5 | 11.0% | 27.7% | +16.7 |
| **Mean** | **24.3%** | **40.6%** | **+16.2** |

补充（Self-Generated Skills）：
- Opus 4.5: 21.6%（相对 no-skills -0.4pp）
- GPT-5.2: 25.0%（-5.6pp）
- Opus 4.6: 32.0%（+1.4pp）
- Sonnet 4.5: 15.2%（-2.1pp）
- Haiku 4.5: 11.0%（0.0pp）
- **Mean: 21.0%（相对 no-skills -3.3pp）**；对应表中 mean normalized gain = **-1.8%**。

### 4.3 Analysis experiments（强制“现象+解释”）
- **现象1：Curated Skills 平均 +16.2pp，但跨度很大（+13.6 到 +23.3pp）。**  
  **解释（作者）：**skills 效果强依赖 harness×model 组合，不是“给了就稳涨”。  
  **【标注】（我的判断）：**这直接提示我们做 memory/skill 系统时要纳入“执行器依赖项”（例如 skill 激活机制、上下文编排方式），不能只看模型本体。

- **现象2：Self-generated Skills 不但没带来收益，反而平均退化。**  
  **解释（作者）：**模型常见两类失败：
  1) 识别到需要知识，但写出的 skill 过泛/不完整；
  2) 在高专业任务里甚至识别不出需要专门 skill。  
  **【标注】（我的判断）：**“写 skill”是元认知+过程压缩任务，难度高于“读 skill 并执行”。这对 agent memory 很关键：应优先做**人类先验+在线检索**，再逐步引入自动 skill 编写。

- **现象3：Domain uplift 极不均衡。**  
  **解释（作者）：**预训练覆盖弱、流程强的领域收益大；预训练覆盖强的领域收益小。  
  **【标注】（我的判断）：**这个结论和 memory 系统的“稀缺知识优先缓存”一致。
  - 最高：Healthcare **+51.9pp**（34.2→86.1）
  - 次高：Manufacturing **+41.9pp**（1.0→42.9）
  - 低增益：Software Engineering **+4.5pp**（34.4→38.9）

- **现象4：并非总是正收益，84 任务中有 16 个任务负增益。**  
  **解释（作者）：**某些 task 上 skills 引入冲突指引或额外复杂度。  
  **【标注】（我的判断）：**这说明 skill 系统必须加“冲突检测/置信门控”。例子：
  - `taxonomy-tree-merge` **-39.3pp**
  - `energy-ac-optimal-power-flow` **-14.3pp**
  - `trend-anomaly-causal-inference` **-12.9pp**

- **现象5：Skill 数量不是越多越好，2–3 个最好。**  
  **解释（作者）：**4+ skills 造成认知负担与上下文干扰。  
  **【标注】（我的判断）：**和 long-context 的“检索精度优先于召回规模”一致。数字：
  - 1 skill: +17.8pp
  - **2–3 skills: +18.6pp（最优）**
  - 4+ skills: +5.9pp

- **现象6：Skill 文档复杂度存在倒U型；comprehensive 反而伤害。**  
  **解释（作者）：**过长文档占上下文预算，关键信息提取失败。  
  **【标注】（我的判断）：**建议做“可执行摘要层 + 按需展开层”。数字：
  - Detailed: +18.8pp
  - Compact: +17.1pp
  - Standard: +10.1pp
  - Comprehensive: **-2.9pp**

- **现象7（成本侧）：小模型+skills 可能更省钱。**  
  **解释（作者）：**Gemini Flash 每任务输入 token 更高（**1.08M vs 0.47M**，约 2.3×），但单价更低（$0.50 vs $2.00 /1M），综合后每任务 **$0.55 vs $0.98（便宜 44%）**。  
  **【标注】（我的判断）：**这对多轮 agent memory 非常实用：可把大模型用于 skill 维护，小模型用于 skill 执行。

---

## 5) Why it matters for our work
- 对 **agent memory**：论文证据支持“先写入结构化 procedural memory，再做执行”优于“临场让模型自写规则”。
- 对 **long-context**：给太多、太长的技能会降性能，说明我们需要 memory packing / routing，而不是盲目扩上下文。
- 对 **multimodal RL**：任务级正负增益并存（16/84 负增益）意味着 reward 设计应包含“skill 使用质量”而不只最终 pass/fail。

---

## 6) Actionable next step
- [ ] **Agent memory 实验：**实现一个“Skill Memory Bank + 置信门控检索器”，对照 no-memory / full-memory / top-k-memory 三组；先用 SkillsBench 的 3 个高收益域（Healthcare/Manufacturing/Cybersecurity）复现实验，指标用 pass rate + negative-delta task 比例。
- [ ] **Long-context 实验：**做 1 / 2–3 / 4+ skill 注入 ablation，并加入“摘要版 skill（≤300 tokens）vs 全文版”对照，验证是否能复现 2–3 最优与 comprehensive 退化现象。
- [ ] **Multimodal RL 实验：**在视频/文档任务上定义 skill-usage reward（是否调用正确 skill、是否遵循步骤、是否减少无效回合），做 GRPO 或 PPO 微调，目标是降低“有 skill 反而变差”的任务占比（当前论文是 16/84）。

---

## 7) 评分解释（必填）
- **质量分 1/2：**
  - 优点：评测设计清晰（3 条件、跨 harness、deterministic verifier）、样本规模足（7308 轨迹）。
  - 扣分：文中存在局部数字不一致（+12.66pp vs +16.2pp），且显著性检验报告不足（无可提取 p 值）。
- **Observation 分 2/2：**
  - 高价值观察非常明确：
    1) curated skill 显著有效；
    2) self-generated skill 平均无效；
    3) skill 数量/复杂度存在最优区间；
    4) 成本-性能可被“小模型+好 skill”重塑。
- **总分 4/5：**维持原评分倾向，不做无依据改分。
- **为什么不是更高分：**统计报告粒度与一致性还可加强（例如全量 CI 展示、显著性检验、冲突结果的更系统误差分析）。
