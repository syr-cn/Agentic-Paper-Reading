# DNL Deep Note — Reasoning Shift

## 0) Metadata
- **Title:** Reasoning Shift: How Context Silently Shortens LLM Reasoning
- **Alias:** Reasoning Shift
- **Authors / Org:** Gleb Rodionov / Yandex
- **Venue / Status:** arXiv 2604.01161v1 (preprint, work in progress)
- **Date:** 2026-04-01
- **Links:**
  - Abs: https://arxiv.org/abs/2604.01161
  - HTML: N/A (not available yet)
  - PDF: https://arxiv.org/pdf/2604.01161
  - Code: N/A
- **Tags:** reasoning models, test-time scaling, context robustness, self-verification, reasoning compression, LLM behavior analysis
- **My rating:** ★★★★☆ (4/5)
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1.5 + Observation 2 = **4.5/5**

---

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：** Reasoning LLMs 在非孤立 context 条件下（长无关上下文、多轮对话、子任务嵌套）会 **静默压缩推理链**，reasoning tokens 最多减少 50%，且这种压缩伴随 self-verification 和 uncertainty management 行为的显著下降。核心 observation：resampling 实验证明**即使前缀推理链完全相同**，不同 context 条件仍会抑制后续的高级推理模式（如 "wait"、"alternatively" 等自检 token 出现率大幅下降）。

---

## 2) CRGP 拆解 Introduction
### C — Context
- Reasoning LLMs（如 o1、QwQ、Gemini Flash Thinking）通过 test-time scaling（延长推理链、自我验证）在复杂推理任务上取得了显著成功。
- 但这些推理行为的**鲁棒性**几乎没有被研究过——当 prompt 的上下文条件变化时，推理质量是否会受影响？

### R — Related work
- **Test-time scaling 线：** OpenAI o1/o3、DeepSeek R1、Qwen QwQ 等展示了延长推理链对性能的提升。
- **Reasoning 行为分析线：** 已有工作研究过 overthinking（推理链过长但无实际收益）和 underthinking（推理不充分导致错误）。
- **Context 影响线：** Lost-in-the-middle、needle-in-a-haystack 等工作研究了长 context 对信息检索的影响，但**未涉及 context 对推理行为本身的影响**。

### G — Research gap
1. 现有研究都在**孤立设置**（isolated baseline）下评估推理模型，但实际使用中 LLM 几乎总是在**非孤立 context** 下工作（agentic 多轮、长文档、嵌套任务）。
2. 没有工作系统性地研究 context 条件如何影响推理链的**长度、结构和行为模式**（而非仅仅影响准确率）。
3. self-verification 和 uncertainty management 这些关键推理行为是否对 context 变化具有鲁棒性——完全未知。

### P — Proposal
- 设计三种非孤立 context 条件来系统性评估推理行为的鲁棒性：
  1. **Long input:** 在 prompt 前插入 64K tokens 的无关文本（莎士比亚戏剧）
  2. **Multi-turn:** 将问题放在多轮对话的后续轮次中
  3. **Subtask:** 将问题作为复合任务的子问题呈现
- 在 4 个推理模型（Qwen-3.5-27B、GPT-OSS-120B、Gemini 3 Flash Preview、Kimi K2 Thinking）上评估 IMOAnswerBench。
- 用 OLMo-3 的不同后训练阶段（Instruct → SFT → DPO → Think）分析后训练对 reasoning shift 的影响。
- 通过 resampling 实验验证 context 对推理行为的**因果性**影响。

---

## 3) Figure 区

- 图1（三种 context 条件设置）：论文 Figure 1 展示了 Baseline vs. Long input / Multi-turn / Subtask 三种设置的 prompt 构造方式。Long input 在问题前插入 64K tokens 莎士比亚文本；Multi-turn 将问题放在第二轮对话中；Subtask 将目标问题与另一个问题组合为复合任务。

- 图2（reasoning tokens 分布对比）：Figure 3 展示了不同 context 条件下，同一问题产生的 reasoning tokens 数量分布。所有非 baseline 条件都显著左移（推理链变短），Long input 条件下缩短最为严重（部分模型减少 ~50%）。

- 图3（Transition probability 差异矩阵）：Figure 4 展示了 Baseline 与 Long input 条件下推理行为转移概率的差异。最显著的变化是从各种推理阶段到 `</think>`（结束推理）的转移概率大幅增加（+0.11），而 `self_check` 和 `uncertainty` 阶段的转移概率显著降低，说明 context 压缩了深层自检行为。

---

## 4) Experiments
### 4.1 Experimental setup
- **任务/数据：** IMOAnswerBench（高难度数学竞赛）、MATH-500（中等难度数学）
- **模型/agent 配置：** Qwen-3.5-27B、GPT-OSS-120B、Gemini 3 Flash Preview、Kimi K2 Thinking；thinking budget 80K tokens；OLMo-3-7B 系列（Instruct/Think-SFT/Think-DPO/Think）用于后训练阶段分析
- **对比基线：** Baseline（孤立问题呈现）vs. 三种非孤立条件（Subtask / Long input / Multi-turn）
- **评测指标：** 准确率（Acc.）、平均推理 token 数

### 4.2 Main result table

**IMOAnswerBench (Table 1):**

| Model | Baseline Acc/Tok | Subtask Acc/Tok | Long input Acc/Tok | Multi-turn Acc/Tok |
|---|---|---|---|---|
| Qwen-3.5-27B | 74.5 / 28,771 | 62.4 / 20,165 | 67.8 / 16,415 | 67.0 / 17,404 |
| GPT-OSS-120B | 73.8 / 24,180 | 64.0 / 17,408 | 64.0 / 11,876 | 69.3 / 19,831 |
| Gemini 3 Flash | 82.8 / 23,090 | 67.0 / 13,653 | 80.3 / 19,879 | 82.5 / 21,693 |
| Kimi K2 Thinking | 74.8 / 29,615 | 65.0 / 19,630 | 70.8 / 23,380 | 72.8 / 30,421 |

