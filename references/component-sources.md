# Component sources

Read this only when a task adds icons or a ready-made interactive component. These sources are optional and used on demand; this skill does not install or pin them. All of them are React. Before adding one, confirm the project uses React, the chosen design direction wants the effect, and the license allows it; follow the upstream README for setup.

Rules for every source:
- One icon family per site, and at most one signature interactive piece per page.
- Motion only where it means something. Respect `prefers-reduced-motion`, adding a fallback when the component has none.
- Keep keyboard and screen-reader access. Don't install a package for an effect a few lines of CSS can do.
- Install only the package names listed here. For anything else, take the install line from that component's own README and confirm the npm maintainer or repository matches; never guess a package name from a display name.

| Need | Source | How to add | Notes |
| --- | --- | --- | --- |
| Animated icons | [lucide-animated](https://github.com/pqoqubbw/icons) by pqoqubbw, MIT | `npx shadcn@latest add https://lucide-animated.com/r/<name>.json` | Adds one component file and `motion`; ships no reduced-motion fallback |
| Playful physics pieces | [FeralUI](https://feralui.dev) by Sarthak Navalekar ([mortspace](https://github.com/mortspace)) | npm: `pullcord`, `playcaptcha`, `feral-blob`, `feral-fur` (not `fur`, which is someone else's package). Copy `src` from the GitHub repo: `stamp`, `liquid-glass-tip` | MIT per repo. Other pieces on the site are demos; DeskFolio and AniMaps have no license, so don't copy them |

FeralUI's claw-machine captcha (`playcaptcha`) is a playful check that runs in the browser, not bot protection. Keep server-side rate limits and spam defenses, and offer an accessible way through. Its Gradient Builder exports gradients; use them only when the chosen direction allows gradients.
