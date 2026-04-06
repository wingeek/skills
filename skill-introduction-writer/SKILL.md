---
name: skill-introduction-writer
description: Use when you need to generate a comprehensive introduction document for a SKILL. Triggers when the user asks to create, write, or generate an introduction, whitepaper, or promotional document for any skill or agent capability.
---

# Skill Introduction Writer

Generate professional, structured introduction documents for any SKILL following a standardized whitepaper template.

## Overview

This skill helps you create compelling introduction documents that explain what a skill does, why it's valuable, and how to use it. The output follows a professional whitepaper format optimized for technical audiences.

## When to Use

- Creating promotional materials for a skill
- Writing documentation for skill catalogs
- Generating whitepaper-style introductions
- Onboarding users to a new skill

## Template Structure

Always generate introductions using this 9-section structure:

**文档标题格式**: `# 📊 SKILL 介绍：skill-name（中文名称）`

> 选择与技能主题相关的 emoji：📊 图表、📘 论文、🔧 工具、🤖 AI、📝 文档、🔍 搜索

### 01. 技能名片 (At a Glance)

Create a quick-reference summary:

| 字段 | 内容 |
|:-----|:-----|
| **技能名称** | `Skill_Name` |
| **一句话定义** | [30-second elevator pitch describing core value] |
| **适用人群** | [Target user personas] |
| **技能评级** | ⭐⭐⭐⭐⭐（复杂度：低/中/高 | 准确度：高 | 实用性：极高） |

**注意**:
- 标题使用 emoji + 双语格式：`# 📊 SKILL 介绍：skill-name（中文名称）`
- 选择与技能主题相关的 emoji（如 📊 图表、📘 论文、🔧 工具、🤖 AI）

### 02. 痛点对标 (Why we need it)

Create a before/after comparison table:

| 现状 (Before) | 使用 SKILL 后 (After) |
|:--------------|:----------------------|
| [Manual pain point 1] | [Automated solution 1] |
| [Manual pain point 2] | [Automated solution 2] |
| [Manual pain point 3] | [Automated solution 3] |

**Guidelines:**
- List 3-5 concrete pain points
- Make comparisons specific and measurable
- Use time savings, error reduction, or quality improvements
- 章节标题格式：`## 02. 痛点对标 (Why we need it)`

### 03. 核心逻辑与工作流 (How it works)

Explain how the skill works internally:

**Workflow Diagram (Mermaid):**
```mermaid
graph LR
    Input(用户需求) --> Parser(解析器)
    Parser --> Thinking[逻辑拆解与推理]
    Thinking --> Tool[工具调用/API连接]
    Tool --> Summarizer(结果聚类)
    Summarizer --> Output(结构化输出)
```

**Four-Layer Architecture:**
1. **感知层 (Perception)**: How the skill parses input
2. **认知层 (Cognition)**: Core algorithm/prompt strategy
3. **行动层 (Action)**: External tools/APIs called
4. **反馈层 (Feedback)**: How results are refined

**Guidelines:**
- 章节标题格式：`## 03. 核心逻辑与工作流 (How it works)`
- 必须包含 Mermaid 工作流图
- 使用四层架构模板解释内部机制

### 04. 接口规范与参数 (The Specification)

Document inputs and outputs:

**输入 (Inputs):**

| 参数 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| `param_name` | string | ✅/❌ | 参数描述 |

**输出 (Outputs):**

| 字段 | 类型 | 说明 |
|:-----|:-----|:-----|
| `output_name` | file/string | 输出描述 |

**Example:**
```markdown
**输入 (Inputs):**

| 参数 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| `document_url` | string | ✅ | 文档 URL |
| `target_metrics` | list | ❌ | 需提取的指标 |

**输出 (Outputs):**

| 字段 | 类型 | 说明 |
|:-----|:-----|:-----|
| `summary_report` | file | 分析报告文件 |
| `data_chart` | image | 数据图表 |
```

**Guidelines:**
- 章节标题格式：`## 04. 接口规范与参数 (The Specification)`
- 使用表格格式而非列表，更清晰
- 必填用 ✅，可选用 ❌

### 05. 真实用例展示 (Case Study)

Show a complete example:

```markdown
**用户输入**: "[Actual user request]"

**SKILL 执行过程**:
1. [Step 1 description]
2. [Step 2 description]
3. [Step 3 description]

**技能输出展示**:
> [Simulated output or screenshot placeholder]
> **分析结论**: [Key finding from the output]
```

