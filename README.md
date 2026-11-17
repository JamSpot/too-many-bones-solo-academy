# Too Many Bones Solo Academy

A research-led, multi-page solo and multi-handed learning guide for **Too Many Bones**. This is an independent fan-made learning resource and is not affiliated with Chip Theory Games.

## Website

Expected GitHub Pages URL (deployment must be verified before treating it as live):

https://jamspot.github.io/too-many-bones-solo-academy/

## Structure

- `index.html` — homepage and navigation
- `getting-started.html` — first solo session learning path and setup safeguards
- `rules.html` — verified official battle FAQ rulings
- `gearlocs.html` — character dossier framework and provisional Picket/Patches learning pair
- `tyrants.html` — Tyrant and Baddie research framework
- `expansions.html` — collection register
- `solo-strategy.html` — solo strategy and experiment plan
- `research.html` — official-source register, verified rulings and progress
- `assets/style.css` — responsive light theme
- `assets/site.js` — accessible mobile navigation
- `scripts/validate_site.py` — dependency-free local-link, navigation and required-asset checks

## Rules and research standards

1. Use ONLY Chip Theory Games rulebooks, reference sheets, FAQs, errata and official clarifications as rules authority.
2. Use official product pages only to verify product scope and contents, not to override rules.
3. Separate confirmed rules from strategic recommendations, table-tested findings and untested hypotheses.
4. Record game/expansion scope, party size, Gearlocs, Tyrant, source and page/section for rules questions.
5. Do not publish exact setup counts or numbered card sequences until every step is verified against the applicable official rulebook and Tyrant instructions.
6. Do not reproduce complete rulebooks or card text; summarise and cite official sources.
7. Do not use fan guides, forums, videos or third-party summaries as rules authority.

## GitHub Pages

The site uses plain HTML, CSS and JavaScript and does not require a build framework. The repository includes `.github/workflows/pages.yml`, which runs `scripts/validate_site.py` before uploading and deploying the site with GitHub Actions.

**One-time repository setup:** open [Settings → Pages](https://github.com/JamSpot/too-many-bones-solo-academy/settings/pages) and set **Build and deployment → Source** to **GitHub Actions** if this has not already been done. Then check the [Actions runs](https://github.com/JamSpot/too-many-bones-solo-academy/actions) and confirm the build and deploy jobs both pass before treating the website as live.

## Current status — 17 November 2026

- The eight-page navigation and responsive light theme are present.
- The Rules page now summarises eight battle-related clarifications linked directly to official CTG FAQ articles.
- The Rules page now includes the official 15 September 2026 “Gearlocs Need Food Badly” special-Encounter procedure, including critter movement, alternating activations, action restrictions and the HP-stack reward.
- The Rules and Research pages also record CTG's official clarification that only Gearlocs can have Buff HP; the first-game guide and homepage link directly to the new Encounter walkthrough.
- The Rules, First Game and Solo Strategy pages now explain CTG's official party-size clarification: party size counts Gearlocs, not human players, when someone plays multi-handed.
- The First Game page explicitly withdraws the earlier unverified Drellen deck recipe. Do not use the old 8-General-card / numbered-Special-Encounter sequence.
- Picket and Patches remain the provisional first learning pair; this is a strategy choice, not a CTG-required combination or a tested claim that they are optimal.
- The exact official Drellen setup and numbered Encounter-card sequence remain unresolved. They will not be published until checked against the current official base-game rulebook and Tyrant instructions.
- Static checks of all eight HTML pages found the navigation, stylesheet and script references present, with no broken internal page links. The new validator also passed a local eight-page fixture test.
- GitHub Pages deployment is not yet independently verified. The latest commit has no reported commit status, and the published URL could not be reached from the current verification environment.
