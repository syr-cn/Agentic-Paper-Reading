# SkillOrchestra 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** SkillOrchestra: Learning to Route Agents via Skill Transfer
- **Alias:** skillorchestra
- **Authors / Org:** Jiayu Wang, Yifei Ming, Zixuan Ke, Shafiq Joty, Aws Albarghouthi, Frederic Sala（UW-Madison + Salesforce AI Research）
- **Venue / Status:** arXiv 2602.19672v1（preprint）
- **Date:** 2026-02-23
- **Links:**
  - Abs: https://arxiv.org/abs/2602.19672
  - HTML: N/A（arXiv 页面显示该稿件无 HTML 转换）
  - PDF: https://arxiv.org/pdf/2602.19672
  - Code: https://github.com/jiayuww/SkillOrchestra
- **Case 对齐（>=2）:**
  - `papers/2026-03-11_evo-memory.md`
  - `papers/2026-03-13_reasoning-judge.md`
- **Tags:** agent-orchestration, model-routing, skill-transfer, cost-aware-inference, RL-collapse
- **My rating:** ★★★☆☆（维持原倾向）
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3**

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：**SkillOrchestra 用“Skill Handbook（技能手册）”替代端到端 RL 路由策略学习，在多轮路由/编排中把“能力匹配+成本约束”显式化，既提升准确率又降低推理成本，并缓解 RL router 的 routing collapse。

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- 多轮 agent 编排的关键痛点：一次性 query-level 路由太粗；端到端 RL 编排训练贵、迁移慢、上线后常退化为单模型高频调用。

### R — Related work
- **无/弱编排路由：** Largest LLM、Prompt Router、KNN/MLP/BERT Router、RouterDC、GraphRouter、FrugalGPT。
- **RL 编排：** Router-R1、ToolOrchestra，能做序列决策但训练与维护成本高。

### G — Research gap
- 缺少一种可落地方案同时满足：
  1) 多轮状态条件化决策；
  2) 显式性能-成本权衡；
  3) 可跨 orchestrator / 模型池迁移，避免反复重训。

### P — Proposal
- 提出 **SkillOrchestra**：
  - 从轨迹学习并维护 **Skill Handbook**（mode insight + skill registry + agent profile）；
  - 路由时先判 mode，再按 skill-competence 与 cost 做 agent 选择；
  - 通过 Pareto 验证为目标 orchestrator 选择匹配粒度的手册子集。

