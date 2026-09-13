from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

T = {
 "dark":  dict(bg1="#12091f", bg2="#0a1622", card="#161b22", line="#26303b", name="#f0f6fc",
               sub="#22d3ee", mute="#8b949e", dot="#8B5CF6", a1="#8B5CF6", a2="#06B6D4",
               g1="#ff5f57", g2="#febc2e", g3="#28c840", code1="#c792ea", code2="#7fdbca"),
 "light": dict(bg1="#f2edff", bg2="#e8f6fb", card="#ffffff", line="#d8dee6", name="#161b22",
               sub="#0891b2", mute="#59636e", dot="#8B5CF6", a1="#8B5CF6", a2="#06B6D4",
               g1="#ff5f57", g2="#febc2e", g3="#28c840", code1="#8250df", code2="#0f766e"),
}
MONO = "JBMono,ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "JBMono,ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

def build(t):
    c = T[t]
    dotop = ".16" if t == "dark" else ".13"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 240" width="1000" height="240">
<defs>
  <style>@font-face{{font-family:JBMono;font-weight:400;src:url(data:font/woff2;base64,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) format("woff2")}}@font-face{{font-family:JBMono;font-weight:800;src:url(data:font/woff2;base64,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) format("woff2")}}</style>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{c['bg1']}"/><stop offset="100%" stop-color="{c['bg2']}"/>
  </linearGradient>
  <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{c['a1']}"/><stop offset="100%" stop-color="{c['a2']}"/>
  </linearGradient>
  <pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.6" fill="{c['dot']}" opacity="{dotop}"/>
  </pattern>
  <clipPath id="round"><rect width="1000" height="240" rx="14"/></clipPath>
</defs>

<g clip-path="url(#round)">
  <rect width="1000" height="240" fill="url(#bg)"/>
  <rect width="1000" height="240" fill="url(#dots)"/>
  <rect x="0" y="0" width="7" height="240" fill="url(#bar)"/>

  <text x="64" y="104" font-family="{SANS}" font-size="54" font-weight="800"
        fill="{c['name']}" letter-spacing="-1.5">Joy Mridha</text>
  <text x="66" y="142" font-family="{MONO}" font-size="19" fill="{c['sub']}">building things that run while I sleep</text>
  <text x="66" y="180" font-family="{MONO}" font-size="13.5" fill="{c['mute']}" letter-spacing=".6">Go &#183; Python &#183; TypeScript &#183; Agentic AI</text>

  <g transform="translate(676,42)">
    <rect width="268" height="156" rx="10" fill="{c['card']}" stroke="{c['line']}"/>
    <rect width="268" height="30" rx="10" fill="{c['line']}" opacity=".5"/>
    <rect y="20" width="268" height="10" fill="{c['line']}" opacity=".5"/>
    <circle cx="18" cy="15" r="5" fill="{c['g1']}"/>
    <circle cx="36" cy="15" r="5" fill="{c['g2']}"/>
    <circle cx="54" cy="15" r="5" fill="{c['g3']}"/>
    <text x="20" y="62" font-family="{MONO}" font-size="12.5" fill="{c['code2']}">$ ./joy --ship</text>
    <text x="20" y="86" font-family="{MONO}" font-size="12.5" fill="{c['mute']}">building...</text>
    <text x="20" y="110" font-family="{MONO}" font-size="12.5" fill="{c['code1']}">ok. sleeping now</text>
    <text x="20" y="134" font-family="{MONO}" font-size="12.5" fill="{c['code2']}">$ </text>
    <rect x="34" y="124" width="8" height="14" fill="{c['sub']}">
      <animate attributeName="opacity" values="1;1;0;0" dur="1.1s" repeatCount="indefinite"/>
    </rect>
  </g>
</g>
</svg>'''

for t in T:
    open(ROOT/f"assets/header-{t}.svg","w",newline="\n",encoding="utf-8").write(build(t))
    print(f"assets/header-{t}.svg")
