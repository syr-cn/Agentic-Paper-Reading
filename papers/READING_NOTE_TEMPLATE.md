# Paper Reading Note Template (DNL: Deep Note & List) (for `papers/`)

> 用法：复制本模板新建文件（建议命名：`YYYY-MM-DD_short-title.md`）。
> 目标：避免流水摘要，输出"可决策、可复用"的研究笔记。
> 术语约定：**DNL = Deep Note & List**。其中 `Deep Note` 指单篇深读笔记，`List` 指 readinglist 索引更新。

<!-- Agent 写作约束（不要将本注释块中的括号提示词输出到最终笔记标题中）：
- 满足 0~7 全结构要求
- 至少参考 1-2 篇历史笔记风格：evo-memory / reasoning-judge / arise
- Figure 区至少 1 张真实图链 + 解释，不可空写
- Experiments 必须含具体数字
- Main result table 必须有 baseline/proposed/delta
- Analysis 必须用"现象+解释"格式
- 评分解释、Why-read、CRGP 均为必填
- 章节标题保持简洁，不要带"（必填）""（至少 1 张）"等指令性括号后缀
-->

## 0) Metadata
- **Title:** 
- **Alias:** 
- **Authors / Org:** 
- **Venue / Status:** 
- **Date:** 
- **Links:**
  - Abs: 
  - HTML: 
  - PDF: 
  - Code: 
- **Tags:** 
- **My rating:** 
- **Read depth:** skim / normal / deep
- **Scoring (1+2+2):** 基础 1 + 质量 x + Observation y = z

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：**

## 2) CRGP 拆解 Introduction
### C — Context
- 
### R — Related work
- 
### G — Research gap
- 
### P — Proposal
- 

## 3) Figure 区
<!-- 图策略：
1) 优先 arXiv HTML 直链（如 https://arxiv.org/html/<id>v1 对应图片资源）；
2) 若 HTML 不可用，使用 arXiv source 图并存到 assets/<alias>/，在笔记中放相对路径；
3) 不能只写图意，不给链接/图片。
至少 1 张主图 + 1-2 句解释。-->

- 图1（方法或主结果）：`![fig1](<URL>)` + 1-2 句解释
- 图2（可选，分析图）：`![fig2](<URL>)` + 1-2 句解释
- 图3（可选，ablation/热力图）：`![fig3](<URL>)` + 1-2 句解释

## 4) Experiments
### 4.1 Experimental setup
- 任务/数据：
- 模型/agent 配置：
- 对比基线：
- 评测指标：

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
|  |  |  |  |

### 4.3 Analysis experiments
<!-- 每条分析用"现象+解释"格式，可选加【标注】写个人判断 -->
- **现象：**
  **解释（作者）：**
  **【标注】（我的判断，可选）：**

- **现象：**
  **解释（作者）：**
  **【标注】（我的判断，可选）：**

## 5) Why it matters for our work
- 

## 6) Actionable next step
- [ ] 
- [ ] 

## 7) 评分解释
- **质量分 x/2：**
- **Observation 分 y/2：**
- **总分 z/5：**
- **为什么不是更高分：**
