# 🧭 Research Guide — 科研脉络与阅读标准

> **目的**：(1) 给 Master 看——梳理科研思路和领域 landscape；(2) 给 Twilight 用——作为阅读笔记写作的 Standard。
> 
> **维护者**：Yaorui Shi + Twilight | **最后更新**：2026-05-13

---

## 一、核心研究定位

**Yaorui Shi（史曜睿）** — USTC PhD, Meituan LongCat Team

核心问题：**如何让 AI Agent 在长期部署中持续学习、记忆、和自我改进？**

三条主线：
1. **Agentic Memory** — Agent 如何存储、检索、更新、遗忘经验？
2. **Long-Horizon Reasoning** — Agent 如何在长上下文/长任务中保持有效推理？
3. **Self-Evolving Agents** — Agent 如何在不改权重的情况下持续改进？（或最小化权重更新）

代表工作：MemOCR, ReMemR1 (ICLR 2025), AutoRefine (NeurIPS 2025), LongCat-Flash-Thinking

---

## 二、三类方法的关注框架（Master 2026-05-13 手写）

> 这是最核心的评判逻辑。每篇论文首先归类，然后按类型评判。

### Type A: RL Training 方法
- **关注点**：evolving / 自进化 / memory / long-horizon 的训练方法
- **发论文方便性**：最高（刷分容易出结果）
- **理念先进性要求**：相对宽容
- **质量评判重点**：
  - 训练方法的 novelty（不只是换 reward/换数据）
  - 消融实验（reward / data / schedule 各自贡献）
  - Scaling / generalization 分析
  - 性能提升幅度 + 有趣的实验现象
- **⚠️ 重要校准**：越开创性、越大的工作越难有艺术般的单点创新。Conceptual innovation 和方向性价值应独立于组件 novelty 评估。把完整 pipeline 首次跑通本身就是 contribution。
- **校准样例**：Agent-World (2604.18292) — Rel 4/5, Qual 4/5

### Type B: Harness Engineering 方法
- **关注点**：不训练但整体关注点、设计理念很有价值
- **发论文方便性**：最低（reviewer 常质疑 contribution）
- **理念先进性要求**：最高
- **质量评判重点**：
  - 设计理念的前瞻性和完整性
  - 系统性消融（哪个组件贡献多少）
  - 泛化性分析（不只是在一个 task 上 work）
  - 是否开源、是否可复现
- **校准样例**：Continual Harness (2605.09998) — Rel 4/5, Qual 4/5

### Type C: Benchmark 方法
- **关注点**：对问题本身的看法有价值
- **发论文方便性**：中等
- **理念先进性要求**：最高（好的 benchmark 定义问题边界）
- **质量评判重点**：
  - 对问题的定义是否有新意（不只是"更大更全"）
  - 评测维度是否揭示现有系统的 failure mode
  - Deterministic verifier / 强可复现协议
  - Leaderboard 之外的 diagnostic analysis
- **校准样例**：LongMemEval-V2 (2605.12493) — Rel 5/5, Qual 4/5

### 理念先进性排序
```
benchmark ≈ harness > training
```

### 发论文方便性排序
```
training > benchmark > harness
```

---

## 三、质量评判三指标（所有 Type 通用）

### 指标 1：作者/机构影响力
- 一作/通讯的 citation、是否大组、是否大公司
- 知名企业组（Seed, DeepSeek, OpenAI, Anthropic, DeepMind, FAIR, MSR, ByteDance, Meituan）：+1
- 知名学术组（Stanford, MIT, CMU, Berkeley, Tsinghua, PKU, USTC, ETH）：+0.5
- 不因此一票否决，作为 tiebreaker

### 指标 2：叙事与方法
- Motivation 是否清晰，叙事是否符合逻辑
- Related work 把握是否到位（是否了解领域 landscape）
- 方法设计的 elegance 和 novelty

### 指标 3：实验与现象
- 是否有显著的性能提升（**必须报数字**，禁止"有显著提升"）
- 是否有有趣的实验现象（反直觉发现、failure analysis、scaling behavior）
- 消融实验的完整性

---

## 四、当前领域热点（2026-05 snapshot）

> 详细版维护在 `~/.openclaw/workspace/field-intelligence/README.md`，此处为精简版。

### 🔥 最热问题

1. **Agent Memory Evaluation** — 怎么评价 agent 的记忆能力？
   - 代表：LongMemEval-V2, MEME
   - 关键发现：reading > writing（读取是瓶颈）；temporal reasoning 最难

2. **Self-Evolving Agent** — Agent 如何自我改进？
   - 两条路线：改权重（Agent-World 式 RL）vs 改 harness（Continual Harness 式 scaffolding evolution）
   - Environment-agent co-evolution 是新 paradigm

3. **Long-Context Training** — 如何让模型真正利用长上下文？
   - Attention dilution（FocuSFT）；context budget 建模（ContextBudget）

### ⚡ 快速升温

4. **On-Policy Data Evolution** — 训练数据动态跟踪 policy 演进
5. **Harness > Model** — Harness engineering 比改模型更 impactful 的证据越来越多

### 范式转变信号
- Benchmark 论文开始关注 diagnostic analysis 而非 leaderboard
- Agent 系统从 reactive tool use 向 predictive world model 演进

---

## 五、品味对齐记录

> 每次 Master 给出反馈，记录在此。用于校准后续推荐和评分。

### 2026-03-18
- SkillsBench：benchmark 论文不应一概降权。好的 benchmark = 机制诊断 + 可操作评测 + 指导系统迭代
- SkillRL 校准：Rel 4/5, Qual 2/5（有启发但实验差）

### 2026-05-13（Master 手写核心偏好）
- 三类方法框架 + 不同标准（见上方第二节）
- Memory evaluation/benchmark 反应极强（LongMemEval-V2 "窝糙牛逼"）
- Agent-World 校准：Qual 应为 4/5 而非 3/5 → 大工作的 conceptual innovation 不能因为"组件不新"就降分
- 推荐优先级：memory evaluation > memory system design > continual learning

---

## 六、阅读笔记写作 Standard

> 所有新笔记（`papers/YYYY-MM-DD_alias.md`）必须遵循以下规范。

### Metadata 必填项
```yaml
Type: A/B/C
Relevance: X/5
Quality: Y/5
Why Not Higher: [一句话]
```

### 结构要求
1. **TL;DR** — 一句话核心贡献
2. **CRGP** — Context / Related work / Gap / Proposal
3. **Method** — 方法概述 + 关键步骤
4. **Experiments** — 必须有 baseline / proposed / delta 数字
5. **Interesting Observations** — 反直觉现象 / failure mode / scaling behavior
6. **Limitations** — 诚实评估
7. **My Technical Take** — 个人判断用 `【标注】` 标记
8. **Transfer to Ongoing Projects** — 对当前研究的具体价值
9. **Next Actions** — 至少 2 条可执行 follow-up

### 质量红线
- Figure 区至少 1 张真实图链 + 解释，不可空写
- 禁止"有显著提升"不给数字
- Analysis 必须用「现象 + 解释」格式
- 更新笔记后必须同步 readinglist summary

### 风格对齐
参考标杆笔记：
- `papers/2026-03-11_evo-memory.md`
- `papers/2026-03-19_arise.md`
- `papers/2026-03-23_comp-rl.md`
