# In-Context Reinforcement Learning for Tool Use（ICRL）阅读笔记（DNL Deep Note，按新规重做）

## 0) Metadata
- **Title:** In-Context Reinforcement Learning for Tool Use in Large Language Models  
- **Alias:** ICRL  
- **Authors / Org:** Yaoqi Ye, Yiran Zhao, Keyu Duan, Zeyu Zheng, Kenji Kawaguchi, Cihang Xie, Michael Qizhe Shieh（NUS / Salesforce AI Research / UC Berkeley / UC Santa Cruz）  
- **Venue / Status:** arXiv 2603.08068 (v1, 2026-03-09)  
- **Date:** 2026-03  
- **Links:**  
  - Abs: https://arxiv.org/abs/2603.08068  
  - PDF: https://arxiv.org/pdf/2603.08068  
  - Code: https://github.com/applese233/ICRL  
  - Source(e-print): https://arxiv.org/e-print/2603.08068  
- **Tags:** tool-use RL, GRPO, curriculum, few-shot→zero-shot, RL-only training  
- **My rating:** ★★★★☆（维持原评分倾向）  
- **Read depth:** deep（主文+源码包）  
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = **4/5**

---

## 1) 一句话 Why-read
这篇最值得读的是：它把“先 SFT 再 RL”的冷启动范式替换为“**rollout 内 few-shot 支架 + 课程退火到 zero-shot**”的 RL-only 训练，并在 3B/7B 多数据集上给出可复现的显著增益。

---

## 2) CRGP
### C — Context
- 工具增强 LLM（Search/Python）已成主流，但高质量 SFT 轨迹贵且更新慢。  
- 纯 RL 从零学工具调用常遇到：格式不合规、有效搜索少、奖励稀疏导致探索塌缩。  

### R — Related work
- **Direct Prompting:** Direct, CoT  
- **Retrieval-based:** RAG, IRCoT, Search-o1  
- **RL / FT-based:** SFT, R1, Reject Sampling, Search-R1, ZeroSearch, O²-Searcher, ParallelSearch  

### G — Research gap
1. 不做 SFT 时，模型如何快速学会 `<think>/<search>/<information>/<answer>` 结构化协议？  
2. 纯 RL 冷启动如何提高早期探索有效性？  
3. 如何把“依赖示例”平滑过渡到“无示例自主工具使用”？

### P — Proposal
- **ICRL 三件套：**
  1) 在 RL rollout prompt 里放 few-shot 演示（而不是单独做 SFT）；  
  2) 多阶段减少示例数（主方案 `3→2→0`）；  
  3) GRPO + loss masking（屏蔽工具返回 token）+ 复合奖励（EM + 格式）。

---

## 3) Figure 区（含真图链）
> 说明：arXiv HTML 页面当前不可用（官方提示无 HTML 转换），以下使用论文 source 真图链。

