# Testing

- Structure checks (stdlib only): `python -m unittest discover -s tests -t .` from the site folder. CI runs them too.
- Design gate: Taste `lint.mjs` and `inspect.mjs` (Node 22+ and Chrome or Edge) at 1440, 768 and 390 px.
- Browser walk-through: serve the folder and use the page at desktop and 375 px widths, keyboard only once, and with reduced motion.

Viewport emulation is not physical-device testing. Record what actually ran in the sprint record.
