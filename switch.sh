#!/usr/bin/env bash
# Быстрое переключение варианта оформления профиля.
#   ./switch.sh            — показать список и выбрать
#   ./switch.sh A          — включить вариант A сразу
set -euo pipefail
cd "$(dirname "$0")"

declare -a files=(.github/variants/[A-Z]*-*.md)

pick=""
if [ $# -ge 1 ]; then
  for f in "${files[@]}"; do
    case "$(basename "$f")" in "$1"*|"$1".md) pick="$f"; break;; esac
  done
  [ -n "$pick" ] || { echo "Нет варианта '$1'."; exit 1; }
else
  echo "Доступные варианты:"
  select f in "${files[@]}"; do pick="$f"; break; done
  [ -n "$pick" ] || exit 1
fi

cp "$pick" README.md
sed -i '' -E 's/ \*\(активен\)\*//' .github/variants/README.md 2>/dev/null \
  || sed -i -E 's/ \*\(активен\)\*//' .github/variants/README.md
name="$(basename "$pick")"
sed -i '' -E "s#\[\`${name}\`\]#[\`${name}\`] *(активен)*#" .github/variants/README.md 2>/dev/null \
  || sed -i -E "s#\[\`${name}\`\]#[\`${name}\`] *(активен)*#" .github/variants/README.md

if git diff --quiet; then echo "Вариант $name уже активен."; exit 0; fi
git commit -qam "Switch profile variant to ${name%.md}"
git push -q
echo "Готово — активен $name. Обнови https://github.com/Zishwhwhw"
