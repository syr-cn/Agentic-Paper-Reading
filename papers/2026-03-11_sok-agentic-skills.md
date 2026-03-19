# SoK: Agentic Skills 阅读笔记（DNL Deep Note 重写）

## 0 Metadata
- **Title:** SoK: Agentic Skills — Beyond Tool Use in LLM Agents  
- **Alias:** SoK-Agentic-Skills  
- **Venue / Status:** arXiv 2602.20867 (v1, 2026-02-24)  
- **Links:**  
  - Abs: https://arxiv.org/abs/2602.20867  
  - PDF: https://arxiv.org/pdf/2602.20867  
- **My rating:** ★★★☆☆  
- **Read depth:** skim（结构化精读摘要）  
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = 3  

---

## 1 一句话 Why-read
- 如果你在做 agent memory / skill library / 安全治理，这篇是“把 skills 当一等系统对象”的总地图：它给了统一定义、生命周期、设计模式与安全评估框架，适合拿来做架构审查清单。

---

## 2 CRGP
### C — Context
- LLM agent 从单次工具调用走向长程任务执行，但“每次从头推理”导致上下文重复消耗与稳定性波动。  
- 作者把 **agentic skill** 定义为可调用、可复用、可治理的程序化能力，区别于 tool / plan / episodic memory。  
- 论文定位是 SoK（systematization），核心是整理已有系统实践，不是提出新训练算法。

### R — Related Work
- 已有 survey 常见三类：
  1) 宏观 LLM agent 综述；
  2) tool-use 综述；
  3) multi-agent 协作综述。  
- 作者认为缺口在于：缺少“**skill-centric** 且覆盖从获取到治理全生命周期”的系统化梳理。

### G — Research Gap
- 缺少统一的 skill 抽象边界（和 tool/plan/memory 的可操作区分）。  
- 缺少跨系统的生命周期对照框架（discovery→update）。  
- 缺少把安全/治理放到 skill supply chain 层的统一讨论（不仅是 prompt 层）。

### P — Proposal
- 提出统一形式化定义：**S = (C, π, T, R)**。  
- 提出两套互补 taxonomy：
  - 系统层 **7 种设计模式**；
  - 正交的 **representation × scope** 分类。  
- 补充安全治理分析（含 ClawHavoc 案例）与评估框架（含确定性评测取向及 SkillsBench 证据）。

---

## 3 Figure 区（抓主图，不跳过）
### Figure 1：Skill 四元组内部结构
- 输入观测 O（和目标 G），先过适用性条件 C，再由策略 π 产生活动作/子技能调用，终止条件 T 决定何时退出，R 提供可调用接口。  
- **意义：** 把“可执行性+可复用性+可组合性”明确拆成可检查部件。

### Figure 2：Skill 生命周期
- 7 阶段：discovery → practice/refinement → distillation → storage → retrieval/composition → execution → evaluation/update，并包含反馈回路。  
- **意义：** 强调 skill 是持续演化资产，而非一次性 prompt artifact。

### Figure 3：七种设计模式（按自主性轴）
- 从 metadata progressive disclosure 到 meta-skills，自主性逐步增强；marketplace 分发模式跨越全轴。  
- **意义：** 可直接映射到工程中的“能力封装与发布策略”。

---

## 4 Experiments / Evidence
> 这篇是 SoK，不是单一实验论文；这里记录其“证据来源设置 + 锚点结果”。

### 4.1 Evidence setup（原文给出的具体数字/设置）
- **文献检索库数量：6 个**  
  （Google Scholar, Semantic Scholar, DBLP, ACM DL, IEEE Xplore, arXiv）  
- **时间窗：** 2020-01 到 2025-02（LLM agent 主体）；额外纳入 2026-02 的 SkillsBench 作为并行关键证据。  
- **候选文献：约 180 篇**；筛后 **65 篇** 深入分析。  
- 其中 **24 个系统** 被重点映射到表格。  
- 语料覆盖：**8 个 benchmark 环境 / 7 种设计模式 / 5 类表示类型**。  
- taxonomy 构建通过 **3 轮修订** 完成。  
- 形式化贡献点中，系统层模式数是 **7**（与 lifecycle 的 7 阶段呼应）。

