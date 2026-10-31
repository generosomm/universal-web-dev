# More skills

Read this only when a task needs something the routing table doesn't cover. Nothing here is installed by Universal Web Dev. Recommend an entry with its license and what it runs; install it only with the developer's approval, using the source's own instructions, into their skills folder. Checked on 2026-10-27; re-check before installing.

## Vetted, not installed

| Need | Skill | License | Before installing |
| --- | --- | --- | --- |
| Diagrams for docs or case studies: architecture, flows, data models | [diagram-design](https://github.com/cathrynlavery/diagram-design) | MIT | About 6 MB, with a long description every session loads. Its Python scripts run only when asked |
| A second copy pass, or a detect-only review | [no-ai-slop](https://github.com/petergyang/no-ai-slop) | MIT | Same job as the installed `humanizer`; keep one |
| A different website design direction | [Hallmark](https://github.com/Nutlope/hallmark) | MIT | Alternative to the existing director, never another simultaneous layer. Render checks need Node 18+, Chrome/Chromium and a resolvable local/global `puppeteer-core` (or its documented configured path). Rechecked 2026-10-31 |
| Finding another skill | [find-skills](https://github.com/vercel-labs/skills) | MIT | Its commands install globally with `-y` (no confirmation): show the command and get approval first |
| A demo GIF of the site for a README | [demo-gif](https://github.com/conorbronsdon/demo-gif-skill) | MIT | In maintenance mode. Needs vhs, ffmpeg or Playwright; it commits the GIF and edits the README |
| A UI finish gate grounded in real product screens | [anti-ui-slop](https://github.com/uizze/uizze) | Apache-2.0, with MIT notices | Its playbooks are derived from the installed `impeccable`, and its description matches almost every UI task. Use it instead of Impeccable's final review, never both. Its hosted reference library is optional and partly paid |

## Additional on-demand capabilities, reviewed 2026-10-31

These extend capability without increasing the installed core catalog. Review current source/license and runtime before installing or executing; browsing a reference needs no installation. Star counts and marketplace descriptions are not validation.

| Need | Source and license | Route and limits |
| --- | --- | --- |
| GSAP animation in a project using or explicitly choosing GSAP | [Official GSAP skills](https://github.com/greensock/gsap-skills), MIT skill instructions | Best new specialist: select `gsap-core` and only the relevant React, timeline, ScrollTrigger or plugin module. Do not load all eight. Check GSAP runtime terms separately; animation cleanup, reduced motion and performance still need testing |
| Design-reference research | [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md), MIT collection | Read one relevant analysis for layout/type principles, not the whole library. Adapt to this business; do not copy a brand's identity or assume all linked assets are licensed |
| Structured design tokens, lint/export | [Google DESIGN.md](https://github.com/google-labs-code/design.md), Apache-2.0 | Optional alpha format and Node tooling, not a universal skill pack. Preserve existing DESIGN.md; adopt only when useful. Token/contrast lint does not prove rendered accessibility |
| A separate design workspace with CLI/MCP integration | [OpenDesign](https://github.com/nexu-io/open-design), Apache-2.0 | Current source includes skills and headless use, beyond its desktop UI. Separate runtime/configuration and an installer that executes downloaded shell code; explicit setup choice, never a silent dependency |
| Measured component anatomy or redline sheet | [Dimensional Drawing](https://github.com/enesozturk/dimensional-drawing), MIT | Explicit documentation request only. Read its measurement skill; browser measurement required, unknown values stay unknown. Not an automatic build review |
| Reduce excessive animation | [Emil's skills](https://github.com/emilkowalski/skills), MIT | Offer its `remove-animations` specialist if existing motion guidance is insufficient; do not install duplicate versions of existing modules |
| Cinematic video-scrub landing page | [Scroll World](https://github.com/oso95/scroll-world), MIT instructions | Explicit opt-in only: large instruction file, external media-generation accounts/paid services and ffmpeg. Clarify budget, assets, phone fallback and setup first. Video scrubbing is not a true interactive 3D app |

UI/UX Pro Max, Taste, Impeccable and Emil's core skills are already covered; React Bits, Magic UI and Canvas UI are [component sources](component-sources.md). Keep the pinned Impeccable guidance-only: upstream's current hooks, binary downloads, telemetry/catalog access, live edits and subagent runtime are not installed or verified here.

## Watch list

Promising, but very new. Review the source before use.

- [deadcode](https://github.com/seanpaulforonda/deadcode) (MIT): finds unused CSS, JavaScript and imports, and deletes only after approval.
- [fullstack-audit](https://github.com/Eurie92/fullstack-audit-skill) (Apache-2.0): maps routes, components and APIs; runs an npm package through `npx`.
- [agent-qa](https://github.com/vostride/agent-qa) (Functional Source License 1.1, not open source): plain-language end-to-end tests for web apps. Needs Node 24 or later and a model provider key; link to it rather than redistributing it.

## Not recommended

| Repository | Reason, as of 2026-10-27 |
| --- | --- |
| [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) | Works in your logged-in browser profile, and its background service updates its own binary. If used at all, use a separate browser profile |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | The first time it reads a site, it copies that site's login from your Chrome |
| [ItsssssJack/SlopMonster](https://github.com/ItsssssJack/SlopMonster) | Its rewrite step sends drafts to another model's command-line tool or chat |
| [seanpaulforonda/github-repo-explainer](https://github.com/seanpaulforonda/github-repo-explainer) | Tells the agent to load and strictly follow a different local skill |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills), [normieg/Readme-gen](https://github.com/normieg/Readme-gen), [ckanthony/Chisel](https://github.com/ckanthony/Chisel) | No license file in the repository, so they can't be redistributed |
| [paulablaza/bare-research](https://github.com/paulablaza/bare-research) | Web research rather than site building; its install line points to a different organization |
| [xerj-org/xerj](https://github.com/xerj-org/xerj), [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-search tools installed by a downloaded script or pip, not website skills |
| [udaysharmadev/Gravitas](https://github.com/udaysharmadev/Gravitas), [rebelytics/one-skill-to-rule-them-all](https://github.com/rebelytics/one-skill-to-rule-them-all) | Install hooks or edit agent configuration; overlap the installed verification and skill-writing skills |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Overlaps the installed Superpowers skills, and its `prototype` name clashes with the installed one |
| [Sahil-SS9/hermes-simplify-swarm](https://github.com/Sahil-SS9/hermes-simplify-swarm) | When a test fails it runs `git checkout -- .`, which discards every uncommitted change, not only its own. It also starts three review agents after each code change |
| [Sahil-SS9/hermaguard](https://github.com/Sahil-SS9/hermaguard) | Setup uses `sudo` and a Python static-analysis toolchain; overlaps the installed code-review and security skills |
| [bergside/typeui](https://github.com/bergside/typeui) | Its `typeui-fundamentals` skill (MIT) repeats UI principles the installed `ui-ux-pro-max` covers |

Browsing directories, not vetted: [skills.sh](https://www.skills.sh), [MCP Market](https://mcpmarket.com), [Hermes Atlas](https://hermesatlas.com/lists/top-skills).
