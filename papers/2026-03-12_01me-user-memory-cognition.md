# 01.me 用户记忆：从 Memory 到 Cognition（DNL Deep Note）

## 0) Metadata
- **Title:** From Memory to Cognition: How AI Agents Can Deliver Truly Personalized Services  
- **Alias:** 01me-User-Memory-Cognition  
- **Authors / Org:** Bojie Li（Pine AI / 01.me）  
- **Venue / Status:** Blog + Talk Slides（非同行评审）  
- **Date:** 2025-10（由 URL 路径推断）  
- **Links:**  
  - Blog: https://01.me/en/2025/10/user-memory-for-ai-agent/  
  - Slides(HTML): https://01.me/files/user-memory-talk-slides/dist/  
  - Slides Source: https://01.me/files/user-memory-talk-slides/slides.md  
  - Slides PDF: https://01.me/files/user-memory-talk-slides/dist/slidev-exported.pdf  
- **Tags:** agent-memory, personalization, context-aware-retrieval, rubric, llm-as-judge  
- **My rating:** ★★★☆☆（保持原倾向）  
- **Read depth:** normal  
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3/5**

---

## 1) 一句话 Why-read
这篇最有价值的点是把“记忆=存事实”升级为“记忆=可行动认知（偏好×场景×更新）”，并给出一个可操作评估框架（L1/L2/L3 + Rubric + LLM Judge），适合直接指导 agent memory 产品化。

---

## 2) CRGP
### C — Context
- 当前很多 agent 的“个性化”仍停留在：长上下文拼接、或零散事实存储。  
- 真正服务型 agent 需要跨会话、跨时间、跨领域持续理解用户，并在关键节点主动提醒。

### R — Related work
- 文章对比了 Simple Notes / Enhanced Notes / JSON Cards / Advanced JSON。  
- 同时对照 ChatGPT（偏注入式）与 Claude（偏按需检索式）记忆机制。  
- 检索侧强调 context-aware retrieval，而不是扁平 RAG 直接塞片段。

### G — Gap
- 工程方向清晰，但公开证据强度有限：  
  - 缺标准开源 benchmark 配置细节；  
  - 缺模型/检索参数/统计检验；  
  - 缺与公开 baseline 的可复现实验曲线。

### P — Proposal
- 给出“从记忆到认知”的落地框架：  
  1) 双层记忆（JSON 常驻 + RAG 按需）；  
  2) 三层能力目标（L1 回忆 / L2 多会话 / L3 主动服务）；  
  3) Rubric + LLM Judge 做持续评估；  
  4) 强调记忆更新、覆盖与消歧（而非静态画像）。

---

