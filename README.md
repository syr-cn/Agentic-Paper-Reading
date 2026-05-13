# Agentic Paper Reading

> Research notebook for **agentic memory / long-horizon reasoning / RL for agents / skill evolution**.
> Maintained by Yaorui Shi (史曜睿) + Twilight 🦄✨

## 📊 Project Snapshot

| Metric | Value |
|---|---:|
| Total paper notes | **39** |
| Reading lists | **5** |
| Last updated | **2026-05-13** |

---

## 🧭 Reading Lists

| List | Focus | Papers |
|---|---|---:|
| [Memory & Long-Horizon](readinglist/memory-long-horizon.md) | Memory systems + evaluation + long-context reasoning | 11 |
| [Skill](readinglist/skill.md) | Skill evolution, skill benchmark, continual learning | 11 |
| [On-Policy Distillation](readinglist/on-policy-distillation.md) | RL training, GRPO, on-policy data evolution | 7 |
| [General LLM/Agent](readinglist/general-llm-agent.md) | Tool use, harness, agent benchmark/safety | 6 |
| [Blog](readinglist/blog-topic.md) | High-signal blog analyses | 8 |

---

## 📐 Scoring & Evaluation

**双维度评分体系（2026-05-13）**：
- **Type**: A (RL Training) / B (Harness Engineering) / C (Benchmark)
- **Relevance**: 话题相关性 1-5
- **Quality**: 论文质量 1-5（按 Type 差异化标准）

三个质量指标：
1. 作者/机构影响力
2. 叙事与方法
3. 实验与现象（必须有数字）

详见 [PAPER_PREFERENCES.md](PAPER_PREFERENCES.md) 和 [RESEARCH_GUIDE.md](RESEARCH_GUIDE.md)。

---

## 🧠 Research Guide

[RESEARCH_GUIDE.md](RESEARCH_GUIDE.md) — 科研脉络整理，包含：
- 三类方法的关注框架（Training / Harness / Benchmark）
- 当前领域热点问题
- 评判标准的设计哲学
- 作为之后阅读笔记写作的 Standard

---

## 🗂️ Repository Structure

```
├── PAPER_PREFERENCES.md    ← 论文选择偏好 & 双维度评分框架
├── RESEARCH_GUIDE.md       ← 科研脉络 & 写作标准
├── papers/                 ← 结构化阅读笔记（一篇一文件）
│   └── READING_NOTE_TEMPLATE.md
├── readinglist/            ← 按话题分类的论文列表
│   ├── general-llm-agent.md
│   ├── memory-long-horizon.md
│   ├── on-policy-distillation.md
│   ├── skill.md
│   ├── blog-topic.md
│   ├── TEMPLATE.md
│   └── _archive/           ← 旧 list 归档
├── daily/                  ← 每日论文推荐记录
├── weekly/                 ← 周报/趋势追踪
├── assets/                 ← 图片资源
├── scripts/                ← HTML 生成脚本
└── templates/              ← HTML 模板
```

---

## 🔧 Reading Pipeline Standard

1. **Source extraction**: 优先 arXiv HTML → fallback PDF
2. **Figure policy**: 至少 1 张带链接的图 + 解释
3. **Main result table**: 必须有 baseline / proposed / delta 数字
4. **Analysis writing**: 「现象 + 解释」格式；个人判断用 `【标注】`
5. **Scoring**: 双维度（Rel X/5 + Qual Y/5）+ "Why Not Higher"
6. **Sync**: 更新笔记后同步 readinglist summary