**Guidelines:**
- 章节标题格式：`## 05. 真实用例展示 (Case Study)`
- 必须包含完整的执行过程描述
- 输出展示使用引用块 `>` 格式

### 06. 快速开始 (Quick Start)

Provide two usage methods:

**方式一：在对话框中使用**
```
直接发送指令: "调用 [技能名]，参数为：[具体对象]"
```

**方式二：触发词**
```
以下表述会自动触发技能：
- "[关键词1]"、"[关键词2]"
- 分享特定类型的链接或文件
```

**方式三：指定配置参数**
```
"创建 [配置] 的 [图表类型]，展示 [具体内容]"
```

**Guidelines:**
- 章节标题格式：`## 06. 快速开始 (Quick Start)`
- 提供多种使用方式，降低上手门槛
- 包含触发词说明，帮助用户了解自动触发条件

### 07. 局限性与避坑指南 (Boundary)

Be honest about boundaries:

```markdown
**不支持**:
- ❌ [Limitation 1]
- ❌ [Limitation 2]

**注意**:
- ⚠️ [Edge case warning 1]
- ⚠️ [Edge case warning 2]

**常见问题**:

| 问题 | 解决方案 |
|:-----|:---------|
| [常见问题 1] | [解决方案 1] |
| [常见问题 2] | [解决方案 2] |
```

**Guidelines:**
- 章节标题格式：`## 07. 局限性与避坑指南 (Boundary)`
- 不支持项用 ❌，注意事项用 ⚠️
- 添加常见问题表格，提供故障排除指引

### 08. 仓库与资源 (Repository & Resources)

Always include the skill's source location:

```markdown
**GitHub 地址**: [GitHub 仓库链接]
**本地路径**: `[local-path]/`

**相关文件**:

| 文件 | 说明 |
|:-----|:-----|
| `SKILL.md` | 主技能文件 |
| `scripts/` | 辅助脚本（如有） |
| `references/` | 参考文档（如有） |
```

**Guidelines:**
- 章节标题格式：`## 08. 仓库与资源 (Repository & Resources)`
- 使用表格列出相关文件
- 同时提供 GitHub 地址和本地路径

### 09. 总结 (Summary)

End with a memorable summary:

```markdown
## 总结

**[skill-name] 是给"[目标用户]"用的[技能类型]** —— [核心定位，不是为了 X，是为了 Y]。

核心价值：
- 🎯 **[价值点1]**：[具体说明]
- 🧠 **[价值点2]**：[具体说明]
- 🔧 **[价值点3]**：[具体说明]
- 📝 **[价值点4]**：[具体说明]

**一句话：[核心 Slogan，让人记住这个技能]**
```

**Guidelines:**
- 必须包含一句话定位
- 核心价值用 emoji + 粗体标题 + 说明的格式
- Slogan 要简洁有力，突出差异化价值

---

## Writing Principles

1. **标题格式统一**: 所有章节使用双语格式 `## 01. 中文名 (English Name)`
2. **表格左对齐**: 使用 `|:-----|:-----|` 而非 `|-------|---------|`
3. **可视化优先**: 用 Mermaid 图替代长文本说明
4. **结果导向**: 聚焦输出和价值，而非实现细节
5. **场景化**: 提供具体、可关联的使用场景
6. **诚实透明**: 前置说明局限性和边界
7. **Emoji 点缀**: 标题和重点处适度使用，但不滥用
8. **中文优先**: 面向中文用户，中文在前，英文补充

## Output Format

Generate output in Markdown format with:
- Clear section headers
- Tables for comparisons
- Mermaid diagrams for workflows
- Code blocks for examples
- Blockquotes for key outputs

## Generation Process

1. **Analyze the target skill** - Read its SKILL.md to understand purpose and workflow
2. **Extract key information** - Name, description, inputs, outputs, workflow
3. **Generate each section** - Follow the 9-section template
4. **Add visual elements** - Mermaid diagrams, tables, emoji
5. **Format consistently** - 双语标题、左对齐表格、引用块输出
6. **Review and refine** - Ensure clarity and completeness

## Example Invocation

When asked to generate an introduction for a skill:

```
用户: 帮我生成 skill-creator 的介绍文档

执行:
1. 读取 skill-creator/SKILL.md
2. 提取: name, description, workflow, inputs, outputs
3. 按模板生成 9 个部分
4. 输出完整的 Markdown 文档
```
