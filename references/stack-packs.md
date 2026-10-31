# Stack packs

Official skills published by the makers of a framework or service. Universal Web Dev does not pin or install them; it recognizes the stack and offers the right pack, so the expert loads only in projects that use it. Checked on 2026-10-27; re-check the source before installing.

## How to offer a pack

1. Detect the stack from the project files below, once per project. Skip a pack that is already installed.
2. Tell the developer the pack, its publisher, its license and what it runs, in two lines.
3. Install only after approval, into their skills folder, using the vendor's README. The general skills CLI is `npx skills add <owner/repo> --skill <name>`; show the exact command first and leave out `-y`, which installs globally without confirmation.
4. Route that stack's work to the pack from then on. This skill's design, testing and release rules still apply.

## Packs

| Stack or service | Detect | Pack | Publisher and license | Notes |
| --- | --- | --- | --- | --- |
| WordPress | `wp-config.php`, `wp-content/`, a theme `style.css` header, `block.json` | [`wordpress-router`](https://github.com/WordPress/agent-skills) and its sibling `wp-*` skills | WordPress contributors, GPL-2.0-or-later | The router sends work to 18 sibling skills; install the set together |
| Shopify | `shopify.app.toml`, `.liquid` templates, `@shopify/*` packages | [`shopify`](https://github.com/Shopify/Shopify-AI-Toolkit) | Shopify, MIT | One skill covers the CLI, Admin and Storefront APIs, Functions and Polaris |
| Laravel | `artisan`, `laravel/framework` in composer.json | [`laravel-best-practices`](https://github.com/laravel/boost) | Laravel, MIT | Ships with Laravel Boost, a Composer dev package that also adds an MCP server |
| Svelte, SvelteKit | `svelte.config.js`, `svelte` dependency | [`svelte-core-bestpractices`](https://github.com/sveltejs/ai-tools) | Svelte team, MIT | |
| React, Next.js | `react` or `next` dependency | [`vercel-react-best-practices`](https://github.com/vercel-labs/agent-skills) | Vercel; MIT declared in the skill, no license file in the repository | 70 performance rules; good with `performance` |
| GSAP motion | `gsap` dependency, or an explicit GSAP implementation request | [`gsap-core` plus the relevant module](https://github.com/greensock/gsap-skills) | GreenSock, MIT skill instructions; checked 2026-10-31 | Official animation specialist. Choose only needed React/ScrollTrigger/timeline/plugin guidance; verify runtime terms separately, no whole-pack context load |
| Stripe payments | `stripe` dependency, Stripe keys in env examples | [`stripe-best-practices`](https://github.com/stripe/ai) | Stripe, MIT | Checkout vs PaymentIntents, test environments, Connect |
| Email | `resend`, `nodemailer` or an email provider SDK | [`email-best-practices`](https://github.com/resend/resend-skills) | Resend, MIT | Deliverability (SPF, DKIM, DMARC), consent rules, webhooks; useful with any provider |
| Sanity CMS | `sanity.config.*`, `sanity` dependency | [`sanity-best-practices`](https://github.com/sanity-io/agent-toolkit) | Sanity, MIT | `seo-aeo-best-practices` from the same repository is already installed |
| Prisma | `prisma/schema.prisma` | [Prisma skills](https://github.com/prisma/skills) | Prisma, MIT | Pick the one matching the task: ORM setup, client API, upgrades |
| Neon Postgres | Neon connection strings, `@neondatabase/*` | [`neon`](https://github.com/neondatabase/agent-skills) | Neon, Apache-2.0 | Use with the `postgres` profile's Supabase Postgres guidance for SQL itself |
| Supabase | `supabase/` folder, `@supabase/*` | `supabase-postgres-best-practices` | Supabase, MIT | Already available as this skill's `postgres` profile |
| Convex | `convex/` folder, `convex` dependency | [`convex`](https://github.com/convex/agent-skills) | Convex, Apache-2.0 | Offer only when the project already uses Convex; its description promotes Convex for new backends |
| Clerk | `@clerk/*` packages | [Clerk skills](https://github.com/clerk/skills) | Clerk; no license file | Link only: read in the source, don't copy or redistribute |
| Better Auth | `better-auth` dependency | [Better Auth skills](https://github.com/better-auth/skills) | Better Auth; no license file | Link only, as above |

No official pack was found for Tailwind CSS, Nuxt, Astro, Drizzle or Django as of the check date. For any other stack, read [more skills](more-skills.md) and offer only packs with a license, a named publisher and no hidden network or login access.
