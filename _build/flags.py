"""Simplified inline SVG flags (30x20) for region tags. Aggregates get globe icons; Taiwan is intentionally text-only."""
import math

def star(cx, cy, r, rot=-90, fill="#FFDE00"):
    pts = []
    for i in range(10):
        a = math.radians(rot + i * 36)
        rr = r if i % 2 == 0 else r * 0.382
        pts.append(f"{cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'

def jack(x=0, y=0, w=30, h=20):
    """Union Jack scaled into a w x h box at x,y."""
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 60 40" preserveAspectRatio="none">'
            '<rect width="60" height="40" fill="#012169"/>'
            '<path d="M0 0L60 40M60 0L0 40" stroke="#fff" stroke-width="8"/>'
            '<path d="M0 0L60 40M60 0L0 40" stroke="#C8102E" stroke-width="3"/>'
            '<path d="M30 0V40M0 20H60" stroke="#fff" stroke-width="13"/>'
            '<path d="M30 0V40M0 20H60" stroke="#C8102E" stroke-width="8"/></svg>')

def globe(tint):
    return (f'<circle cx="15" cy="10" r="8.2" fill="{tint}" stroke="#14262E" stroke-width="1.2"/>'
            '<ellipse cx="15" cy="10" rx="3.6" ry="8.2" fill="none" stroke="#14262E" stroke-width="1"/>'
            '<path d="M6.9 7.2H23.1M6.9 12.8H23.1M15 1.8V18.2" stroke="#14262E" stroke-width="1" fill="none"/>')

F = {}
F["kr"] = ('<rect width="30" height="20" fill="#fff"/>'
           '<path d="M9.5 10a5.5 5.5 0 0 1 11 0z" fill="#CD2E3A"/><path d="M9.5 10a5.5 5.5 0 0 0 11 0z" fill="#0047A0"/>'
           '<circle cx="12.25" cy="10" r="2.75" fill="#CD2E3A"/><circle cx="17.75" cy="10" r="2.75" fill="#0047A0"/>'
           '<g stroke="#000" stroke-width="1.1"><path d="M3.2 4.2l2.6-1.8M4.2 5.6l2.6-1.8M24.2 2.4l2.6 1.8M23.2 3.8l2.6 1.8M3.2 15.8l2.6 1.8M4.2 14.4l2.6 1.8M24.2 17.6l2.6-1.8M23.2 16.2l2.6-1.8"/></g>')
F["us"] = ('<rect width="30" height="20" fill="#fff"/>'
           + "".join(f'<rect y="{i*20/7*1:.2f}" width="30" height="{20/13:.2f}" fill="#B22234" transform="translate(0,{i*0})"/>' for i in [])  # placeholder
           + "".join(f'<rect y="{y:.2f}" width="30" height="1.54" fill="#B22234"/>' for y in [i * 3.077 for i in range(7)])
           + '<rect width="13" height="10.77" fill="#3C3B6E"/>'
           + "".join(f'<circle cx="{2+c*2.8:.1f}" cy="{2+r*2.4:.1f}" r=".5" fill="#fff"/>' for r in range(4) for c in range(4)))
F["cn"] = ('<rect width="30" height="20" fill="#DE2910"/>' + star(6, 6, 3.4) + star(11.5, 2.6, 1.1, -70) + star(13.5, 5, 1.1, -50) + star(13.5, 8, 1.1, -30) + star(11.5, 10.3, 1.1, -10))
F["eu"] = ('<rect width="30" height="20" fill="#003399"/>' + "".join(star(15 + 6 * math.cos(math.radians(i * 30)), 10 + 6 * math.sin(math.radians(i * 30)), 1.15, -90, "#FFCC00") for i in range(12)))
F["uk"] = jack()
F["jp"] = '<rect width="30" height="20" fill="#fff"/><circle cx="15" cy="10" r="6" fill="#BC002D"/>'
F["au"] = ('<rect width="30" height="20" fill="#012169"/>' + jack(0, 0, 15, 10) + star(7.5, 15, 2.6, -90, "#fff") + star(22, 4.5, 1.2, -90, "#fff") + star(25.5, 9, 1.2, -90, "#fff") + star(22, 15, 1.2, -90, "#fff") + star(18.5, 9, 1.2, -90, "#fff"))
F["ca"] = ('<rect width="30" height="20" fill="#fff"/><rect width="7.5" height="20" fill="#D52B1E"/><rect x="22.5" width="7.5" height="20" fill="#D52B1E"/>'
           '<path d="M15 3.2l1.6 3.1 1.9-.6-.9 4.4 2.5-2.2.5 1.2 2-.3-.8 2.8.9.5-3.6 3.1.3 1.1-3.9-.5v3.2h-1v-3.2l-3.9.5.3-1.1-3.6-3.1.9-.5-.8-2.8 2 .3.5-1.2 2.5 2.2-.9-4.4 1.9.6z" fill="#D52B1E"/>')
