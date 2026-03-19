# 01.me Agent Continual Learning（DNL 重做版）

## 0) Metadata
- **Title:** The Dilemma of Continuous Learning for Agents: Why a Reasoner Is Not a True Agent  
- **Alias:** 01me-Agent-Continual-Learning  
- **Authors / Org:** Pine AI / 01.me（博客作者未给出标准论文作者列表）  
- **Venue / Status:** Blog / System Experience（非同行评审论文）  
- **Date:** 2025-10（页面时间）  
- **Links:**
  - Blog: https://01.me/en/2025/10/agent-continual-learning/
  - DAPO（文中引用）: https://arxiv.org/pdf/2503.14476
  - DeepSeek-OCR（文中引用）: https://arxiv.org/html/2510.18234v1
- **Tags:** continual learning, agent memory, dual-lora, world model, online adaptation, real-time agent  
- **My rating:** ★★★☆☆（保持原倾向）  
- **Read depth:** normal（观点+工程细节精读）  
- **Scoring (1+2+2):** 基础 1 + 质量 0 + Observation 2 = **3/5**

---

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：** 这篇文最有价值的主张是“Reasoner ≠ Agent，真正分水岭是持续学习能力”，并给出一个可执行工程方向：**Dual-LoRA 把 policy learning 与 world-model learning 解耦**，试图提升现实任务样本效率。

---

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- 文章背景是当前 Agent 系统在真实任务中的表现落差：单轮推理很强，但进到真实流程（电话、工具调用、企业规则）后适应慢、错误多。  
- 作者把问题指向“缺持续学习机制”，而不只是“模型还不够大”。

### R — Related work
- 关联 RL 路线：PPO/GRPO/DAPO（文中强调 model-free RL 主要依赖 reward，难学 observation）。  
- 关联 memory 路线：长上下文、外部知识库、动态总结。  
- 关联 world-model 路线：文中提到 Meta “Early Experience”式思路（预测环境反馈而非只学动作）。

### G — Research gap
- Gap 1：把长上下文当作“自动学习器”是误解；它更像 retrieval，不会自动总结规则。  
- Gap 2：纯 reward 驱动的 RL 对现实任务反馈利用不足，样本效率低。  
- Gap 3：当前很多系统混淆 reasoner 与 true agent 的评价标准，缺“持续变强”视角。

### P — Proposal
- 提出 **Dual-LoRA**：
  - LoRA1 学 policy（reward/advantage 驱动）
  - LoRA2 学 world model（预测 observation）
- 技术上用 rank 空间拆分与梯度隔离减少互扰：总 rank=64，拆为 32+32。  
- 系统层面强调“知识抽取/结构化”而非“原文堆上下文”。

---

## 3) Figure 区（至少 1 张，抓主图，不跳过）
- 图1（真实图链，训练效率对比）：  
  ![fig1-minimind-loss](https://01.me/en/images/2025/10/minimind-loss.png)  
  文中说明该图对比了 MiniMind 预训练 loss 曲线（改进版 vs 原版）；对应文字给出关键数字：达到 loss=3.0 的步数从 **36 → 12**，10 epoch 最终 loss **2.0 → 1.7**。

- 图2（真实图链，实测输出案例图之一）：  
  ![fig2-retool-1](https://01.me/en/images/2025/10/retool-1.png)  
  这组图（retool-1~4）展示了改进前后问答样例的可读性与事实性变化，属于“定性支持”。

---

## 4) Experiments（必须含具体数字）
> 说明：本文是博客，不是标准论文；实验披露混合“明确数字 + 案例描述”。以下只记录可明确提取的数字，并标注证据强弱。

### 4.1 Experimental setup
- **Dual-LoRA 参数拆分**：总 rank = **64**，policy 分支 **32**，world-model 分支 **32**。  
- **World-model loss**：\(L_{world}=-\mathbb{E}[\log P(o_{t+1}|s_t,a_t)]\)。  
- **实时交互速率（文中给出）**：
  - model prefill：**500–1000 tokens/s**
  - model output：**100 tokens/s**
  - human speech input/output：**20 tokens/s**（text 约 5 tokens/s）
- **Mistral-7B 韩语 LoRA 案例设置（文中）**：
  - Stage1：韩语维基 **5%** 数据，LoRA rank **128**，lr **5e-5 + 1e-5**，**1 epoch**，**8×4090，4h**
  - Stage2：韩语指令 SFT，**2 epochs**，**8×4090，4h**
- **MiniMind 2（100M）训练成本示例**：
  - pretrain **6h** + SFT **8h** = **14h**（8×4090）
  - 成本估算 **$33.6**（对比 NanoChat **$64**）

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| MiniMind：到 loss=3.0 所需步数 | 36 steps | 12 steps | **-24**（约 **3.0×** 更快） |
| MiniMind：10 epoch 最终 loss | 2.0 | 1.7 | **-0.3**（约 **-15%**） |
| MiniMind 2 训练总成本（文中对比） | $64（NanoChat基准） | $33.6 | **-$30.4**（约 **-47.5%**） |
| Long context 压缩引用（DeepSeek-OCR） | 10×压缩常规担忧 | 10×下OCR约97% | 作为“压缩可行性”证据 |
| DeepSeek-OCR 高压缩点 | - | 20×下OCR约60% | 给出性能-压缩折中点 |

> 注：前3行是本文作者/文中明确给出的核心数字；后2行是文中引用他文数字，用于支持“压缩并非必然崩溃”的论点。

### 4.3 Analysis experiments（强制“现象+解释”）
1) **现象：** 文中把“长上下文自动学习”明确判为误解，并给出多个失败 case。  
   **解释（作者）：** attention 本质更像检索，不会自动把历史压缩成稳定规则。  
   **【标注】（我的判断）：** 这个判断和我们在长轨迹 agent 里的经验一致，尤其在计数、约束追踪任务上复现频率很高。

2) **现象：** 通过结构化提示（例如直接写“这是第3次电话”）可显著减少越界调用。  
   **解释（作者）：** 显式结构字段把“重复扫描并计数”的负担从模型隐式推理迁移到外部状态表达。  
   **【标注】（我的判断）：** 这说明“状态工程”在 agent 系统里常比“继续加长 context”更高 ROI。