### 4.2 Main result table（按“可提取数字”写）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| SkillsBench 锚点：Curated skills vs No skills（文中引用） | No-skills pass rate（原文未在此 SoK 主文给绝对值） | Curated skills | **+16.2 percentage points（平均）** |
| SkillsBench 锚点：Self-generated skills vs No skills（文中引用） | No-skills pass rate（原文未在此 SoK 主文给绝对值） | Self-generated skills | **-1.3 pp** |
| 安全案例：ClawHavoc | 正常 marketplace | 攻击渗透 | **近 1,200 恶意 skills** |
| SkillsBench 评估规模（文中引用） | — | — | **86 tasks / 7,308 trajectories** |

> 注：若你要“各模型绝对 pass rate、方差、统计显著性”，需要回到被引的 SkillsBench 原文表格；本 SoK 内未完整展开这些绝对数字。

### 4.3 Analysis（至少 3 条：现象 + 解释 + 我的判断）
1) **现象：** curated skills 平均提升 +16.2pp，而 self-generated skills 反而 -1.3pp。  
   **解释（作者）：** 技能质量控制是核心瓶颈；自生成技能容易编码错误或过拟合启发式。  
   **我的判断：** 这说明“skill layer 不是天然增益层”，必须把 verification + versioning + rollback 作为默认机制，否则会把 agent 变成“可持续注入错误策略”的系统。

2) **现象：** 论文把风险重心从 prompt 注入扩展到 skill supply chain，并给出 ClawHavoc（近 1,200 恶意技能）案例。  
   **解释（作者）：** skill 具备可执行性与复用性，攻击一旦进入市场分发链，会跨任务放大。  
   **我的判断：** 对企业落地来说，skills 的签名、来源证明、沙箱分级权限，应和依赖管理（pip/npm）同等对待，不能只做“提示词安全”。

3) **现象：** 作者将 skill 定义为 S=(C,π,T,R)，并强调缺一不可（去掉 C/T/R/π 都会破坏可用边界）。  
   **解释（作者）：** skill 要可自选择、可终止、可调用、可执行，才能支持层级组合与治理。  
   **我的判断：** 这个四元组非常适合做工程 contract：特别是 T（termination）在很多 agent 框架里常被弱化，导致“长上下文反复循环”问题。把 T 显式化有助于 long-context 稳定性和成本控制。

4) **现象：** taxonomy 是“非互斥模式”，系统可同时命中多模式。  
   **解释（作者）：** 真实系统是组合式，不应强行互斥分类。  
   **我的判断：** 这更贴近生产架构；但也意味着评估要从“单点能力对比”升级到“模式组合 + 风险组合”的矩阵测试。

---

## 5 Why it matters for our work
- 对 **agent memory**：论文把 skill 明确为程序性记忆（procedural memory），可和 episodic/semantic memory 分层设计。  
- 对 **long-context**：通过技能封装减少重复推理 token 开销，把“过程知识”从上下文迁出到可调用库。  
- 对 **multimodal RL/agent**：representation × scope 框架允许把语言技能、代码技能、策略技能放进同一治理与评测框架，便于跨环境迁移。

---

## 6 Actionable next steps（面向 memory / long-context / multimodal RL）
1) **做一个 skill contract 最小落地版（两周内）**  
   - 在现有 agent 框架给每个 skill 增加 `(C, T, R)` 显式字段；  
   - C 至少支持 soft score + threshold；T 支持 success/fail/timeout 三态；  
   - 接入最小审计日志（skill-id, version, caller, duration, outcome）。

2) **搭建 long-context 友好的 skill retrieval A/B（一个 sprint）**  
   - A 组：纯上下文内计划；B 组：检索 skill + 调用；  
   - 指标：任务成功率、总 token、平均步骤数、循环率；  
   - 目标：验证“程序性记忆替代上下文重复推理”是否带来稳定收益。

3) **为 multimodal RL agent 加“技能供应链防线”（持续工程）**  
   - 所有外部 skill 包执行前做来源校验（签名/哈希/发布者信誉）；  
   - 依据 trust tier 分级沙箱权限（文件/网络/系统调用）；  
   - 引入 canary tasks + 回滚策略，监控 self-generated skill 的性能漂移与安全异常。

---

## 7 评分解释（保持原倾向）
- **维持 ★★★☆☆（3/5）**，不做无依据上调。  
- **给 3 分的原因：**
  1) 结构化价值高：定义、taxonomy、治理框架完整；
  2) 但它本质是 SoK，不是提出并验证新方法的大规模原创实验论文；
  3) 关键效果数字多来自被引工作（如 SkillsBench），主文更多承担“整合与解释”角色。  
- **结论：** 适合作为系统设计与评审蓝图，不应当作“单篇新算法 SOTA 证据”。