F["br"] = ('<rect width="30" height="20" fill="#009C3B"/><path d="M15 2.2L27 10 15 17.8 3 10z" fill="#FFDF00"/><circle cx="15" cy="10" r="4.4" fill="#002776"/>'
           '<path d="M10.8 9c3-.9 6.2-.4 8.6 1.4" stroke="#fff" stroke-width=".9" fill="none"/>')
F["mx"] = ('<rect width="10" height="20" fill="#006847"/><rect x="10" width="10" height="20" fill="#fff"/><rect x="20" width="10" height="20" fill="#CE1126"/>'
           '<circle cx="15" cy="10" r="2.6" fill="#8C6A2F"/><path d="M12.8 12.2q2.2 1.6 4.4 0" stroke="#006847" stroke-width=".9" fill="none"/>')
F["ar"] = ('<rect width="30" height="20" fill="#74ACDF"/><rect y="6.67" width="30" height="6.67" fill="#fff"/><circle cx="15" cy="10" r="2.2" fill="#F6B40E"/>')
F["il"] = ('<rect width="30" height="20" fill="#fff"/><rect y="2.2" width="30" height="2.6" fill="#0038B8"/><rect y="15.2" width="30" height="2.6" fill="#0038B8"/>'
           '<g fill="none" stroke="#0038B8" stroke-width="1"><path d="M15 6.2l3.5 6.1h-7z"/><path d="M15 13.8l-3.5-6.1h7z"/></g>')
F["ke"] = ('<rect width="30" height="20" fill="#000"/><rect y="6.2" width="30" height="7.6" fill="#BB0000"/><rect y="5.6" width="30" height="1" fill="#fff"/><rect y="13.4" width="30" height="1" fill="#fff"/>'
           '<rect y="14.4" width="30" height="5.6" fill="#006600"/><rect y="0" width="30" height="5.6" fill="#000"/>'
           '<ellipse cx="15" cy="10" rx="3" ry="4.6" fill="#BB0000" stroke="#fff" stroke-width=".9"/><path d="M15 5.6v8.8" stroke="#fff" stroke-width=".8"/>')
F["za"] = ('<rect width="30" height="20" fill="#fff"/><rect width="30" height="10" fill="#DE3831"/><rect y="10" width="30" height="10" fill="#002395"/>'
           '<path d="M0 0L11 10 0 20z" fill="#000" stroke="#FFB612" stroke-width="1.6" stroke-linejoin="round"/>'
           '<path d="M0 0L11.5 10 0 20M11.5 10H30" fill="none" stroke="#fff" stroke-width="5"/>'
           '<path d="M0 0L11.5 10 0 20M11.5 10H30" fill="none" stroke="#007A4D" stroke-width="3"/>'
           '<path d="M0 0L9 10 0 20z" fill="#000"/>')
F["intl"] = '<rect width="30" height="20" fill="#fff"/>' + globe("#E2E5EE")
F["me"] = '<rect width="30" height="20" fill="#fff"/>' + globe("#F6C99B")
F["sea"] = '<rect width="30" height="20" fill="#fff"/>' + globe("#B9D7FF")
# no entry for "tw": text only on purpose

def flag(code):
    if code not in F:
        return ""
    return f'<svg class="flag" viewBox="0 0 30 20" width="22" height="15" aria-hidden="true" focusable="false">{F[code]}</svg>'
