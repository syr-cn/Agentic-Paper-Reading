# 2026-03-17_bicc-rcc-grpo（DNL 重做）

## 0) Metadata
- **Title:** When Right Meets Wrong: Bilateral Context Conditioning with Reward-Confidence Correction for GRPO
- **Alias:** BiCC-RCC-GRPO
- **Authors / Org:** Yu Li, Tian Lan, Zhengling Qi（机构信息在 arXiv 页面未清晰给出）
- **Venue / Status:** arXiv 2603.13134v1 (2026)
- **Date:** 2026-03-17（本笔记重做：2026-03-19）
- **Links:**
  - Abs: https://arxiv.org/abs/2603.13134
  - HTML: https://arxiv.org/html/2603.13134v1
  - PDF: https://arxiv.org/pdf/2603.13134
  - Code: https://github.com/Skylanding/BiCC
- **Tags:** GRPO, RLVR, reasoning LLM, variance reduction, contrastive optimization
- **My rating:** ★★★☆☆（维持原倾向）
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3/5**

---

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：**
  这篇把 GRPO 从“组内独立样本更新”改写成“right-vs-wrong 对比优化”，并用 reward-confidence 协方差做 baseline 修正（RCC），在不增加推理时开销的前提下提升精度与训练稳定性。

---

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- RLVR 场景下，GRPO 是主流方法之一（不需要单独 critic，工程上简单）。
- 但标准 GRPO 常把组内样本近似独立处理，未充分利用组内“正确 vs 错误”结构信息。

### R — Related work
- 同类 RL 训练：GRPO / Dr.GRPO / DAPO / ASPO / GMPO / GSPO。
- 对比偏好学习（如 DPO 线）启发：相对优劣信号通常比单点监督更稳。
- 方差降低经典结论：最优 baseline 与采样权重相关，而非固定 reward 均值。

### G — Research gap
- **Gap-1（结构）**：GRPO 组内有正负样本，但 loss 没显式让正负样本互作上下文。
- **Gap-2（统计）**：reward 与 confidence（importance 相关项）在训练中相关性增强，固定 baseline 易增方差。
- **Gap-3（工程）**：希望稳定训练，但不引入额外 rollout / reward model / inference 开销。

### P — Proposal
- **BiCC（Bilateral Context Conditioning）**：
  - 正样本（right）条件化错误集合（wrong context）；
  - 错样本（wrong）条件化正确集合（right context）。
- **RCC（Reward-Confidence Correction）**：
  - 用 
  \(b^* \approx \mathbb{E}[R] + 2\,\mathrm{Cov}(R,\delta)\)
  修正 baseline（\(\delta=\log\pi_\theta-\log\pi_{ref}\)），降低梯度方差。

---

