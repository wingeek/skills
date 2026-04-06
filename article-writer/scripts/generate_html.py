# -*- coding: utf-8 -*-
import sys
import io

# 设置标准输出编码为UTF-8 (Windows兼容)
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from mdnice import to_wechat

md_path = r'C:\Users\neychang\workspace\dev-docs\docs\rfc\idea\2026-01-17-文章发布skill\posts\2026-01-24\article.md'
output_dir = r'C:\Users\neychang\workspace\dev-docs\docs\rfc\idea\2026-01-17-文章发布skill\posts\2026-01-24'

print("正在生成微信公众号HTML...")
to_wechat(md_path, theme='rose', output_dir=output_dir)
print("完成！")
