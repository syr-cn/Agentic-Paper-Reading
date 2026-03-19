# SkillOrchestra（Learning to Route Agents via Skill Transfer）DNL Deep Note

## 0) Metadata
- **Title:** SkillOrchestra: Learning to Route Agents via Skill Transfer
- **Alias:** SkillOrchestra
- **Authors / Org:** Jiayu Wang, Yifei Ming, Zixuan Ke, Shafiq Joty, Aws Albarghouthi, Frederic Sala（UW-Madison + Salesforce AI Research）
- **Venue / Status:** arXiv 2602.19672（v1, 2026-02-23）
- **Links:**
  - Abstract: https://arxiv.org/abs/2602.19672
  - PDF: https://arxiv.org/pdf/2602.19672
  - Code: https://github.com/jiayuww/SkillOrchestra
- **Tags:** agent orchestration, model routing, skill transfer, cost-aware inference, routing collapse
- **My rating:** ★★★☆☆（3/5）
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3**

---

## 1) 一句话 Why-read
它把“路由策略”从端到端 RL 参数学习，改成“技能手册（Skill Handbook）+ 能力画像”的可迁移知识层，在多轮编排里同时提升准确率并压低成本。

---

## 2) CRGP
### C — Context
在多轮 agent 工作流中，query-level 一次性路由太粗；而 RL 训练 orchestrator 虽灵活，但训练贵、适配新模型池慢，还会出现 routing collapse（反复调用单一昂贵模型）。

### R — Related work
- **启发式/判别式路由：** FrugalGPT、KNN/MLP/BERT Router、RouterDC、GraphRouter 等，通常是输入级一次决策。
- **RL 路由/编排：** Router-R1、ToolOrchestra，做序列决策但训练成本高，且有 collapse 风险。

### G — Research gap
缺少一种同时满足以下条件的编排方法：
1. 多轮、状态条件化（state-conditioned）决策；
2. 显式性能-成本权衡；
3. 可迁移到新 orchestrator / 新模型池，尽量不重训。

### P — Proposal
SkillOrchestra：
- 从轨迹中学习 **Skill Handbook**（mode insight + skill registry + agent profile）。
- 路由时先选 mode，再按激活 skill 的能力估计与成本做 agent 选择：
  \(\arg\max_A [\text{competence}(A,\Sigma_t)-\lambda_c\cdot \hat C_A]\)。
- 通过 Pareto 验证选择“与当前 orchestrator 能力匹配”的手册粒度。

---

## 3) Figure 区（读图抓手）
- **Figure 1（核心）：**
  - 左图（模型路由）和右图（完整 agent 编排）都显示 SkillOrchestra/SkillOrchestra+ 在 Pareto 前沿。
  - 关键数字：相对 RL 基线最高 **+22.5 个百分点**；学习成本相对 Router-R1 / ToolOrchestra 分别 **700× / 300×** 降低（摘要与引言给出）。
- **Figure 3（方法总览）：**手册学习 → 手册选择 → 部署路由三阶段。
- **Figure 6（行为诊断）：**直接给出 collapse 对比：Router-R1 对 Llama-3.1-70B 调用 **98.02%**。

---

## 4) Experiments
### 4.1 Experimental setup（可提取设置）
**A) Model Routing setting**
- 数据：9 个 QA/推理基准
  - General QA：NQ, TriviaQA, PopQA
  - Multi-hop QA：HotpotQA, 2Wiki, Musique, Bamboogle
  - Math：MATH, AMC23
- Orchestrator：**Qwen2.5-3B**
- Model pool（6）：Qwen2.5-7B, Llama-3.1-8B, Llama-3.1-70B, Mistral-7B, Mixtral-8x22B, Gemma-2-27B
- 模式：search + answer
- 最大轮数：**4 turns**
- 指标：EM、总完成成本（completion cost）
- 训练数据规模：SkillOrchestra 为低数据（每数据集默认 **k<50** 样本建手册，另 **k** 用于验证/检索）；Router-R1 报告 **14k samples**。

**B) Agent Orchestration setting（FRAMES）**
- 基准：**FRAMES**
- modes：search / code / answer
- 最大交互长度：**50 turns**
- 工具：Tavily WebSearch + FAISS LocalSearch（Qwen3-Embedding-8B）+ Python sandbox
- 模型池：
  - search: GPT-5, GPT-5-mini, Qwen3-32B
  - code: GPT-5, GPT-5-mini, Qwen2.5-Coder-32B
  - answer: GPT-5, GPT-5-mini, Llama-3.3-70B-Instruct, Qwen3-32B, Qwen2.5-Math-72B, Qwen2.5-Math-7B
- 答案评估：GPT-5-mini as judge

