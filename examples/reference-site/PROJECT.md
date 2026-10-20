# Project

Stack: static HTML, one CSS file and one small script. No build step, no dependencies, no backend.
Fonts: Bricolage Grotesque from Google Fonts. Photographs: Unsplash photos served by picsum.photos (atmosphere only).

```text
index.html     the page
404.html       not-found page
styles.css     tokens, layout, motion
site.js        tide window, card deck, entrances, index preview
tests/sprints/ executable checks per sprint
```

Conventions: tokens only in CSS custom properties; every script feature has a no-script fallback; motion respects `prefers-reduced-motion`.
Deployment: not deployed. A hostname is pending, so canonical URLs, sitemap.xml and social image URLs are pending too.