## 3) Figure 区（真图链）
- **图1（演讲页真图链，来源页面截图）**  
  ![fig1-memory-cognition-slides](https://image.thum.io/get/width/1400/https://01.me/files/user-memory-talk-slides/dist/)  
  解释：这是原始 slides 的真实页面截图链接，概览了五个模块（重要性、表示、检索、评估、前沿研究），对应全文结构。  

- **图2（博客页真图链，来源页面截图）**  
  ![fig2-memory-cognition-blog](https://image.thum.io/get/width/1400/https://01.me/en/2025/10/user-memory-for-ai-agent/)  
  解释：对应博客主页面，确认本文是“方法论 + 案例 + 评估框架”而非论文式单一实验报告。

---

## 4) Experiments（含数字 + 缺失标注）
### 4.1 Experimental setup
从 slides 可提取的明确实验信息：
- 三层评估框架：**L1/L2/L3**。  
- 总测试数：**60** 个 case（每层 **20** 个）。  
- 每个 case：**1–3** 个 session。  
- 每个 session：约 **50** 轮对话。  
- 示例强度：银行案例含 **47 分钟**、**50+ turns**、账号精确检索（如 4429853327）。

**缺失标注（原文未披露）：**
- 使用的底模与版本：**原文未给出可提取数字**。  
- 检索参数（embedding 模型、top-k、rerank）：**原文未给出可提取数字**。  
- 统计显著性/置信区间：**原文未给出可提取数字**。  
- 与外部 baseline 的统一对照：**原文未给出可提取数字**。

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 评测集规模 | 原文未给出统一公开基线数字 | 60 cases（20×3层） | N/A |
| 单case上下文复杂度 | 常见短对话（原文未给出数字） | 1–3 sessions, ~50 turns/session | N/A |
| L1 示例难度 | 原文未给出可比数字 | 47分钟 + 50+轮后精确召回 | N/A |
| 检索失败率改进（引用 Anthropic context-aware） | BM25 基线 | 失败率降低 **49%**（+re-ranker 至 **67%**） | 明确改进 |
| ReasoningBank 外部实验（slides 引述） | 对照系统 | 相对提升最高 **34.2%**，步骤减少 **16.0%** | 明确改进 |

> 说明：后两行属于 slides 引用的外部研究数字，不是本文自建主实验的完整公开表。

### 4.3 Analysis experiments（现象+解释）
1. **现象：** 作者把能力分成 L1/L2/L3，并将“主动服务”定义为最高层。  
   **解释（作者）：** L1/L2 仍是被动响应，L3 才体现跨时空关联与前瞻推理。  
   **【标注】我的判断：** 这个分层对产品路线很实用，能避免“召回准=智能高”的误判。

2. **现象：** 双层结构（JSON Cards 常驻 + context-aware RAG 按需）是主推架构。  
   **解释（作者）：** 常驻层提供稳定事实骨架，检索层补充证据细节。  
   **【标注】我的判断：** 是当前工程最稳妥折中；关键瓶颈其实在“写入治理/冲突覆盖”。

3. **现象：** 文章明确强调“不能直接把原始案例扔进 RAG”。  
   **解释（作者）：** 扁平检索会造成规则边界缺失与统计失真（如猫比例、职业折扣规则）。  
   **【标注】我的判断：** 与我们线上经验一致，index-time distillation 比盲增 top-k 更有效。

4. **现象：** 评估部分强调 Rubric + LLM Judge + 人工补充。  
   **解释（作者）：** 仅靠自动指标无法覆盖真实用户体验与失败边角。  
   **【标注】我的判断：** 正确，但需额外防 judge 偏置和 reward hacking。

#### Case（>=2）
- **Case 1（L2 消歧，多实体冲突）**  
  用户有两辆车（2019 Honda / 2023 Tesla），当请求“schedule service for my car”时，系统应主动消歧，而非默认单车。  
  价值：验证“多实体状态管理 + 决策询问”。

- **Case 2（L2 覆盖更新，版本有效性）**  
  定制家具订单多次修改（颜色、椅型、交付期），最终状态应只保留“最新有效版本”。  
  价值：验证“记忆覆盖/失效管理”，避免历史脏信息污染。

- **Case 3（L3 主动提醒，跨会话推理）**  
  护照到期（2025-02-18）与东京行程（1月）分散在独立会话，系统需主动提示入境有效期风险。  
  价值：验证“主动服务是否真实发生”。

---

## 5) Why it matters for our work
- 对 **agent memory**：给了“结构化常驻 + 证据检索”可落地组合。  
- 对 **long-context**：明确长上下文应降级为证据池，不应承担全部长期记忆职责。  
- 对 **多模态/策略学习**：L1/L2/L3 可直接映射成分层奖励与评测面板。

---

## 6) Actionable next step
- [ ] 在现有系统补一个 **L1/L2/L3 仪表盘**（先 20-case 小集，逐步扩到 60-case）。  
- [ ] 实做 **覆盖更新规则**（同一槽位多版本只保留当前有效项 + 保留审计链）。  
- [ ] 做一次 **双层架构 A/B**：纯长上下文 vs JSON常驻+按需检索，记录正确率/Token/P95 延迟。

---

## 7) 评分解释（保持原倾向）
- **质量分 1/2：** 框架有价值、案例扎实，但公开可复现实验细节不足。  
- **Observation 分 1/2：** 对系统设计启发强，但缺大规模可验证数字支撑。  
- **总分 3/5：** 与原倾向一致。  
- **为什么不是更高分：** 缺统一 baseline 数字表、缺统计检验、缺可复现实验配置。