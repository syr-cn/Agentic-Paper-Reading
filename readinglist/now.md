# Now Reading Queue

## Must-read (this week)
- [ARISE](../papers/2026-03-19_arise.md) — policy-driven skill selection + evolving skill library；和当前 memory/agent RL 主线直接相关。
- [01me-Distillation-Notes](../papers/2026-03-19_01me-distillation-notes.md) — context asset + writer-reviewer loop；对系统化反思闭环设计有直接启发。✅（2026-03-19 deep note synced）

## Should-read
- [AutoSkill](../papers/2026-03-11_autoskill.md) — 已升级为 deep note（2026-03-19）；下一步建议做 sidecar A/B 验证（skill-memory vs summary-memory）。

| Alias (link to note) | Title | Source | Institution | Benchmarking | ⭐ | Figure 1 | Summary |
|---|---|---|---|---|---:|---|---|
| [ExGRPO](../papers/2026-03-23_exgrpo.md) | ExGRPO: Learning to Reason from Experience | [arxiv 2510](https://arxiv.org/pdf/2510.02245) | First: University of Macau; High-impact: Shanghai AI Laboratory | AIME24/25, AMC, MATH-500, Minerva, OlympiadBench, ARC-c, GPQA★, MMLU-Pro | ★★★★☆ | ![fig1](https://arxiv.org/html/2510.02245v1/x1.png) | 首个系统研究 RLVR 经验价值的工作：中等难度题+低熵轨迹是最优经验来源；bucketed replay + entropy selection + mixed-policy objective 在 5 模型上平均 +3.5/+7.6（ID/OOD），并能稳定弱模型训练崩溃。 |
| [TRT](../papers/2026-03-23_trt.md) | Test-time Recursive Thinking: Self-Improvement without External Feedback | [arxiv 2602](https://arxiv.org/pdf/2602.03094) | First: Microsoft Research; High-impact: Microsoft Research | AIME-24/25, LiveCodeBench v6 Hard | ★★★★☆ | N/A（arXiv 未提供可用 HTML Figure 资源） | 无需外部反馈的 test-time 迭代自改进：Generate-Select-Reflect 三阶段闭环 + 负约束知识列表（<1.5% context）；开源模型 AIME 100%，o4-mini/o3 在 LCB Hard +10.4/+14.8 pp；核心发现：失败知识 > 成功知识，depth > breadth。 |

## Nice-to-read
- 

## Notes
- Prioritize papers with direct transfer value to current projects.
- Follow-up: 产出一页《ARISE × 我们系统》的 ablation 计划。
