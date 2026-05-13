# General LLM/Agent Reading List

> 通用 Agent 能力：tool use orchestration, agent benchmark, agent safety, harness engineering

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [DIVE](../papers/2026-03-13_dive.md) | DIVE: Scaling Diversity in Agentic Task Synthesis for Generalizable Tool Use | [arXiv 2603.11076](https://arxiv.org/abs/2603.11076) | First: N/A（已检查 arXiv HTML/PDF，未显式给出机构）; High-impact: N/A | — | — | — | https://arxiv.org/html/2603.11076/x1.png | 采用“先执行工具取证据，再反推任务”的合成顺序，提升点主要由 diversity scaling 驱动，而非单纯扩数据量。 |
| [MADQA](../papers/2026-03-13_madqa.md) | Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections | [arXiv 2603.12180](https://arxiv.org/abs/2603.12180) | First: Snowflake; High-impact: Snowflake | — | — | — | N/A（arXiv 未提供可用 HTML Figure 资源） | 将评估从 accuracy-only 扩展为 accuracy + effort calibration，揭示许多高分 agent 依赖高成本试错而非高效导航策略。 |
| [Reasoning-Judge](../papers/2026-03-13_reasoning-judge.md) | Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training | [arXiv 2603.12246](https://arxiv.org/abs/2603.12246) | First: Meta; High-impact: Meta | — | — | — | https://arxiv.org/html/2603.12246/x1.png | 证明 reasoning judge 虽较难被早期低级 hack，但长期仍可能把 policy 推向更高阶 judge-deception，不等于“更强就更安全”。 |
| [AutoRL-Env](../papers/2026-03-13_auto-rl-env.md) | Automatic Generation of High-Performance RL Environments | [arXiv 2603.12145](https://arxiv.org/abs/2603.12145) | First: N/A（正文可提取片段未给出机构）; High-impact: N/A | — | — | — | https://arxiv.org/html/2603.12145/x1.png | 贡献不只在加速环境，而在“自动翻译 + 分层语义等价验证”流程化；强调性能收益必须与等价性验证绑定。 |
| [Agentic-MME](../papers/2026-04-08_agentic-mme.md) | Agentic-MME: What Agentic Capability Really Brings to Multimodal Intelligence? | [arXiv 2604.03016](https://arxiv.org/abs/2604.03016) | First: N/A; High-impact: N/A | — | — | — | N/A | 系统评估 agentic 能力对多模态智能的真实贡献；Visual+Knowledge Expansion 联合 > 单独使用；benchmark 标注质量极高。 |
