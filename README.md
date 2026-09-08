# MatchFit

School sport injury cover. A servicing and rewards platform over an Oneplan ActiveCare policy,
underwritten by Bryte.

This repo currently holds the **scoping demo** — a single-file clickable prototype with the spec
written into it, screen by screen. It exists to settle flow, information architecture and feature
scope before any plumbing is written.

```
docs/
  index.html          redirect, so the bare Pages URL lands on the scoping demo
  demo/
    index.html        the scoping artefact: screens + the spec, side by side
    README.md         how to add a screen, change the palette, edit notes
  app/
    index.html        the working demo: interactive, five personas, real flows
tools/
  contrast.py         the WCAG gate — run after any palette change
```

## Two artefacts, two jobs

| | `docs/demo/` — scoping | `docs/app/` — working |
|---|---|---|
| Job | settle scope and flow | show it behaving |
| State | none, every screen a pure function | one state object, real interactions |
| Read it for | the notes column and the flow map | the claim clearing funds |

They are linked, not merged. Every screen in the scoping demo has a **Try this flow →**
button that opens the working demo at the matching persona and tab, and the working demo has a
**← Back to the spec** link that returns to the screen you came from.

Keeping them separate is deliberate. The scoping artefact's value is that a stakeholder reads
the spec beside the screen; interactivity competes with that, and a stateless file can be
regenerated screen by screen without touching the rest.

## View it

Open `docs/demo/index.html` in any browser. No build step, no dependencies, no server.

Hosted:

- **Roadmap — https://hps-tech-org.github.io/matchfit/#ROADMAP** (start here)
- Scoping demo — https://hps-tech-org.github.io/matchfit/
- Working demo — https://hps-tech-org.github.io/matchfit/app/

## What it is

18 screens across five personas — member app, dependant login, coach portal, school console and
partner portal — plus a six-lane process map. Every screen carries its spec in the right-hand
column, in three forms:

- **plain** — how the screen behaves
- **green** — what changes versus today
- **amber** — an open question, with the trade-off stated

**When the amber notes are gone, the scope is settled and the notes are the build spec.**

## What it is NOT

Not the app and not its starting code. No backend, no state, no persistence, no routing library.
It gets thrown away, and that is fine — its output is decisions.

## The roadmap

Four phases, each shippable on its own. Open the **Roadmap** view in the demo for the full version;
every screen also carries a phase badge in the rail.

| Phase | Scope | Screens |
|---|---|---|
| **1 · MVP** | Web app only. Onboard policyholders over 18 and hand the application to Oneplan. Proven live at a Golden Oldies tournament: activation stand, QR code, policy sold on the spot. | M1–M5 |
| **2 · Schools & dependants** | Whole-school onboarding via fee inclusion or school referral. Dependant logins. Emergency and concussion pathways. Native iOS and Android. | M6–M8, D1, C1–C2, S1 |
| **3 · Shop & cross-sell** | Member pricing, batch track-and-trace, referrals for additional insurance to policyholders over 18. | M9–M12, X1–X2 |
| **4 · Sports integration** | A tracker with rewards, and progressive feature expansion. Last, deliberately. | — |

## What we need from Oneplan to scope and price

**Phase 1 is blocked on two answers, and only two:**

1. **The onboarding endpoint.** Field-level payload, authentication, validation rules, sandbox
   access, and what a successful response returns.
2. **Premium collection.** Oneplan-initiated DebiCheck mandates, card strikes or debit orders —
   it decides whether the app captures a mandate or simply hands over.

Also for Phase 1: whether supporting documents are needed at onboarding, what communication
Oneplan sends once a policy is active, and how claims are handled before the app carries them.

**Phase 2** turns on whether Oneplan has claims APIs, whether premiums are collected in-app, and
whether we build school- and club-specific tenants. **Phase 3** turns on who holds the merchant
account, and what regulatory review each new revenue line needs.

Every one of these sits on a screen in the demo as an amber note, next to the thing it affects.

## Two things missing from the client's scope

- **A coach or school portal.** Concussion pathway 4 starts on a field, pathway 1 usually starts
  with a coach, and the fee-bundled distribution plan runs through schools. An app only a parent
  can open leaves an injured child at an away fixture with nothing. Both are drawn here (C1, C2,
  S1) as the argument for putting them in phase 1.
- **Netball and hockey depth.** The school console shows netball and hockey are 64 of 148 enrolled
  players. A rugby-shaped product understates this book by nearly half.

## Placeholder content

Every sponsor and supplier name is a **generic placeholder** — "National Motor Group", "Insurance
Partner", "Sportswear partner A" and so on. No real company is named and none is a signed partner.
Player names, member numbers, claim references, fund balances and savings figures are fictional.
Cover limits are taken from the Oneplan SportActive brief and remain unverified against policy
wording.

"MatchFit" is an unregistered working name. Trademark clearance across CIPC, SA classes 36 and 42,
IP Australia and both app stores has **not** been run.

## Enable GitHub Pages

Settings → Pages → Source: **Deploy from a branch** → Branch `main`, folder `/docs` → Save.

The site appears at `https://<owner>.github.io/matchfit/` within a minute or two.

The artefact is safe to share: the spec notes cover product and scoping decisions only. Internal
commercial positions — pricing splits, margin structure and negotiating stances — are deliberately
kept out of this repo and live in HPS's own planning documents instead.
