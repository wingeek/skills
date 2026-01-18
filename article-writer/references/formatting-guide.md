# Article Formatting Guide

Complete guide for formatting articles using mdnice library.

## Installation

```bash
# Install mdnice
pip install mdnice

# Install Playwright browser (one-time setup)
playwright install chromium
```

## Basic Usage

### WeChat Official Account

```python
from mdnice import to_wechat

# Simple conversion
html = to_wechat('article.md')

# With custom theme
html = to_wechat(
    'article.md',
    theme='rose',
    code_theme='monokai',
    mac_style=True,
    output_dir='output/wechat'
)
```

### Other Platforms

```python
from mdnice import to_wechat, to_zhihu, to_juejin

# Zhihu
html_zhihu = to_zhihu('article.md', theme='geekBlack')

# Juejin
html_juejin = to_juejin('article.md', theme='scienceBlue')

# Multi-platform publishing
to_wechat('article.md', theme='rose', output_dir='output/wechat')
to_zhihu('article.md', theme='geekBlack', output_dir='output/zhihu')
to_juejin('article.md', theme='scienceBlue', output_dir='output/juejin')
```

## Article Themes (20 options)

| Theme Code | Chinese Name | Style | Best For |
|------------|-------------|-------|----------|
| `rose` | 蔷薇紫 | Elegant purple | Quality articles ⭐ |
| `geekBlack` | 极客黑 | Developer favorite | Tech blogs ⭐ |
| `scienceBlue` | 科技蓝 | Tech-focused | Tech articles ⭐ |
| `extremeBlack` | 极简黑 | B&W minimalist | Minimalist style |
| `blueMountain` | 前端之巅同款 | Professional | Technical sharing |
| `normal` | 默认主题 | Clean and simple | General articles |
| `shanchui` | 山吹 | Warm yellow | Cozy content |
| `fullStackBlue` | 全栈蓝 | Professional blue | Tech articles |
| `nightPurple` | 凝夜紫 | Deep purple | Deep analysis |
| `cuteGreen` | 萌绿 | Fresh green | Light reading |
| `orangeHeart` | 橙心 | Vibrant orange | Energetic content |
| `ink` | 墨黑 | Ink style | Artistic |
| `purple` | 姹紫 | Purple series | Fashion-forward |
| `green` | 绿意 | Green series | Fresh and natural |
| `cyan` | 嫩青 | Cyan series | Fresh and light |
| `wechatFormat` | WeChat-Format | WeChat official | Official accounts |
| `blueCyan` | 兰青 | Blue-cyan | Professional |
| `red` | 红绯 | Red series | Passionate |
| `blue` | 蓝莹 | Blue series | Steady and大气 |
| `simple` | 简 | Ultra simple | Minimalism |

## Code Themes (7 options)

| Theme Code | Theme Name | Style |
|------------|-----------|-------|
| `atom-one-dark` | Atom One Dark | Dark classic (default) ⭐ |
| `monokai` | Monokai | Classic Monokai ⭐ |
| `github` | GitHub | GitHub style |
| `vs2015` | VS2015 | Visual Studio style |
| `atom-one-light` | Atom One Light | Light classic |
| `xcode` | Xcode | Xcode editor style |
| `wechat` | WeChat | WeChat official style |

## Image Upload Configuration

### Custom Upload Function

```python
from mdnice import to_wechat

def upload_image(image_path: str) -> str:
    """Custom image upload handler"""
    # Your upload logic here
    # Return the uploaded image URL
    return "https://cdn.example.com/image.jpg"

html = to_wechat(
    'article.md',
    image_uploader=upload_image,
    image_upload_mode='local'  # Only upload local images
)
```

### Built-in Image Hosting

```python
from mdnice import to_wechat, create_smms_uploader

# SM.MS hosting
uploader = create_smms_uploader(token='YOUR_SMMS_TOKEN')
html = to_wechat(
    'article.md',
    image_uploader=uploader,
    image_upload_mode='all'  # Upload all images
)
```

**Upload Modes**:
- `'local'`: Only upload local images (default)
- `'remote'`: Only upload network images
- `'all'`: Upload all images

## Network Proxy Configuration

```python
from mdnice import to_wechat

# HTTP/HTTPS proxy
html = to_wechat(
    'article.md',
    proxy={
        'server': 'http://127.0.0.1:7890'
    }
)

# SOCKS5 proxy
html = to_wechat(
    'article.md',
    proxy={
        'server': 'socks5://127.0.0.1:1080'
    }
)

# Proxy with authentication
html = to_wechat(
    'article.md',
    proxy={
        'server': 'http://proxy.example.com:8080',
        'username': 'your_username',
        'password': 'your_password',
        'bypass': 'localhost,127.0.0.1,*.local'  # Bypass rules
    }
)
```

## Remote Browser Configuration

```python
from mdnice import to_wechat

# Connect to remote browser (e.g., browserless)
html = to_wechat(
    'article.md',
    browser_ws_endpoint='ws://localhost:3000',
    browser_token='your_secret_token'
)
```

## Advanced Options

```python
from mdnice import to_wechat

html = to_wechat(
    'article.md',
    theme='rose',
    code_theme='monokai',
    mac_style=True,
    output_dir='output',
    return_html=True,
    headless=True,
    wait_timeout=30,
    retry_count=3,
    clean_html=True,
    wrap_full_html=False
)
```

**Parameter Reference**:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `markdown` | str/Path/List | Required | Markdown content or file path |
| `theme` | str/List | `'normal'` | Article theme |
| `code_theme` | str | `'atom-one-dark'` | Code highlighting theme |
| `mac_style` | bool | `True` | Mac-style code blocks |
| `output_dir` | str/Path | `None` | Output directory |
| `return_html` | bool | `True` | Return HTML content |
| `headless` | bool | `True` | Headless browser mode |
| `wait_timeout` | int | `30` | Wait timeout (seconds) |
| `retry_count` | int | `1` | Retry count on failure |
| `clean_html` | bool | `True` | Clean editor markers |

## Error Handling

```python
from mdnice import to_wechat

def error_handler(error_msg: str, context: dict):
    """Custom error handler"""
    print(f"❌ Error: {error_msg}")
    print(f"📍 Stage: {context.get('stage')}")
    print(f"📄 Details: {context}")

html = to_wechat(
    'article.md',
    on_error=error_handler,
    retry_count=3
)
```

## Batch Conversion

```python
from mdnice import to_wechat

files = ['article1.md', 'article2.md', 'article3.md']

# Batch convert with random theme
html_list = to_wechat(
    files,
    theme='random',
    output_dir='output/batch'
)

print(f"Successfully converted {len(html_list)} files")
```

## Common Issues

### Timeout Errors

```python
# Increase timeout
html = to_wechat(
    'article.md',
    wait_timeout=60,  # Increase to 60 seconds
    retry_count=3     # Add retries
)
```

### Browser Installation

```bash
# Download Chromium browser
playwright install chromium

# With proxy
export HTTPS_PROXY=http://127.0.0.1:7890
playwright install chromium
```

### Image Upload Failures

```python
def safe_uploader(image_path: str) -> str:
    """Uploader with error handling"""
    try:
        url = your_upload_function(image_path)
        print(f"✅ Upload success: {url}")
        return url
    except Exception as e:
        print(f"⚠️ Upload failed: {e}, keeping original path")
        return image_path  # Return original on failure

html = to_wechat(
    'article.md',
    image_uploader=safe_uploader
)
```
