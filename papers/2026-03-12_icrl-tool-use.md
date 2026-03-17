# In-Context RL for Tool Use 阅读笔记

## 0) Metadata
- **Title:** In-Context Reinforcement Learning for Tool Use in Large Language Models
- **Alias:** ICRL
- **Authors / Org:** NUS, Salesforce AI Research, UC Berkeley, UC Santa Cruz
- **Venue / Status:** arXiv 2603.08068
- **Date:** 2026-03
- **Links:**
  - Abs: https://arxiv.org/abs/2603.08068
  - PDF: https://arxiv.org/pdf/2603.08068
  - HTML: N/A（arXiv 未提供 HTML 版本）
  - Code: https://github.com/applese233/ICRL
- **Tags:** tool-use, reinforcement-learning, in-context-learning, search-agent, SFT-free
- **My rating (★☆☆ / ★★☆ / ★★★):** 4.6
- **Read depth:** deep

## 1) TL;DR
- 这篇工作要解决的核心问题是：**工具调用训练通常依赖 cold-start SFT**，标注/合成数据成本高。
- ICRL 用一个“**仅 RL**”的替代路线：在 rollout prompt 中放 few-shot 示例，随后按 curriculum 逐步去掉示例（3→2→0），让模型从“带扶手”过渡到“零样本自主工具调用”。
- 方法上最关键的两个设计：
  1) curriculum few-shot rollout；
  2) RL loss masking（只训模型自己生成的 token，屏蔽工具返回内容）。
- 在 Qwen2.5-3B / 7B 的 5 个 QA 基准上，平均 EM 分别达到 **40.16 / 49.12**，较最强对比提升 **+8.94 / +7.34**。
- 无 SFT 条件下对比 O²-Searcher（含 cold-start SFT）仍更优，说明“少监督 + RL 内化工具调用”路径可行。

## 2) Problem & Motivation
- 以前方法的核心缺口：
  - 从零直接 RL：探索效率差，模型不会调工具。
  - SFT+RL：效果常好，但 SFT 需要大量高质量标注轨迹，昂贵且不易迁移。
- 这篇 paper 目标：
  - 去掉 SFT 阶段，仅通过 RL + in-context 示范实现工具调用能力学习。
- 为什么重要：
  - 如果这个路径成立，能显著降低“工具型 agent”的训练门槛与数据成本。

## 3) Method (结构化)
### 3.1 Task Formulation
- 将工具增强推理建模为 MDP：模型在 `<think>/<search>/<information>/<answer>` 等结构化 token/action 下与外部工具交互。
- 工具（如搜索）返回内容写回上下文，影响后续动作。

### 3.2 ICRL 核心机制
1. **Few-shot rollout prompts**：训练初期在 rollout 模板加入 N 个示例（论文实验主线是 3-shot 起步）。
2. **阶段式去示例 curriculum**：训练中逐步减少示例数量，最终 0-shot。
3. **GRPO 优化**：用可验证 reward 做策略更新。
4. **Loss masking for tool outputs**：只对模型生成 token 反传，工具返回文本不计入损失。

### 3.3 Reward Design
- 奖励由“答案正确性 + 格式合法性”组合构成；格式违规有分项惩罚。
- 文中给了超参数：
  - 组合系数 `α = 0.8`；
  - 格式违规惩罚权重按表中顺序为 `0.5, 0.2, 0.15, 0.1, 0.1, 0.2`。

## 4) Experiments & Evidence
### 4.1 Benchmarks / Setup
- QA 基准：TriviaQA, HotpotQA, 2Wiki, Musique, Bamboogle（每集最多采样 500 题）。
- 训练数据：NQ（为避免泄露，评测不含 NQ）。
- 模型：Qwen2.5-3B / 7B / 14B（instruct）。
- 工具：Serper API（Google 搜索 top-3）。

### 4.2 Main Results（关键数字）
#### Qwen2.5-3B
- ICRL：TriviaQA **72.6**, HotpotQA **35.4**, 2Wiki **39.2**, Musique **20.0**, Bamboogle **33.6**，平均 **40.16**。
- 文中报告：较最强基线（Search-R1, 31.10）提升 **+8.94**。

#### Qwen2.5-7B
- ICRL：TriviaQA **75.4**, HotpotQA **42.6**, 2Wiki **53.6**, Musique **26.0**, Bamboogle **48.0**，平均 **49.12**。
- 文中报告：较最强基线（ParallelSearch, 41.78）提升 **+7.34**。

#### 无 SFT 对比
- 与 O²-Searcher（含 cold-start SFT）比，ICRL 在论文给出的对比表里平均更高（ICRL **40.16** vs O²-Searcher **37.26**）。

#### 大模型扩展
- Qwen2.5-14B 上平均 EM **51.84**（75.0/43.2/61.8/25.6/53.6）。
- 文中报告：较 CoT **+20.7**，较 direct prompting **+27.0**。

#### 数学工具调用（代码执行）
- AIME2024: **64.1**；AIME2025: **51.7**。
- 文中叙述：相对 ReTool 在 AIME2024 低 **2.9**，AIME2025 高 **2.4**。

### 4.3 Ablation / Analysis
- **Curriculum 设计敏感**：`3→2→0` 明显优于 `3→2→1→0`。
  - 论文举例：TriviaQA **75.4 vs 20.8**，2Wiki **53.6 vs 26.8**。
- 现象解释：额外的“1-shot 中间阶段”可能导致过早缩短推理/搜索链，牺牲准确率。

### 4.4 Limitations
- 主要实验集中在搜索型 QA 和部分数学任务，环境多样性仍有限。
- 格式奖励和模板设计对效果影响大，迁移到新工具协议可能要重调。
- 文中强调“无需 SFT”，但仍依赖高质量 few-shot 示例模板与工程规范。

## 5) My Technical Take
### 5.1 What I believe
- 这篇最有价值的点是把“cold-start SFT”替换为“rollout 内 ICL + curriculum”，工程收益很高。
- loss masking 是实用关键件：不让工具输出污染梯度，逻辑合理且通用。

### 5.2 What I doubt
- 对极长链条、多工具协作场景是否仍稳，需要更强基准验证。
- few-shot 示例质量是否成为新的隐性瓶颈（替代了部分 SFT 成本）值得量化。

### 5.3 Transfer to our projects
- 在现有 agent RL 中引入“**示例退火**”训练流程（N-shot→0-shot）。
- 对 tool-augmented rollout 强制加“**tool-output masking**”。
- 把 reward 拆成 accuracy + format 两部分做可解释诊断面板。

## 6) Repro Checklist
- [x] 方法定义清晰
- [x] 奖励设计有具体超参
- [x] 基线覆盖较广
- [x] 代码可得（GitHub）
- [ ] 多环境可泛化性仍需补

## Appendix
- Figure 1: N/A（arXiv 无 HTML 图像资源）
- 备注：本笔记主依据论文源码 LaTeX + arXiv abs；因官方 HTML 不可用，按规则退回 PDF/源码信息。
