# Web quality baseline

Use for new builds and releases; select affected areas for edits. Reviewed 2026-10-31. Re-check official sources when versions, browser support or requirements affect a decision. "Modern" means useful, accessible, fast and maintainable for the target audience; it does not require every new API or visual trend.

| Area | Default and evidence |
| --- | --- |
| Accessibility | Aim for WCAG 2.2 AA: semantic controls, keyboard operation, visible/unobscured focus, labelled forms, useful errors, text alternatives, zoom/reflow and measured contrast. Check touch target requirements and applicable exceptions. Use automated checks plus manual interaction; do not claim conformance from one scan |
| Browser support | Agree a browser/device audience. Check MDN compatibility/Baseline for unfamiliar APIs, use feature detection and progressive enhancement for optional effects, and test representative target engines. A newly available feature may still need a fallback for older devices |
| Performance | Measure relevant routes and critical interactions. Core Web Vitals good thresholds: LCP <=2.5 s, INP <=200 ms, CLS <=0.1 at the 75th percentile, assessed separately for mobile/desktop. Distinguish lab diagnostics from real field data; no invented passing score |
| Functionality | Follow [completion evidence](feature-completion.md): real outcomes, persistence, relevant denied/failure cases and honest provider verification |
| Trust and security | Server authorization/validation, safe session handling, HTTPS, dependency/version checks, protected secrets, bounded resource use and safe user content. Use the relevant OWASP ASVS requirements for the actual exposure; no blanket certification |
| Content and discovery | Accurate content and metadata, usable links/deep routes/404, licensed assets, appropriate indexing/canonicals and sharing previews. Structured data reflects visible facts. Never promise search or AI-answer rankings |
| Operations | Reproducible setup/build, environment example without secrets, suitable migration/backup/recovery for stored data, useful safe errors/logging and a verified deployment procedure. Add monitoring when the system's risk warrants it |

Account for privacy, consent and policy requirements for the actual audience and data. Check current official jurisdiction guidance when applicable. A banner or generic legal template is not proof of compliance. See [website readiness](website-readiness.md) for release details.

## Sources

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Web Platform Baseline](https://web.dev/baseline)
- [Core Web Vitals](https://web.dev/articles/vitals)
- [OWASP ASVS](https://asvs.owasp.org/)

For unfamiliar stacks or capabilities (CMS, localization, realtime, offline/PWA, web games, 3D, AI features), use current official framework/provider documentation and a narrowly relevant specialist if available. Identify setup, cost and verification requirements first. Do not claim knowledge of every platform or add a dependency simply to fill a catalog.
