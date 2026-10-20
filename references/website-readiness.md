# Website readiness

Use at kickoff and release review; inspect only affected sections for a small feature. Record verified evidence, pending work or not applicable with a reason in the project's existing tracker; every item fits the site being built, so a portfolio with no forms gets no invented bot defense. A checklist entry is not proof or authorization to expand the task. Prioritize actual exposure and the agreed release scope.

## Privacy and policy pages

- Privacy policy: describe actual data, purposes, providers, retention, contact and user choices. Include browser storage and analytics where used. Verify jurisdiction-specific requirements from current official guidance when drafting; don't invent guarantees or declare legal compliance.
- Terms and conditions: evaluate the site's accounts, user content, rules, services and audience. Draft only terms that match implemented behavior; flag unresolved owner/legal decisions. Neither page is universally mandatory merely because the site exists.
- Cookie/storage consent: inventory cookies, localStorage, trackers, embeds and similar technologies, their purposes and applicable requirements. Add a consent mechanism when needed; no decorative banner. Where consent is required, block affected nonessential technologies until consent, support reject/withdraw, and persist the actual choice. Don't assume cookieless tracking is automatically exempt. Explain a not-applicable decision.

## Security and abuse

- Secrets: no privileged API keys, database credentials, service-role keys or private tokens in browser code, public build variables, assets, logs or Git. An .env file does not make a bundled value private. Distinguish provider-documented public/publishable configuration from secrets; public keys still require server authorization/RLS and appropriate restrictions. Check affected source/build/config without printing sensitive values. Handle a discovered leak with the owner through the authorized revocation/rotation workflow.
- HTTPS: verify production HTTPS, HTTP redirects, certificate validity, mixed content and secure session configuration. Verify rather than assume hosting defaults. Changes to security policy must fit the actual host and app.
- Forms and abuse: visible labels, accessible field errors, useful loading/success/failure feedback, and server validation/authorization at trust boundaries. Use relevant rate/size limits and spam defenses on public forms/auth/score endpoints. Add bot challenges only when justified; don't block genuine users or rely on client checks.

## Discovery and sharing

- Accurate, distinct meta titles/descriptions on public routes; canonical URLs and social metadata. Verify delivered HTML for the intended crawler, not only an updated browser title.
- A product-specific social preview image and favicon: valid public paths, appropriate dimensions/formats, no private data, and rendered/share-preview checks where available.
- One h1 per page that names it, then headings in order without skipped levels; headings describe sections, not styling.
- Structured data (schema.org JSON-LD) only for what the page really is (organization, local business, product, article, event, FAQ), matching visible content; validate it. Multilingual sites add reciprocal hreflang, with x-default for the fallback page.
- Generate sitemap.xml and robots.txt where appropriate to public indexing. Include canonical public pages only; check deployment hostname and preview/staging behavior. robots.txt is not access control or a reliable way to prevent indexing. Keep private routes authenticated; use appropriate indexing controls separately.

## Usability and accessibility

- One clear primary action per screen or task; secondary actions remain available with clear hierarchy. Don't paste "follow me for more" into the product.
- Meaningful image alt text; decorative images use empty alt. Icon controls have names; decorative icons are hidden from assistive technology. Give 3D/canvas content an appropriate textual alternative and usable controls.
- Measure text/control contrast, keep visible keyboard focus, semantic headings/labels, predictable navigation and reduced-motion support. Don't certify accessibility from visual inspection alone.
- Mobile-friendly layout: small phone, tablet and desktop checks, zoom/reflow, touch targets, landscape where relevant, and no hidden critical controls or unintended horizontal scroll. Label viewport emulation honestly.
- Helpful custom 404 with a recovery link; correct not-found HTTP status where supported. Check internal/external links, deep links, navigation and recovery. A screen labelled 404 returning 200 is not automatically a correct HTTP 404.

## Assets, speed and analytics

- Compress/resize images, use suitable modern formats and responsive sources, set dimensions, and lazy-load noncritical media. Don't degrade essential visual quality or lazy-load the primary hero indiscriminately.
- Measure representative initial load and the critical user interaction, including mobile and heavy 3D routes. Record tool, route, conditions and actual findings; fix material bottlenecks. Don't invent performance scores or guarantee a target from a build alone.
- Find slow resources: scripts, styles, fonts and images that block rendering or load slowly on a throttled mobile connection; defer, shrink or remove them. Remove third-party scripts, pixels and embeds nobody asked for.
- Analytics: evaluate a concrete measurement goal, approved provider, minimized data and consent requirements. Configure only when in scope and authorized; don't install tracking by default or send personal data/secrets in events. If enabled, verify events and relevant consent behavior. Otherwise record deferred/not applicable.

## Who checks what

Use the installed skills instead of improvising, each once at release and only when its area applies:

| Area | Skill |
| --- | --- |
| Accessibility, contrast, performance, responsive layout | `impeccable`, once per release: `audit` when a measured report is needed, otherwise the `polish` pass, never both; `optimize` only for a page measured as slow. Without its launcher, do the detector's checks by hand with available tools |
| Worst-case content: long names, empty lists, huge numbers, other scripts | `break-ui` |
| Real-phone feel: viewport height, input zoom, notch, tap states | `mobile-native` |
| Security review the developer requests | `security-best-practices` (backend profile) |
| Final evidence before calling it done | `verification-before-completion` |

For a human second opinion, free tools such as Chrome's Lighthouse or Plerdy's SEO Analyzer and UX & Usability Testing extensions show SEO issues and predicted attention. Treat their scores and heatmaps as hints, not pass/fail gates, and run AI page-review tools only on pages that hold no private data.

## Sources for implementation checks

Use current official guidance for the actual provider and audience. These are starting references, not universal jurisdiction rules:

- [OWASP frontend security](https://cheatsheetseries.owasp.org/cheatsheets/Web_Frontend_Security_Cheat_Sheet.html)
- [ICO storage/access technologies, UK scope](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/what-are-storage-and-access-technologies/)
- [Google robots.txt guidance](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
