# More skills

Read this only when a task needs something the routing table doesn't cover. Nothing here is installed by Universal Web Dev. Recommend an entry with its license and what it runs; install it only with the developer's approval, using the source's own instructions, into their skills folder. Checked on 2026-10-27; re-check before installing.

## Vetted, not installed

| Need | Skill | License | Before installing |
| --- | --- | --- | --- |
| Diagrams for docs or case studies: architecture, flows, data models | [diagram-design](https://github.com/cathrynlavery/diagram-design) | MIT | About 6 MB, with a long description every session loads. Its Python scripts run only when asked |
| A second copy pass, or a detect-only review | [no-ai-slop](https://github.com/petergyang/no-ai-slop) | MIT | Same job as the installed `humanizer`; keep one |
| A different website design direction | [Hallmark](https://github.com/Nutlope/hallmark) | MIT | Overlaps the installed design skills. Needs Node 18 or later, and its browser checks need a global `puppeteer-core` install with Chrome. Never run it next to Taste on one project |
| Finding another skill | [find-skills](https://github.com/vercel-labs/skills) | MIT | Its commands install globally with `-y` (no confirmation): show the command and get approval first |

## Watch list

Promising, but very new. Review the source before use.

- [deadcode](https://github.com/seanpaulforonda/deadcode) (MIT): finds unused CSS, JavaScript and imports, and deletes only after approval.
- [fullstack-audit](https://github.com/Eurie92/fullstack-audit-skill) (Apache-2.0): maps routes, components and APIs; runs an npm package through `npx`.

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

Browsing directories, not vetted: [skills.sh](https://www.skills.sh), [MCP Market](https://mcpmarket.com), [Hermes Atlas](https://hermesatlas.com/lists/top-skills).