### 4.2 Main result table（关键数字）
| 场景 | Baseline | SkillOrchestra | SkillOrchestra+ / 备注 |
|---|---:|---:|---:|
| QA 平均 EM（7个 QA 集） | Router-R1 **41.6** | **47.4**（+5.8） | **51.6**（+10.0） |
| TriviaQA EM | Router-R1 70.6 | 71.6 | **80.2** |
| Musique EM | Router-R1 13.8 | 18.2 | **20.6** |
| Bamboogle EM | Router-R1 51.2 | 58.4 | **63.2** |
| QA 平均成本（¢） | Router-R1 **51.8¢** | **38.4¢** | 41.6¢ |
| Math(MATH) acc / cost | Router-R1 55.8 / 6.5¢ | **73.6 / 3.6¢** | — |
| Math(AMC) acc / cost | Router-R1 25.0 / 1.6¢ | **52.5 / 0.5¢** | — |
| FRAMES acc / total $ | ToolOrchestra 76.3% / $92.7 | **84.3% / $72.7** | 文中另处报告 85.0%（100 样本消融） |
| FRAMES 对比专有编排器 | GPT-5: 74.6% / $120.4 | **84.3% / $72.7** | Claude Opus 4.5: 77.9% / $758.1；Gemini 3 Pro: 78.9% / $1729.3 |

> 注：论文正文在不同段落中出现 **84.3%**（主结果叙述）与 **85.0%**（Table 2 full system, 100样本）两组数值，语境不同（全量评测 vs 消融子集）。

### 4.3 Analysis（现象 + 解释 + 我的判断）
1. **现象：** Router-R1 出现明显 collapse：Llama-3.1-70B 调用占比 **98.02%**，其余模型单个都 ≤0.92%。  
   **解释（作者）：** 端到端 RL 容易收敛到“单强模型反复调用”的局部最优。  
   **我的判断：** 这个证据很强，且直接解释了“高成本+泛化弱”。对生产系统而言，先做路由行为分布监控（熵/集中度）是必要监控项。

2. **现象：** SkillOrchestra 路由更均衡：Mixtral-8x22B **44.53%**、Qwen2.5-7B **25.99%**、Llama-3.1-70B **15.38%**、Qwen2.5-3B **11.50%**。  
   **解释（作者）：** skill-conditioned competence + cost 显式权衡，让模型按能力分工而非盲目上大模型。  
   **我的判断：** 这是方法最有工程价值的点：能把“什么时候该贵、什么时候该省”固化为可解释规则层。

3. **现象：** 手册可跨 orchestrator 迁移且增益显著：例如 Qwen2.5-7B **35.7→60.0（+24.3）**，Llama3.1-8B **35.5→58.0（+22.5）**。  
   **解释（作者）：** 手册是模型无关的编排知识，不绑定某个 router 参数。  
   **我的判断：** 这比“重训一个新 router”更符合快速迭代团队需求；但仍需验证跨任务域迁移（当前主要在同类 QA/FRAMES 框架内）。

4. **现象：** FRAMES 消融中，去掉手册后准确率 **85.0%→71.0%**，成本 **9.3→122.9**（100 样本）。  
   **解释（作者）：** 没有结构化技能约束时，编排会走向冗余调用与错误 mode/agent 选择。  
   **我的判断：** 成本暴涨幅度极大，说明“技能层”不仅提升精度，还提供了强约束，类似 policy regularizer。

### 4.4 证据缺口（明确标注）
- 统计显著性（置信区间/方差/检验）：**原文未给出可提取数字**。  
- 真实线上延迟分位数（P50/P95）与吞吐：**原文未给出可提取数字**。  
- 更大规模长期在线学习稳定性（>周级持续更新）：**原文未给出可提取数字**。

---

## 5) Why it matters for our work
- **Agent memory：** Skill Handbook 很像“可执行记忆层”，可把经验沉淀成可检索、可版本化的技能图谱，而非纯文本历史。
- **Long-context：** 把“全部历史塞上下文”改为“按技能检索必要知识”，能降低 token 成本与注意力稀释。
- **Multimodal RL：** skill 抽象可扩展到视觉/工具动作（如 GUI 操作、代码执行、检索策略），为跨模态 option routing 提供统一接口。

---

## 6) Actionable next steps（3 条，可执行）
1. **Memory 方向：**做一个 Skill-Handbook sidecar（JSON/图结构），把每次多步任务记录为 `mode→skill→agent→outcome→cost`，并在线更新 Beta 能力参数 \((\alpha,\beta)\)。
2. **Long-context 方向：**在现有 agent pipeline 做 A/B：`全量长上下文` vs `技能检索注入`，统一比较任务成功率、平均 token、总成本、路由熵。
3. **Multimodal RL 方向：**把“mode”扩展为 `search / code / vision / ui-action`，先离线做 skill discovery + merge/split，再用 Pareto 选择不同容量 orchestrator 的最优粒度手册。

---

## 7) 评分解释（保持原评分倾向）
- **维持 3/5，不上调。**
- 优点：问题定义准、方法结构化、结果数字硬，尤其是 collapse 诊断和成本收益都清楚。
- 扣分点：泛化与统计稳健性报告还不充分；部分结果在不同实验子集之间口径不同（需更统一的主表与置信区间）。
- 结论：值得作为“低训练成本编排”路线重点跟进，但在生产前要补齐稳定性与统计证据链。