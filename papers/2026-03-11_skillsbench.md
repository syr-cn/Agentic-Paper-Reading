# SkillsBench 阅读笔记（重写版 v2）

## 0 Metadata
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

## 1 一句话 Why-read
- 待补证据

## 2 CRGP
### C — Context
- LLM agent 已从“文本生成”转向“多步任务执行”（CLI/工具调用/环境交互）。
- 基础模型有通用能力，但缺 domain-specific procedural knowledge。
- skill（指令+模板+资源+验证逻辑）成为推理期增强手段，生态增长很快。

### R — Related Work
- 现有 benchmark 主要评估裸模型/裸 agent 在任务上的性能。
- 缺少“同任务下，有无 skill 的增量评估”框架。

### G — Gap
- 缺少把 skills 当作一等评测对象的标准 benchmark。
- 缺少对“何时有用、何时有害、为什么”的系统证据。

### P — Proposal
- 提出 SkillsBench：84 个评测任务（跨 11 域）、deterministic verifier、全轨迹日志。
- 三条件评测：no-skills / curated skills / self-generated skills。
- 在 7 个 model-harness 配置上做 7308 条有效轨迹的大规模实验。

---

## 3 Figure 区
### 图1：评测流程总览（pipeline）
![pipeline](../assets/skillsbench/pipeline.png)

### 图2：性能-成本 Pareto
![pareto](../assets/skillsbench/pareto.png)

### 图3：skills uplift 热力图
![uplift](../assets/skillsbench/heatmap_uplift.png)

> 注：图片来自论文源码 figs（从 arXiv source 导出并本地化）。

---

## 4 Experiments
### 4.1 Experimental setup
- **任务**：84 tasks，11 domains。
- **模型/Agent 组合（7 个）**：
  - Claude Code × {Opus 4.5, Opus 4.6, Sonnet 4.5, Haiku 4.5}
  - Gemini CLI × {Gemini 3 Pro, Gemini 3 Flash}
  - Codex CLI × {GPT-5.2}
- **条件**：
  1) No Skills
  2) Curated Skills
  3) Self-Generated Skills（Gemini CLI 不支持）
- **规模**：7308 条有效 trajectory。
- **指标**：Pass Rate + Normalized Gain（论文 Eq.1）。

---

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 原文摘要 | 原文未给出可提取数字 | 原文未给出可提取数字 | 原文未给出可提取数字 |

### 4.3 Analysis
- **现象：** 待补证据。
  **解释（作者）：** 待补证据。
  **【标注】（我的判断，可选）：** 待补证据。

## 5 Why it matters for our work
- 待补证据

## 6 Actionable next step
- [ ] 待补证据

## 7 评分解释
- 维持原评分倾向，不做无根据上调。
- 待补证据（需补质量分/Observation 分拆解）。
