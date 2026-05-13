# OPD Survey Reading Notes — 基于组内调研文档的综合读后感

> **来源**：组内研究者的 OPD 综述文档（62 页深度分析 15 篇论文 + 6 个 research ideas）
> **日期**：2026-05-13
> **性质**：这不是单篇论文笔记，而是对整个 OPD 领域的 landscape 理解

---

## 一、OPD 的本质定位

OPD 处于 SFT 和 RL 之间的 sweet spot：

```
Pure SFT ←——— OPD ———→ Pure RL
(off-policy,      (on-policy,        (on-policy,
 dense signal,     dense signal,       sparse signal,
 distribution      distribution        no ceiling)
 mismatch)         aligned)
```

核心三步：
1. Student 自己生成 rollouts（on-policy sampling）
2. Teacher 在 student 的 rollouts 上给 token-level supervision（通常 KL divergence）
3. Student 根据信号更新参数

**为什么比 SFT 好**：消除 distribution mismatch（exposure bias）
**为什么比 RL 好**：信号密度高（token-level vs sequence-level reward）
**为什么不如 RL**：有天花板（受限于 teacher quality）

## 二、核心技术维度的理解

### KL 方向选择
- **Forward KL** (mode-covering)：student 试图覆盖 teacher 所有 mode → 保持多样性但可能分散
- **Reverse KL** (mode-seeking)：student 聚焦 teacher 的高概率区域 → 精确但可能 collapse
- **关键洞察**：两者都不绝对最优。Entropy-Aware OPD 按 teacher confidence 动态切换是目前最好方案。OPSD 发现 self-distill 中 Forward KL 反而更好（因为 teacher-student 已接近）

### Self-Distillation 的信息不对称来源
| 方法 | 如何创造 teacher-student 差异 |
|------|------|
| OPSD | 给 teacher 看 GT CoT |
| SDFT | 给 teacher 看 demonstrations (in-context) |
| SDPO | 给 teacher 看 rich feedback (error messages) |
| OPSDC | 给 teacher 一个 "be concise" instruction |
| OPCD | 给 teacher 看 experiential knowledge context |

**共性**：同一个模型，teacher 有 privileged information → 产生分布差 → 作为学习信号。
这本质上是在 **不改模型的情况下制造 "未来的自己"**，然后向它学习。

### OPD = RL 的理论等价

G-OPD 的核心推导：
```
min KL(π_θ || π_teacher) = max E_π_θ[log π_teacher / π_θ]
                         = max E_π_θ[r(s,a)] where r = log(π_teacher/π_ref)
```

这意味着：
- OPD 的 reverse KL minimization = policy gradient with log-likelihood-ratio reward
- teacher 的 log-probability 就是 implicit reward
- OPD 可以直接享受 RL 的所有 stabilization tricks（clipping, baseline, entropy bonus）

**G-OPD 的杀手发现**：设 λ>1（reward extrapolation）→ student 可以超越 teacher。
这在纯 distillation 框架里不可想象，但在 RL 框架里完全自然（over-optimize implicit reward）。

## 三、最大的研究机会：OPD + RL Hybrid

这是领域最大的空白。15 篇论文几乎都是 pure OPD or pure RL，组合训练几乎未探索。

### 为什么 hybrid 应该更好？

| | OPD | RL | Hybrid |
|---|:---:|:---:|:---:|
| 信号密度 | ✅ token-level | ❌ sequence-level | ✅ adaptive |
| 天花板 | ❌ 受限于 teacher | ✅ 无限 | ✅ 无限 |
| 稳定性 | ✅ smooth KL | ❌ high variance | ✅ teacher as baseline |
| 探索能力 | ❌ 收敛到 teacher | ✅ 发现新解 | ✅ adaptive |
| 难题表现 | ❌ noisy teacher | ❌ zero reward | ⚡ guided exploration |

### 最有希望的 hybrid 方案（来自调研文档的 ideas）

