# Варианты оформления профиля

Активный README лежит в корне репозитория. Здесь — альтернативные версии.
GitHub рендерит эти `.md` прямо здесь, так что можно просто кликнуть и посмотреть,
как выглядит вариант, прежде чем его включать.

| Вариант | Файл | Настроение |
| :-- | :-- | :-- |
| **A — Kyōka Suigetsu** | [`A-kyoka-suigetsu.md`](A-kyoka-suigetsu.md) | Кастомный анимированный SVG-баннер, гифки Айзена, Java-класс вместо «About me», сетка проектов «Эспада» |
| **B — Hōgyoku Terminal** *(активен)* | [`B-hogyoku-terminal.md`](B-hogyoku-terminal.md) | Монохромный терминал: neofetch, `career.log`, `ls ./projects`. Минимум гифок — самый «взрослый» под рекрутёров |
| **C — Soul Society** | [`C-soul-society.md`](C-soul-society.md) | Максимальный пафос: анимированная capsule-шапка, большие гифки, YAML-досье, шкалы силы, свёрнутый ростер Эспады |

## Как переключить

```bash
git clone git@github.com:Zishwhwhw/Zishwhwhw.git && cd Zishwhwhw
cp .github/variants/A-kyoka-suigetsu.md README.md   # или C-soul-society.md
git commit -am "switch profile variant" && git push
```

Текущий README при этом не теряется — он всегда лежит в истории git,
и каждый вариант дополнительно лежит здесь отдельным файлом.

## Что откуда берётся

| Виджет | Источник | Примечание |
| :-- | :-- | :-- |
| Шапка | `assets/banner.svg` | Самописный анимированный SVG, лежит в репозитории — не сломается |
| Печатающийся текст | `readme-typing-svg.demolab.com` | ✅ работает |
| Stats / top-langs / pin | `github-readme-stats.shion.dev` | Зеркало: официальный `…vercel.app` сейчас отдаёт 503 |
| Streak | `streak-stats.demolab.com` | Старый `…herokuapp.com` мёртв, не использовать |
| Змейка | GitHub Action `Platane/snk` → ветка `output` | Генерируется раз в сутки, хостится в этом же репозитории |
| Иконки стека | `skillicons.dev` | ✅ |
| Счётчик просмотров | `komarev.com/ghpvc` | ✅ |
| Гифки | `assets/*.gif` | Лежат в репозитории — не зависят от Tenor |

Не использованы (отдают `402 Payment Required`, деплои умерли):
`github-profile-trophy.vercel.app`, `github-readme-activity-graph.vercel.app`,
`github-readme-quotes.vercel.app`.
