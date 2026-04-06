---
name: harness-practice-story
description: Use when analyzing and documenting AI-assisted engineering practices with Claude Code (Harness). Triggers when user wants to reflect on their Harness workflow, extract meta-lessons about AI collaboration patterns, identify effective prompting strategies, or write practice guides for leveraging AI in software engineering.
---

# Harness Practice Story Generator

Analyze Claude Code (Harness) session artifacts to extract **AI collaboration patterns**, **effective workflows**, and **engineering practice insights**. Focus on HOW to work effectively with AI, not just WHAT was built.

## Overview

**Core Principle:** The goal is not to document the technical solution, but to extract **meta-knowledge about AI-assisted engineering**—what works, what doesn't, and how to systematically improve human-AI collaboration.

## When to Use

**Use when:**
- Reflecting on Harness (Claude Code) usage patterns
- Extracting lessons about effective AI collaboration
- Analyzing what prompts/strategies worked well
- Identifying friction points in AI-assisted workflow
- Creating guides for team AI adoption
- Documenting "aha moments" in human-AI pairing

**Do NOT use for:**
- Technical documentation of the solution (use other skills)
- Code comments or API docs
- Feature announcements or release notes
- General project summaries without AI practice focus

## Key Perspective Shift

| ❌ Wrong Focus | ✅ Right Focus |
|----------------|----------------|
| "How we migrated to Babylon.js" | "How Harness helped us evaluate framework trade-offs" |
| "The camera sync algorithm" | "How we iterated on the solution with AI feedback" |
| "Architecture decisions" | "How we leveraged AI for systematic analysis" |
| "Code implementation details" | "Prompting patterns that produced good code" |
| "What was built" | "How we worked with AI to build it" |

## Artifact Sources

### 1. Conversation History
Location: `~/.claude/ide/` or project-specific session files

Contains: Full conversation transcripts with Claude, including:
- User prompts and context
- Claude responses and actions
- Tool invocations and results
- Error messages and resolutions

### 2. Memory Files
Location: `~/.claude/projects/{project-hash}/memory/`

Contains:
- `MEMORY.md` - Memory index
- `user*.md` - User preferences and patterns
- `feedback*.md` - Feedback memories
- `project*.md` - Project-specific memories
- `reference*.md` - External references

### 3. Plan Files
Location: Project directory, typically `**/plan*.md` or `.claude/plans/`

Contains:
- Implementation plans
- Task breakdowns
- Design decisions
- Progress tracking

### 4. Git History
Location: `.git/` in project root

Contains:
- Commit messages
- Branch patterns
- Merge history
- Code evolution

### 5. CLAUDE.md
Location: Project root (`CLAUDE.md`)

Contains:
- Project background and AI working conventions
- Key architectural decisions (often AI-assisted)
- Commands and workflow conventions
- The best quick entry point for understanding how AI is used in the project

## Story Structure (AI-PRACTICE Framework)

### A - Approach (How did we engage AI?)
Document the human-AI collaboration pattern:
- What type of assistance was sought?
- How were prompts structured?
- What context was provided to AI?
- What iteration patterns emerged?

### I - Insights (What did AI reveal?)
Knowledge gained through AI interaction:
- What analysis did AI provide that we hadn't considered?
- What connections did AI make between concepts?
- What trade-offs did AI identify?
- What alternatives did AI suggest?

### P - Pain Points (Where did AI struggle?)
Honest assessment of limitations:
- What required multiple iterations?
- What context was missing?
- Where did AI go down wrong paths?
- What required human intervention?

### R - Refinement (How did we improve the process?)
Process optimization lessons:
- What prompt patterns worked best?
- How did we provide better context over time?
- What verification strategies were effective?
- How did we balance AI suggestions vs human judgment?

### A - Artifacts (What Harness features helped?)
Harness-specific capabilities leveraged:
- Skills used and their effectiveness
- Memory system utility (see Memory Analysis Guidance below)
- Plan/mode workflow benefits
- MCP tool integrations

#### Memory System Analysis Guidance

Memory files are often the **highest information density** artifacts — more revealing than plan files or git history for understanding AI collaboration patterns.

