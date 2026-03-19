# BiCC-RCC-GRPO 精读重写（DNL Deep Note）

## 0) Metadata（文献元信息）
- **Title:** When Right Meets Wrong: Bilateral Context Conditioning with Reward-Confidence Correction for GRPO  
- **Alias:** BiCC-RCC  
- **Authors:** Yu Li, Tian Lan, Zhengling Qi  
- **Affiliation:** 原文未明确给出可提取机构信息（arXiv HTML 可见作者名，但无清晰单位标注）  
- **Venue / Status:** arXiv 2603.13134v1（2026-03）  
- **Primary Area:** RL for reasoning LLMs / GRPO 训练稳定性  
- **Links:**  
  - Abs: https://arxiv.org/abs/2603.13134  
  - PDF: https://arxiv.org/pdf/2603.13134  
  - HTML: https://arxiv.org/html/2603.13134  
  - Code: https://github.com/Skylanding/BiCC  
- **My Rating（保持原倾向）:** ★★★☆☆  
- **Read Depth:** single-paper deep read  
- **Score (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3/5**

---

## 1) Why-read（一句话动机）
这篇值得读的核心不是“又加一个 trick”，而是把 GRPO 明确写成**组内正确/错误样本的对比优化**，并给出一个几乎零额外推理开销的训练增强路径（BiCC + RCC）。

---

## 2) CRGP（Context / Related / Gap / Proposal）

### C — Context
- GRPO 在 reasoning RLVR（可验证奖励）中常用，因为它不需要单独 critic。  
- 但标准 GRPO 虽然用组均值构造 advantage，本质优化仍按样本独立计算 ratio，组内 right-vs-wrong 的结构信号没有显式利用。

### R — Related Work
- **GRPO 家族**：GRPO、Dr.GRPO、DAPO、ASPO、GMPO、GSPO。  
- **对比/偏好方向**：DPO/IPO 等偏好优化强调“相对优劣”而非单点监督。  
- **方差降低经典线**：policy gradient baseline 最优解与 importance weight 相关（并非总是简单 reward mean）。

### G — Research Gap
1. **结构 gap**：已有 GRPO 训练时“知道组里有对有错”，但 loss 未显式让对错样本互相提供上下文。  
2. **统计 gap**：标准 baseline 常假设 reward 与 importance/confidence 独立；实际训练中相关性上升，导致方差上升。  
3. **工程 gap**：希望改进稳定性时不引入额外采样、额外辅助模型和推理时开销。

### P — Proposal
- **BiCC（Bilateral Context Conditioning）**：
  - 对正确样本，用 query + 错误样本集作条件；对错误样本，用 query + 正确样本集作条件。  
  - 本质是把 opposite partition 当作训练时 privileged information。  
- **RCC（Reward-Confidence Correction）**：
  - 用 reward-confidence 协方差修正 baseline，近似最优方差基线：  
  - \( b^* \approx \mathbb{E}[R] + 2\,\mathrm{Cov}(R,\delta) \), 其中 \(\delta = \log \pi_\theta - \log \pi_{ref}\)。

---

## 3) Figure 区（读图抓主线）

### Figure 1（方法总览）
- 标准 GRPO：采样 G 个解 → reward → group-normalized advantage。  
- BiCC：按 reward 划分 \(\mathcal O^+\), \(\mathcal O^-\)，并做双向条件化（right 看 wrong，wrong 看 right）。  
- RCC：额外估计 \(\mathrm{Cov}(R,\delta)\) 来修正 advantage。

### Figure 2（相关性证据）
- 训练过程中 \(\mathrm{Cov}(R,\delta)\) 单调上升：
  - Qwen3-4B 到约 **0.066**；
  - Phi-4-mini 到约 **0.138**。
- 2.5k–3k step 时 \(\delta\) 分布按 reward 出现明显分离：
  - Qwen3-4B 均值差 **0.27**；
  - Phi-4-mini 均值差 **0.56**。

### Figure 3（训练与Pass@k）
- BiCC 训练曲线与 baseline 相比不显示额外不稳定。  
- BiCC+RCC 在 Pass@k 上继续提升，并显示方差下降（见 §4 详细数值）。

---

## 4) Experiments（实验设置与结果）

### 4.1 Experimental Setup（具体设置）
- **Models:** Qwen3-4B-Instruct-2507；Phi-4-mini-instruct-3.8B。  
- **Train data:** DAPO-Math-17k（约 **17K** 数学题，整数答案，二值奖励）。  
- **Benchmarks:** Math500, AMC 2023, AIME 2024, AIME 2025。  
- **Hardware:** **4 × A100**。  
- **Batch:** batch size **8**，global batch size **32**。  
- **Optimizer / LR:** AdamW，learning rate **1e-6**。  
- **Group size:** 默认 **G=8**（另有 G=2 对照）。  
- **Clip:** \(\epsilon=0.2\)。  
- **Eval:** Pass@1，**32** 次独立运行取平均。  
- **Context allocation ablation:** opposite-partition context 比例 20% / 40% / 60%。

### 4.2 Main Results（主结果，含数字）
- 论文宣称 BiCC 在多设置下带来 **+0.3 到 +1.9** 个百分点提升。  
- 典型数字：
  - **GRPO, G=8, Qwen3-4B, Math500:** 91.4 → **92.2**（+0.8）  
  - **GRPO, G=8, Phi-4-mini, Math500:** 76.2 → **78.1**（+1.9）  
  - **BiCC-DAPO** 在 Math500：Qwen3-4B 到 **93.1**；Phi-4-mini 到 **79.0**  
  - **BiCC-GSPO** 在 Math500：Qwen3-4B **92.9**；Phi-4-mini **79.2**。
- 少数负迁移也有披露（如 BiCC Dr.GRPO 在 Phi AIME25: -0.1，BiCC GMPO 在 Phi AMC23: -0.1），说明并非“全绿无例外”。

### 4.3 RCC / 方差与收敛
- 文中报告 RCC 可降低梯度方差：
  - 在一处总结写 **25–35%**；
  - 在 Figure 3 描述写 Qwen **31–36%**、Phi **32–37%**；
  - 在 §5.3 还有 “约 **25–30%**”。
- 收敛速度：给出 **15–20% faster convergence**（分析段结论）。
- 说明：不同段落区间存在轻微不一致，但都指向“显著降方差 + 更快收敛”。

### 4.4 Ablation（上下文长度分配）
Math500（BiCC-GRPO, G=8）：
- Qwen3-4B：20% = 91.8，40% = **92.2**，60% = 92.0  
- Phi-4-mini：20% = 77.4，40% = **78.1**，60% = 77.8  
=> 40% 最优，且弱模型（Phi）更敏感。

### 4.5 原文未给出的可提取数字（明确标注）
- 单步 wall-clock 训练耗时与 token/s：**原文未给出可提取数字**。  
- BiCC 引入的显存开销（GB）和吞吐下降比例：**原文未给出可提取数字**。  
- 多模态任务上的同等实验配置与结果：**原文未给出可提取数字**。

---

## 5) Analysis（现象 + 解释 + 我的判断）

1. **现象：**G 从 2 提升到 8 后，BiCC 增益变大（如 Phi Math500 +0.6 → +1.9）。  
   **解释（作者逻辑）：**更大组提供更丰富 opposite-partition 信息，条件化更“像样”。  
   **我的判断：**这与“对比学习需要负例多样性”一致；对 agent memory 来说等价于“候选轨迹池越丰富，错误模式对齐越有效”。

2. **现象：**弱基座模型（Phi-4-mini）增益普遍大于强模型（Qwen3-4B）。  
   **解释：**弱模型原始策略更不稳定，更依赖显式 right-vs-wrong 信号。  
   **我的判断：**合理且实用：在小模型/蒸馏模型/边缘部署模型上，这类训练 trick 的性价比更高。

3. **现象：**\(\mathrm{Cov}(R,\delta)\) 随训练上升，且正负样本 \(\delta\) 分布分离加剧。  
   **解释：**模型对“自己认为更可能正确”的输出给更高概率，reward-confidence 相关性增强。  
   **我的判断：**这直接挑战“baseline=reward mean 永远够用”的默认假设；RCC 的统计动机是成立的。

4. **现象：**RCC 降低梯度方差并提升 Pass@k，但论文不同段落给出 25–37% 不同区间。  
   **解释：**可能是不同模型/阶段/统计口径（全程 vs 后期）导致。  
   **我的判断：**方向可信，但复现时必须统一方差定义与测量窗口，否则难横向比较。

---

## 6) Why it matters & Next Steps（面向 agent memory / long-context / multimodal RL）

### Why it matters for our work
- 这篇把“组内候选轨迹”从独立样本变成可互相解释的训练资源，和我们做 agent trajectory memory 的目标高度一致。  
- RCC 提供了一个非常轻量的稳定器，不需要额外 reward model 或额外 rollout。

### 3 条可执行 next steps
1. **Agent memory 版 BiCC：**
   - 在现有 GRPO 训练里，把同 query 的成功/失败轨迹写入短期 memory bank；训练时按 BiCC 逻辑交叉拼接上下文。  
   - 记录指标：Pass@1、错误类型迁移、memory 命中率。  
2. **Long-context 稳定性实验：**
   - 复现 20/40/60% context allocation，并扩展到 80%；测量长上下文下的收益衰减点与显存曲线。  
   - 同时比较“截断错误轨迹 vs 摘要错误轨迹”两种注入方式。  
3. **Multimodal RL 迁移验证：**
   - 在图文推理任务中，将 opposite-partition context 改为“失败视觉证据 + 成功文本链”互条件化。  
   - 先做小规模 sanity check：是否同样出现 \(\mathrm{Cov}(R,\delta)\) 上升与 RCC 降方差。

---

## 7) 评分解释（保持原评分倾向）
- **维持 3/5（★★★☆☆）**，不做无依据改分。  
- 给 3 分的理由：
  1) 机制洞见清晰（把 GRPO 写成对比形式）；
  2) 方法工程化程度高（无额外采样、可插拔）；
  3) 数学任务上结果稳定且有消融。  
- 仍未上调到更高分的原因：
  - 任务域集中在数学 reasoning；
  - 训练代价/吞吐/显存等系统级数字披露不足；
  - 方差下降区间表述在文中口径不完全一致，需复现验证。