## 3) Figure 区（至少 1 张，抓主图，不跳过）
- 图1（方法主图，BiCC 流程）：
  ![fig1](https://arxiv.org/html/2603.13134v1/x2.png)
  解释：该图展示组内样本先分为 right/wrong 两个分区，再进行双向条件化（right 看 wrong，wrong 看 right），对应本文核心训练机制。

- 图2（分析图，相关性与方差/性能）：
  ![fig2](https://arxiv.org/html/2603.13134v1/x3.png)
  解释：图中给出 reward-confidence 相关性随训练上升，以及 RCC 对梯度方差/Pass@k 的改善趋势，支持作者的统计动机。

- 图3（补充分析图）：
  ![fig3](https://arxiv.org/html/2603.13134v1/x5.png)
  解释：展示不同上下文分配比例对效果影响，40% opposite context 在两模型上都较优。

---

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- **任务/数据：** DAPO-Math-17k（约 17K 数学题，整数答案，二值奖励）。
- **模型/agent 配置：** Qwen3-4B-Instruct-2507；Phi-4-mini-instruct-3.8B。
- **对比基线：** GRPO / Dr.GRPO / DAPO / ASPO / GMPO / GSPO（并报告 BiCC 插件版本）。
- **评测指标：** Pass@1（32 次独立运行取平均）；基准包括 Math500、AMC 2023、AIME 2024、AIME 2025。
- **训练细节（关键数字）：** 4×A100；batch=8，global batch=32；AdamW；LR=1e-6；默认 group size G=8；clip ε=0.2。

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| GRPO, G=8, Qwen3-4B, Math500 | 91.4 | **92.2** | +0.8 |
| GRPO, G=8, Phi-4-mini, Math500 | 76.2 | **78.1** | +1.9 |
| DAPO, Qwen3-4B, Math500 | 92.5 | **93.1** (BiCC-DAPO) | +0.6 |
| DAPO, Phi-4-mini, Math500 | 78.0 | **79.0** (BiCC-DAPO) | +1.0 |
| GSPO, Qwen3-4B, Math500 | 92.6 | **92.9** (BiCC-GSPO) | +0.3 |
| GSPO, Phi-4-mini, Math500 | 78.6 | **79.2** (BiCC-GSPO) | +0.6 |

> 论文整体叙述：BiCC 在多设置下约 +0.3 到 +1.9 个百分点；也有少量负迁移（如个别子集 -0.1），不是“全绿”。

### 4.3 Analysis experiments（强制“现象+解释”）
- **现象：** reward-confidence 协方差随训练上升（文中示例：Qwen 约至 0.066，Phi 约至 0.138），且正负样本 \(\delta\) 分布分离加剧（文中示例均值差：Qwen 0.27，Phi 0.56）。
  **解释（作者）：** 随策略收敛，模型对高奖励轨迹赋予更高置信，导致 \(R\) 与 \(\delta\) 相关性增强，固定 baseline 变得次优。
  **【标注】（我的判断，可选）：** 这是 RCC 成立的关键证据，统计假设比“经验 trick”更扎实。

- **现象：** RCC 报告可降梯度方差并提升收敛速度；文中给出多个区间（约 25–35%、31–36%、32–37%、约 25–30%）。
  **解释（作者）：** 不同模型/阶段/统计窗口导致数字区间差异，但方向一致。
  **【标注】（我的判断，可选）：** 结论方向可信，但复现时要统一“方差计算口径”和“时间窗口”。

- **现象：** context allocation 消融中，40% opposite context 最优：
  Qwen（91.8/92.2/92.0 对应 20/40/60%）；Phi（77.4/78.1/77.8）。
  **解释（作者）：** 太少信息不足，太多则侵占原答案上下文，存在平衡点。
  **【标注】（我的判断，可选）：** 该结论对 long-context memory 注入非常有参考价值（应做比例扫描而非盲目加长）。

- **现象：** G=8 时 BiCC 增益明显大于 G=2（文中描述趋势清晰）。
  **解释（作者）：** 更大组带来更丰富的 opposite partition 信息，条件化更有效。
  **【标注】（我的判断，可选）：** 与对比学习“负例多样性”直觉一致，适合轨迹池/记忆池场景。

### 4.4 缺失数字标注（原文未给出可提取值）
- 单 step 训练 wall-clock、token/s 吞吐：**原文未给出可提取数字**。
- BiCC/RCC 的显存额外开销（GB 或 %）：**原文未给出可提取数字**。
- 多模态任务上的同等实验表格：**原文未给出可提取数字**。

---

## 5) Why it matters for our work
- 对 agent memory 来说，BiCC 的本质是“把失败轨迹显式变成成功轨迹的对照上下文”，这比只做 replay 更直接。
- RCC 提供了低成本稳定器：不需要额外 reward model，不改 inference path，适合快速接入现有 GRPO pipeline。
- 对小模型更有效（Phi 增益更高）这一点，契合我们在轻量模型上的落地目标。

---

## 6) Actionable next step
- [ ] **Case-1 对齐（参考 `2026-03-11_evo-memory.md`）**：在现有 trajectory memory 训练中加入 right/wrong 分区记忆，验证错误模式能否被“反向条件化”抑制。
- [ ] **Case-2 对齐（参考 `2026-03-13_reasoning-judge.md`）**：把“解释一致性/判别稳定性”作为附加观测，检查 BiCC 是否减少 judge 级别的波动误判。
- [ ] 复现 20/40/60（可加 80）context 分配曲线，联合记录 Pass@1、显存、有效上下文占比，找工程最优点。
- [ ] 在长上下文任务试 RCC-only / BiCC-only / BiCC+RCC 三组，拆分“结构收益”与“统计收益”。

---

## 7) 评分解释（必填）
- **质量分 x/2：** 1/2（方法清晰、实验覆盖较全，但系统开销披露不足）
- **Observation 分 y/2：** 1/2（给出 reward-confidence 相关性这一关键观察，但口径一致性一般）
- **总分 z/5：** **3/5（★★★☆☆）**
- **为什么不是更高分：**
  1) 任务域主要在数学推理，外部泛化证据仍有限；
  2) 工程关键指标（吞吐/显存/时延）缺失；
  3) 方差下降数字在不同段落区间不完全一致，仍需独立复现校准。
