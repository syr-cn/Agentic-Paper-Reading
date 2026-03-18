# In-Context RL for Tool Use 阅读笔记

## 0) Metadata
- **Title:** In-Context Reinforcement Learning for Tool Use in Large Language Models
- **Alias:** ICRL
- **Authors / Org:** NUS, Salesforce AI Research, UC Berkeley, UC Santa Cruz
- **Venue / Status:** arXiv 2603.08068
- **Links:** Abs https://arxiv.org/abs/2603.08068 | PDF https://arxiv.org/pdf/2603.08068 | Code https://github.com/applese233/ICRL
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = 4

## 1) Core Insight
- 这篇最有价值的点是把“冷启动 SFT”替换成“rollout 内 few-shot + 逐步退火”的 RL-only 路线，证明工具调用可在低监督下稳定学出来。

## 2) Interesting Observations
- `3→2→0` 的 curriculum 显著优于更细颗粒退火（`3→2→1→0`），说明中间阶段可能诱导“过早收缩搜索链”。
- tool-output masking 是关键工程细节：只对模型 token 反传可避免工具返回文本污染梯度。
- 无 SFT 仍可与强基线竞争，数据成本优势明显。

## 3) Evidence / Method
- GRPO + few-shot rollout + curriculum。
- 5 个 QA benchmark 上，Qwen2.5-3B/7B 平均 EM 分别到 40.16/49.12，较强基线有稳定增益。

## 4) Why It Matters for Your Work
- 对你做 tool-use RL 很直接：可以降低对人工轨迹依赖，把训练成本从“高质量 SFT 数据”转到“可控 rollout 设计”。

## 5) Actionable Next Step
- 在现有 pipeline 做 `N-shot→0-shot` 退火对照，并单独 ablate masking 开关。

## 6) Why not higher score
- 不是更高分的原因：多工具长链和开放环境上的泛化证据还不够。
