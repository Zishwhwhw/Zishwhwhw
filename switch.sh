#!/usr/bin/env bash
# Быстрое переключение варианта оформления профиля.
#   ./switch.sh            — показать список и выбрать по номеру
#   ./switch.sh A          — включить вариант A сразу
set -euo pipefail
cd "$(dirname "$0")"

shopt -s nullglob
files=(.github/variants/[A-Z]*-*.md)
(( ${#files[@]} )) || { echo "Вариантов не найдено."; exit 1; }

pick=""
if [ $# -ge 1 ]; then
  for f in "${files[@]}"; do
    case "$(basename "$f")" in "$1"*) pick="$f"; break;; esac
  done
  [ -n "$pick" ] || { echo "Нет варианта '$1'. Доступны: ${files[*]##*/}"; exit 1; }
else
  echo "Доступные варианты:"
  select f in "${files[@]}"; do pick="${f:-}"; break; done
  [ -n "$pick" ] || exit 1
fi

name="$(basename "$pick" .md)"
cp "$pick" README.md
python3 .github/mark-active.py "$name"

if git diff --quiet; then echo "Вариант $name уже активен."; exit 0; fi
git commit -qam "Switch profile variant to $name"
git push -q
echo "Готово — активен $name. Обнови https://github.com/Zishwhwhw"