## 3) Figure 区（至少 1 张，抓主图，不跳过）
- 图1（主结果：Pareto 前沿，模型路由+agent 编排）：
  ![fig1](https://arxiv.org/src/2602.19672v1/figures/pareto_overview_v3.pdf)
  - 对应论文 Figure 1：SkillOrchestra / SkillOrchestra+ 在准确率-成本上处于 Pareto 前沿，优于启发式、判别式和 RL 基线。

- 图2（方法总览：手册学习→选择→部署）：
  ![fig2](https://arxiv.org/src/2602.19672v1/figures/skillorchestra_overview_final_v8.pdf)
  - 对应论文 Figure 3：把“技能知识层”与“具体 orchestrator 参数”解耦，解释了其迁移能力来源。

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- 任务/数据：
  - **Model routing:** 9 个 benchmark（NQ, TriviaQA, PopQA, HotpotQA, 2Wiki, Musique, Bamboogle, MATH, AMC23）
  - **Agent orchestration:** FRAMES
- 模型/agent 配置：
  - orchestrator（routing setting）: **Qwen2.5-3B**
  - model pool（6）: Qwen2.5-7B, Llama-3.1-8B, Llama-3.1-70B, Mistral-7B, Mixtral-8x22B, Gemma-2-27B
  - routing 最高 **4 turns**；FRAMES 最高 **50 turns**
- 对比基线：Largest LLM / Prompt LLM / KNN/MLP/BERT Router / RouterDC / GraphRouter / FrugalGPT / **Router-R1** / ToolOrchestra
- 评测指标：EM / accuracy、completion cost（¢）与 total cost（$）
- 训练样本效率：文中给出 Router-R1 使用 **14k** 样本；SkillOrchestra 为小样本手册构建（默认每数据集 `k<50`）。

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| QA Avg. EM（7个QA） | Router-R1 **41.6** | SkillOrchestra **47.4** | **+5.8** |
| QA Avg. EM（7个QA） | Router-R1 **41.6** | SkillOrchestra+ **51.6** | **+10.0** |
| QA Avg. cost | Router-R1 **51.8¢** | SkillOrchestra **38.4¢** | **-13.4¢** |
| TriviaQA EM | 70.6 | 80.2（SkillOrchestra+） | +9.6 |
| Musique EM | 13.8 | 20.6（SkillOrchestra+） | +6.8 |
| Bamboogle EM | 51.2 | 63.2（SkillOrchestra+） | +12.0 |
| MATH acc / cost | 55.8 / 6.5¢ | 73.6 / 3.6¢ | +17.8 / -2.9¢ |
| AMC acc / cost | 25.0 / 1.6¢ | 52.5 / 0.5¢ | +27.5 / -1.1¢ |
| FRAMES acc / total $ | ToolOrchestra 76.3% / $92.7 | SkillOrchestra **84.3% / $72.7** | +8.0 / -$20.0 |

补充主文强调数字：
- 相对 RL 编排基线最高 **+22.5 pct**；学习成本相对 Router-R1 / ToolOrchestra 约 **700× / 300×** 下降（摘要与引言口径）。

### 4.3 Analysis experiments（强制“现象+解释”）
- **现象：** Router-R1 出现明显 routing collapse：**98.02%** 调用 Llama-3.1-70B，其余模型单个占比 ≤0.92%。  
  **解释（作者）：** 端到端 RL 易收敛到“单一强模型反复调用”的局部最优。  
  **【标注】（我的判断，可选）：** 这是本文最有说服力证据之一；工程上应把“路由分布熵/集中度”作为上线监控 KPI。

- **现象：** SkillOrchestra 的调用分布更均衡：Mixtral-8x22B **44.53%**、Qwen2.5-7B **25.99%**、Llama-3.1-70B **15.38%**、Qwen2.5-3B **11.50%**。  
  **解释（作者）：** skill-conditioned competence 与成本项共同约束路由。  
  **【标注】（我的判断，可选）：** 这说明方法不是“只省钱”而是“按技能分工”，可解释性明显好于黑盒 RL policy。

- **现象：** 手册可跨 orchestrator 迁移：Qwen2.5-7B **35.7→60.0（+24.3）**，Llama3.1-8B **35.5→58.0（+22.5）**，Mistral-7B **36.5→59.8（+23.3）**。  
  **解释（作者）：** 手册作为知识层，不绑定特定 router 参数。  
  **【标注】（我的判断，可选）：** 对频繁换模型池的团队非常实用；但目前主要验证在同任务族，跨域泛化还需补证。

- **现象：** FRAMES 消融中，去掉手册后 accuracy **85.0%→71.0%**，cost **9.3→122.9**（100 样本设置）。  
  **解释（作者）：** 缺失结构化技能约束会导致错误模式选择和冗余调用。  
  **【标注】（我的判断，可选）：** 成本恶化幅度很大，手册在这里起到了“策略正则器”的作用。

### 4.4 Case studies（>=2）
- **Case 1（AMC，Figure 8）**：router 在有手册条件下判断可由自身能力直接解题，不发起 `<search>` 外部模型调用，仍得到正确答案。  
  **要点：** SkillOrchestra 不是“强制多模型”，而是“可选调用”，能避免不必要升级。

- **Case 2（PopQA，Figure 9）**：初始模型响应噪声较大后，router 基于技能需求重新选更匹配模型，经过多步外部调用恢复到正确答案。  
  **要点：** 手册化技能让路由具备“纠错式重试”能力，而不是固定单路策略。

### 4.5 证据缺口（明确标注）
- 统计显著性/置信区间：**原文未给出可提取数字**。  
- 在线延迟分位数（P50/P95）与吞吐：**原文未给出可提取数字**。  
- 长周期在线更新稳定性（周级以上）：**原文未给出可提取数字**。

## 5) Why it matters for our work
- 对 memory 系统：Skill Handbook 可视作“可执行记忆层”，比纯历史拼接更利于版本化与治理。
- 对 long-context：把“全历史注入”改为“技能检索注入”，有机会同时降 token 与提稳定性。
- 对 multimodal agent：mode/skill 抽象可扩展到 vision、UI-action、tool-use，便于统一路由接口。

## 6) Actionable next step
- [ ] 做一个 handbook sidecar：记录 `mode→skill→agent→outcome→cost`，在线更新技能能力分布参数。  
- [ ] 在现有 pipeline 跑 A/B：`全量上下文` vs `技能检索注入`，统一比较成功率、成本、路由熵。  
- [ ] 增加 collapse 监控：模型调用分布熵、top-1 占比、无效升级率（调用更贵模型但收益不足）。

## 7) 评分解释（必填）
- **质量分 x/2：** 1/2（方法结构清晰、结果硬；但统计稳健性与线上指标报告不足）
- **Observation 分 y/2：** 1/2（collapse→skill-regularized routing 的证据链很清楚）
- **总分 z/5：** **3/5**
- **为什么不是更高分：**
  - 缺少显著性与方差报告；
  - 部分结果口径存在不同语境（如 FRAMES 84.3% 与 85.0%）；
  - 仍需更多跨任务域与长周期部署证据。
