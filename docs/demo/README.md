# MatchFit scoping demo — how to edit it

One file: `index.html`. No build step, no dependencies, no server. Open it in a browser.

It is a **scoping artefact**, not the app. Its output is decisions, not code. When the amber
questions are gone, the notes are the build spec and this file can go stale.

---

## Add a screen

Append an entry to `SCREENS[]` near the bottom of the `<script>`. The rail and the router pick it
up automatically — there is no registration step.

```js
{id:'M13', app:'Member app', name:'Claims history',
 ix:1,                        // optional: marks an integration point, puts a dot in the rail
 frame:'desk',                // optional: 'desk' renders browser chrome instead of the phone
 dark:1,                      // optional: scoped dark chrome (used by the coach portal)
 notes:[
   'Plain string — how the screen behaves and what it is for.',
   ['new','Green — what changes versus today.'],
   ['q','Amber — an open question, with the trade-off stated.'],
 ],
 html:()=>`${sb()}${hd('Claims history','All claims this season.')}
   ${lrow(ic('doc',17),'var(--surface-2)','var(--ink)','CLM-4473','MRI scan · 15 May',pill('DONE','ok'))}
   </div>${tabbar(TABS_M,1)}`},
```

Reorder the array to reorder the app. IDs are stable and used in the rail, the URL hash and the
flow map, so **do not renumber an existing screen** — a link in `FLOW[]` will break silently.

### The `html()` contract

Every screen is a pure function returning an HTML string. No state, no lifecycle.

It must open with `sb()` (the status bar) and close with `</div>` plus a `tabbar(...)` for phone
screens. The opening `<div class="body">` is supplied by `sb()`'s sibling in the router, so the
stray closing `</div>` before `tabbar` is deliberate — it closes `.body`.

Desktop screens (`frame:'desk'`) skip both: no status bar, no tab bar.

---

## Write the notes

**The notes are the deliverable.** If a screen has no notes it is not finished.

| Form | Renders | Use for |
|---|---|---|
| `'text'` | plain | how the screen behaves, what it is for |
| `['new','text']` | green | what changes versus today |
| `['q','text']` | amber | an open question, **with the trade-off stated** |

Write open questions with the tension in them. Not *"do we build card checkout?"* but *"card
checkout is 3–4× the build and makes us the retailer, liable for goods we never handle — decide
against the launch date, not on preference."* A question with the cost attached gets answered.

As answers land, an amber note becomes a plain note or a `['new',...]`. When the amber is gone,
the scope is settled.

---

## Change the palette

Everything lives in `:root`. Change it there and the whole artefact re-skins.

**Two rules that will bite you if you ignore them:**

1. **A colour that works as a fill can fail as text.** WCAG wants 4.5:1 for text but only 3:1 for
   UI components. Three of this palette's colours failed the gate and have `-text` variants:

   | Token | Fill | As text on white | Text variant |
   |---|---|---|---|
   | `--brand-3` green | ✓ 3.58:1 | ✗ fails | `--ok-text` #14764D, 5.63:1 |
   | `--warn` amber | ✓ 3.77:1 | ✗ fails | `--warn-text` #8A5A12, 5.91:1 |
   | `--sp-netball` | ✓ 4.12:1 | ✗ fails | `--netball-text` #A8541A, 5.32:1 |

   Use the fill token for bars, badges and backgrounds. Use the `-text` token for any type,
   including currency amounts.

2. **Never build a gradient from a themed token.** `--grad`, `--card-*`, `--chip` and `--qr-quiet`
   are pinned to literal hexes and are **not** re-pointed in the dark block. The member card was
   originally built from `--sp-rugby` and silently turned mint in dark mode — caught by looking at
   a screenshot and by nothing else.

Re-run the gate after any palette change:

```bash
python tools/contrast.py
```

### Dark mode

The `[data-theme="dark"]` block re-points tokens. `--brand-1` and `--brand-2` stay put, because
they are chrome and `--ink` is type — inverting one would break the other.

The dark tints are **hand-picked, not derived.** Mixing the dark background toward each hue gives
mud. These lean into their hue instead and sit within **1.09:1** of each other in luminance, so
they separate by hue rather than lightness.

**Consequence:** the state system must not rely on colour alone. Every status pill carries a text
label (`COVERED`, `LAPSED`, `BLUE CARD`, `UNINSURED`). Keep it that way.

---

## The flow map

`FLOW[]` is one lane per path, one node per step.

```js
{ln:'Path B · The injury loop', nodes:[
  ['Injury on the field','Official match or practice'],      // exists today
  ['Emergency tab','Four pathways','M6','new'],               // links to M6, new in this build
  ['Pick facility','Capability-tagged directory',null,'gap'], // known gap
  ['Clear funds to card','Oneplan card API','M7','partner'],  // another system
]},
```

Node styles: omitted = exists today · `new` · `gap` · `partner`.

The flow map is the highest-value screen here. It is the one thing a board absorbs in thirty
seconds, and the six red `gap` nodes are how you get a room to agree where the risk actually is.
Four of them sit in **Path D**, the catastrophic HNS pathway.

---

## Currency and numbers

South African conventions, and they are not the JS defaults:

```js
money(1799)  // "R 1 799,00"  — space thousands, comma decimal
rnd(250000)  // "R 250 000"   — no decimals, for large round figures
```

Every figure carries `class="num"` for `font-variant-numeric:tabular-nums`. Without it, columns of
numbers do not align and the whole thing looks amateur.

---

## Placeholder names

Sponsors and suppliers are **generic placeholders** by design: "National Motor Group", "Insurance
Partner", "Sportswear partner A", "Supplement partner B". No real company is named anywhere.

Keep it that way while the artefact is public. If you swap in a real sponsor for a specific
pitch, do it on a branch and do not merge it — a named sponsor on a public URL reads as a signed
sponsor, and that is a conversation you do not want to have in a board meeting.

---

## Acceptance checklist

- [x] Opens from `file://` with no console errors
- [x] Every screen reachable from the rail; the URL hash routes and survives a reload
- [x] Every screen has notes, and every screen has at least one open question
- [x] Flow map renders; all 18 linked nodes resolve to a real screen
- [x] Theme toggle works; both themes screenshotted and eyeballed
- [x] No hardcoded hex outside `:root` and `[data-theme="dark"]`
- [x] Card face and gradient identical in both themes
- [x] Contrast gate run; every text colour clears 4.5:1 in both themes
- [x] State system readable without colour — every pill carries a label
- [x] All figures use tabular numerals; currency is `R 1 799,00`
