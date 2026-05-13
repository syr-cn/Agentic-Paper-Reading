# DNL Deep Note — GameMultiverse Survey

## 0) Metadata
- **Title:** Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Alias:** GameMultiverse-Survey
- **Authors / Org:** Kuan Zhang, Dongchen Liu et al. (15 authors) / Tsinghua (College of AI) + MMLab (HKU) + UCAS
- **Venue / Status:** arXiv preprint (cs.CV)
- **Date:** 2026-05-12
- **Links:**
  - Abs: https://arxiv.org/abs/2605.09965
  - HTML: https://arxiv.org/html/2605.09965v2
- **Tags:** survey, foundation models, game playing, generalist agents, world models, VLA, harness
- **Type:** C (Benchmark/Survey)
- **Relevance:** 4/5 — 不直接做 memory/long-context，但 survey 的 harness taxonomy（含 memory 模块）、self-evolving 范式分析、five trade-offs 对 agent 研究高度有启发
- **Quality:** 4/5 — Tsinghua+HKU 大组 survey，框架化能力强（四柱+五 trade-off+五级路线图），覆盖面极广
- **Why Not Higher:** 纯 survey 无新实验/模型；覆盖面广但每个子题浅；Minecraft 生态偏重

## 1) TL;DR
全面 survey 将 foundation model 做游戏通才玩家的全生命周期组织为四柱（Dataset→Model→Harness→Benchmark），识别五个根本 trade-off，并规划从单游戏精通到「创世主」的五级路线图。

## 2) CRGP
- **Context:** 游戏是 AGI 终极测试场（需要感知、规划、推理、运动控制）；foundation model 正从窄专家转向通才玩家
- **Related Work:** Deep RL specialists (AlphaGo, AlphaStar), LLM agents (Voyager, CICERO), VLAs (SIMA, VPT), World Models (Genie, GameNGen, Oasis)
- **Gap:** 无 prior survey 将 Dataset→Model→Harness→Benchmark 作为耦合闭环处理，也未在统一 POMDP 框架下建模
- **Proposal:** 统一四柱 pipeline + 五个 fundamental trade-offs + 五级路线图

## 3) Method (Survey Framework)

### 四时代演化框架
Symbolic Systems → Deep RL → Foundation Models → Creator/Demiurge，统一在 Goal-Conditioned POMDP (M = ⟨G,S,A,T,R,Ω,O,γ⟩)

### 四柱 Pipeline
1. **Dataset**: human play → competitive archives → cross-game scaling → world-model-as-data-engine
2. **Model**: LLMs → VLMs → VLAs → WAMs (World Action Models)
3. **Harness**: Perception, Action, Reasoning, Real-time Reactivity, **Memory**, Adaptive Learning
4. **Benchmark**: 5-level taxonomy (rule understanding → cross-game generalization)

### 五个 Fundamental Trade-offs
1. **Scale vs. Fidelity vs. Diversity** in data
2. **Breadth vs. Depth** (heterogeneity wall)
3. **Reasoning vs. Reactivity** (latency-intelligence dilemma)
4. **Modular Workflow vs. Model-as-Whole** (harness paradox)
5. **Code Engine vs. World Model** (simulation gap)

### 五级路线图
L1 Single-Game Mastery → L2 Within-Genre Transfer → L3 Cross-Genre Generalization → L4 Lifelong Adaptation → L5 Demiurge (agent as world creator)

## 4) Experiments & Evidence
Survey 无新实验。关键引用的数据：

| System | Scope | Key Result |
|--------|-------|------------|
| Game-TARS | 500+ games | 2× prior SOTA on Minecraft; near fresh-human on unseen web games |
| SIMA 2 | Unseen games | 26/50 MineDojo tasks (vs 2/50 SIMA 1)；15-20 min autonomous play |
| VideoGameBench | 23 games | Best VLM (Gemini 2.5 Pro) completes only 0.48% tasks in real-time |
| CombatVLA | Black Myth: Wukong | Human-level ARPG combat with 50× speedup via truncated AoT |
| NitroGen | 1000+ games, 40K hrs | Cross-game generation but no goal-directed behavior |

## 5) Interesting Observations
1. **Reasoning hurts in fast games**：Game-TARS 的 "Greedy Thinking" 在快节奏场景触发 hallucinated reasoning loops，性能低于 no-reasoning baseline — more thinking ≠ better acting
2. **Game RL transfers to general reasoning**：Game-RL 和 ViGaL 显示纯游戏 RL 训练也能提升 general VLM benchmark — games as scalable training ground
3. **Self-amplifying data flywheel**：World model 作为 adaptive data engine，根据 learner 弱点生成训练数据 → closed-loop co-evolution（类似 Agent-World 的思路）
4. **Harness paradox**：Frontier VLMs 不加 scaffolding 连开场几分钟都过不去，但 modular harness 引入 knowing-doing gap（策略对但执行错）

## 6) Limitations
- 纯 survey，无新实验贡献
- 广而浅，每个子题无法深入
- 对 Minecraft 生态偏重，其他 genre 证据不足
- L4-L5 路线图纯推测，缺乏实证
- 未提供定量的跨系统统一对比

## 7) My Technical Take
五个 trade-offs 是最有价值的贡献：

**Trade-off 3 (Reasoning vs. Reactivity)** 直接映射到 agentic planning 的核心矛盾 — 何时深度推理、何时快速反应？Dual-thread 架构（planning 5Hz + reactive 30Hz）是可迁移的 pattern。

**Trade-off 4 (Harness Paradox)** 和 Continual Harness 论文形成互补：survey 指出问题（modular harness 有 knowing-doing gap），Continual Harness 给出解法（让 harness 自我演化）。

**WAM (World Action Model)** 概念 — 统一 world prediction 与 action generation — 是 agent architecture 的前沿方向。

## 8) Transfer to Ongoing Projects
- **Agentic Memory**：Section 5.5 提供 memory taxonomy — Working Memory (sliding window, LIFO stack, history summarization) vs Long-Term Memory (semantic KG, episodic vector DB, procedural skill library)。CoALA 框架直接可用。
- **Long-Horizon Reasoning**：Dual-thread 架构（plan at 5Hz, act at 30Hz）和 selective reasoning（Lumine 模式）可迁移到 adaptive computation for agents
- **Self-Evolving**：SIMA 2 的 bootstrapped self-improvement cycle（human demo → Gemini label → self-play → self-train）和 Voyager/Steve-Evolving 的 skill library 演化模式

## 9) Next Actions
1. **深入 SIMA 2**：bootstrapped self-improvement loop 的架构细节，最接近 self-evolving game agent 的实现
2. **调研 Harness Memory designs**：CoALA 框架 + Steve-Evolving 的 episodic/procedural memory 实现
3. **Game-RL transfer 现象**：纯游戏 RL 训练也能提升 general reasoning — 作为 agentic 能力的 scalable training ground 值得验证