**Analysis dimensions:**
- **Volume & type distribution**: feedback vs project vs reference ratio reflects collaboration maturity. Many feedback memories = active learning loop; mostly project memories = progress tracking; no memories = one-shot interactions.
- **"Why" field quality**: Good memories explain *why* something works/fails, not just *what* happened. The "Why" enables future judgment on whether the memory still applies.
- **Write triggers**: When were memories created? After breakthroughs? After mistakes? Proactive write patterns indicate mature AI collaboration habits.
- **Cross-memory patterns**: Look for chains of related memories (e.g., a sequence of feedback entries showing iterative problem-solving). These reveal how the human-AI pair evolved their approach.
- **Cross-session reuse**: Which memories would actually help in a new session? Memories that are too specific (file paths, exact API calls) decay faster than ones capturing principles.

### C - Collaboration (What human-AI patterns worked?)
Effective pairing patterns:
- When to trust AI vs verify
- How to guide without over-specifying
- Balance of exploration vs execution
- Documentation practices during AI work

### T - Takeaways (What should we remember?)
Actionable lessons for future:
- Prompt templates that worked
- Workflow improvements identified
- Tool feature requests
- Team adoption recommendations

### E - Evolution (How can we improve?)
Future improvement areas:
- Skills to develop
- Context to capture
- Verification to automate
- Knowledge to preserve

## Input Format

When invoking this skill, provide:

```
Project directory: [path to project]
Focus areas: [optional: specific topics to emphasize]
Output format: [markdown/blog post/technical report]
Target audience: [team/public/personal]
```

## Output Template

```markdown
# [Project Name]: Harness 工程实践总结

> **Project**: [Project Name] — [GitHub URL]
> **Coding Agent**: [e.g. Claude Code / Cursor / Copilot]
> **LLM Model**: [e.g. Claude Opus 4.6 / GLM-5.1 / GPT-4o]

## 概要
[2-3句话：项目背景 + 核心AI协作模式 + 关键收获]

## 项目度量

| 指标 | 数值 |
|------|------|
| Memory 文件数 | N (feedback: N, project: N, reference: N) |
| Plan 文件规模 | N 行 / N 个阶段 |
| 关键架构转向次数 | N |
| 有效提示模式数 | N |
| 主要痛点数 | N |

*(Quantitative metrics enable cross-project comparison and track AI collaboration maturity over time.)*

## AI协作模式

### 介入方式
[如何启动AI辅助？什么阶段引入？]

### 提示策略
[有效的提示模式，上下文提供方式]

### 迭代模式
[如何与AI迭代改进？验证循环]

## 关键洞察

### AI揭示的分析
[AI提供了哪些有价值的分析/对比/建议]

### 意外发现
[AI带来的意料之外的价值]

### 思维扩展
[AI如何帮助拓展思考边界]

## 痛点与局限

### 多轮迭代场景
[哪些任务需要反复调整？]

### 上下文缺失
[AI缺少什么信息导致偏离？]

### 幻觉与验证
[需要人工验证的环节]

## Harness功能利用

### Skills与工具
[使用了哪些技能/MCP工具？效果如何？]

### Memory系统
[记忆机制的帮助与局限，参考 Memory System Analysis Guidance]

### Plan模式
[规划-执行分离的效果]

## 协作与信任

### 信任与验证平衡
[何时信任AI，何时必须验证——按场景分类]

### 探索vs执行
[AI在探索和执行阶段的不同作用]

### 知识沉淀
[如何将AI交互转化为持久知识——Memory/Plan/CLAUDE.md 的角色分工]

## 改进建议

### 提示模式优化
[未来可复用的提示模板]

### 工作流与技能
[流程优化建议 + 需要开发的新技能]

### 团队推广建议
[如何让团队更好地使用Harness]

## 附录：关键提示词记录
[记录有效的提示词示例]
```

## Analysis Process

1. **Gather Artifacts**
   - CLAUDE.md (project context and AI working conventions — read this first)
   - Memory files (start with MEMORY.md index, then read individual files by type)
   - Plan files (how tasks were structured)
   - Git history (what was actually committed)
   - Conversation history (human prompts + AI responses)

