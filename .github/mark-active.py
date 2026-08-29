#!/usr/bin/env python3
"""Ставит пометку *(активен)* напротив нужного варианта в .github/variants/README.md."""
import re, sys, pathlib

variant = sys.argv[1]
p = pathlib.Path(__file__).parent / "variants" / "README.md"
s = p.read_text(encoding="utf-8")

s = s.replace(" *(активен)*", "")
link = f"[`{variant}.md`]"
new, n = re.subn(
    r"(" + re.escape(link) + r"\([^)]*\))",
    r"\1 *(активен)*",
    s,
    count=1,
)
if n == 0:
    sys.exit(f"не нашёл ссылку {link} в {p}")
p.write_text(new, encoding="utf-8")
print(f"активен: {variant}")
