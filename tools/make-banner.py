#!/usr/bin/env python3
"""
Генератор анимированного SVG-баннера «Сэмбонзакура Кагэёси».

    python3 tools/make-banner.py "ИМЯ" "ПОДПИСЬ" > assets/banner.svg

Всё рисуется тегами <animate>/<animateTransform> — GitHub отдаёт SVG как есть,
анимация играет прямо в README. Внешних запросов нет, ломаться нечему.
"""
import random, sys

NAME = sys.argv[1] if len(sys.argv) > 1 else "YOUR NAME"
SUB  = sys.argv[2] if len(sys.argv) > 2 else "PYTHON · FASTAPI · AI ENGINEERING"
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 20260829

W, H = 1200, 300
rnd = random.Random(SEED)
out = []

out.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{NAME}">
  <defs>
    <linearGradient id="night" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#120a1c"/>
      <stop offset="55%"  stop-color="#1e0f2b"/>
      <stop offset="100%" stop-color="#08050e"/>
    </linearGradient>
    <radialGradient id="bloom" cx="50%" cy="55%" r="62%">
      <stop offset="0%"   stop-color="#f472b6" stop-opacity="0.42"/>
      <stop offset="45%"  stop-color="#be185d" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="blade" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%"   stop-color="#fbcfe8" stop-opacity="0"/>
      <stop offset="35%"  stop-color="#f9a8d4" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#ec4899" stop-opacity="0"/>
      <stop offset="50%"  stop-color="#fbcfe8" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#ec4899" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="48%"  stop-color="#fce7f3" stop-opacity="0.8"/>
      <stop offset="56%"  stop-color="#f472b6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow" x="-70%" y="-70%" width="240%" height="240%">
      <feGaussianBlur stdDeviation="9"/>
    </filter>
    <filter id="glow2" x="-70%" y="-70%" width="240%" height="240%">
      <feGaussianBlur stdDeviation="2.5"/>
    </filter>
    <clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}"/></clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="url(#night)"/>
    <rect width="{W}" height="{H}" fill="url(#bloom)">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="8s" repeatCount="indefinite"/>
    </rect>

    <circle cx="1050" cy="66" r="52" fill="#fbcfe8" opacity="0.12" filter="url(#glow)"/>
    <circle cx="1050" cy="66" r="27" fill="#fdf2f8" opacity="0.9">
      <animate attributeName="opacity" values="0.9;0.62;0.9" dur="9s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1064" cy="57" r="24" fill="#120a1c"/>
''')

# --- 千本桜景厳: клинки, поднимающиеся из земли ---
out.append('    <g>')
for i in range(46):
    x = 8 + i * 26 + rnd.randint(-6, 6)
    h = rnd.randint(52, 128)
    dur = round(rnd.uniform(3.4, 7.2), 2)
    beg = round(rnd.uniform(0, dur), 2)   # отрицательный begin ниже
    w = rnd.choice([2, 2, 3, 4])
    out.append(
        f'      <rect x="{x}" y="{H}" width="{w}" height="{h}" fill="url(#blade)" opacity="0">'
        f'<animate attributeName="y" values="{H};{H-h-14}" dur="{dur}s" begin="{beg}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0;0.85;0" dur="{dur}s" begin="{beg}s" repeatCount="indefinite"/></rect>'
    )
out.append('    </g>')

# --- падающие лепестки сакуры ---
PETAL = "M0 0 C 3 -5.5, 9.5 -6.5, 12.5 -0.5 C 9.5 6, 3 5, 0 0 Z"
out.append('    <g>')
for i in range(38):
    x0 = rnd.randint(-40, W)
    drift = rnd.randint(-150, 90)
    dur = round(rnd.uniform(7, 17), 2)
    beg = round(rnd.uniform(0, dur), 2)   # отрицательный begin ниже:
    # на нулевой секунде лепестки уже распределены по всему кадру
    s = round(rnd.uniform(0.45, 1.25), 2)
    rot = round(rnd.uniform(2.2, 6.5), 2)
    op = round(rnd.uniform(0.35, 0.95), 2)
    col = rnd.choice(["#fbcfe8", "#f9a8d4", "#f472b6", "#fde7f3", "#ffffff"])
    # часть лепестков без анимации прозрачности: иначе в статичных превью
    # (где SMIL не проигрывается) баннер выглядит пустым
    fade = (
        f'<animate attributeName="opacity" values="0;{op};{op};0" keyTimes="0;0.12;0.8;1"'
        f' dur="{dur}s" begin="-{beg}s" repeatCount="indefinite"/>'
        if i % 5 < 3 else ""
    )
    out.append(f'''      <g transform="translate({x0},-40)">
        <animateTransform attributeName="transform" type="translate" values="{x0},-40; {x0+drift},{H+40}" dur="{dur}s" begin="-{beg}s" repeatCount="indefinite"/>
        <g transform="scale({s})">
          <path d="{PETAL}" fill="{col}" opacity="{op}">
            <animateTransform attributeName="transform" type="rotate" values="0;360" dur="{rot}s" repeatCount="indefinite"/>
            {fade}
          </path>
        </g>
      </g>''')
out.append('    </g>')

esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
out.append(f'''
    <text x="46" y="92" font-family="'Hiragino Mincho ProN','Yu Mincho',serif" font-size="25" fill="#f9a8d4" opacity="0.34" writing-mode="tb">千本桜景厳</text>

    <text x="600" y="150" text-anchor="middle" font-family="'Trebuchet MS',Verdana,Geneva,sans-serif"
          font-size="54" font-weight="bold" letter-spacing="11" fill="#fdf2f8" filter="url(#glow2)" opacity="0.55">{esc(NAME)}</text>
    <text x="600" y="150" text-anchor="middle" font-family="'Trebuchet MS',Verdana,Geneva,sans-serif"
          font-size="54" font-weight="bold" letter-spacing="11" fill="#ffffff">{esc(NAME)}</text>
    <text x="600" y="184" text-anchor="middle" font-family="'Trebuchet MS',Verdana,Geneva,sans-serif"
          font-size="16" letter-spacing="5.5" fill="#f9a8d4" opacity="0.95">{esc(SUB)}
      <animate attributeName="opacity" values="0.95;0.6;0.95" dur="6s" repeatCount="indefinite"/>
    </text>

    <g transform="skewX(-14)">
      <rect x="-380" y="-40" width="160" height="400" fill="url(#sweep)" opacity="0.45" filter="url(#glow2)">
        <animate attributeName="x" values="-380;-380;1460;1460" keyTimes="0;0.55;0.8;1" dur="10s" repeatCount="indefinite"/>
      </rect>
    </g>

    <rect x="200" y="204" width="800" height="1.5" fill="url(#rule)" opacity="0.8">
      <animate attributeName="opacity" values="0.35;0.9;0.35" dur="5s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>''')

print("\n".join(out))
