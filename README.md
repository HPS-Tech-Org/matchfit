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

- Scoping demo — **https://hps-tech-org.github.io/matchfit/**
- Working demo — **https://hps-tech-org.github.io/matchfit/app/**

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

## The decisions it is waiting on

Six amber questions carry real cost. In rough order of what they move:

1. **Onboarding pattern (M5).** Oneplan-hosted handoff, as drawn, keeps HPS outside FAIS. Fully
   native in-app onboarding is more seamless and makes MatchFit the party presenting the product,
   which needs an FSP with a rep register, compliance officer, PI cover and Ombud exposure.
   **This one changes the price of the whole build.**
2. **Shop payment model (M9).** Vouchers redeemed at the partner, or card checkout in-app.
   Checkout is roughly 3–4× the build and brings PCI scope, fulfilment and returns with it. It
   also decides who is the seller of record, and therefore who owns Consumer Protection duties.
3. **Facility directory (M7).** Nobody owns a hospital list tagged for casualty, ICU and trauma
   capability. It gates emergency pathways 1 and 2 both, and wrong data sends a child to the
   wrong hospital.
4. **Emergency dispatch (M6).** API or phone call? Whether pathway 2 can be automated at all
   depends on the answer, and nobody has asked ER24 yet.
5. **The insured-only contradiction (M6).** Emergency is scoped to insured players, but the HNS
   Fund pays out whether or not a player is insured. So who triggers it for an uninsured player?
6. **Dependant login age floor (M2, D1).** POPIA needs the competent person's consent for a
   child's data. A 16-year-old with their own login is uncontroversial; a 10-year-old is not.

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