2. **Extract AI Collaboration Patterns**
   - Prompt structure analysis
   - Context provision strategies
   - Iteration and correction cycles
   - Decision-making moments (human vs AI led)

3. **Identify Meta-Lessons**
   - What prompting approaches worked?
   - What context was missing?
   - Where did AI excel vs struggle?
   - What Harness features were most valuable?

4. **Synthesize Practice Guide**
   - Actionable recommendations
   - Reusable prompt templates
   - Workflow improvements
   - Skill development opportunities

## Quality Checklist

- [ ] Focus on AI collaboration patterns, not just technical content
- [ ] Includes specific prompt examples that worked
- [ ] Documents both successes and failures honestly
- [ ] Identifies actionable improvements for future AI work
- [ ] References Harness-specific features used
- [ ] Provides recommendations for team adoption
- [ ] Extracts reusable patterns, not just project-specific observations

## Red Flags - STOP

- Writing only about technical solution, ignoring AI collaboration patterns
- No mention of prompting strategies or context provision
- Skipping the "what didn't work" section
- Generic advice without specific Harness feature references
- No actionable recommendations for future AI work
- Missing specific prompt examples
- No analysis of memory file content or patterns (when memory files exist)
- Treating memory files as just "notes" rather than AI collaboration artifacts
- Listing all memories individually instead of extracting cross-cutting patterns
- Missing analysis of memory write triggers (when/why memories were created)
- Skipping CLAUDE.md when it exists in the project

**If you catch yourself doing these, refocus on AI collaboration patterns.**

## Common Rationalizations to Avoid

| Excuse | Reality |
|--------|---------|
| "The plan file only has technical content" | Extract the meta-pattern: HOW was AI used to create this analysis? |
| "There's no conversation history" | Analyze the plan structure itself - what does it reveal about AI-assisted planning? |
| "This is a new project with no AI interaction yet" | Analyze how the plan COULD leverage AI, identify gaps |
| "I'll just summarize what was built" | That's technical documentation, not AI practice analysis |
| "Memory files are just notes" | They encode AI collaboration patterns — when/why they were written reveals workflow habits |
| "There are too many memory files to analyze" | Read MEMORY.md index first, then group by type and extract cross-cutting patterns |

## Handling Limited Artifacts

If only plan files exist (no conversation history):

1. **Analyze the planning process**: How was AI used to structure the analysis?
2. **Extract prompt patterns**: What questions does the plan answer? What prompts might have generated this?
3. **Identify AI-friendly structures**: Tables, comparisons, systematic analysis - these are AI outputs
4. **Document what's missing**: What conversation context would add value?

## Handling Rich Artifacts

When you have many memory/feedback files, detailed plans, and CLAUDE.md:

1. **Read MEMORY.md index first** — it's a summary directory of all memories, helping you quickly identify focus areas
2. **Group by type for analysis** — feedback files reveal pain points, project files reveal progress, reference files reveal toolchain. Don't read them all linearly.
3. **Find patterns, don't list items** — don't enumerate each memory individually; extract cross-cutting collaboration patterns (e.g., "3 feedback entries trace an iterative GL context debugging chain")
4. **Note inter-memory relationships** — look for sequences where one memory leads to the next (e.g., `feedback_gl_context` → `feedback_overlay_mode` → `feedback_coordinates` forming a progressive problem-solving chain)
5. **Start with CLAUDE.md** — it provides the architectural context that makes memory content meaningful. Read it before individual memories.

## Example Usage

```
Analyze my react-babylon-map project from Harness practice perspective.

Project directory: C:\Users\neychang\workspace\react-babylon-map
Focus: How was AI used for technical analysis and planning?
Output: Practice summary for team sharing
```

## Tips for Quality Practice Summaries

1. **Focus on Process, Not Just Product**: The goal is understanding HOW to work with AI
2. **Extract Prompt Patterns**: What types of prompts produced good results?
3. **Document Friction**: Where did AI struggle? What context was missing?
4. **Be Honest About Limitations**: Include iterations that went off track
5. **Make Recommendations Actionable**: Future projects should benefit from these lessons
