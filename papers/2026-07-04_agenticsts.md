# AgenticSTS 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents
- **Alias:** AgenticSTS
- **Authors / Org:** Xiangchen Cheng¹², Yunwei Jiang²³, Jianwen Sun¹³⁴, Zizhen Li¹³⁴, Chuanhao Li¹, Xiangcheng Cao¹, Yihao Liu¹, Fanrui Zhang³⁵, Li Jin², Kaipeng Zhang¹†
  - ¹Alaya Lab ²Shanghai Jiao Tong University ³Shanghai Innovation Institute ⁴Nankai University ⁵USTC
  - † Corresponding: kaipeng.zhang@shanda.com
- **Venue / Status:** arXiv 2607.02255v1 (2026-07-02)
- **Links:**
  - Abs: https://arxiv.org/abs/2607.02255
  - PDF: https://arxiv.org/pdf/2607.02255
  - Code: https://github.com/AlayaLab/AgenticSTS
  - Data: https://huggingface.co/datasets/ShandaAI/AgenticSTS-trajectories
  - alphaXiv: https://www.alphaxiv.org/overview/2607.02255
- **Community Stats:** alphaXiv 5 likes / HF Daily Papers ⬆️40
- **Tags:** agent-memory, bounded-context, ablation-testbed, long-horizon, game-agent, skill-library
- **Read depth:** deep

```yaml
Type: C  # Benchmark/Testbed
Relevance: 5/5  # 直接命中 agentic memory evaluation + bounded memory contract + long-horizon agent
Quality: 4/5
```

**Why Not Higher (Quality):** 核心实验规模有限（N=10/cell），Fisher exact p≈0.37 不显著；缺乏最关键的 same-codebase accumulating-context vs bounded-contract 对照（自认 limitation）；单角色单游戏泛化性存疑。但作为 testbed + methodology 贡献，设计优雅且释放完整。

---

## 0.5) 研究组分析

### 通讯作者：Kaipeng Zhang（张凯鹏）
- **机构：** Alaya Lab（盛大集团旗下 AI 实验室）。邮箱域名 shanda.com。
- **背景：** Alaya Lab 是盛大集团（Shanda Group）的 AI 研发部门。盛大从游戏起家（盛大游戏），近年转型做 AI 基础设施（ShandaAI 是 HuggingFace org）。
- **GitHub handle：** mercerme（Alaya Lab org 下的主要贡献者）
- **组的大图景：** 从 GitHub repo 结构看，Alaya Lab 做的是 **game agent as testbed for AI** 的路线——用游戏（尤其是策略游戏）做 agent 能力的 rigorous evaluation，而不是单纯做 game AI。这条路线对标 DeepMind 早年用 Atari/StarCraft 做 RL benchmark 的逻辑。

### 一作：Xiangchen Cheng（程翔宸）
- 上海交大 + Alaya Lab 联合培养（推测硕士/博士生）

