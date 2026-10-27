# Launch Readiness check: Saltrum reference site

A real `check` run with the [Launch Readiness Score](../../../references/readiness-score.md) rubric on 2026-10-27. Nothing was changed before or after; the fixes below are left open on purpose so the example stays honest.

```text
Launch Readiness Score: 70/100, Needs work   Coverage: 21/25 (84%)
Mode: check   Site: examples/reference-site, served locally   Date: 2026-10-27
Conditions: Chromium (desktop app browser), desktop and 375×812 phone emulation, no network throttling
```

| Category | Score | Weight | Items checked | Status |
| --- | --- | --- | --- | --- |
| Works as intended | 88 | 20 | 4 of 5 | Tide planner works, all 8 in-page links resolve, no console errors |
| Works for everyone | 79 | 25 | 7 of 8 | Every measured text passes contrast; one small tap target |
| Trust and safety | 75 | 25 | 2 of 3 | No secrets; third-party font and image requests without a privacy note |
| Speed | 67 | 15 | 3 of 4 | No blocking scripts, images sized and lazy; font CSS blocks rendering |
| Found and shared | 30 | 15 | 5 of 5 | Good title and description; no canonical, share image, structured data or sitemap |

**Blockers:** none.

## Top fixes

| # | Finding | Evidence | Impact | Fix | Effort |
| --- | --- | --- | --- | --- | --- |
| 1 | No structured data | 0 JSON-LD blocks on `/` | Search engines and AI answers can't read the rooms, prices or address as facts | Add a `LodgingBusiness` JSON-LD block that matches the visible content | S |
| 2 | No sitemap.xml or robots.txt | Both return 404 | Crawlers get no index hints | Add a one-URL sitemap and a robots.txt that points to it | S |
| 3 | No canonical URL or share image | No `link rel=canonical`, no `og:image` | Shared links show no picture; duplicate URLs can split ranking | Add both to `<head>` once the domain is known | S |
| 4 | Third-party requests without a privacy note | Google Fonts and picsum.photos receive each visitor's IP address | May need disclosure for EU visitors | Self-host the font and the final photos, or add a short privacy note | M |
| 5 | Small tap target | "Ask about the whole house" link is 21 px tall at 375 px width | Harder to tap on a phone | Pad the link to at least 24 px, ideally 44 px | S |

## Not run

| Item | Why | How to run it |
| --- | --- | --- |
| HTTPS, redirects, mixed content | Not deployed | Re-run `check` against the deployed URL |
| Form failure path | The tide planner has no failure state worth forcing in a `check` | Covered by `audit` |
| Worst-case content (`break-ui`) | Not part of a quick check | Run `audit` |
| Core Web Vitals field data | No real visitors yet | PageSpeed Insights or CrUX after launch |

## Not applicable

Server validation, spam limits and consent: the site has no server, sends no form data and stores nothing in the browser. Hreflang: one language.

## Measurements behind the score

- Contrast: computed text and background colours for every visible text element; none below 4.5:1 (3:1 for large text).
- Keyboard: Tab reaches the skip link first with a 3 px solid outline; later links rely on the same focus style, partially checked.
- Phone (emulation only, so phone items count as partial at most): no sideways scroll at 375 px, date input text 20 px (no zoom on focus).
- Load (unthrottled, local): DOMContentLoaded 617 ms, load 2.1 s, mostly the remote placeholder image (1.7 s).
- 404: the local Python server returns a real 404 status but not the site's own `404.html`; that depends on the host.
- The site's own tests: 11 passed (`python -m unittest discover -s tests`).
