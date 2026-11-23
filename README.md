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
- `battle-drills.html` — six practical exercises based on official CTG FAQ clarifications
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

## Current status — 23 November 2026

- The nine-page site has a responsive light theme and shared navigation; the validator checks that every page links to all nine pages.
- The Rules page contains 15 selected official battle/Baddie clarifications and the official “Gearlocs Need Food Badly” special-Encounter walkthrough.
- Battle Drills now contains six practical exercises. The sixth covers Carcass's Meat Hooks and an Undead Baddie's simultaneous defeat trigger, including the requirement that Carcass deal the defeating blow.
- The Tyrants page records the six rulings currently listed in CTG's official Tyrants FAQ category, including Rol's movement clarification.
- The Research register includes the official Carcass FAQ and records its 3 January 2025 modification date and 23 November 2026 recheck.
- Party-size, Buff HP, Baddie skills, battle timing and special-Encounter notes remain linked to the publisher's own FAQ articles.
- The First Game page explicitly withdraws the earlier unverified Drellen deck recipe. Do not use the old 8-General-card / numbered-Special-Encounter sequence.
- The exact official Drellen setup and numbered Encounter-card sequence remain unresolved. They will not be published until checked against the current official base-game rulebook and Tyrant instructions.
- The validator checks all nine HTML pages, required assets, every page's complete navigation, local links and in-page anchors. Run `python3 scripts/validate_site.py` before publishing.
- GitHub Pages deployment must be checked in Actions after each repository update; do not treat a successful file write or local validation as proof of deployment.
