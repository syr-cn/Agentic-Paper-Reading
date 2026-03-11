# PAPER_PREFERENCES.md

## Primary Interests (High Priority)
1. Agentic memory systems (episodic/semantic/procedural memory for agents)
2. Long-context reasoning and revisitable memory
3. Retrieval-augmented reasoning (not only retrieval-augmented generation)
4. Multi-modal memory for agents (vision-language-action)
5. RL for tool-using / planning agents

## Secondary Interests
- Scientific literature understanding and automation
- Efficient memory compression, indexing, replay, and forgetting
- Test-time compute × memory interaction
- Training-time curriculum for memory capabilities

## Priority Sources
- arXiv: cs.CL, cs.AI, cs.LG, cs.CV
- HuggingFace Daily Papers (prefer to keep strong coverage)
- Top venues: NeurIPS / ICLR / ICML / ACL / EMNLP / CVPR

## Preferred Paper Signals
- Clear problem framing + strong motivation
- Solid experimental design with ablations
- Practical insights beyond benchmark score gains
- Strong analysis of failure cases
- Reproducibility signals (code/data/training details)
- Positioning against closest baselines (not only weak ones)

## De-prioritize (unless unusually strong)
- Pure benchmark-chasing without insight
- Incremental architecture tweaks with weak analysis
- Heavy claims with limited evidence
- Missing reproducibility details or opaque evaluation

## Reading Output Standard
For each paper note, include:
- 3-sentence summary
- Core novelty
- Method sketch
- Key results + caveats
- Relevance to ongoing projects
- 2–3 follow-up ideas

## Scoring Rubric (100)
- Relevance to current research: 40
- Technical novelty: 20
- Experimental rigor: 20
- Actionability (can influence current work soon): 15
- Clarity / reproducibility: 5

### Quick Triage Rule
- **A-tier (>=80)**: deep read this week
- **B-tier (65–79)**: keep in near backlog
- **C-tier (<65)**: skim only unless topic urgency changes

## Balance Constraint
When generating daily picks, avoid source collapse:
- keep at least ~30% from HuggingFace Daily Papers when candidate quality is comparable
- avoid all-venue domination by a single source

## Output Tone Preference
- concise, technical, non-marketing
- avoid fluffy AI-style phrasing
- prefer concrete claims with evidence pointers
