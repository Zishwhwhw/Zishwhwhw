# Варианты оформления профиля

Активный README лежит в корне репозитория. Здесь — все версии целиком.
GitHub рендерит эти `.md` прямо на месте, так что можно кликнуть и посмотреть вариант
живьём, прежде чем включать.

| Вариант | Файл | Настроение |
| :-- | :-- | :-- |
| **AB — Kyōka Terminal** | [`AB-kyoka-terminal.md`] *(активен)*(AB-kyoka-terminal.md) | Совмещённый: баннер, гифки и сетка «Эспады» из A + neofetch, `career.log` и `./contact.sh` из B |
| **A — Kyōka Suigetsu** | [`A-kyoka-suigetsu.md`](A-kyoka-suigetsu.md) | Java-класс вместо «About me», опыт простым блоком, без терминальной подачи |
| **B — Hōgyoku Terminal** | [`B-hogyoku-terminal.md`](B-hogyoku-terminal.md) | Чистый терминал: минимум гифок, pin-карточки вместо карточек-описаний |

## Как переключить

**Из браузера, за три клика** — вкладка [Actions → Switch profile variant](../../actions/workflows/switch-variant.yml) →
`Run workflow` → выбрать вариант в выпадающем списке → `Run`.
Работает и с телефона, терминал не нужен.

**Из терминала:**

```bash
./switch.sh          # список с выбором по номеру
./switch.sh A        # включить вариант A сразу
```

Скрипт сам подменяет `README.md`, обновляет пометку «активен» в этой таблице,
коммитит и пушит. Ничего не теряется: каждый вариант всегда лежит здесь отдельным файлом.

## Что откуда берётся

| Виджет | Источник | Примечание |
| :-- | :-- | :-- |
| Шапка | `assets/banner.svg` | Самописный анимированный SVG, лежит в репозитории — не сломается |
| Печатающийся текст | `readme-typing-svg.demolab.com` | ✅ работает |
| Stats / top-langs / pin | `github-readme-stats.shion.dev` | Зеркало: официальный `…vercel.app` отдаёт 503 |
| Streak | `streak-stats.demolab.com` | Старый `…herokuapp.com` мёртв, не использовать |
| Змейка | GitHub Action `Platane/snk` → ветка `output` | Генерируется раз в сутки, хостится в этом же репозитории |
| Иконки стека | `skillicons.dev` | ✅ |
| Счётчик просмотров | `komarev.com/ghpvc` | ✅ |
| Гифки | `assets/*.gif` | Лежат в репозитории — не зависят от Tenor |

Не использованы (отдают `402 Payment Required`, деплои умерли):
`github-profile-trophy.vercel.app`, `github-readme-activity-graph.vercel.app`,
`github-readme-quotes.vercel.app`.
