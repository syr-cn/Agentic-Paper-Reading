# AutoSkill（Experience-Driven Lifelong Learning via Skill Self-Evolution）DNL Deep Note

## 0) Metadata
- **Title:** Experience-Driven Lifelong Learning via Skill Self-Evolution  
- **Alias:** AutoSkill  
- **Authors / Org:** Yutao Yang*, Junsong Li*, Qianjun Pan*, Bihao Zhan, Yuxuan Cai, Lin Du, Jie Zhou†, Kai Chen†, Qin Chen, Xin Li, Bo Zhang, Liang He（ECNU + Shanghai AI Lab）  
- **Venue / Status:** arXiv preprint（2603.01145, cs.AI）  
- **Date:** 2026-03  
- **Links:**  
  - Abstract: https://arxiv.org/abs/2603.01145  
  - PDF: https://arxiv.org/pdf/2603.01145  
  - Code: https://github.com/ECNU-ICALK/AutoSkill  
- **Tags:** lifelong-learning, agent-memory, skill-evolution, personalization, training-free  
- **My rating:** ★★★☆☆（3/5）  
- **Read depth:** deep  
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3**

---

## 1) 一句话 Why-read
AutoSkill 的核心价值在于：把“长期记忆”从可检索文本片段升级为**可版本化、可合并、可编辑的技能工件（SKILL.md）**，并在 **training-free** 前提下实现跨会话持续个性化。

---

## 2) CRGP
### C — Context
长期个性化 Agent 的瓶颈不只是上下文窗口大小，而是如何把零散交互经验沉淀为稳定可复用行为。

### R — Related work
现有 memory/RAG 方法多聚焦“召回历史片段”，对“行为策略资产化（可维护、可演化）”支持不足。

### G — Research gap
缺少一个**不改底座参数**、支持在线更新且具备可解释结构的终身学习层；同时还要避免 memory 被模型自生成噪声污染。

### P — Proposal
AutoSkill 给出双循环机制：
1. **在线循环（inference-time）**：rewrite → hybrid retrieval（dense + BM25）→ skill 注入生成。  
2. **后台循环（asynchronous）**：技能抽取 → 邻域检索 → judge（add / merge / discard）→ 版本递增 merge。  
3. **关键约束**：抽取证据优先来自用户 query，减少“模型自回声”进入长期记忆。

---

## 3) Figure 区（读图抓手）
- **Figure 2:** SkillBank 总体统计（总技能数 N=1858）。
- 我重点关注：
  - 技能总量与子库分布（语言 × 模型来源）
  - 单技能版本迭代深度（如高频技能是否更快演化）
- 图表定位：论文 PDF 中 Figure 2（https://arxiv.org/pdf/2603.01145）。

---

## 4) Experiments
### 4.1 Experimental setup（可提取设置）
- **训练方式：** training-free（不更新 LLM 参数）。
- **数据来源：** WildChat-1M。
- **筛选条件：** 保留 **>8 turns** 的对话。
- **分桶方式：** 按语言（zh/en）× 对话模型来源（GPT-3.5/GPT-4）形成四个子集。
- **输出对象：** 四个 SkillBank 子库 + 技能演化统计。

> 说明：检索融合权重、重写 prompt 长度、judge 阈值等关键超参，原文在当前可提取信息中**未给出明确数字**。

### 4.2 Main results（只写可提取数字）
| Item | Value |
|---|---:|
| SkillBank 总技能数（Fig.2） | **1858** |
| 英文 GPT-3.5 子集 conversations | **10,243** |
| 英文 GPT-3.5 子集 messages | **267,681** |
| 英文 GPT-3.5 子集 skills | **631** |
| 中文 GPT-4 子集 conversations | **1,145** |
| 中文 GPT-4 子集 messages | **36,834** |
| 中文 GPT-4 子集 skills | **224** |
| 示例技能版本（professional_text_rewrite） | **v0.1.34** |

### 4.3 Analysis（现象 + 解释 + 我的判断）
1. **现象：** 技能分布集中在编程、写作等高频任务域。  
   **解释（作者）：** 技能抽取受真实交互频次驱动，高频需求更容易被沉淀。  
   **我的判断：** 这是“用户行为分布驱动的记忆偏置”，工程上合理，但会导致长尾能力难以积累；后续应考虑低频高价值任务的加权保留策略。

2. **现象：** 技能演化速率不均，部分技能版本快速增长（如 v0.1.34）。  
   **解释（作者）：** 高频触发 + 多轮反馈会提升 merge 发生概率。  
   **我的判断：** 版本号增长本身不等于质量提升；如果没有任务成功率或回归测试，可能出现“频繁重写但收益不稳定”的伪进化。

3. **现象：** 同一 SKILL.md schema 可覆盖风格技能（如改写语气）与流程技能（如步骤化任务执行）。  
   **解释（作者）：** 统一工件格式提高跨任务复用与维护效率。  
   **我的判断：** 统一 schema 是对的，但需防止“过宽 schema”导致检索歧义；建议增加 trigger/constraints/failure-pattern 三段式字段，提升调用精度。

4. **现象：** 论文强调“证据优先来自用户 query”来抑制模型自回声。  
   **解释（作者）：** 降低模型自生成内容被误写入长期记忆的风险。  
   **我的判断：** 方向正确，但仍需要显式污染率指标；否则难判断该机制相对普通日志抽取到底减少了多少噪声。

### 4.4 当前证据缺口（必须明确）
- 与主流 baseline 的严格对比（如 summary-memory / vector-memory / reflective-memory）：**原文未给出可提取数字**。  
- 任务级效果（成功率、用户满意度、长期一致性）：**原文未给出可提取数字**。  
- 关键消融（去掉 rewrite / judge / merge 各模块）：**原文未给出可提取数字**。  
- 统计显著性、置信区间或方差报告：**原文未给出可提取数字**。

---

## 5) Why it matters for our work
- **Agent memory：** 提供“记忆工件化”路线，把记忆从文本缓存变成可治理资产（可审计、可回滚、可版本控制）。  
- **Long-context：** 通过技能压缩历史经验，减少对超长上下文的被动依赖，潜在降低 token 成本和噪声注入。  
- **Multimodal RL：** 可把工具调用轨迹、GUI 操作序列、视觉决策模式也抽象成技能项，为 option-like 库构建提供中间层。

---

## 6) Actionable next steps（3 条，面向 memory / long-context / multimodal RL）
1. **Memory 侧（两周 PoC）**：实现 training-free sidecar（rewrite + hybrid retrieve + async extract + versioned merge），并对每条技能记录 source span 与 merge reason，确保可追溯。  
2. **Long-context 侧（A/B 实验）**：对同一任务集比较三种配置：`纯长上下文` vs `summary-memory` vs `AutoSkill-style skill memory`；统一统计任务成功率、平均 token、响应延迟。  
3. **Multimodal RL 侧（schema 扩展）**：将技能结构扩展为 `trigger / constraints / procedure / tool-state / failure-pattern / recovery`，先在 GUI-tool use 轨迹上离线抽取，再做在线检索调用。

---

## 7) 评分解释（保持原评分倾向）
- **总分维持：3/5（不改分）**。  
- **质量分 1/2：** 框架完整、工程可落地，但实证层面缺少强 baseline 与任务级量化。  
- **Observation 分 1/2：** “技能工件化”视角有启发，但反直觉结论与因果证据不够强。  
- **为什么不是更高分：** 关键指标与消融数据不足，难以判断其相对现有 memory 系统的真实增益幅度与稳定性。