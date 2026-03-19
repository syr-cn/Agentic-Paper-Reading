# SkillsBench 阅读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks
- **Alias:** SkillsBench
- **Authors / Org:** Xiangyi Li, Wenbo Chen, Yimin Liu, Shenghan Zheng, et al.（大规模协作团队）
- **Venue / Status:** arXiv 2602.12670v3（2026）
- **Date:** 2026-03-11（重做覆盖：2026-03-19）
- **Links:**
  - Abs: https://arxiv.org/abs/2602.12670
  - PDF: https://arxiv.org/pdf/2602.12670
  - Source tarball: https://arxiv.org/src/2602.12670v3
- **Tags:** agent-skill, benchmark, harness-eval, procedural-knowledge, long-context
- **My rating:** ★★★★☆
- **Read depth:** deep（含源码 tex 交叉核对）
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 2 = 4

---

## 1) 一句话 Why-read（必填）
这篇论文把“Skill 本身”作为被评估对象，而不是只看“模型裸能力”：在 **84 个有效任务、7 个 model-harness 配置、7308 条有效轨迹**上，作者给出清晰证据——**人工 curated skills 平均 +16.2pp**；而 **self-generated skills 平均 normalized gain 为 -1.8%（且文中结论称绝对提升近乎为负）**，说明“会消费技能”与“会生产技能”是两种不同能力。

---

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- LLM agents 已从单轮问答走向多步执行（CLI、工具、容器环境）。
- 社区大量使用 Skills（通常是 `SKILL.md` + 脚本/模板/参考资料）补 procedural knowledge。
- 但此前 benchmark 多评“整体成功率”，较少直接量化“skills 的净增益”。

### R — Related work
- execution-based benchmark（如 Terminal-Bench 体系）重任务完成率，但不单独估计 skill 的因果增益。
- prompt / RAG / tools 各有增强作用，但与 skills（可移植、模块化、过程导向）并不等价。

### G — Research gap
- 缺统一协议回答：同一个任务同一个 agent，给 skills 后到底涨多少。
- 缺系统 failure analysis：为什么某些任务被 skill 反向伤害。
- 缺跨 model-harness 的稳定比较结果。

### P — Proposal
- 提出 SkillsBench：**86 个任务、11 个 domain**，配 deterministic verifier。
- 实际评测剔除 2 个任务后为 **84 任务**（一个 GPU 依赖、一个 verifier timeout）。
- 三种条件：No Skills / Curated Skills / Self-Generated Skills（Gemini CLI 不支持 self-gen）。
- 在 7 个 model-harness 配置上跑出 **7308 条有效轨迹**，报告 pass rate + normalized gain。

---

## 3) Figure 区（至少 1 张，真图链）
> 说明：该论文 arXiv 无 HTML 图像页，但可用 **PDF 页面锚点真链** + **source tarball** 双重定位。

- **Figure 1（pipeline 总览）真链：**
  - 论文页链：https://arxiv.org/pdf/2602.12670#page=3
  - 对应源文件位于 source tarball 中：`figs/pipeline.pdf`
- **Figure 2（性能-成本 Pareto）真链：**
  - 论文页链：https://arxiv.org/pdf/2602.12670#page=5
  - 对应源文件：`figs/pareto_cost_vs_performance.pdf`
- **Task-level 热力图（with/no/uplift）页链：**
  - 论文页链：https://arxiv.org/pdf/2602.12670#page=15
  - 对应源文件：`figs/heatmap_skills_uplift.pdf`

---

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- **数据规模与划分：**
  - 总任务：86
  - 实际评测：84（排除 `mhc-layer-impl` 与 `fix-visual-stability`）
  - Domain：11
- **模型/执行器配置（7）：**
  - Claude Code × {Opus 4.5, Opus 4.6, Sonnet 4.5, Haiku 4.5}
  - Gemini CLI × {Gemini 3 Pro, Gemini 3 Flash}
  - Codex CLI × {GPT-5.2}
- **条件：**
  1) No Skills
  2) Curated Skills
  3) Self-Generated Skills（仅 Claude/Codex；Gemini CLI 不支持）
- **运行规模：**
  - 总计 **7308 valid trajectories**
  - 论文 protocol：主条件每任务 5 runs；self-gen 另设运行（文内并报告 5 个配置）。
- **指标：**
  - Pass Rate（按 task 先均值，再跨 84 任务汇总）
  - Normalized gain:  
    \( g = \frac{pass_{skill}-pass_{vanilla}}{1-pass_{vanilla}} \)
  - 95% bootstrap CI（1000 resamples）

### 4.2 Main result table（必填）
| Harness × Model | No Skills | Curated Skills (Pass) | Curated g | Self-Gen (Pass) | Self-Gen g |
|---|---:|---:|---:|---:|---:|
| Gemini CLI × Gemini 3 Flash | 31.3% | 48.7% | 25.3 | -- | -- |
| Claude Code × Opus 4.5 | 22.0% | 45.3% | 29.9 | 21.6% | -0.5 |
| Codex CLI × GPT-5.2 | 30.6% | 44.7% | 20.3 | 25.0% | -8.1 |
| Claude Code × Opus 4.6 | 30.6% | 44.5% | 20.0 | 32.0% | +2.0 |
| Gemini CLI × Gemini 3 Pro | 27.6% | 41.2% | 18.8 | -- | -- |
| Claude Code × Sonnet 4.5 | 17.3% | 31.8% | 17.5 | 15.2% | -2.5 |
| Claude Code × Haiku 4.5 | 11.0% | 27.7% | 18.8 | 11.0% | 0.0 |
| **Mean** | **24.3%** | **40.6%** | **21.5** | **21.0%** | **-1.8** |

