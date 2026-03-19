# In-Context RL for Tool Use 阅读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** In-Context Reinforcement Learning for Tool Use in Large Language Models  
- **Alias:** ICRL  
- **Authors / Org:** Yaoqi Ye, Yiran Zhao, Keyu Duan, Zeyu Zheng, Kenji Kawaguchi, Cihang Xie, Michael Qizhe Shieh（NUS / Salesforce AI Research / UC Berkeley / UC Santa Cruz）  
- **Venue / Status:** arXiv 2603.08068 (v1, 2026-03-09)  
- **Links:** [Abs](https://arxiv.org/abs/2603.08068) | [PDF](https://arxiv.org/pdf/2603.08068) | [Code](https://github.com/applese233/ICRL)  
- **My rating:** ★★★★☆（维持原倾向）  
- **Read depth:** deep（通读方法+实验+附加分析）  
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = **4**

---

## 1) 一句话 Why-read
这篇最值得读的是：它把“先 SFT 再 RL”的冷启动路径替换成“**rollout 中 few-shot + 逐步退火到 0-shot**”的 RL-only 训练，且在工具调用 QA 上给出了稳定且显著的增益。

---

## 2) CRGP
### C — Context
工具增强 LLM（search / python）是趋势，但主流训练仍依赖 cold-start SFT，标注/合成轨迹成本高；纯 RL 从零开始又常因探索无效而崩。

### R — Related work
文中对比了三类路线：
- **Direct Prompting：** Direct / CoT
- **Retrieval-based：** RAG / IRCoT / Search-o1
- **Fine-tuning / RL-based：** SFT / R1 / Reject Sampling / Search-R1 / ZeroSearch / O²-Searcher / ParallelSearch

### G — Research gap
作者明确要填的空白：
1. 如何在**不做 SFT**的情况下让模型学会结构化工具调用格式（`<think><search><information><answer>`）。
2. 如何避免纯 RL 的冷启动探索低效（reward 稀疏、格式错误多）。
3. 如何从“有示例依赖”过渡到“无示例自治调用工具”。

### P — Proposal
ICRL 核心是三件事：
1. **few-shot rollout**：把演示样例放进 RL rollout prompt，而不是先做 SFT。  
2. **curriculum 退火**：演示数按阶段递减（主推 `3→2→0`）。  
3. **GRPO + loss masking + 复合奖励**：
   - GRPO 组内相对优势训练；
   - tool 返回内容不参与梯度；
   - 奖励 = EM 准确率 + 格式正确性。

---

## 3) Figure 区（这篇该看的图/表）
1. **Fig.1（方法总览）**：ICRL 训练流程图。重点是“示例数逐步减少”的多阶段训练，而不是单阶段 RL。  
2. **Table 主结果（Qwen2.5-3B/7B, 5个QA集）**：ICRL 平均 EM 达到 **40.16 / 49.12**。  
3. **Fig. curriculum ablation（3→2→0 vs 3→2→1→0）**：
   - 准确率上三阶段显著更好（如 TriviaQA **75.4 vs 20.8**）。
   - 但四阶段更“早停”：2 turn 内完成率 **59.39%**（四阶段）vs **29.65%**（三阶段）。
4. **Table 无SFT对比（vs O²-Searcher）**：不做 SFT 的 ICRL 平均 **40.16**，高于 O² 的 **37.26**。  
5. **Table 数学泛化（Qwen3-8B）**：AIME2024 **64.1**（低于 ReTool 67.0），AIME2025 **51.7**（高于 ReTool 49.3）。

---

## 4) Experiments
### 4.1 Experimental setup（可复现信息）
- **Backbone**：Qwen2.5-3B/7B/14B-Instruct，另测 Qwen3-8B。  
- **训练集**：Natural Questions（NQ，FlashRAG版本）。  
- **few-shot 演示来源**：随机 3 个 web 问题 + GPT-5.2 生成格式化示例。  
- **工具**：Serper API（Google Search），每次 query 取 **top-3 文档**。  
- **评测集**：TriviaQA / HotpotQA / 2Wiki / Musique / Bamboogle；每个数据集最多采样 **500** 题。  
- **RL细节**：
  - 算法：GRPO  
  - 每题 rollout 数：**8**  
  - temperature：**1.0**  
  - learning rate：**1e-6**  
  - max prompt len：**5000** tokens  
  - max response len：**2048** tokens  
  - 最大搜索轮数：**6** turns  
  - KL 系数：**0.001**  
  - batch size：**64**  
  - 资源：**4×A100 80GB**，FSDP + gradient checkpointing
- **奖励函数**：
  - `r = α * reward_acc + (1-α) * reward_format`，其中 **α=0.8**。  
  - 格式惩罚权重（按表顺序）：**0.5, 0.2, 0.15, 0.1, 0.1, 0.2**。

> 注：原文算法里写了每阶段训练步数 `T`，但**最终正文未给出固定数值**；早期注释里出现“约100 steps/阶段”，但该段在正文被注释，不能当最终实验设定。

### 4.2 Main result table（关键结果压缩）
| Setting | Baseline (best non-ICRL) | ICRL | Delta |
|---|---:|---:|---:|
| Qwen2.5-3B 平均EM | 31.10 (Search-R1) | **40.16** | **+8.94** |
| Qwen2.5-7B 平均EM | 41.78 (ParallelSearch) | **49.12** | **+7.34** |
| Qwen2.5-3B vs O²-Searcher | 37.26 | **40.16** | **+2.90** |

补充（数据集级）：
- 3B：TriviaQA **72.6**, HotpotQA **35.4**, 2Wiki **39.2**, Musique **20.0**, Bamboogle **33.6**。  
- 7B：TriviaQA **75.4**, HotpotQA **42.6**, 2Wiki **53.6**, Musique **26.0**, Bamboogle **48.0**。  
- 14B ICRL 平均 **51.84**（Direct 24.80, CoT 31.16）。

### 4.3 Analysis（现象 + 解释 + 我的判断）
1. **现象：** `3→2→0` 明显优于 `3→2→1→0`，例如 TriviaQA **75.4 vs 20.8**，2Wiki **53.6 vs 26.8**。  
   **解释（作者）：** 四阶段会让模型更快结束（2 turn 累计完成率 59.39%），但牺牲多跳推理质量。  
   **我的判断：** 中间 `1-shot` 阶段可能强化“模板压缩 + 早停策略”，让 policy 学到“少搜快答”而不是“必要时继续搜”。

2. **现象：** 在不做 SFT 的条件下，ICRL 仍超 O²-Searcher（40.16 vs 37.26）。  
   **解释（作者）：** few-shot rollout 在 RL 内提供了足够“软监督”，可替代冷启动 SFT。  
   **我的判断：** 这证明了“演示作为探索先验”比“静态 SFT 对齐格式”更经济；尤其适合工具协议变动频繁的场景。

3. **现象：** 训练曲线显示 0-shot 阶段 response length 先降后升，valid search 数持续上升。  
   **解释（作者）：** 去掉示例后模型先短答，再逐步学会独立组织更长结构并稳定调用工具。  
   **我的判断：** 这是典型“支架移除后的能力回填”信号，说明策略不是记住示例，而是在 RL 中内化了调用模式。

4. **现象：** 跨域到 code tool（AIME）时，ICRL 对 2024 略输（64.1<67.0）但 2025 反超（51.7>49.3）。  
   **解释（作者）：** 方法具有任务泛化性，且无需大规模标注。  
   **我的判断：** RL-only 在代码数学任务上已可竞争，但上限可能受 reward 颗粒度限制；若加过程奖励/执行轨迹奖励，可能继续拉开。

---

## 5) Why it matters for our work
对我们做 agent memory / long-context / multimodal RL，价值很直接：
- **训练范式层面**：可以把“昂贵 SFT 轨迹”转成“可控 rollout 课程设计”。
- **策略迁移层面**：`few-shot→zero-shot` 课程就是“外部脚手架→内部策略”的显式迁移路径，和 memory policy 蒸馏思路一致。
- **工程层面**：loss masking + 格式奖励这套组合，适合所有“模型token + 外部观测token”混合轨迹场景。

---

## 6) Actionable next steps（只给可执行项）
1. **Agent Memory 方向：做“记忆示例退火”实验**  
   - 设计 `k-memory demos: 3→2→0` vs `3→2→1→0`。  
   - 指标：任务成功率、平均检索步数、早停率、memory hit@k。  
   - 目标：验证是否同样存在“中间阶段诱导过早收缩搜索链”。

2. **Long-context 方向：把 format reward 升级成“结构+引用”双奖励**  
   - 在 `<answer>` 外增加对“引用 span 是否可追溯”的奖励。  
   - 对比仅EM奖励 vs EM+格式 vs EM+格式+引用一致性。  
   - 目标：降低长上下文下的幻觉压缩与无依据总结。

3. **Multimodal RL 方向：复刻 ICRL 课程到图文工具链**  
   - 工具标签扩展为 `<vision_query>/<ocr>/<table_read>/<answer>`。  
   - 先 3-shot 图文示例，再退火到 0-shot。  
   - 指标：工具调用有效率、跨模态证据一致性、最终EM/F1。  
   - 目标：验证 ICRL 课程是否可作为通用“多工具多模态策略学习”模板。

---

## 7) 评分解释（维持原评分，不无依据改分）
- 我维持 **4/5**。  
- 给高分原因：方法简洁、工程可落地、关键 ablation（尤其 curriculum）有说服力，且跨 QA / Math 都给了数字。  
- 暂不 5 分原因：
  1) 开放环境多工具（并行/规划/恢复）证据还不够；  
  2) 训练步数与部分实现细节披露不够完整（如每阶段 T 未最终明确）；  
  3) 还缺更系统的长程记忆型任务验证。