**MATH-500 OLMo 后训练阶段 (Table 2):**

| Model | Baseline Acc/Tok | Subtask Acc/Tok | Long input Acc/Tok | Multi-turn Acc/Tok |
|---|---|---|---|---|
| OLMo-3-7B-Instruct | 95.5 / 1,522 | 93.0 / 1,487 | 93.1 / 1,635 | 94.5 / 1,266 |
| OLMo-3-7B-Think-SFT | 96.0 / 4,456 | 94.4 / 3,470 | 93.6 / 3,547 | 95.0 / 3,705 |
| OLMo-3-7B-Think-DPO | 97.4 / 4,140 | 94.3 / 3,021 | 94.2 / 3,693 | 93.8 / 3,538 |
| OLMo-3-7B-Think | 96.4 / 5,227 | 95.0 / 3,126 | 94.8 / 3,888 | 93.0 / 3,587 |

### 4.3 Analysis experiments

- **现象：** Long input 条件下，GPT-OSS-120B 的推理 token 数从 24,180 骤降至 11,876（-51%），同时准确率下降 9.8%。
  **解释（作者）：** 长无关 context 使模型"认为"问题更简单或已有充分信息，从而提前终止推理链。
  **【标注】：** 这里 Gemini 3 Flash 很有趣——token 数降幅较小（-14%），准确率几乎不变（80.3 vs 82.8），可能说明不同模型对 context 干扰的鲁棒性差异很大。

- **现象：** Resampling 实验（Table 3）：相同推理前缀下，Long input 条件中 46% 的 trace 直接结束推理（生成 `</think>`），而 Baseline 仅 21%。"wait" token 出现率从 11% 降至 5%，"alternatively" 从 17% 降至 5%，"but" 从 46% 降至 20%。
  **解释（作者）：** Context 条件直接影响模型的 token-level 生成概率分布，即使推理前缀完全相同，非孤立 context 仍会抑制 self-verification 和 uncertainty management 行为。这不是推理内容的自然结果，而是 context 的**因果性**影响。
  **【标注】：** 这是本文最有价值的实验。它排除了"推理链本身质量不同导致后续行为不同"的混淆因素，直接证明了 context → 行为压缩的因果链。对 agentic 系统设计有直接启示：multi-turn context 管理不仅影响信息检索，还影响推理质量。

- **现象：** OLMo-3 后训练阶段分析：Instruct 模型的 token 数变化很小（无推理模式），但 Think 系列（SFT → DPO → Think）的推理 token 数在所有非 baseline 条件下都显著减少（Think 模型从 5,227 降至 3,126-3,888），且 reasoning shift 在每个后训练阶段都存在。
  **解释（作者）：** Reasoning shift 不是某个特定后训练阶段引入的，而是**所有具备 reasoning 能力的模型的共有特征**。
  **【标注】：** 这暗示 reasoning shift 可能是 Transformer 注意力机制的固有属性，而非训练数据或 RL reward 的问题。

---

## 5) Why it matters for our work
- **Agentic memory 系统设计：** 我们的 ReMemR1 和 MemOCR 工作都涉及 multi-turn 或长 context 下的推理。本文揭示的 reasoning shift 意味着：仅仅优化记忆检索的准确性不够，还需要关注 context 对推理行为本身的影响。记忆系统的设计应该考虑如何**保护推理深度不被 context 压缩**。
- **Long-context reasoning：** 对 LongCat 系列工作的直接启示——长 context 不仅有信息检索的 lost-in-the-middle 问题，还有推理行为被静默压缩的问题。可能需要在 RL reward 设计中显式鼓励 self-verification 行为。
- **Reasoning RL 训练：** 如果 reasoning shift 是所有后训练阶段共有的，那么可能需要在训练数据或 reward 中**显式包含非孤立 context 条件**（而非仅在 isolated setting 下训练），以提升鲁棒性。

## 6) Actionable next step
- [ ] 在 ReMemR1/MemOCR 的评测中增加"非孤立 context"条件（multi-turn、长 context），观察记忆系统是否加剧或缓解 reasoning shift
- [ ] 考虑在 RL reward 中引入 self-verification 行为的显式度量（如 "wait"/"alternatively" token 频率）
- [ ] 复现 resampling 实验：用我们自己的模型验证 reasoning shift 是否同样存在

## 7) 评分解释
- **质量分 1.5/2：** 实验设计精巧（尤其是 resampling 实验），三种 context 条件覆盖了主要使用场景。但作为 working paper，分析深度有限：没有解释 WHY context 会导致推理压缩（机制层面），也没有提出解决方案。模型覆盖面合理但不够广（缺少 DeepSeek R1、Claude 等）。
- **Observation 分 2/2：** "Context 静默压缩推理链"是一个非常有价值的 observation，对所有使用 reasoning model 的 agentic 系统都有直接影响。resampling 实验证明的因果性更是亮点。这个 observation 可以直接改变我们设计 multi-turn agent 的方式。
- **总分 4.5/5：** observation 极强（改变认知），实验设计巧妙，但缺少机制解释和解决方案，且为 working paper 状态。
- **为什么不是更高分：** (1) 没有提出任何缓解 reasoning shift 的方法；(2) 没有探索 WHY（注意力权重分析、位置编码影响等机制层面）；(3) 单一作者、单一机构，peer review 前质量保证有限。
