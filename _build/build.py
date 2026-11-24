# -*- coding: utf-8 -*-
import importlib
import i18n_src, os, json, posixpath, html, re
from content import *
from news import *

OUT = os.environ.get("SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
esc = html.escape

# overrides / extra strings
UI["ko"].update({"cta_contact": "프로젝트 문의", "con_h": "프로젝트 이야기부터 시작해 보세요",
 "trace_h": "요구사항에서 근거문서까지, 한 흐름으로",
 "trace_p": "위험, 요구사항, 검증 기록을 한 번 정리하고 모든 문서가 같은 근거를 쓰게 합니다. 문서가 늘어도 어긋나지 않고, 심사에서도 근거를 바로 찾을 수 있습니다.",
 "principles": [("하나의 체계", "품질경영시스템, 기술문서, 위험관리, 사용적합성, 사이버보안이 같은 위험과 요구사항을 공유합니다."),
                ("추적 가능한 근거", "각 요구사항이 어떤 위험통제와 검증 기록으로 이어지는지 확인할 수 있습니다."),
                ("심사까지 함께", "인증기관과 식약처의 질의, 보완 요청, 심사 지적사항 대응을 지원합니다.")],
 "learn": "자세히 보기",
 "tile_h": "어떤 서비스가 맞는지 모르겠다면", "tile_p": "제품과 목표 시장을 알려 주시면 필요한 범위를 함께 정리합니다.", "tile_a": "프로젝트 문의"})
UI["en"].update({"cta_contact": "Start a project", "con_h": "Let's start with your project",
 "trace_h": "From requirement to evidence, in one flow",
 "trace_p": "We organize risks, requirements and verification records once, so every document draws on the same evidence. Documents stay consistent as they grow, and reviewers can trace the evidence quickly.",
 "principles": [("One system", "QMS, technical documentation, risk management, usability and cybersecurity share the same risks and requirements."),
                ("Traceable evidence", "You can see which risk controls and verification records each requirement leads to."),
                ("With you through review", "We support questions, deficiency requests and audit findings from notified bodies and regulators.")],
 "learn": "Learn more",
 "tile_h": "Not sure which service fits?", "tile_p": "Tell us about your product and target markets, and we will define the scope together.", "tile_a": "Start a project"})

UI["ko"].update({"nd_points": "주요 내용", "nd_sources": "공식 출처", "nd_back": "규제 뉴스 목록으로", "nd_check": "확인할 점",
 "nd_related": "관련 서비스", "nd_more": "자세히 보기", "nd_ask": "이 주제로 문의하기", "nd_notice": "공식 발표를 요약한 참고 정보입니다. 법적 효력과 정확한 내용은 원문에 있습니다."})
UI["en"].update({"nd_points": "Key points", "nd_sources": "Official sources", "nd_back": "Back to Regulatory News", "nd_check": "Worth checking",
 "nd_related": "Related service", "nd_more": "Read more", "nd_ask": "Ask about this topic", "nd_notice": "A summary of official announcements for reference. The original documents are authoritative."})

import i18n_zh, i18n_ja
import i18n_es, i18n_pt, i18n_ru, i18n_fr, i18n_de
NEWLANG = (i18n_es, i18n_pt, i18n_ru, i18n_fr, i18n_de)  # news text falls back to English
from extra_services import EXTRA, STD_EXTRA
SERVICES.extend(EXTRA)
LANGS = ["ko", "en", "zh", "ja", "es", "pt", "ru", "fr", "de"]
UI["ko"]["hero_tag"] = "의료기기 규제 컨설팅"; UI["en"]["hero_tag"] = "Medical device regulatory consulting"; 
UI["ko"]["label"] = "한국어"; UI["en"]["label"] = "English"
UI["ko"]["h1"] = "의료기기 규제 대응을<br class='pc-br'> [[하나의 체계]]로 설계합니다"
UI["en"]["h1"] = "We design medical device compliance as [[one system]]"
for _m, _hl in ((i18n_zh, "一个完整体系"), (i18n_ja, "ひとつの体系")):
    UI[_m.LANG] = dict(_m.UI)
for _m in NEWLANG: UI[_m.LANG] = dict(_m.UI)
UI["zh"]["hero_tag"] = "医疗器械法规咨询"; UI["ja"]["hero_tag"] = "医療機器規制コンサルティング"
UI["zh"]["h1"] = "把医疗器械法规合规设计成[[一个完整体系]]"
UI["ja"]["h1"] = "医療機器の規制対応を、[[ひとつの体系]]として設計します"
# --- 자동 갱신용 뉴스 피드 (news_feed.json): 공식 출처 사실만 담는다 ---
_FEED_LANG = {}
_FEED = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news_feed.json")
if os.path.exists(_FEED):
    _SVC = {s["slug"] for s in SERVICES}
    _have = {n["slug"] for n in NEWS}
    for _it in json.load(open(_FEED, encoding="utf-8")):
        if _it["slug"] in _have or _it["region"] not in REGIONS: continue
        _it["svc"] = _it.get("svc") if _it.get("svc") in _SVC else "qms"
        _it["src"] = [tuple(s) for s in _it["src"]]
        _ko, _en = _it["ko"], _it["en"]
        for _l in ("es", "pt", "ru", "fr", "de"):
            if _it.get(_l): _FEED_LANG[(_it["slug"], _l)] = _it[_l]
        i18n_zh.NEWS[_it["slug"]] = _it.get("zh") or _en
        i18n_ja.NEWS[_it["slug"]] = _it.get("ja") or _en
        NEWS.append({k: _it[k] for k in ("slug", "date", "region", "svc", "ko", "en", "src")})
        _have.add(_it["slug"])
    NEWS.sort(key=lambda n: n["date"], reverse=True)
    if NEWS: UPDATED = max(UPDATED, NEWS[0]["date"])
for _m in (i18n_zh, i18n_ja):
    L = _m.LANG
    for k in MAP_NODES: MAP_NODES[k][1][L] = _m.MAP[k]
    for sv in SERVICES:
        if sv["slug"] in _m.SERVICES: sv[L] = _m.SERVICES[sv["slug"]]
    PRIVACY[L] = _m.PRIVACY
    for k in REGIONS: REGIONS[k][L] = _m.REGIONS[k]
    for n in NEWS: n[L] = _m.NEWS[n["slug"]]
for _m in NEWLANG:
    L = _m.LANG
    for k in MAP_NODES: MAP_NODES[k][1][L] = _m.MAP[k]
    for sv in SERVICES:
        sv[L] = _m.SERVICES[sv["slug"]]
    PRIVACY[L] = _m.PRIVACY
    for k in REGIONS: REGIONS[k][L] = _m.REGIONS[k]
    try:
        _nm = importlib.import_module("i18n_news_" + L)
        _tr = _nm.NEWS
    except ImportError:
        _tr = {}
    for n in NEWS: n[L] = _tr.get(n["slug"]) or _FEED_LANG.get((n["slug"], L)) or n["en"]
STD_EN = {"KGMP(의료기기 제조 및 품질관리 기준)": "KGMP (Korean GMP for medical devices)", "MFDS 기술문서 심사": "MFDS technical file review", "임상평가(CEP·CER)": "Clinical evaluation (CEP, CER)",
          "FDA Human Factors 지침": "FDA human factors guidance", "MFDS 사용적합성 가이드라인": "MFDS usability guideline", "FDA Premarket Cybersecurity 지침": "FDA premarket cybersecurity guidance", "MFDS 사이버보안 가이드라인": "MFDS cybersecurity guideline"}
_GSPR = {"en": "GSPR checklist", "zh": "GSPR 检查清单", "ja": "GSPRチェックリスト", "es": "Lista de verificación GSPR", "pt": "Lista de verificação GSPR",
         "ru": "Контрольный перечень GSPR", "fr": "Liste de contrôle GSPR", "de": "GSPR-Checkliste"}
STD_EN["GSPR 체크리스트"] = _GSPR["en"]; i18n_zh.STD["GSPR 체크리스트"] = _GSPR["zh"]; i18n_ja.STD["GSPR 체크리스트"] = _GSPR["ja"]
for _m in NEWLANG: _m.STD["GSPR 체크리스트"] = _GSPR[_m.LANG]
STD_EN.update(STD_EXTRA["en"]); i18n_zh.STD.update(STD_EXTRA["zh"]); i18n_ja.STD.update(STD_EXTRA["ja"])
STDMAP = {"en": STD_EN, "zh": i18n_zh.STD, "ja": i18n_ja.STD, **{_m.LANG: _m.STD for _m in NEWLANG}}
def std_for(sv, lang):
    return [STDMAP.get(lang, {}).get(x, x) for x in sv["std"]]

GLYPH = {
 "digital-medical-products": '<path d="M34 26 L12 50 L34 74 M66 26 L88 50 L66 74" fill="none" stroke="#1D2640" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/><circle cx="50" cy="50" r="9" fill="#1D2640"/>',
 "ai-medical-device": '<rect x="22" y="22" width="56" height="56" rx="9" fill="#1D2640"/><path d="M36 8V24M36 76V92M8 36H24M76 36H92" stroke="#1D2640" stroke-width="7" stroke-linecap="round"/><path d="M50 8V24M50 76V92M8 50H24M76 50H92" stroke="#1D2640" stroke-width="7" stroke-linecap="round"/><path d="M64 8V24M64 76V92M8 64H24M76 64H92" stroke="#1D2640" stroke-width="7" stroke-linecap="round"/><path d="M44 36H56V44H64V56H56V64H44V56H36V44H44Z" fill="var(--bg)"/>',
 "license-holder": '<rect x="10" y="10" width="80" height="80" rx="10" fill="none" stroke="#1D2640" stroke-width="9"/><path d="M30 52 L45 67 L72 34" fill="none" stroke="#1D2640" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>',
 "qms": '<circle cx="50" cy="50" r="42" fill="none" stroke="#1D2640" stroke-width="10"/><circle cx="50" cy="50" r="20" fill="#1D2640"/>',
 "technical-documentation": '<rect x="8" y="8" width="58" height="58" fill="#1D2640"/><rect x="34" y="34" width="58" height="58" fill="none" stroke="#1D2640" stroke-width="8"/>',
 "risk-management": '<polygon points="50,6 95,90 5,90" fill="#1D2640"/><circle cx="50" cy="66" r="11" fill="var(--bg)"/>',
 "usability": '<path d="M6 74 A44 44 0 0 1 94 74 Z" fill="#1D2640"/><circle cx="50" cy="26" r="9" fill="#1D2640"/>',
 "cybersecurity": '<polyline points="16,18 52,18 52,82 84,82" fill="none" stroke="#1D2640" stroke-width="10" stroke-linejoin="miter"/><circle cx="16" cy="18" r="11" fill="#1D2640"/><circle cx="84" cy="82" r="11" fill="#1D2640"/>',
}
COLOR = {"qms": "#DCE5F5", "technical-documentation": "#F7E3DE", "risk-management": "#E6E4F4", "usability": "#F3EBD3", "cybersecurity": "#E9EEF7", "digital-medical-products": "#D9EAF2", "license-holder": "#EEE0EC", "ai-medical-device": "#E4E8F7"}

def glyph(slug, cls="glyph"):
    return f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">{GLYPH[slug]}</svg>'

def out_path(lang, logical):
    return ("" if lang == "ko" else lang + "/") + logical

def rel(cur, target):
    return posixpath.relpath(target, posixpath.dirname(cur) or ".")

class Ctx:
    def __init__(self, lang, logical):
        self.lang, self.logical = lang, logical
        self.cur = out_path(lang, logical)
        self.t = UI[lang]
    def link(self, logical, frag=""):
        return rel(self.cur, out_path(self.lang, logical)) + frag
    def asset(self, p):
        return rel(self.cur, p)
    def other(self, lg):
        return rel(self.cur, out_path(lg, self.logical))

LOGO = "MB"
_LG = {"MB": '<circle r="54" stroke-width="11"/><g transform="translate(0 28) rotate(0) translate(-20 -20)"><path d="M-0.7 33.3L9 6L20 37L31 6L40.7 33.3"/></g><g transform="translate(0 -28) rotate(180) translate(-20 -20)"><path d="M-0.7 33.3L9 6L20 37L31 6L40.7 33.3"/></g><g transform="translate(-28 0) rotate(90) translate(-20 -20)"><path d="M-0.7 33.3L9 6L20 37L31 6L40.7 33.3"/></g><g transform="translate(28 0) rotate(-90) translate(-20 -20)"><path d="M-0.7 33.3L9 6L20 37L31 6L40.7 33.3"/></g>',
      "M": '<circle cx="20" cy="20" r="17.5" stroke-width="2.2"/><path d="M11.5 28V12.5L20 22.5L28.5 12.5V28" stroke-width="3.8"/>',
       "MBS": '<path d="M4 32V8L13 21L22 8V32"/><path d="M27 8V32M27 8H33Q39 8 39 14Q39 20 33 20H27M33 20Q40 20 40 26Q40 32 33 32H27"/><path d="M58 11Q58 8 52 8Q45 8 45 14Q45 19 51.5 20Q58 21 58 26.5Q58 32 51.5 32Q45 32 45 28.5"/>',
       "B": '<path d="M4 32V8L14 21L24 8V32"/><path d="M24 8H31Q38 8 38 14Q38 20 31 20H24M31 20Q40 20 40 26Q40 32 31 32H24"/>',
       "C": '<rect x="3" y="3" width="38" height="34" rx="5"/><path d="M11 28V13L22 24L33 13V28"/><circle cx="11" cy="13" r="2.4" fill="currentColor" stroke="none"/><circle cx="33" cy="13" r="2.4" fill="currentColor" stroke="none"/>'}
def logo_svg(col="currentColor", ns=False):
    a = ' xmlns="http://www.w3.org/2000/svg"' if ns else ' aria-hidden="true"'
    if LOGO == "MB":
        return f'<svg{a} viewBox="-61 -61 122 122" fill="none" stroke="{col}" stroke-width="7.5" stroke-linejoin="round" stroke-linecap="round">{_LG[LOGO]}</svg>'
    return f'<svg{a} viewBox="0 0 {64 if LOGO == "MBS" else (40 if LOGO == "M" else 44)} 40" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round">{_LG[LOGO]}</svg>'

def header(c):
    t = c.t
    cur = lambda lg: ' aria-current="page"' if c.logical == lg else ""
    menu = "".join(f'<li><a href="{c.link("services/" + s["slug"] + ".html")}">{s[c.lang]["name"]}</a></li>' for s in SERVICES)
    langs = "".join(f'<li><a href="{c.other(lg)}" lang="{lg}" hreflang="{lg}"{" aria-current=true" if lg == c.lang else ""}>{UI[lg]["label"]}</a></li>' for lg in LANGS)
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="site-header"><div class="wrap">
<a class="logo" href="{c.link("index.html")}">{logo_svg()}<img class="wm" src="{c.asset("img/wordmark.png")}" alt="mybiosys" width="720" height="154"></a>
<nav class="nav" id="nav" aria-label="main">
<div class="dd"><button type="button" aria-expanded="false" aria-haspopup="true">{t["nav_services"]}</button><ul class="dd-menu">{menu}</ul></div>
<a href="{c.link("news.html")}"{cur("news.html")}>{t["nav_insights"]}</a>
<a href="{c.link("index.html", "#contact")}">{t["nav_contact"]}</a>
</nav>
<a class="pill fill cta-pill" href="{c.link("index.html", "#contact")}">{t["cta_contact"]}</a>
<div class="tools"><details class="langsel"><summary aria-label="Language">{t["label"]}</summary><ul>{langs}</ul></details>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="{t["menu"]}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button></div>
</div></header>'''

import hashlib
ASSET_V = {k: hashlib.md5(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f), "rb").read()).hexdigest()[:8] for k, f in (("css", "css/style.css"), ("js", "js/main.js"))}

def footer(c):
    t = c.t
    svc = "".join(f'<li><a href="{c.link("services/" + s["slug"] + ".html")}">{s[c.lang]["name"]}</a></li>' for s in SERVICES)
    li = f'<li><a href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>' if LINKEDIN_URL else ""
    return f'''<footer class="site-footer"><div class="wrap">
<div class="cols">
<div><a class="logo" href="{c.link("index.html")}">{logo_svg()}<img class="wm" src="{c.asset("img/wordmark-white.png")}" alt="mybiosys" width="720" height="154"></a><p>{t["foot_about"]}</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><h2>{t["foot_services"]}</h2><ul>{svc}</ul></div>
<div><h2>{t["foot_info"]}</h2><ul><li><a href="{c.link("news.html")}">{t["nav_insights"]}</a></li><li><a href="{c.link("privacy.html")}">{t["privacy"]}</a></li>{li}</ul></div>
</div>
<p class="copy">© 2026 mybiosys</p>
</div></footer>'''

OG_LOCALE = {"ko": "ko_KR", "en": "en_US", "zh-CN": "zh_CN", "ja": "ja_JP", "es": "es_ES", "pt": "pt_PT", "ru": "ru_RU", "fr": "fr_FR", "de": "de_DE"}
SERIF = {'ko': 'Noto+Serif+KR', 'en': 'Noto+Serif+KR', 'zh': 'Noto+Serif+SC', 'ja': 'Noto+Serif+JP'}
def page(c, title, desc, body, schema=None):
    t = c.t
    url = f"https://{DOMAIN}/" + c.cur
    hre = "".join(f'<link rel="alternate" hreflang="{lg}" href="https://{DOMAIN}/{out_path(lg, c.logical)}">\n' for lg in LANGS)
    hre += f'<link rel="alternate" hreflang="x-default" href="https://{DOMAIN}/{out_path("ko", c.logical)}">'
    sch = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ""
    s = f'''<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
{hre}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="mybiosys">
<meta property="og:locale" content="{OG_LOCALE.get(t["html_lang"], "ko_KR")}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://{DOMAIN}/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="mybiosys">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="https://{DOMAIN}/img/og-image.png">
<meta name="theme-color" content="#1D2640">
<link rel="icon" href="{c.asset("favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/noto-sans-kr@5/400.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/noto-sans-kr@5/500.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/noto-sans-kr@5/700.css">
<link rel="stylesheet" href="{c.asset("css/style.css")}?v={ASSET_V["css"]}">
{sch}
</head>
<body class="{"home" if c.logical == "index.html" else "inner"}">
{header(c)}
<main id="main">
{body}
</main>
{footer(c)}
<script src="{c.asset("js/main.js")}?v={ASSET_V["js"]}" defer></script>
</body></html>'''
    p = os.path.join(OUT, c.cur)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)

def blocks(items):
    o = []
    for b in items:
        if b[0] == "p": o.append(f"<p>{b[1]}</p>")
        elif b[0] == "h2": o.append(f"<h2>{b[1]}</h2>")
        elif b[0] == "ul": o.append("<ul>" + "".join(f"<li>{x}</li>" for x in b[1]) + "</ul>")
    return "\n".join(o)


HERO_3D = ''
def _make_tiles():
    N, g, r = 120, 8, 22
    cols, rows = 12, 3
    pal = [("#58DFA6","#16282F"),("#58DFA6","#16282F"),("#1E9E6C","#fff"),("#16282F","#58DFA6"),("#CDEFE0","#1E9E6C"),("#3FC48C","#fff"),("#FFD23F","#16282F"),("#58DFA6","#fff")]
    seed = [11]
    def rnd():
        seed[0] = (seed[0]*1103515245+12345) & 0x7fffffff
        return seed[0]/0x7fffffff
    out = []
    for j in range(rows):
        for i in range(cols):
            if rnd() < 0.08: continue
            bg, fg = pal[int(rnd()*len(pal))]
            x, y, w = i*N+g/2, j*N+g/2, N-g
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" rx="{r}" fill="{bg}"/>')
            if rnd() < 0.78:
                out.append(f'<g transform="translate({x+w/2} {y+w/2}) scale(0.78)" fill="none" stroke="{fg}" stroke-width="7.5" stroke-linejoin="round" stroke-linecap="round">{_LG["MB"]}</g>')
    return f'<svg class="tile-art" viewBox="0 0 {cols*N} {rows*N}" preserveAspectRatio="xMidYMid meet" aria-hidden="true" focusable="false">' + "".join(out) + '</svg>'
TILES = _make_tiles()
TRACE_ART = '''<svg class="trace-art" viewBox="0 0 580 420" aria-hidden="true" focusable="false">
<path d="M110 90L300 105L470 185L320 310L120 330" fill="none" stroke="#14262E" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="110" cy="90" r="58" fill="#58DFA6"/>
<polygon points="300,38 365,150 235,150" fill="#1E9E6C"/>
<rect x="420" y="135" width="100" height="100" fill="#14262E"/><circle cx="470" cy="185" r="16" fill="#fff"/>
<g transform="translate(320 310)"><circle r="62" fill="#CDEFE0"/><circle r="40" fill="#fff"/><circle r="19" fill="#58DFA6"/></g>
<rect x="68" y="286" width="104" height="88" rx="10" fill="#fff" stroke="#14262E" stroke-width="6"/>
<path d="M90 314H150M90 332H150M90 350H124" stroke="#14262E" stroke-width="6" stroke-linecap="round"/>
</svg>'''

def tmap(c):
    t = c.t
    X0, DX, W, H = 8, 130, 112, 46
    ys = [48, 128, 208]
    cols = "abcde"
    pos = {k: (X0 + cols.index(k[0]) * DX, ys[int(k[1])]) for k in MAP_NODES}
    heads = "".join(f'<text class="col" x="{X0 + i * DX}" y="24">{esc(n)}</text>' for i, n in enumerate(t["map_cols"]))
    edges = []
    for a, b in MAP_EDGES:
        x1, y1 = pos[a][0] + W, pos[a][1] + H / 2
        x2, y2 = pos[b][0], pos[b][1] + H / 2
        edges.append(f'<path class="edge" pathLength="1" data-from="{a}" data-to="{b}" style="--c:{cols.index(a[0])}" d="M{x1},{y1} C{x1+9},{y1} {x2-9},{y2} {x2},{y2}"/>')
    nodes = []
    for k, (idt, lab) in MAP_NODES.items():
        x, y = pos[k]; l = lab[c.lang]
        nodes.append(f'<g class="node" data-id="{k}" tabindex="0" role="button" aria-label="{idt} {esc(l)}" style="--c:{cols.index(k[0])}"><rect x="{x}" y="{y}" width="{W}" height="{H}" rx="6"/><text class="id" x="{x+10}" y="{y+19}">{esc(idt)}</text><text class="lb" x="{x+10}" y="{y+36}">{esc(l)}</text></g>')
    edata = json.dumps([list(e) for e in MAP_EDGES])
    return f'''<div class="tmap-wrap"><div class="tmap-scroll">
<svg class="tmap" viewBox="0 0 650 270" role="group" aria-label="{esc(t["map_caption"])}" data-edges='{edata}' data-default="{MAP_DEFAULT}">
{heads}{"".join(edges)}{"".join(nodes)}
</svg></div><p class="tmap-cap">{t["map_caption"]}</p></div>'''

HERO_ART = '''<svg class="hero-art" viewBox="0 0 1440 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
<rect x="0" y="110" width="120" height="400" fill="#E5365B"/>
<path d="M120 190A110 110 0 0 1 120 410Z" fill="#EA6A2D"/>
<g transform="translate(470 300)"><circle r="150" fill="#CFC070"/><circle r="108" fill="#fff"/><circle r="70" fill="#CFC070"/><circle r="32" fill="#fff"/></g>
<rect x="720" y="110" width="240" height="240" fill="#B6E04B"/>
<path d="M720 250H1050V500" fill="none" stroke="#E5365B" stroke-width="26"/>
<path d="M880 610H1110" fill="none" stroke="#E5365B" stroke-width="26"/>
<polygon points="1180,600 1310,350 1440,600" fill="#6A3DF0"/>
<circle cx="1310" cy="520" r="26" fill="#fff"/>
</svg>'''

PARTNER = {
 "ko": ("비즈니스 파트너", "mybiosys와 협력하는 의료기기 규제 전문 기업입니다.", "중국 상하이", "MEDWHEAT 그룹의 중국 법인(2014년 설립, 상하이 민항구). 의료기기 해외 인허가·등록과 해외 임상 CRO를 전문으로 하며 약 20개국 등록을 지원합니다. 동물 유래 이식형 기기와 심혈관 중재 분야 경험이 풍부하고, 고위험·혁신 의료기기 기업에 해외 제품 등록과 후향적 데이터 기반 임상시험 면제 대응 솔루션을 제공합니다. 교육 서비스도 운영합니다.", "웹사이트 방문"),
 "en": ("Business partners", "Companies we work with in medical device regulatory affairs.", "Shanghai, China", "The China entity of the MEDWHEAT group (founded 2014, Minhang District, Shanghai). Specializes in international medical device registration and overseas clinical CRO operations, supporting registration in nearly 20 countries. Experienced in animal-derived implants and cardiovascular interventional devices, it offers high-risk and innovative device makers overseas product registration and retrospective-data solutions for clinical exemption. Training services are also offered.", "Visit website"),
 "zh": ("业务合作伙伴", "与 mybiosys 合作的医疗器械法规专业机构。", "中国上海", "MEDWHEAT 集团在中国的分支公司（2014 年成立，位于上海闵行区）。专业从事医疗器械国际注册及境外临床运营 CRO，可运作近 20 个国家的境外注册；在动物源植入及心血管介入等领域经验丰富。为“高风险及创新”医疗器械企业提供“境外产品注册”与“回顾性数据免临床应对解决”方案，并提供培训服务。", "访问网站"),
 "ja": ("ビジネスパートナー", "mybiosys と協力する医療機器規制の専門企業です。", "中国・上海", "MEDWHEAT グループの中国法人（2014年設立、上海市閔行区）。医療機器の海外登録と海外臨床 CRO 運営を専門とし、約20か国での登録に対応します。動物由来インプラントや心血管インターベンション分野の経験が豊富で、高リスク・革新的な医療機器企業に、海外製品登録と後ろ向きデータによる臨床試験免除対応のソリューションを提供します。教育・研修サービスも行っています。", "ウェブサイトを見る"),
 "es": ("Socios comerciales", "Empresas con las que colaboramos en asuntos regulatorios de productos sanitarios.", "Shanghái, China", "Filial en China del grupo MEDWHEAT (fundada en 2014, distrito de Minhang, Shanghái). Especializada en el registro internacional de productos sanitarios y en la operación de CRO clínica en el extranjero, con capacidad para registros en casi 20 países. Con amplia experiencia en implantes de origen animal e intervencionismo cardiovascular, ofrece a fabricantes de productos innovadores y de alto riesgo registro en el extranjero y soluciones basadas en datos retrospectivos para evitar ensayos clínicos. También ofrece formación.", "Visitar el sitio web"),
 "pt": ("Parceiros de negócio", "Empresas com as quais colaboramos em assuntos regulamentares de dispositivos médicos.", "Xangai, China", "Filial na China do grupo MEDWHEAT (fundada em 2014, distrito de Minhang, Xangai). Especializada no registo internacional de dispositivos médicos e na operação de CRO clínica no estrangeiro, com capacidade para registos em quase 20 países. Com ampla experiência em implantes de origem animal e intervenção cardiovascular, oferece a fabricantes de dispositivos inovadores e de alto risco registo no estrangeiro e soluções baseadas em dados retrospetivos para dispensa de ensaio clínico. Presta também formação.", "Visitar o sítio Web"),
 "ru": ("Деловые партнёры", "Компании, с которыми мы сотрудничаем в сфере регулирования медицинских изделий.", "Шанхай, Китай", "Китайское подразделение группы MEDWHEAT (основано в 2014 г., район Миньхан, Шанхай). Специализируется на международной регистрации медицинских изделий и проведении зарубежных клинических исследований в роли CRO; работает с регистрацией почти в 20 странах. Богатый опыт в области имплантатов животного происхождения и сердечно-сосудистой интервенции. Для производителей инновационных изделий высокого риска предлагает регистрацию за рубежом и решения на основе ретроспективных данных для освобождения от клинических исследований. Также проводит обучение.", "Перейти на сайт"),
 "fr": ("Partenaires commerciaux", "Entreprises avec lesquelles nous collaborons en affaires réglementaires des dispositifs médicaux.", "Shanghai, Chine", "Filiale chinoise du groupe MEDWHEAT (fondée en 2014, district de Minhang, Shanghai). Spécialisée dans l'enregistrement international des dispositifs médicaux et la conduite d'activités de CRO clinique à l'étranger, avec une capacité d'enregistrement dans près de 20 pays. Riche expérience des implants d'origine animale et de l'intervention cardiovasculaire ; propose aux fabricants de dispositifs innovants et à haut risque l'enregistrement à l'étranger et des solutions fondées sur des données rétrospectives pour se dispenser d'étude clinique. Propose aussi des formations.", "Visiter le site web"),
 "de": ("Geschäftspartner", "Unternehmen, mit denen wir im Bereich Medizinprodukterecht zusammenarbeiten.", "Shanghai, China", "Chinesische Tochtergesellschaft der MEDWHEAT-Gruppe (gegründet 2014, Bezirk Minhang, Shanghai). Spezialisiert auf die internationale Registrierung von Medizinprodukten und den Betrieb von CRO-Leistungen für klinische Prüfungen im Ausland; Registrierungen in knapp 20 Ländern. Große Erfahrung mit Implantaten tierischen Ursprungs und kardiovaskulären Interventionsprodukten. Für Hersteller innovativer Hochrisikoprodukte bietet das Unternehmen Auslandsregistrierung und Lösungen auf Basis retrospektiver Daten zur Vermeidung klinischer Studien. Außerdem Schulungen.", "Website besuchen"),
}
PARTNERS = [("MedWheat", "https://www.medwheat.com/", "img/partner-medwheat.png", "MedWheat 麦祥", 485, 184, "麦祥医药科技（上海）有限公司", "")]

def home(lang):
    c = Ctx(lang, "index.html"); t = c.t
    tiles = "".join(
        f'<a class="tile" style="--bg:{COLOR[s["slug"]]}" href="{c.link("services/" + s["slug"] + ".html")}">{glyph(s["slug"])}<h3>{s[lang]["name"]}</h3><p>{s[lang]["sum"]}</p><span class="std">{", ".join(std_for(s, lang)[:3])}</span><span class="more">{t["learn"]}</span></a>'
        for s in SERVICES)
    tiles += f'<a class="tile cta-tile" href="#contact"><svg class="glyph" viewBox="0 0 100 100" aria-hidden="true"><path d="M12 50 H80 M56 24 L84 50 L56 76" fill="none" stroke="#2F6F73" stroke-width="10"/></svg><h3>{t["tile_h"]}</h3><p>{t["tile_p"]}</p><span class="more">{t["tile_a"]}</span></a>'
    princ = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in t["principles"])
    steps = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in t["steps"])
    nl = "".join(news_li(c, n, i) for i, n in enumerate(NEWS[:5]))
    opts = "".join(f'<option value="{s["slug"]}">{s[lang]["name"]}</option>' for s in SERVICES) + f'<option value="other">{t["f_other"]}</option>'
    ph, pi, ploc, pd, pv = PARTNER[lang]
    pcards = "".join(f'<li><a class="pcard" href="{u}" target="_blank" rel="noopener"><span class="plogo"><img src="{c.asset(lg)}" alt="{alt}" width="{lw}" height="{lh}" loading="lazy"></span><span class="ploc">{ploc}</span><strong>{n}</strong><span class="plegal">{legal}</span><span class="pdesc">{pd}</span><span class="more">{pv}</span></a></li>' for n, u, lg, alt, lw, lh, legal, mail in PARTNERS)
    consent = t["f_consent"].replace("{priv}", c.link("privacy.html"))
    photo = ""
    for ext in ("webp", "jpg", "jpeg", "png"):
        if os.path.exists(f"{OUT}/img/hero.{ext}"):
            photo = f'<img class="hero-photo" src="{c.asset("img/hero." + ext)}" alt="" loading="eager">'
            break
    body = f'''<section class="hero">{HERO_ART}{photo}<div class="wrap">
<p class="eyebrow">{t["hero_tag"]}</p>
<h1>{t["h1"].replace("[[", '<mark class="hl">').replace("]]", "</mark>")}</h1><p class="lead">{t["lead"]}</p>
<div class="cta"><a class="btn" href="#contact">{t["cta_contact"]}</a><a class="btn-ghost" href="#services">{t["cta_services"]}</a></div></div></section>
<div class="tile-band">{TILES}</div>
<section class="section"><div class="wrap trace">
<div><h2>{t["trace_h"]}</h2><p>{t["trace_p"]}</p><ul class="principles">{princ}</ul></div>
<div class="trace-art-wrap">{TRACE_ART}</div>
</div></section>
<section class="section on-navy" id="services"><div class="wrap">
<div class="section-head"><h2>{t["svc_h"]}</h2><p>{t["svc_p"]}</p></div>
<div class="tiles">{tiles}</div></div></section>
<section class="section"><div class="wrap">
<div class="section-head"><h2>{t["proc_h"]}</h2><p>{t["proc_p"]}</p></div>
<ol class="steps">{steps}</ol></div></section>
<section class="section" style="background:#fff"><div class="wrap">
<div class="section-head"><h2>{t["ins_h"]}</h2><p>{t["ins_p"]}</p></div>
<ul class="news">{nl}</ul>
<p style="margin-top:24px"><a class="btn-ghost" href="{c.link("news.html")}">{t["ins_all"]}</a></p></div></section>
<section class="section" id="partners"><div class="wrap">
<div class="section-head"><h2>{ph}</h2><p>{pi}</p></div>
<ul class="partners">{pcards}</ul></div></section>
<section class="section on-navy" id="contact"><div class="wrap contact-grid">
<div class="side"><h2>{t["con_h"]}</h2><p>{t["con_p"]}</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<form class="contact" novalidate data-endpoint="{FORM_ENDPOINT}" data-key="{FORM_KEY}" data-mailto="{EMAIL}" data-msg-ok="{t["msg_ok"]}" data-msg-err="{t["msg_err"]}" data-msg-mail="{t["msg_mail"]}" data-msg-sending="{t["msg_sending"]}">
<div class="row2"><div class="field"><label for="f-name">{t["f_name"]}</label><input id="f-name" name="name" required autocomplete="name"></div>
<div class="field"><label for="f-company">{t["f_company"]}</label><input id="f-company" name="company" required autocomplete="organization"></div></div>
<div class="row2"><div class="field"><label for="f-email">{t["f_email"]}</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
<div class="field"><label for="f-topic">{t["f_topic"]}</label><select id="f-topic" name="topic">{opts}</select></div></div>
<div class="field"><label for="f-msg">{t["f_msg"]}</label><textarea id="f-msg" name="message" required></textarea></div>
<input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="consent"><input type="checkbox" name="consent" required><span>{consent}</span></label>
<div><button class="btn" type="submit">{t["f_submit"]}</button></div>
<p class="status" role="status" aria-live="polite"></p>
</form></div></section>'''
    schema = {"@context": "https://schema.org", "@type": "ProfessionalService", "@id": f"https://{DOMAIN}/#org", "name": "mybiosys", "url": f"https://{DOMAIN}/", "description": t["home_desc"],
              "email": "contact@mybiosys.com", "sameAs": ["https://www.linkedin.com/in/minyong-choi-78040369/"], "inLanguage": t["html_lang"], "availableLanguage": LANGS,
              "serviceType": [x[lang]["name"] for x in SERVICES],
              "hasOfferCatalog": {"@type": "OfferCatalog", "name": "mybiosys",
                                  "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": x[lang]["name"], "url": f"https://{DOMAIN}/" + out_path(lang, f"services/{x['slug']}.html")}} for x in SERVICES]}}
    page(c, t["home_title"], t["home_desc"], body, schema)

def service(lang, s):
    c = Ctx(lang, f"services/{s['slug']}.html"); t = c.t; d = s[lang]
    scope = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in d["scope"])
    when = "".join(f"<li>{w}</li>" for w in d["when"])
    std = "".join(f"<li>{x}</li>" for x in std_for(s, lang))
    others = "".join(f'<li><a href="{c.link("services/" + o["slug"] + ".html")}">{o[lang]["name"]}</a></li>' for o in SERVICES if o is not s)
    ask = c.link("index.html") + f"?topic={s['slug']}#contact"
    body = f'''<section class="svc-head" style="--bg:{COLOR[s["slug"]]}"><div class="wrap">
<p class="crumb"><a href="{c.link("index.html")}">{t["crumb_home"]}</a> / <a href="{c.link("index.html", "#services")}">{t["nav_services"]}</a></p>
<h1>{d["name"]}</h1><p class="lead">{d["lead"]}</p></div>{glyph(s["slug"])}</section>
<div class="wrap"><div class="two"><div>
<section><h2>{t["scope_h"]}</h2><ul class="list">{scope}</ul></section>
<section><h2>{t["when_h"]}</h2><ul>{when}</ul></section></div>
<aside><div class="aside-box"><h2>{t["std_h"]}</h2><ul>{std}</ul><a class="btn lime" href="{ask}">{t["ask"]}</a></div></aside></div>
<div class="others"><strong>{t["others"]}</strong><ul>{others}</ul></div></div>'''
    sch = {"@context": "https://schema.org", "@type": "Service", "name": d["name"], "description": d["lead"][:150], "inLanguage": t["html_lang"],
           "url": "https://" + DOMAIN + "/" + c.cur, "provider": {"@type": "ProfessionalService", "@id": f"https://{DOMAIN}/#org", "name": "mybiosys"}}
    page(c, f'{d["name"]} | mybiosys', d["lead"][:150], body, sch)

def news_li(c, n, i):
    d = n[c.lang]; t = c.t
    href = c.link("news/" + n["slug"] + ".html")
    return (f'<li class="news-item" id="n{i}" data-region="{n["region"]}"><time datetime="{n["date"]}">{n["date"]}</time>'
            f'<div><span class="tag" data-r="{n["region"]}">{REGIONS[n["region"]][c.lang]}</span>'
            f'<h3><a href="{href}">{esc(d["title"])}</a></h3><p>{esc(d["sum"])}</p>'
            f'<p class="more-link"><a href="{href}">{t["nd_more"]}</a></p></div></li>')

def news_detail(lang, n):
    c = Ctx(lang, f"news/{n['slug']}.html"); t = c.t; d = n[lang]
    pts = "".join(f"<li>{esc(x)}</li>" for x in d["points"])
    def _sn(x):
        k, e, u = x[0], x[1], x[2]
        if lang == "ko": return k
        if lang == "en": return e
        ex = x[3] if len(x) > 3 and isinstance(x[3], dict) else {}
        return ex.get(lang) or i18n_src.SRC.get(e, {}).get(lang) or e
    srcs = "".join(f'<li><a href="{x[2]}" target="_blank" rel="noopener">{esc(_sn(x))}</a></li>' for x in n["src"])
    check = f'<section><h2>{t["nd_check"]}</h2><p>{esc(d["check"])}</p></section>' if d.get("check") else ""
    rel = ""
    if n.get("svc"):
        s = next(x for x in SERVICES if x["slug"] == n["svc"])
        rel = f'<p class="rel"><b>{t["nd_related"]}</b> <a href="{c.link("services/" + s["slug"] + ".html")}">{s[lang]["name"]}</a></p>'
    ask = c.link("index.html") + f"?topic={n['svc'] or 'other'}#contact"
    body = f'''<div class="wrap"><div class="page-head">
<p class="crumb"><a href="{c.link("index.html")}">{t["crumb_home"]}</a> / <a href="{c.link("news.html")}">{t["nav_insights"]}</a></p>
<p class="meta"><span class="tag" data-r="{n["region"]}">{REGIONS[n["region"]][lang]}</span> <time datetime="{n["date"]}">{n["date"]}</time></p>
<h1 class="nd-title">{esc(d["title"])}</h1><p class="lead">{esc(d["sum"])}</p></div>
<div class="two"><div>
<section><h2>{t["nd_points"]}</h2><ul class="bullets">{pts}</ul></section>
{check}
<p class="muted note">{t["nd_notice"]}</p>
<p style="margin-top:28px"><a class="btn-ghost" href="{c.link("news.html")}">{t["nd_back"]}</a></p></div>
<aside><div class="aside-box"><h2>{t["nd_sources"]}</h2><ul class="srcs">{srcs}</ul>{rel}
<a class="btn lime" href="{ask}">{t["nd_ask"]}</a></div></aside></div></div>'''
    sch = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": d["title"][:110], "description": d["sum"][:150], "datePublished": n["date"],
           "inLanguage": t["html_lang"], "mainEntityOfPage": "https://" + DOMAIN + "/" + c.cur,
           "publisher": {"@type": "Organization", "name": "mybiosys", "url": f"https://{DOMAIN}/"}, "citation": [x[2] for x in n["src"]]}
    page(c, f'{d["title"]} | mybiosys', d["sum"][:150], body, sch)

def news_page(lang):
    c = Ctx(lang, "news.html"); t = c.t
    items = "".join(news_li(c, n, i) for i, n in enumerate(NEWS))
    used = [k for k in REGIONS if any(n["region"] == k for n in NEWS)]
    chips = f'<button type="button" class="chip on" data-r="all">{t["all"]}</button>' + "".join(
        f'<button type="button" class="chip" data-r="{k}">{REGIONS[k][lang]}</button>' for k in used)
    body = f'''<div class="wrap"><div class="page-head"><h1>{t["ins_h"]}</h1><p class="lead">{t["ins_p"]}</p>
<p class="muted" style="margin-top:12px;font-size:.92rem">{t["news_updated"]}: {UPDATED}</p></div>
<div class="chips" role="group">{chips}</div><ul class="news">{items}</ul>
<p class="muted note">{t["news_note"]}</p></div>'''
    page(c, t["ins_page_title"], t["ins_page_desc"], body)

def privacy(lang):
    c = Ctx(lang, "privacy.html"); d = PRIVACY[lang]
    inner = blocks(d["body"]).replace("{email}", f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    body = f'<div class="wrap"><div class="page-head"><h1 style="font-size:clamp(2rem,4.5vw,3.4rem)">{d["title"]}</h1></div><div class="legal">{inner}</div></div>'
    page(c, f'{d["title"]} | mybiosys', d["title"], body)

def notfound():
    c = Ctx("ko", "404.html"); t = UI["ko"]; e = UI["en"]
    body = f'''<div class="wrap"><div class="page-head" style="padding-bottom:96px"><h1>{t["notfound_h"]}</h1><p class="lead">{t["notfound_p"]}</p>
<p style="margin-top:24px"><a class="btn" href="/">{t["notfound_a"]}</a></p>
<p class="muted" style="margin-top:32px">{e["notfound_h"]}. <a href="/en/">English</a> · <a href="/zh/">中文</a> · <a href="/ja/">日本語</a> · <a href="/es/">Español</a> · <a href="/pt/">Português</a> · <a href="/ru/">Русский</a> · <a href="/fr/">Français</a> · <a href="/de/">Deutsch</a></p></div></div>'''
    page(c, t["notfound_h"] + " | mybiosys", t["notfound_p"], body)
    p = os.path.join(OUT, "404.html")
    s = open(p, encoding="utf-8").read()
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', "", s)
    s = re.sub(r'<link rel="canonical" href="[^"]*">\n?', "", s)
    s = s.replace('<meta name="robots"', '<meta name="robots"')
    s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1)
    s = re.sub(r'href="(?:\.\./)?(en|zh|ja|es|pt|ru|fr|de)/404\.html"', r'href="/\1/"', s)
    for a in ["css/style.css", "js/main.js", "favicon.svg"]:
        s = s.replace('"' + a + '"', '"/' + a + '"')
    s = re.sub(r'href="(index\.html)([^"]*)"', r'href="/\1\2"', s)
    s = re.sub(r'href="(services/|news\.html|privacy\.html|en/)', r'href="/\1', s)
    open(p, "w", encoding="utf-8").write(s)

for lang in LANGS:
    home(lang); news_page(lang); privacy(lang)
    for n in NEWS: news_detail(lang, n)
    for s in SERVICES: service(lang, s)
notfound()

open(os.path.join(OUT, "favicon.svg"), "w").write(logo_svg("#1D2640", True))
open(os.path.join(OUT, "CNAME"), "w").write(DOMAIN + "\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
_pages = ["index.html", "news.html", "privacy.html"] + [f"services/{s['slug']}.html" for s in SERVICES] + [f"news/{n['slug']}.html" for n in NEWS]
_mod = {f"news/{n['slug']}.html": n["date"] for n in NEWS}
_ent = []
for lp in _pages:
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{lg}" href="https://{DOMAIN}/{out_path(lg, lp)}"/>' for lg in LANGS)
    alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="https://{DOMAIN}/{out_path("ko", lp)}"/>'
    for lang in LANGS:
        _ent.append(f"<url><loc>https://{DOMAIN}/{out_path(lang, lp)}</loc><lastmod>{_mod.get(lp, UPDATED)}</lastmod>{alts}</url>\n")
urls = _ent
open(os.path.join(OUT, "sitemap.xml"), "w").write(
 '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "".join(_ent) + "</urlset>\n")
print("built", len(urls), "pages")
