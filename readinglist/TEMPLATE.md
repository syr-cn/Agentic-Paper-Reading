# Reading List Table Template

> 用法：每篇论文一行；`Alias` 列请写成**指向具体阅读笔记的超链接**。
> 
> **评分体系（2026-05-13 双维度版）**：
> - **Type**: A = RL Training / B = Harness Engineering / C = Benchmark
> - **Rel**: 话题相关性 1-5（5=核心命中, 4=强相关, 3=有启发, 2=边缘, 1=无关）
> - **Qual**: 论文质量 1-5（按 Type 分别评判，详见 RESEARCH_PREFERENCES.md）

## Markdown 表格模板

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [Paper-Alias](../papers/YYYY-MM-DD_short-title.md) | Paper Title | [arXiv 2511](https://arxiv.org/abs/2511.20857) | First: Org A; High-impact: Org B | A | 4 | 3 | ![fig1](https://arxiv.org/html/2511.20857v1/x1.png) | 核心发现 |

## 字段说明

| 字段 | 规则 |
|---|---|
| **Alias** | `[Alias](相对路径)` 指向阅读笔记，禁止死链 |
| **Source** | `[arXiv xxxx](url)` 统一用 `/abs/` 链接 |
| **Institution** | 多机构写 `First: X; High-impact: Y`；中国机构用简称 |
| **Type** | A = RL Training, B = Harness Engineering, C = Benchmark |
| **Rel** | 话题相关性 1-5 |
| **Qual** | 论文质量 1-5 |
| **Figure 1** | 优先 arXiv HTML 直链；不可得写 `N/A（原因）` |
| **Summary** | 高信息密度要点，含关键数字，不写空话 |

## 子分类标记（用于 memory-long-horizon.md 等含子类的 list）

在同一个表格文件中，用 `### 子分类名` 分隔不同区块，每个区块各有独立表头：

```markdown
### Memory Systems
| Alias | Title | ... |

### Memory Evaluation
| Alias | Title | ... |

### Long-Horizon & Context
| Alias | Title | ... |
```
