# Component sources

Read this only when a task adds icons or a ready-made component. Reusing a maintained component saves code and tokens; these sources are optional and this skill does not install or pin them. Most are React with Tailwind and the shadcn CLI. Before adding one, confirm the project's stack matches, the chosen design direction wants the effect, and the license allows the use.

## Make it look like it belongs

- Restyle every piece to the project's tokens: its colours, typeface, radius and spacing. Remove the library's demo palette, glows and gradients.
- Pick pieces that serve the page's idea. Many showcase effects (aurora and gradient backgrounds, glowing borders, glass cards, logo marquees, sparkle text) are the generic AI look the direction skills ban; use them only when the direction asks for them.
- One icon family per site, and at most one signature interactive piece per page.
- Motion only where it means something, with a `prefers-reduced-motion` fallback when the component has none. Keep keyboard and screen-reader access.
- Check it rendered at phone and desktop widths before calling it done. Don't install a package for an effect a few lines of CSS can do.

## Install safely

- Use the install command from the component's own page or README, copied exactly; never guess a package or registry name from a display name.
- For npm packages, confirm the maintainer or repository matches the source below.
- Components copied into the project become its code: keep the license notice the source asks for.

## Sources

| Source | License | Good for |
| --- | --- | --- |
| [FeralUI](https://feralui.dev) (mortspace) | MIT per piece | Playful physics. npm: `pullcord`, `playcaptcha`, `feral-blob`, `feral-fur` (not `fur`, another author's package). Copy `src`: `stamp`, `liquid-glass-tip`. DeskFolio and AniMaps have no license: don't copy |
| [Motion Primitives](https://motion-primitives.com) | MIT | Restrained motion building blocks, such as text effects |
| [Magic UI](https://magicui.design) | MIT | Animated sections and effects; filter hard against the generic-look list above |
| [Cult UI](https://www.cult-ui.com) | MIT | Tactile shadcn components: docks, toolbars, expandable cards |
| [Animata](https://animata.design) | MIT | Small interaction and animation snippets |
| [React Bits](https://reactbits.dev) | MIT + Commons Clause | Text, background and interactive effects |
| [Animate UI](https://animate-ui.com) | MIT + Commons Clause | Animated versions of common shadcn components |
| [Sonner](https://sonner.emilkowal.ski) | MIT | Toasts that feel physical |

Commons Clause allows the components inside websites and apps, including paid client work. It forbids distributing the components themselves, paid or free: no UI kit, starter, boilerplate or website template that ships them.

## Icons

| Source | License | Notes |
| --- | --- | --- |
| [Lucide](https://lucide.dev) | ISC | Default outline set, framework packages for most stacks |
| [lucide-animated](https://lucide-animated.com) (pqoqubbw) | MIT | `npx shadcn@latest add https://lucide-animated.com/r/<name>.json`; adds `motion`, no reduced-motion fallback |
| [itshover](https://itshover.com) | Apache-2.0 | Animated hover icons |
| [Tabler](https://tabler.io/icons), [Phosphor](https://phosphoricons.com) | MIT | Larger sets; Phosphor has several weights |

FeralUI's claw-machine captcha (`playcaptcha`) runs in the browser and is not bot protection: keep server-side rate limits and spam defenses, and offer an accessible way through.
