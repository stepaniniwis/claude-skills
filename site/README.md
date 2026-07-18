# Stepanini — Static Portfolio Site

Eine ruhige, statische Portfolio-Seite im Stil aktueller Studio-Websites
(dunkler Hintergrund, Serif-Display, viel Whitespace, blauer Akzent).
Gebaut als Referenz nach https://www.blunarova.com — die Originalseite
war im Build-Sandbox nicht erreichbar, daher ist der Stil
interpretiert, nicht repliziert.

## Struktur

```
site/
├── index.html      Eine Seite, fünf Abschnitte (Hero, Work, Approach, About, Contact)
├── styles.css      Komplettes Stylesheet, kein Framework
└── assets/         Für eigene Bilder
```

## Lokal ansehen

```bash
cd site
python3 -m http.server 8000
# dann http://localhost:8000 im Browser öffnen
```

Oder einfach `index.html` direkt im Browser öffnen.

## Inhalte anpassen

Alle Texte sind Platzhalter und stehen direkt in `index.html`:

- **Wordmark / Titel**: `<title>` und `.wordmark` ändern
- **Hero**: `<section class="hero">` — H1, lede, Status-Badge
- **Projekte**: drei `<article class="card">` Blöcke
- **Prinzipien**: vier `<li>` in `<ol class="principles">`
- **About**: `.about-lead` und `.facts`
- **Kontakt**: E-Mail in `.big-mail` (zwei Stellen: href und Text)

## Farben / Typografie ändern

Oben in `styles.css` stehen die CSS-Variablen:

```css
:root {
  --bg: #0b0e14;      /* Hintergrund */
  --ink: #e9e5dc;     /* Textfarbe */
  --accent: #6aa6ff;  /* Blauer Akzent */
  --accent-2: #cdb6ff;
}
```

Fonts werden von Google Fonts geladen (Fraunces + Inter).
Für offline-Hosting Fonts lokal einbinden.

## Hosting

Statische Seite — läuft überall:
- **Netlify**: Drag & Drop des `site/` Ordners auf netlify.com/drop
- **GitHub Pages**: `gh-pages` Branch oder Actions-Workflow
- **Vercel**: `vercel` CLI im `site/` Ordner

Keine Build-Schritte, keine Abhängigkeiten.

## Was bewusst NICHT drin ist

- Kein Tracking, keine Analytics, keine Cookies
- Kein JavaScript-Framework
- Kein Build-Tool, kein Bundler
- Keine externen Skripte außer Google Fonts
