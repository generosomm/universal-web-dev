# Built-in fallback

Read only the section for a routed skill that is not installed. Tell the developer which skill was missing and that this shorter fallback was used; installing the companion skills ([INSTALL.md](../INSTALL.md)) gives the full version. These are minimums, not replacements.

## Discovery and planning

Use [discovery](discovery.md) and [bootstrap](project-bootstrap.md). Reuse approved decisions, recommend defaults and keep records proportional to the project. A companion's absence is not a reason to stop a clear task.

## Motion and component usability

Reuse native semantic controls and existing patterns. Animate only for a useful state change or the accepted visual direction. Support keyboard, focus, reduced motion and touch; measure rendering cost before adding a heavy effect. Prefer no animation to a broken or inaccessible one.

## Reviews and execution workflow

Read the existing plan/current slice, implement the smallest complete change, inspect its diff and run the relevant checks. Preserve unrelated edits. Use isolated work only when needed, respecting the host's Git rules. Do not invent an independent reviewer or spawn agents without authorization. Branch integration/publication follows the user's actual request, not a missing skill's assumed workflow.

## Design direction (`design-taste-frontend`, `frontend-design`, `impeccable`)

- Before layout, write one sentence on what makes this business different and let it choose the layout, type and palette. Reuse an accepted design or brand instead.
- Avoid the generic AI page: centred hero over a soft gradient, three icon cards, purple-blue gradients, glass cards, emoji icons, stock "trusted by" logo rows, every section the same width and rhythm.
- One type pairing with a real scale, one accent colour used sparingly, spacing from a fixed scale, real or clearly placeholder content (never invented testimonials, numbers or logos).
- Check in a real browser at phone and desktop width: hierarchy reads in one glance, nothing overlaps or overflows, hover, focus, loading, empty and error states exist.

## Debugging (`systematic-debugging`)

Reproduce the bug, read the full error, find where good data turns bad, test one hypothesis at a time with the smallest change, and add a test that fails before the fix and passes after. After two failed fixes, stop and re-examine the assumption.

## Tests (`test-driven-development`, `verification-before-completion`)

Write the failing test for the new behaviour first, then the code. Before saying done, run the project's real test and build commands and read the output; report anything not run.

## Copy (`humanizer`)

Rewrite from the developer's own words. Cut filler, hype, "not X but Y" contrasts, one-line closers and stacked triads; keep every fact and add none.

## Release checks (`break-ui`, `mobile-native`, `webapp-testing`)

Try the main screens with very long text, empty lists, huge numbers and other scripts. On phones, check input zoom (16px minimum font size), safe areas, sticky hover and tap targets. Walk the critical flow in a browser and read the console. Label anything checked only in emulation.

## Speed and search (`performance`, `core-web-vitals`, `seo-aeo-best-practices`)

Measure before changing: one throttled phone load of each main route, then fix the largest measured cost first (hero image, blocking scripts, fonts, layout shifts). For search, use the "Found and shared" items in [the readiness score](readiness-score.md#categories-and-items).

## Minimal code (`ponytail`)

Make the smallest change that fully solves the task, reuse what the project has, add no dependency or abstraction without a concrete need, and explain the change in a few lines.