- 绝对提升角度（curated）：**平均 +16.2pp**。
- self-gen：论文正文 Finding 3 口径为“相对 no-skills 近乎负收益（约 -1.3pp）”，表中 normalized gain 均值为 **-1.8%**。

### 4.3 Analysis experiments（强制“现象+解释”，>=3）
1) **现象：curated skills 显著有效，但跨配置波动大（+13.6 到 +23.3pp）。**  
   **解释：**skill 的效果受模型与 harness 的耦合方式影响，不是“给了就一定同幅度提升”。

2) **现象：self-generated skills 整体无效甚至退化。**  
   **解释：**作者给出两类失败：
   - 能意识到要技能，但生成内容过泛/不完整；
   - 高专业任务中连“需要专门技能”都识别失败。

3) **现象：domain uplift 高度不均衡。**  
   **解释：**预训练覆盖弱而流程知识强的领域，skill 增益更高。  
   - Healthcare: **34.2% → 86.1%（+51.9pp）**
   - Manufacturing: **1.0% → 42.9%（+41.9pp）**
   - Software Engineering: **34.4% → 38.9%（+4.5pp）**

4) **现象：并非总是正收益；84 任务中 16 个负增益。**  
   **解释：**skills 在部分任务引入冲突路径或额外上下文负担。代表任务：
   - `taxonomy-tree-merge`：**-39.3pp**
   - `energy-ac-optimal-power-flow`：**-14.3pp**
   - `trend-anomaly-causal-inference`：**-12.9pp**

5) **现象：skills 数量存在最优区间，2–3 最好。**  
   **解释：**过多 skill 增加检索/决策负担。  
   - 1 skill：+17.8pp
   - **2–3 skills：+18.6pp（最优）**
   - 4+ skills：+5.9pp

6) **现象：复杂度不是越高越好；comprehensive 反而负增益。**  
   **解释：**冗长文档占用上下文预算，关键信息难提取。  
   - Detailed：+18.8pp
   - Compact：+17.1pp
   - Standard：+10.1pp
   - Comprehensive：**-2.9pp**

7) **现象（成本面）：小模型 + skills 可重塑性价比。**  
   **解释：**Gemini Flash 输入 token 更高（**1.08M vs 0.47M**，约 2.3×），但价格更低（$0.50 vs $2.00 /1M input tokens），综合单任务约 **$0.55 vs $0.98（低 44%）**。

---

## 5) Case studies（硬要求：case >= 2）
### Case 1（正例，高增益）
- **Task:** `mario-coin-counting`
- **结果：**+85.7pp（2.9% → 88.6%）
- **解读：**该任务高度依赖步骤性方法，curated skill 提供了可执行流程，显著提升成功率。

### Case 2（正例，高增益）
- **Task:** `sec-financial-report`
- **结果：**+74.3pp
- **解读：**金融任务里 procedural template 的价值很高，skills 充当“可复用 SOP”。

### Case 3（反例，负增益）
- **Task:** `taxonomy-tree-merge`
- **结果：**-39.3pp
- **解读：**错误/冗余 skill 可把 agent 从原本可行路径拉偏，说明需要 skill gating 与冲突检测。

---

## 6) Why it matters + Actionable next step
- **对我们的启示（Why it matters）：**
  1) memory 系统优先建设“高质量可检索 procedural memory”，而非盲目让模型在线自写；
  2) long-context 不是越长越好，关键是 skill 路由和压缩质量；
  3) 评估时必须看负增益任务占比，不只看平均 pass rate。

- **下一步可执行计划（Actionable）：**
  - [ ] 做 `no-memory / top-k memory / full-memory` 三组对照，指标包含 pass rate + 负增益任务比例；
  - [ ] 在 1 / 2–3 / 4+ skills 下复现数量效应，并加“摘要版（≤300 tokens）vs 全文版”对照；
  - [ ] 引入 skill-use quality reward（选对 skill、按步骤执行、减少无效回合）做策略优化。

---

## 7) 评分解释（必填，保持原倾向）
- **质量分 1/2：**
  - 优点：评测协议完整（3 条件、跨 harness、deterministic verifier）、数据规模足（7308 轨迹）。
  - 扣分：文内仍可见口径差异（例如 self-gen 平均绝对提升描述与表格口径需更统一），显著性报告可更细。
- **Observation 分 2/2：**
  - 关键观察非常有价值：
    1) curated 明显有效；
    2) self-generated 难以稳定获益；
    3) skill 数量/复杂度有最佳区间；
    4) 小模型+优质 skills 可重塑成本-性能前沿。
- **总分：4/5（不改评分倾向）**