### 其他：
- Yunwei Jiang（姜昀蔚）：上海交大 + 上海创新院，也是 [SoK: Agentic Skills](https://arxiv.org/abs/2606.xxxxx) 的作者之一（本文 ref [16]），做 skill 形式化定义
- Fanrui Zhang（张帆瑞）：USTC + 上海创新院（老乡 👀）

### 是否值得 Follow：
**值得。** Alaya Lab 选题精准（bounded memory + ablation methodology），工程释放完整（298 trajectories + scripts + frozen snapshots），且 SoK 论文同组出品说明有理论野心。这个组在 agent memory evaluation 赛道上有一席之地。

---

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：** 论文将 agent memory 从"工程细节"提升为"可形式化、可消融、可评估的合约（contract）"；用 5 层类型化检索替代 transcript accumulation，使 memory 的每一层独立可控。核心观察：在 Slay the Spire 2 上，L5（triggered strategic skills）是最大贡献层（3/10→6/10 win rate），而 L4（episodic memory）在固定难度下效果饱和。

---

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- Long-horizon LLM agent 的 memory 本质上是"每次决策被允许看到什么"的 contract
- 主流方法（ReAct/Reflexion）简单累加历史 transcript，导致 context 爆炸 + 效果归因困难
- 实践社区（Anthropic context engineering blog）越来越关注 agent loop 中的 memory stage 设计

### R — Related work
- **Prompt-history agents:** ReAct, Reflexion — 追加 transcript
- **Typed/structured memory:** MemGPT, Mem0, MemoryOS, GAM, Agent Workflow Memory — 外部存储但通常缺乏 ablation
- **Skill libraries:** Voyager, SkillsBench, SkillOS, Memento-Skills — 外部技能但未与 memory 统一评估
- **Game testbeds:** Crafter, NetHack, BALROG, RAGEN — 提供随机环境但多不支持 memory 消融

### G — Research gap
- 没有一个 testbed 能**同时**做到：bounded context + typed retrieval + 各层独立消融 + game policy evaluation
- 现有 agent 评估要么 open-ended（难归因）、要么 short-horizon（不需 memory）
- 公开 STS2 agents（STS2MCP, CharTyr）跑 A0 胜率为零，但没人做 ablation

### P — Proposal
- **Bounded Memory Contract:** 每次决策从 5 个类型化 slot（L1-L5）重新组合 user message，不追加跨决策 transcript
- **Slay the Spire 2 作为 testbed:** 封闭规则 + 长 horizon（median ~67 strategic calls/run）+ 多维随机性 + 未饱和（人类 A0 win rate 16%）
- **释放 298 条 trajectory + 冻结 snapshot + 分析脚本**，支持社区复现和扩展

---

## 3) Figure 区（至少 1 张）

- **Figure 1（概览）：**
  ![fig1](https://raw.githubusercontent.com/AlayaLab/AgenticSTS/main/assets/fig1-overview.png)
  解释：对比 transcript accumulation（左）vs bounded typed contract（右）。右侧展示 L1-L5 五层的 per-decision composition，以及如何把 memory 变成可消融的 evaluation surface。

- **Figure 4（Fixed-A0 ablation surface）：**
  五个 cell 共享 bounded contract，相邻 bar 沿 named ablation axis 排列：baseline-strict → prompt-only → mode-a → mode-b-frozen → full-frozen。冻结 store SHA 1888a62。

---

## 4) Method

### 4.1 Per-Decision Compositional Context
核心公式：对决策 d 和状态 s_d，engine 组装：
```
u_d = compose(L1, L2(s_d), L3(s_d), L4(s_d), L5(s_d))
```
发送为 ⟨sys, u_d⟩。**不追加跨决策 raw transcript。**

Context 增长为 O(|sys| + s_thread + Σᵢ kᵢ · sᵢ)，独立于决策数量 d（vs transcript 的 Ω(d · s̄)）。

### 4.2 Five Typed Knowledge Layers
| Layer | Store | Key | Mutability | Ablation |
|-------|-------|-----|------------|----------|
| L1 | protocol | state type | fixed | always on |
| L2 | schema | decision type | fixed | always on |
| L3 | game rules | entity lookup | patch-refreshed | filterable |
| L4 | episodic memory | char/ascension/act/enemy | postrun write | on/off |
| L5 | skill library | trigger condition | gated write (4-level) | off/A/B |

关键设计：L5 skill 有 Boolean trigger + prose policy + 4-level write gate（cosine → Jaccard → LLM judge → reap）

### 4.3 Routing & Combat Truncation
- 四层 model tier: fast / strategic / analysis / evolution
- 只有 combat 有 local conversation（≤3 msg/round: start, ok, state）
- 结果：median 67 strategic calls/run（不是每个 in-game action 都调 LLM）

### 4.4 Skill Discovery (L5 Population)
- **Mode A:** 人工 seed + mistake-driven self-evolve（combat loss → baseline comparison → A/B check → write gate）
- **Mode B:** stub-template-filled authoring（5 个角色参数化模板）
- 两者 A0 win rate 一致（6/10），说明 skill layer 的存在比具体 prose 来源更重要

---

## 5) Experiments & Evidence

### 5.1 Fixed-A0 Ablation (N=10/cell, Table 2)
| Cell | L5 | L4 | Win | Score |
|------|----|----|-----|-------|
| baseline-strict | – | – | 3/10 | 70.4 |
| prompt-only | – | – | 4/10 | 69.6 |
| mode-a (hand skills) | A | – | 6/10 | 85.5 |
| mode-b-frozen (template skills) | B | – | 6/10 | 83.3 |
| full-frozen (skills + episodes) | A | ✓ | 6/10 | 82.1 |

- **ΔL5 = +2/10** (largest observed)，但 Fisher exact p≈0.37 → directional, not significant
- **L4 at A0 is saturated:** mode-a vs full-frozen score CI [−21.7, +14.9] → 加 episodic memory 没帮助（在低难度下）
- Wilson 95% CI for 6/10: [31.3%, 83.2%]

### 5.2 Cross-Backbone Transfer (Table 3)
Gemini-trained L4+L5 stack 移植：
- **Qwen 3.6-27B:** 0/5→0/5, score +84.5%（帮了一些但没赢）
- **DeepSeek V4-Pro:** 0/5→0/5, score −18.1%（反而伤了！）
- **Gemini 3.1-Pro:** 3/10→6/10, +16.6%

→ 冻结 skill stack 是 backbone-specific 的，不能 assume transferability

### 5.3 Auto-Mode Ascension Ladder
- 有 postrun memory write → 到达 A6-A8
- 无 postrun → 止步 A2-A4
- L4 在 ladder 中有效（高难度需要经验累积）

### 5.4 vs Open-Source Accumulating-Context Agents (§7)
**重要 caveat：** 这是 "shipped system comparison"，不是 controlled ablation。
- **STS2MCP:** 0/5 wins, mean floor 17.6, per-call prompt 增长到 ~500k tokens
- **CharTyr:** 0/5 wins, mean floor 5.6（频繁 invalid_action 错误）
- **AgenticSTS (bounded):** baseline-strict 3/10, full-frozen 6/10
- **Token efficiency:** bounded contract ~5k/call（恒定） vs accumulating 9k→500k/call
- **Cost gap:** 66-90× more fresh tokens per score point

---

## 6) Limitations
1. **N=10 样本量** → 统计检验力不足（作者诚实承认）
2. **缺乏 same-codebase accumulating-context baseline** → 最关键对照留给 future work
3. **单角色（Silent）+ 单游戏 + 单 backbone（Gemini）** → 泛化性未验证
4. **Architectural scope:** training-free, turn-based only → 不适用 streaming/visual/multi-agent 场景
5. **Skill 内容依赖 author curation** → Mode B 是 "within-interface template filling"，非 fully autonomous invention

---

## 7) My Technical Take

### 方法论贡献 > 结果贡献
这篇文章最核心的 insight 不是 "6/10 beats 3/10"（本身不显著），而是：
1. **Memory 可以被形式化为 contract**——每层有明确的 mutability, retrieval key, write gate
2. **Bounded contract 使 ablation 成为可能**——transcript accumulation 下你无法回答 "哪一层 memory 在起作用"
3. **Released 298 trajectories + frozen snapshots** 使 future ablation 能用同一个 codebase 做 controlled comparison

### 对我们工作的启示
这篇文章对 agentic memory 研究有几个直接相关的设计点：
- **"Memory is a contract about what each future decision is allowed to see"** — 这个 framing 非常 elegant，可以作为我们 memory 工作的理论基础
- **Five-layer typed retrieval** 的设计（fixed protocol → state schema → knowledge → episodes → skills）是一种实用的 memory taxonomy
- **L5 > L4 的发现**：strategic skills（经验蒸馏的 tactics）比 raw episodic memory 更有用，至少在 closed-rule game 中
- **Backbone specificity** 警示：frozen memory/skill stack 不一定 transfer——memory 可能和 backbone 有耦合

### 弱点与机会
- 论文 **不能证明** bounded contract > accumulating context（只证明了它是 ablatable 的）
- 这恰恰是 **后续工作的最大机会**：在同一 codebase 加 accumulating baseline，做 controlled comparison
- 样本量问题可以用 bootstrap 或 Bayesian estimation 缓解，298 条 trajectory 已经有足够数据做 power analysis
- **Open question:** 在 open-ended environments（非 closed-rule game）中，bounded contract 是否同样有效？

---

## 8) Transfer to Ongoing Projects
- **对 agentic memory 研究的直接对标：** AgenticSTS 的 5-layer taxonomy 可以和我们的 memory architecture 设计做映射对比
- **Evaluation methodology 参考：** 如果做 memory 的 benchmark 工作，"typed, bounded, ablatable" 是一个非常好的 desiderata checklist
- **Game as testbed 的可行性：** STS2 的 closed-rule + long-horizon + stochastic 属性确实是 memory evaluation 的理想特性；但如何迁移到 open-domain agent 是 gap

---

## 9) Next Actions
- [ ] 关注 AlayaLab 后续是否发布 same-codebase accumulating-context 对比
- [ ] 考虑在自己的 memory 工作中引用 "memory as contract" framing
- [ ] 审视 AgenticSTS 的 5-layer design 是否可以 generalize 到 non-game settings
- [ ] Follow Yunwei Jiang（SoK: Agentic Skills 同作者）的后续 skill 形式化工作
