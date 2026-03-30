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

Always generate introductions using this 7-section structure:

### 01. Skill Card (技能名片)

Create a quick-reference summary:

| Field | Content |
|-------|---------|
| **技能名称** | `Skill_Name` |
| **一句话定义** | [30-second elevator pitch describing core value] |
| **适用人群** | [Target user personas] |
| **技能评级** | ⭐⭐⭐⭐⭐ (rate based on complexity, accuracy, efficiency) |

### 02. Pain Points Comparison (痛点对标)

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

### 03. Core Logic & Workflow (核心逻辑与工作流)

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

### 04. Interface Specification (接口规范与参数)

Document inputs and outputs:

**Inputs:**
- `parameter_name`: Description (Required/Optional)

**Outputs:**
- `output_name`: Description and format

**Example:**
```markdown
**输入 (Inputs):**
- `document_url`: File URL (Required)
- `target_metrics`: Metrics to extract (Optional)

**输出 (Outputs):**
- `summary_report`: Text summary
- `data_chart`: Chart object
```

### 05. Real-World Case Study (真实用例展示)

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

### 06. Quick Start Guide (快速开始)

Provide two usage methods:

**方式一：在对话框中使用**
```
直接发送指令: "调用 [技能名]，参数为：[具体对象]"
```

**方式二：API/代码集成**
```python
# 示例代码块
agent.use_skill("Skill_Name", {
    "param1": "value1",
    "mode": "operation_mode"
})
```

### 07. Limitations & Pitfalls (局限性与避坑指南)

Be honest about boundaries:

```markdown
**不支持**:
- [Limitation 1]
- [Limitation 2]

**注意**:
- [Edge case warning 1]
- [Edge case warning 2]
```

### 08. Repository & Resources (仓库与资源)

Always include the skill's source location:

```markdown
## 📦 获取与资源

**仓库地址**: [GitHub 仓库链接或本地路径]
**技能目录**: `[skill-name]/`

**相关文件**:
- `SKILL.md` - 主技能文件
- `scripts/` - 辅助脚本（如有）
- `references/` - 参考文档（如有）
```

**Example:**
```markdown
## 📦 获取与资源

**仓库地址**: https://github.com/anthropics/skills/tree/main/skill-creator
**技能目录**: `skill-creator/`

**相关文件**:
- `SKILL.md` - 主技能文件
- `scripts/run_eval.py` - 评估运行脚本
- `scripts/package_skill.py` - 打包脚本
- `agents/` - 子代理指令
```

## Writing Principles

1. **可视化优先**: Use flowcharts/diagrams instead of long text
2. **结果导向**: Focus on outputs and value, not implementation details
3. **场景化**: Provide concrete, relatable scenarios
4. **诚实透明**: Acknowledge limitations upfront

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
3. **Generate each section** - Follow the 7-section template
4. **Add visual elements** - Mermaid diagrams, tables, formatting
5. **Review and refine** - Ensure clarity and completeness

## Example Invocation

When asked to generate an introduction for a skill:

```
用户: 帮我生成 skill-creator 的介绍文档

执行:
1. 读取 skill-creator/SKILL.md
2. 提取: name, description, workflow, inputs, outputs
3. 按模板生成 7 个部分
4. 输出完整的 Markdown 文档
```
