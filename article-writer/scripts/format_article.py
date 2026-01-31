#!/usr/bin/env python3
"""
Article Formatter using mdnice

This script formats Markdown articles for different platforms.
Usage: python format_article.py --article article.md --platform wechat --theme rose
"""

import argparse
import io
import sys
from pathlib import Path

# 设置标准输出编码为UTF-8 (Windows兼容)
# 必须在导入 mdnice 之前执行，否则会遇到 emoji 输出的 GBK 编码错误
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_article(article_path: str, platform: str = "wechat",
                   theme: str = "rose", code_theme: str = "monokai",
                   output_dir: str = "output") -> str:
    """
    Format article for specified platform using mdnice.

    Args:
        article_path: Path to Markdown article
        platform: Target platform (wechat, zhihu, juejin)
        theme: Article theme
        code_theme: Code highlighting theme
        output_dir: Output directory

    Returns:
        Path to formatted HTML file
    """
    try:
        from mdnice import to_wechat, to_zhihu, to_juejin
    except ImportError:
        print("ERROR: mdnice not installed. Run: pip install mdnice")
        sys.exit(1)

    article = Path(article_path)
    if not article.exists():
        print(f"ERROR: Article not found: {article_path}")
        sys.exit(1)

    print(f"Formatting article: {article.name}")
    print(f"Platform: {platform}")
    print(f"Theme: {theme}")

    # Format based on platform
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    if platform == "wechat":
        html = to_wechat(
            str(article),
            theme=theme,
            code_theme=code_theme,
            mac_style=True,
            output_dir=str(output_path)
        )
    elif platform == "zhihu":
        html = to_zhihu(
            str(article),
            theme=theme,
            code_theme=code_theme,
            output_dir=str(output_path)
        )
    elif platform == "juejin":
        html = to_juejin(
            str(article),
            theme=theme,
            code_theme=code_theme,
            output_dir=str(output_path)
        )
    else:
        print(f"ERROR: Unsupported platform: {platform}")
        sys.exit(1)

    # Find generated file
    generated_files = list(output_path.glob(f"{article.stem}_*.html"))
    if generated_files:
        output_file = generated_files[0]
        print(f"SUCCESS: Article formatted: {output_file}")
        return str(output_file)
    else:
        print(f"SUCCESS: Article formatted successfully")
        return ""


def list_themes():
    """List available themes"""
    try:
        from mdnice import MarkdownConverter
    except ImportError:
        print("ERROR: mdnice not installed. Run: pip install mdnice")
        sys.exit(1)

    print("\nArticle Themes:")
    for theme in MarkdownConverter.AVAILABLE_THEMES:
        name = MarkdownConverter.THEME_NAMES.get(theme, theme)
        print(f"  - {theme}: {name}")

    print("\nCode Themes:")
    for theme in MarkdownConverter.AVAILABLE_CODE_THEMES:
        config = MarkdownConverter.CODE_THEME_CONFIG[theme]
        print(f"  - {theme}: {config['name']}")


def main():
    parser = argparse.ArgumentParser(description="Format article for publishing platforms")
    parser.add_argument("--article", "-a", help="Path to Markdown article")
    parser.add_argument("--platform", "-p", default="wechat",
                       choices=["wechat", "zhihu", "juejin"],
                       help="Target platform")
    parser.add_argument("--theme", "-t", default="rose",
                       help="Article theme")
    parser.add_argument("--code-theme", "-c", default="monokai",
                       help="Code highlighting theme")
    parser.add_argument("--output-dir", "-o", default="output",
                       help="Output directory")
    parser.add_argument("--list-themes", action="store_true",
                       help="List available themes and exit")

    args = parser.parse_args()

    if args.list_themes:
        list_themes()
        return

    if not args.article:
        print("ERROR: Please specify article path with --article")
        sys.exit(1)

    format_article(
        article_path=args.article,
        platform=args.platform,
        theme=args.theme,
        code_theme=args.code_theme,
        output_dir=args.output_dir
    )


if __name__ == "__main__":
    main()
