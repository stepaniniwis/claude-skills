# stephaniewissmann.de — static site

One page, plain HTML and CSS, no build step. Content architecture follows
Blunarova (hero statement → work → services → sweet spot / not so much →
voices → fields → studio → writing → Substack → about → contact). Visual
register follows p5aholic.me, alasdairmonk.com and rauno.me: fixed left
rail, text-first index, one large element, hairlines instead of boxes.

```
site/
├── index.html      the page
├── styles.css      all styling; design tokens at the top of :root
├── copy-deck.md    every text block, paste-ready, with alternates and open questions
└── README.md
```

## Preview

```bash
cd site && python3 -m http.server 8000   # → http://localhost:8000
```

Or open `index.html` directly. Inter loads from Google Fonts; offline it
falls back to the system sans.

## Edit

- **Colours, rail width, base size** — `:root` at the top of `styles.css`.
  `--accent` is the single accent colour.
- **Copy** — all in `index.html`; `copy-deck.md` mirrors it with alternates.
- **Portrait** — replace `.plate` inside `.portrait` with an `<img>`
  (aspect 4:5, min 1400px wide).
- **Studio series images** — set `background-image` on `.w1` … `.w4`,
  or drop an `<img>` into each `.world`.
- **Testimonials** — six slots in `#voices`, each marked with `.todo`.

## Still open

- Real portrait and four series images (launch shoot)
- Six testimonials with name and role
- Four copy points to verify, listed in `copy-deck.md` under *Sweet spot*
- German landing page, Impressum, Datenschutz
- Project sub-pages and publication archive (post-launch)

## Deploy

Static — Netlify drop, GitHub Pages, Vercel, or any web server.
No trackers, no cookies, no scripts beyond web fonts and ~20 lines of
inline JS (smooth scroll, scroll-spy, year).
