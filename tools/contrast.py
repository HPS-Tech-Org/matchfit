"""WCAG contrast gate for the MatchFit palette.

Run after ANY palette change:  python tools/contrast.py

Anything below 4.5:1 that is used as TEXT needs a -text variant. Mix the colour
toward black on light backgrounds, toward white on dark, in 2% steps, until it clears.
A colour can be a perfectly good progress bar at 3.2:1 and an inaccessible number.
"""

def _s(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(h):
    h = h.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return .2126 * _s(r) + .7152 * _s(g) + .0722 * _s(b)


def cr(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + .05) / (min(la, lb) + .05)


LIGHT_BG, DARK_BG = '#FFFFFF', '#1A2027'

LIGHT = {
    'brand-1':      '#151C25',
    'brand-3 (ok)': '#1D9A66',   # FILL only
    'brand-4':      '#8E1F1C',
    'danger':       '#C0392B',
    'warn':         '#B5761A',   # FILL only
    'ink':          '#111823',
    'ink-2':        '#4F5966',
    'sp-rugby':     '#17643E',
    'sp-soccer':    '#22499E',
    'sp-hockey':    '#0C7B80',
    'sp-netball':   '#C2631F',   # FILL only
    'partner-line': '#1B3C8C',
    'partner-2':    '#D6001C',
    'ok-text':      '#14764D',
    'warn-text':    '#8A5A12',
    'netball-text': '#A8541A',
}

DARK = {
    'ink':          '#E8EAEC',
    'ink-2':        '#A7ADB2',
    'muted-1':      '#959CA3',
    'ok-text':      '#5BC28C',
    'warn-text':    '#DDA455',
    'netball-text': '#E09257',
    'danger':       '#E58C89',
    'sp-rugby':     '#5FBF8E',
    'sp-soccer':    '#7FA3E8',
    'sp-hockey':    '#57C2C7',
    'partner-line': '#6F9FE8',
    'partner-2':    '#E8918E',
}

# dark tints are hand-picked to lean into hue, not derived from the background
DARK_TINTS = {
    'ok': '#12281E', 'warn': '#2A2214', 'bad': '#2A1717', 'info': '#1A222B',
    'rugby': '#0F2419', 'soccer': '#16203A', 'hockey': '#0E2427', 'netball': '#2B1D12',
}

FILL_ONLY = {'brand-3 (ok)', 'warn', 'sp-netball'}

fails = 0
for bg, label, palette in [(LIGHT_BG, 'light', LIGHT), (DARK_BG, 'dark', DARK)]:
    print(f'--- on {label} surface {bg} ---')
    for name, hexv in palette.items():
        r = cr(hexv, bg)
        verdict = 'text OK' if r >= 4.5 else 'UI/large only' if r >= 3.0 else 'FAIL'
        flag = ''
        if r < 4.5 and name not in FILL_ONLY:
            flag = '   <-- needs a -text variant'
            fails += 1
        elif r < 4.5:
            flag = '   (fill only, by design)'
        print(f'  {name:<15}{hexv}  {r:5.2f}:1  {verdict}{flag}')
    print()

print('--- dark tint separation (rule 5) ---')
ls = {n: lum(h) for n, h in DARK_TINTS.items()}
for n, h in DARK_TINTS.items():
    print(f'  {n:<9}{h}  lum {ls[n]:.4f}')
spread = (max(ls.values()) + .05) / (min(ls.values()) + .05)
print(f'  spread {spread:.2f}:1 -> they separate by HUE, not lightness.')
print('  So every status must also carry an icon or a text label. Do not rely on colour.')

print()
print('GATE FAILED' if fails else 'GATE PASSED - every text colour clears 4.5:1 in both themes')
raise SystemExit(1 if fails else 0)