- **图1：训练动态三联图（response length / reward / valid search）**  
![ICRL training dynamics](https://arxiv.org/src/2603.08068v1/reward_3plots.png)  
  读图要点：0-shot 阶段 reward 不暴涨，但 valid search 持续升，说明策略在“结构化调用”层面持续内化。

- **图2：response length 曲线（同组图源）**  
![ICRL response length](https://arxiv.org/src/2603.08068v1/response_length_3plots.png)  
  读图要点：去示例后长度先降再回升，符合“支架移除后重建自主推理链”的训练轨迹。

- **图3：valid search 曲线（同组图源）**  
![ICRL valid search](https://arxiv.org/src/2603.08068v1/valid_search_3plots.png)  
  读图要点：0-shot 期有效搜索上升，是比单看终局 EM 更关键的过程证据。

---

## 4) Experiments
### 4.1 Experimental setup
- **Backbone:** Qwen2.5-3B/7B/14B-Instruct；泛化实验含 Qwen3-8B。  
- **训练数据:** Natural Questions（FlashRAG 版本）。  
- **few-shot 演示:** 随机 3 个 web 问题 + GPT-5.2 生成格式化示例。  
- **工具:** Serper/Serp 后端检索；每次 query 取 top-3 文档。  
- **评测集:** TriviaQA / HotpotQA / 2Wiki / Musique / Bamboogle；每集最多采样 500。  
- **RL 关键超参:** GRPO，rollout=8，temp=1.0，lr=1e-6，max prompt=5000，max response=2048，max search turns=6，KL=0.001，batch=64。  
- **训练资源:** 4×A100 80GB，FSDP + gradient checkpointing。  
- **奖励函数:** `r = 0.8*reward_acc + 0.2*reward_format`；格式惩罚权重：0.5/0.2/0.15/0.1/0.1/0.2。  

【缺失标注】  
- 每阶段训练步数 `T` 在最终正文未给固定值（早期注释提及“约100 steps/阶段”但已注释掉），因此不可当最终设定。  
- 部分曲线图（training dynamics）未给逐点原始数值表，仅可读趋势。

### 4.2 Main result table（主结果压缩）
| Setting | Baseline | ICRL | Delta |
|---|---:|---:|---:|
| Qwen2.5-3B 平均 EM | 31.10 (Search-R1) | **40.16** | **+8.94** |
| Qwen2.5-7B 平均 EM | 41.78 (ParallelSearch) | **49.12** | **+7.34** |
| 3B 无SFT对比 O²-Searcher | 37.26 | **40.16** | **+2.90** |
| Qwen2.5-14B 平均 EM | 31.16 (CoT) | **51.84** | **+20.68** |

补充数据（ICRL）：  
- 3B：72.6 / 35.4 / 39.2 / 20.0 / 33.6（按 Trivia→Bamboogle）  
- 7B：75.4 / 42.6 / 53.6 / 26.0 / 48.0  
- 数学泛化（Qwen3-8B）：AIME2024 **64.1**（vs ReTool 67.0），AIME2025 **51.7**（vs ReTool 49.3）

### 4.3 Analysis experiments（现象 + 解释）
1. **现象：** `3→2→0` 显著优于 `3→2→1→0`（如 TriviaQA 75.4 vs 20.8；2Wiki 53.6 vs 26.8）。  
   **解释（作者）：** 四阶段更早结束，2 turn 完成率 59.39%，但牺牲多跳质量。  
   **【标注】我的判断：** 中间 1-shot 阶段把策略推向“保守早停模板”，形成低搜索深度局部最优。

2. **现象：** 不做 SFT 仍超过 O²-Searcher（40.16 > 37.26）。  
   **解释（作者）：** few-shot rollout 已提供软监督，足够替代冷启动 SFT。  
   **【标注】我的判断：** 这对工具协议频繁变化场景很关键，避免每次协议改动都重做大规模 SFT。

3. **现象：** 0-shot 阶段 response length 先降后升，同时 valid search 增长。  
   **解释（作者）：** 去除示例后模型先短答，再逐步重建自主工具链。  
   **【标注】我的判断：** 这是“脚手架撤除后的能力回填”，说明并非纯提示依赖。

4. **现象：** 跨到 code tool（AIME）时 2024 略输、2025 反超。  
   **解释（作者）：** ICRL 可泛化到非搜索工具场景。  
   **【标注】我的判断：** RL-only 已有竞争力，但上限可能受稀疏 outcome reward 限制；可尝试过程奖励增强。

---

## 5) Why it matters for our work
- **Agent memory:** `few-shot→zero-shot` 课程可类比“外部记忆提示→内部策略内化”。  
- **Long-context:** loss masking（只训可控 token）非常适合“模型生成 + 外部观测”混合轨迹。  
- **Multimodal RL:** ICRL 的课程退火可直接迁移到视觉工具链（OCR/检索/表格工具）。

---

## 6) Actionable next step（含 case）
### Case 1（正例复刻）
- **目标：** 复刻论文 Bamboogle 多跳案例（“两届总统先例+就职日期”）。  
- **执行：** 固定 2-hop 问题集，记录 `<search>` 次数、证据命中、最终 EM。  
- **验收：** 至少 80% 样本呈现“先实体定位，再时间检索”的链式策略。

### Case 2（负例诊断）
- **目标：** 对比 `3→2→0` 与 `3→2→1→0` 的“早停塌缩”现象。  
- **执行：** 在同数据上跑两条课程，跟踪 turn@finish 分布与 EM。  
- **验收：** 若 1-shot 中间阶段显著抬高 1~2 turn 完成率且 EM 下滑，即判定存在早停诱导。

### Case 3（迁移验证）
- **目标：** 在 memory agent 上做“记忆示例退火”小实验。  
- **执行：** `k-demo: 3→2→0` vs `3→2→1→0`，指标加上 memory hit@k 与无效检索率。  
- **验收：** 找到兼顾成功率与低无效检索的课程。

---

## 7) 评分解释（维持原倾向）
- **质量分 2/2：** 方法简洁、主结果和关键 ablation 数字充分、工程可落地。  
- **Observation 分 1/2：** 有强课程结论与训练动态证据，但开放环境多工具（并行规划/恢复）验证仍不足。  
- **总分 4/5：** 维持不变。  
- **为什么不是更高分：**
  1) 每阶段训练步数等关键细节披露不完整；  
  2) 长程记忆型任务验证不足；  
  3) 复杂开放工具场景证据还不够。
