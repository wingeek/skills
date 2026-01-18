---
name: article-writer
description: Automated article writing and publishing for WeChat Official Accounts. Use when users need to: (1) Compile technology newsletters/digests from collected links and comments, (2) Generate structured reports following specific outline formats, (3) Format and beautify articles for WeChat platform, (4) Publish articles to WeChat via API, (5) Handle multi-platform publishing with format adaptation
license: MIT
---

# Article Writer - WeChat Publishing Skill

## Overview

This skill automates the creation and publication of technology newsletters and articles for WeChat Official Accounts. It handles content compilation, formatting, beautification, and API-based publishing.

## Core Workflow

### Step 1: Collect and Analyze Source Material

Gather all provided resources:
- Article links and URLs
- Commentary notes and insights
- Images and media files
- Target publication platform requirements

### Step 2: Generate Article Structure

Follow the technology newsletter outline structure in [references/newsletter-structure.md](references/newsletter-structure.md).

Key sections include:
1. **卷首语 (Editor's Note)** - Week's core theme and trends
2. **重磅头条 (Breaking News)** - Major industry updates
3. **深度好文 (Curated Articles)** - Quality article summaries
4. **开源宝藏 (Open Source)** - Tools and projects
5. **技术深度思考 (Deep Thoughts)** - Topic analysis
6. **碎片化资讯 (Quick Bites)** - Brief updates
7. **每周一词 (Tech Trivia)** - Educational content

### Step 3: Write Content with Value Triangle

Apply the three-dimensional value model when writing commentary:

1. **连接性 (Connectivity)**: Connect to historical context
   - Example: "This reminds me of XX technology from 10 years ago, essentially..."

2. **批判性 (Criticality)**: Provide balanced analysis
   - Example: "While it claims 10x performance improvement, in large-scale distributed scenarios it may face XX risks..."

3. **落地性 (Actionability)**: Give actionable advice
   - Example: "For small teams, I recommend waiting; for high-concurrency scenarios, start researching now..."

### Step 4: Format for Platform

#### WeChat Official Account Formatting

Use mdnice library for professional formatting:

```python
from mdnice import to_wechat

html = to_wechat(
    'article.md',
    theme='rose',              # Article theme
    code_theme='monokai',      # Code highlighting
    mac_style=True,            # Mac-style code blocks
    output_dir='output/wechat'
)
```

**Theme options**:
- `rose` - Elegant purple (recommended for quality articles)
- `geekBlack` - Developer favorite
- `scienceBlue` - Tech-focused
- 20+ themes available

**Platform-specific functions**:
- `to_wechat()` - WeChat Official Account
- `to_zhihu()` - Zhihu platform
- `to_juejin()` - Juejin platform

For advanced formatting options and image uploading, see [references/formatting-guide.md](references/formatting-guide.md).

### Step 5: Publish to WeChat

Use the provided publishing script to deploy via WeChat API:

```bash
python scripts/publish_wechat.py --article output/article_wechat.html
```

**Prerequisites**:
1. WeChat AppID and AppSecret
2. Server IP whitelisted in WeChat backend
3. Cover image (recommended <64KB)

**Publishing workflow**:
1. Get Access Token
2. Upload cover image (get thumb_media_id)
3. Create draft with article content
4. Publish draft (non-push, visible in history)

For API details and troubleshooting, see [references/wechat-api.md](references/wechat-api.md).

## Content Guidelines

### Title Templates

- **常规型**: 《技术周报第 52 期：GPT-5 传闻与 Vue 4.0 展望》
- **深度型**: 《本周硬核：从 Llama 3 源码看大模型长文本的极限》
- **争议型**: 《除了提效,AI 编程工具正在摧毁新人的底层能力吗?》
- **工具型**: 《告别 Docker?这 3 个开源项目正在重塑容器化流程》

### Writing Best Practices

- **Quality over quantity**: Each article should provide unique insights
- **Evidence-based claims**: Support assertions with data and examples
- **Reader-centric**: Answer "What does this mean for me?"
- **Balanced perspective**: Present multiple viewpoints on controversial topics
- **Actionable takeaways**: Include practical recommendations

## Troubleshooting

### Formatting Issues

If mdnice conversion fails:
- Check Markdown syntax validity
- Verify image paths and URLs
- Try alternative themes
- Increase timeout: `wait_timeout=60`

### Publishing Failures

Common causes:
- **Access Token expired**: Token有效期2小时,自动刷新机制
- **Cover image too large**: Optimize to <64KB
- **IP not whitelisted**: Add server IP to WeChat backend
- **Content review pending**: WeChat reviews content before publishing

For detailed error codes and solutions, see [references/troubleshooting.md](references/troubleshooting.md).

## Dependencies

**Required**:
- Python 3.10+
- mdnice: `pip install mdnice`
- Playwright browser: `playwright install chromium`

**Optional**:
- Image hosting service for automatic uploads
- Proxy configuration for network restrictions

## Quick Start Example

```bash
# 1. Create article from source material
# (Use the workflow in Step 1-3)

# 2. Format for WeChat
python -c "
from mdnice import to_wechat
to_wechat('article.md', theme='rose', output_dir='output')
"

# 3. Publish to WeChat
python scripts/publish_wechat.py \
  --article output/article_wechat.html \
  --cover cover.jpg \
  --title "技术周报第XX期"
```

## Advanced Features

For multi-platform publishing, batch processing, and custom workflows, see:
- [references/batch-publishing.md](references/batch-publishing.md) - Batch operations
- [references/multi-platform.md](references/multi-platform.md) - Cross-platform strategies
- [references/automation.md](references/automation.md) - CI/CD integration