**Idea 1: Teacher-as-Baseline**
```
A_hybrid(i,t) = [r_i - mean(r)]  +  α · [log π_tea(y_t|s_t) - log π_θ(y_t|s_t)]
                RL outcome signal       teacher token-level baseline
```
- RL outcome → 方向（rollout 整体好不好）
- Teacher token-level → 精度（哪个 token 的决策好/坏）
- α 可以 decay：早期大（靠 teacher baseline），后期→0（纯 RL exploration）

**Idea 2: Token-Level Adaptive Routing**
```
w_t = σ(γ · teacher_confidence_t - τ) · σ(γ · student_teacher_gap_t - δ)
L_t = w_t · L_OPD + (1-w_t) · L_RL
```
- Teacher confident AND student far behind → OPD（high efficiency）
- Teacher uncertain OR student close → RL（explore beyond）

**与我们的研究方向的连接**：
- Self-evolving agents 本质上需要 "先 imitate 再 surpass" 的训练范式
- OPD+RL hybrid 正是这个范式的训练侧实现
- Agent-World 的 self-evolving loop 可以看作 macro-level 的 OPD→RL spiral

## 四、对各论文的质量判断

### Top Tier（Rel ≥ 4, Qual ≥ 4）
- **SDPO** — 最实际有效（LCB v6 超 Claude），rich feedback 是真正的 dense signal 来源
- **G-OPD** — 理论最 elegant（OPD=RL + reward extrapolation 超越 teacher）
- **POPE** — 发现最重要（ray interference + privileged exploration 解决难题）
- **Nemotron-Cascade 2** — 工业验证最强（NVIDIA, 30B→3B, 40 步收敛）
- **Revisiting OPD** — 诊断最有价值（首次系统化 failure modes）
- **OEL / ExGRPO** — 经验价值研究最深

### Solid Tier（Rel 3-4, Qual 3）
- REOPOLD — 框架化但 over-packaged（OPD=RL 等价性并非新发现）
- OPSD — Forward KL 反直觉发现值得关注，但实验规模小
- OPSDC — "be concise" 生效机制未知，但效果惊人
- BiCC-RCC — 降方差有效但 incremental

### Weak Tier
- Veto — 实验规模太小（0.5B-2B），理论与实践矛盾
- RL-Judge-Distill — Novelty 有限
- GAD — 唯一评估是 GPT-4o score，无客观 benchmark

## 五、对我们 reading list 分类的验证

当前 5 个子分类应该能覆盖所有新论文：

| 子分类 | 覆盖什么 | 边界判断 |
|---|---|---|
| **OPD ↔ RL Unification** | 理论等价证明、hybrid training、reward extrapolation | 如果论文的核心 contribution 是建立 OPD-RL 连接 |
| **Self-Distillation** | 自己教自己、信息不对称、privileged info | 如果 teacher = self（或 self + context） |
| **KL Direction & Stability** | Forward vs Reverse、adaptive selection、failure modes | 如果核心关注 KL 方向选择或训练稳定性 |
| **Exploration & Curriculum** | 难题探索、ray interference、数据合成 | 如果核心问题是"teacher 也不会怎么办" |
| **Industrial & Scaling** | 大规模验证、多域训练、工业 pipeline | 如果核心贡献是规模化和工程实践 |
| **Application Extension** | 新领域应用（video, code, agent, continual learning） | 如果核心是把 OPD 迁移到新 domain |

新来的 OPD 论文按以上分类直接放入对应子分类。如果一篇论文横跨两个子分类，放到其**主要贡献**所在的分类。

## 六、与 Master 研究方向的交叉点

1. **Self-Evolving Agent Training** ← Agent-World 的 self-evolving loop 就是 macro-level OPD→RL spiral
2. **Memory-Augmented Training** ← OPCD (context distillation) 和 SDFT (demo-conditioned) 本质是把 memory/experience 蒸馏进权重
3. **Long-Horizon RL** ← POPE 的 ray interference 直接影响 long-horizon agent 训练的 curriculum 设计
4. **Harness Evolution** ← Continual Harness 的 self-improvement 可以看作 inference-time OPD（不改权重，但改 harness）

最关键的研究机会：**OPD + RL hybrid for agent training** — 用 teacher distillation 做基础能力获取，用 RL 做环境适应和超越。这正是 Agent-World 的训练范式，但目前没有 token-level 的 adaptive hybrid。