3) **现象：** Dual-LoRA 主张用 observation-prediction 补足 reward-only 学习盲点。  
   **解释（作者）：** reward=0 时 policy 梯度信息稀薄，但 observation 仍提供高密度学习信号。  
   **【标注】（我的判断）：** 方向很对，但目前缺正式 ablation（单LoRA vs 双LoRA）与统计显著性，证据级别仍偏工程报告。

4) **现象：** MiniMind 里 QK Norm + Muon 给出 36→12 steps、2.0→1.7 等改进。  
   **解释（作者）：** 优化器与注意力归一化改动虽小，但可显著改善收敛速度与最终损失。  
   **【标注】（我的判断）：** 这些数字是有价值的“算法工程证据”，但与核心命题（Agent 持续学习）之间仍是间接支持。

#### Case 对齐（>=2，来自原文）
- **Case 1（黑白猫计数）**：100 条样本（90黑/10白）若不先总结，模型每次都重复扫描与统计。  
- **Case 2（Xfinity 折扣规则）**：仅堆“老兵可折扣/医生可折扣/其他不可”历史片段，模型在新案例中容易错配。  
- **Case 3（电话次数上限）**：约束“最多3次”在长上下文里常失控，增加显式计数字段后明显稳定。

---

## 5) Why it matters for our work
- 对 **agent memory**：这篇文支持“memory 不是日志仓”，而是要有结构化状态、规则抽取与更新闭环。  
- 对 **long-context**：提示我们把长上下文当“缓存层”，而不是当“学习层”；学习仍需蒸馏与参数/外存协同更新。  
- 对 **tool-use / RL agent**：Dual-LoRA 思路可迁移为“policy-head 与 world-state head 分路更新”，减少互相污染。

---

## 6) Actionable next step
- [ ] **复现一个最小 Dual-Adapter 原型**：总 rank 64，策略/世界模型各 32，先在工具调用环境做 1 周离线验证。  
- [ ] **做 context 状态工程 A/B**：对同任务比较“纯日志上下文”vs“显式状态字段（计数/规则摘要）”，看错误率与token成本。  
- [ ] **加 observation 学习信号**：在 reward 稀疏任务里增加 next-observation 预测损失，测样本效率（达到同成功率所需 episodes）。

---

## 7) 评分解释（必填）
- **质量分 x/2：0/2**（非论文体，实验设计与统计披露不充分）  
- **Observation 分 y/2：2/2**（问题拆解非常到位，工程启发强）  
- **总分 z/5：3/5（维持原倾向）**  
- **为什么不是更高分：**
  1) 缺统一 benchmark 与完整对比；
  2) Dual-LoRA 缺公开严谨 ablation/显著性；
  3) 证据更多是系统经验与案例，离“可复现实证论文”仍有距离。
