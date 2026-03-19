# SoK: Agentic Skills 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** SoK: Agentic Skills — Beyond Tool Use in LLM Agents  
- **Alias:** SoK-Agentic-Skills  
- **Authors / Org:**（SoK综述，多机构作者；以原文为准）  
- **Venue / Status:** arXiv 2602.20867v1  
- **Date:** 2026-02-24  
- **Links:**  
  - Abs: https://arxiv.org/abs/2602.20867  
  - HTML: https://arxiv.org/html/2602.20867v1  
  - PDF: https://arxiv.org/pdf/2602.20867  
  - Code: N/A（综述）  
- **Tags:** agentic skill, memory, skill lifecycle, safety, evaluation  
- **Case 对齐（>=2）:** 参考 `2026-03-11_evo-memory.md`、`2026-03-19_arise.md` 的 DNL 写法  
- **My rating:** ★★★☆☆（保持原倾向）  
- **Read depth:** normal（结构化精读）  
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3/5**

---

## 1) 一句话 Why-read（必填）
- 这篇 SoK 的核心价值是把 **skill** 从“临时提示技巧”升级为“可定义、可组合、可治理的系统资产”，给出统一四元组定义、全生命周期、设计模式与安全评估框架，可直接当 agent 架构审查 checklist。

---

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- LLM agent 正从单步 tool use 走向长程任务，但“每次从头推理”带来 token 成本高、稳定性波动、复用差。  
- 现有系统里有 skill、tool、plan、memory 等对象，但边界混用，工程治理困难。

### R — Related work
- 已有 survey 多聚焦：
  1) 宏观 LLM agent；
  2) 工具调用（tool-use）；
  3) 多 agent 协作。  
- 作者认为这些工作较少把 **skill 作为一等对象** 去做系统化归纳。

### G — Research gap
- 缺少可操作的统一定义，难区分 skill 与 tool/plan/memory。  
- 缺少贯穿 discovery→update 的生命周期框架。  
- 缺少“skill 供应链”层面的安全治理讨论（不仅是 prompt 安全）。

### P — Proposal
- 给出 skill 统一形式：**S = (C, π, T, R)**。  
- 提出两类 taxonomy：
  - 系统层 **7 种设计模式**（按自主性光谱）；
  - 正交的 **representation × scope** 分类。  
- 总结评估与安全证据（含 SkillsBench、ClawHavoc 等）。

---

## 3) Figure 区（至少 1 张，抓主图，不跳过）
- 图1（Skill anatomy）：

