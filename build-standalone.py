#!/usr/bin/env python3
"""把 Artifact 版（無外框，平台會自己包）轉成可獨立部署的完整 HTML。
沒有 DOCTYPE 的裸檔案會讓瀏覽器進 quirks mode，WebKit 上尤其容易出問題。"""
import sys, pathlib

src, dst = sys.argv[1], sys.argv[2]
core = pathlib.Path(src).read_text(encoding='utf-8')

# <style>…</style> 之後就是 body 的內容
cut = core.index('</style>') + len('</style>')
head, body = core[:cut].strip(), core[cut:].strip()

# charset/viewport 已在 head 片段裡，不重複加
out = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
{head}
</head>
<body>
{body}
</body>
</html>
"""
pathlib.Path(dst).write_text(out, encoding='utf-8')
print(f"已生成 {dst}（{len(out.encode())} bytes）")
