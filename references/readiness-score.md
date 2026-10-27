# Launch Readiness Score

Read this when the developer asks to `check` or `audit` a site, asks "is it ready to launch?", or asks for a `handoff` report. The score turns [website readiness](website-readiness.md) into one number with evidence behind every point. It is never estimated: every item is scored only from a check that actually ran.

## Modes

| Request | Scope | Output |
| --- | --- | --- |
| `check` | The home page and the one critical flow; static reading plus one real browser load | Score, coverage, blockers and the top five fixes |
| `audit` | Every public route and flow; every applicable item below, measured where possible | The full report below |
| `handoff` | The latest audit or check, rewritten for a client or non-developer | What was built, how it was tested, the score, open items and who owns them |
| `compare` | Two real runs of the same mode on the same routes | Both scores and what changed; never a projection |

Use `webapp-testing` (or the host's own browser tool) for browser checks, `performance` and `core-web-vitals` for speed, `seo-aeo-best-practices` for search items, and the skills named in [who checks what](website-readiness.md#who-checks-what) for the rest. Do not change code during `check` or `audit` unless asked; report first.

## Categories and items

Each category scores 0 to 100 from its applicable items. The total is the weighted sum.

| Category | Weight | Items |
| --- | --- | --- |
| Works as intended | 20 | The critical flow completes end to end; forms submit, validate and show success and failure; no console errors on load or during the flow; internal links and deep links resolve; real 404 status with a recovery link |
| Works for everyone | 25 | Measured text and control contrast; visible keyboard focus and full keyboard use; labels, alt text and named icon buttons; one h1 and ordered headings; reduced-motion support; small phone, tablet and desktop layouts without lost controls or sideways scroll; the [phone checks](website-readiness.md#phones) that apply; worst-case content (`break-ui`) on main screens |
| Trust and safety | 25 | No secrets in browser code, build output or Git; HTTPS with redirects and no mixed content; server-side validation and authorization at trust boundaries; spam and rate limits on public forms and auth; privacy policy and terms that match real behaviour; consent only where nonessential storage or tracking exists |
| Speed | 15 | Measured load of the main routes on a throttled phone profile; images sized, compressed and lazy where noncritical; no render-blocking or unused heavy scripts, fonts or embeds; Core Web Vitals from field data when it exists, otherwise labelled lab-only |
| Found and shared | 15 | Distinct titles and descriptions; canonical URLs; social preview image and favicon; structured data that matches visible content; sitemap.xml and robots.txt for public indexing; hreflang for multilingual sites |

## Scoring rules

- Mark each applicable item **pass** (1), **partial** (0.5) or **fail** (0), with the evidence: route, tool or command, conditions, and what was seen.
- **Not applicable** items need a reason and are left out of the total; they never lower or raise the score.
- **Not run** items (missing tool, no deployed URL, no real device) are left out of the score, listed with the command or step that would run them, and lower **coverage**: checked items ÷ applicable items. A check made only in viewport emulation is at most partial for a phone item.
- Show coverage beside the score every time. Below 80% coverage, label the score provisional.
- **Blockers** cap the verdict at "Not ready" whatever the number: an exposed secret, a broken critical flow, no HTTPS in production, a form or login that accepts unauthorized actions, or a page that cannot be used with a keyboard.
- Verdicts: 90 and up **Ready**, 75 to 89 **Almost ready**, 50 to 74 **Needs work**, below 50 **Not ready**.
- Never predict a future score, invent a metric, or quote a statistic without a source. After fixes, run the same mode again and use `compare`.

## Findings

Write each failed or partial item as:

- **Finding**: what is wrong, in one line.
- **Evidence**: where and how it was observed.
- **Impact**: who it affects and how.
- **Fix**: the concrete change, with a ready-to-paste snippet when short.
- **Effort**: S (under 30 minutes), M (under half a day) or L (longer).

Order fixes by blockers first, then impact against effort.

## Report

```text
Launch Readiness Score: <score>/100, <verdict>   Coverage: <checked>/<applicable> (<percent>%)<, provisional>
Mode: <check|audit>   Site: <url or path>   Date: <date>   Conditions: <browser, device profile, network>

| Category | Score | Weight | Items checked | Status |
| Blockers: <none | list>
| Top fixes: # | Finding | Impact | Effort
| Not run: item | why | how to run it
| Not applicable: item | reason
```

For `handoff`, keep the score line, replace jargon with plain words, and list open items with an owner (developer, client or host). Do not include secrets, private URLs or personal data.