![fig1](https://arxiv.org/html/2602.20867v1/figures/skill-anatomy/figure.png)

  用四元组把 skill 的“何时可用（C）—如何执行（π）—何时停止（T）—如何被调用（R）”拆开，便于工程约束与审计。

- 图2（Skill lifecycle）：

![fig2](https://arxiv.org/html/2602.20867v1/figures/skill-lifecycle/figure.png)

  7 阶段闭环（discovery→practice/refinement→distillation→storage→retrieval/composition→execution→evaluation/update），强调 skill 是持续演化资产。

- 图3（Pattern spectrum）：

![fig3](https://arxiv.org/html/2602.20867v1/figures/pattern-spectrum/figure.png)

  从低自主到高自主的 7 模式光谱，可映射为真实系统的封装/发布/治理策略组合。

---

## 4) Experiments（必须含具体数字）
> 说明：本文是 SoK，不是单一新算法论文；这里记录其“系统化证据设置 + 可提取量化结果”。

### 4.1 Experimental setup
- **任务/数据：** 覆盖 agent skill 相关文献与系统，时间窗 **2020-01 ~ 2025-02**（并纳入 2026-02 的 SkillsBench 关键证据）。  
- **模型/agent 配置：** 非单一模型实验；对多个已有 agent 系统做统一映射。  
- **对比基线：** skill/no-skill、curated/self-generated 等来自被引评测（主要是 SkillsBench）。  
- **评测指标：** pass rate（pp 变化）、任务轨迹规模、系统模式覆盖与安全案例规模。

补充可量化设置：
- 检索来源库：**6 个**（Google Scholar, Semantic Scholar, DBLP, ACM DL, IEEE Xplore, arXiv）  
- 候选文献：约 **180**；深度分析：**65**  
- 重点映射系统：**24**  
- 覆盖：**8 个 benchmark 环境 / 7 种设计模式 / 5 类表示类型**  
- taxonomy 修订轮次：**3 轮**

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| SkillsBench（文中引用）：No skills vs Curated skills | No-skills pass rate | Curated skills | **+16.2 pp（平均）** |
| SkillsBench（文中引用）：No skills vs Self-generated skills | No-skills pass rate | Self-generated skills | **-1.3 pp** |
| SkillsBench 评估规模（文中引用） | — | — | **86 tasks / 7,308 trajectories** |
| 安全案例 ClawHavoc（文中引用） | 正常 skill marketplace | 攻击渗透 | **近 1,200 恶意 skills** |

> 注：若需“各 backbone 的绝对 pass rate、显著性检验”，需回到被引 SkillsBench 原文；本 SoK 主文未完整展开该级别细表。

### 4.3 Analysis experiments（强制“现象+解释”）
- **现象：** curated skills 平均 **+16.2pp**，但 self-generated skills 出现 **-1.3pp** 退化。  
  **解释（作者）：** skill 质量控制是瓶颈；自动生成 skill 易含错误、脆弱启发式或低泛化。  
  **【标注】（我的判断）：** skill 层不是天然增益层，必须默认配套 verification / versioning / rollback。

- **现象：** 风险从 prompt 注入扩展到 skill supply chain，出现 ClawHavoc（近 **1,200** 恶意技能）。  
  **解释（作者）：** skill 具备可执行+可复用属性，恶意条目一旦进入分发链会跨任务放大。  
  **【标注】（我的判断）：** 企业侧应把 skill 包治理做成“类 pip/npm 依赖治理”，包含签名、溯源、权限沙箱。

- **现象：** 四元组定义 S=(C, π, T, R) 强调任何一项缺失都会破坏 skill 的系统边界。  
  **解释（作者）：** C/T/R/π分别对应适用性、执行策略、终止性与接口可调用性。  
  **【标注】（我的判断）：** 其中 T（termination）在很多 agent 框架里被弱化，是造成长上下文循环和成本失控的高频根因。

- **现象：** 7 种模式是非互斥的，系统通常多模式叠加。  
  **解释（作者）：** 真实工程是组合架构，单标签分类会丢信息。  
  **【标注】（我的判断）：** 评估也要升级为“模式组合×风险组合”矩阵，而非单点能力榜单。

---

## 5) Why it matters for our work
- **agent memory：** 可把 skill 明确归入 procedural memory，与 episodic/semantic memory 分层治理。  
- **long-context：** 把过程知识从上下文迁移到 skill 库，降低重复推理 token 与循环风险。  
- **multimodal RL/agent：** representation × scope 框架可统一文本技能、代码技能、策略技能的组织与评测。

---

## 6) Actionable next step
- [ ] 在现有 agent 中落地最小 **skill contract**：强制每个 skill 显式声明 `(C, T, R)`，并记录 `skill_id/version/caller/outcome/duration`。  
- [ ] 做一个 sprint 的 A/B：A=纯长上下文规划，B=skill retrieval+调用；比较成功率、token、步数、循环率。  
- [ ] 搭建 skill 供应链防线：签名与来源校验、分级沙箱权限、canary 任务与自动回滚。

---

## 7) 评分解释（必填）
- **质量分 1/2：** 框架化能力强（定义+taxonomy+治理），但非新方法实验论文。  
- **Observation 分 1/2：** 对系统设计启发明确，尤其是 skill contract 与供应链安全。  
- **总分 3/5：** **维持 ★★★☆☆（不改原倾向）**。  
- **为什么不是更高分：** 关键性能数字主要来自被引工作（如 SkillsBench），本文核心贡献是系统化整合而非原创 SOTA 实验。
