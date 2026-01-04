# Cubemap Panoramas

**Cubemap Panoramas** is an open library of real-world HDR panoramas converted into optimized cubemaps for immersive and experimental projects.

The project focuses on:
- minimal storage footprint
- fast CDN delivery
- clear attribution to original authors
- non-commercial, open usage

This repository is designed to be easily consumed by web, mobile, and immersive interfaces (including HidHud).

---

## What’s inside

- 📦 **Cubemap panoramas** (6 faces per panorama, WebP)
- 🧭 **index.json** — a lightweight index of available panorama IDs
- 📚 **sources.json** — original panorama URLs and author attribution
- 🌐 **GitHub Pages** — human-readable catalog with credits
- ⚙️ **Build scripts** — automated conversion from equirectangular HDR panoramas

---

## Panorama format

Each panorama is stored as a cubemap:

<panorama-id>/
px.webp
nx.webp
py.webp
ny.webp
pz.webp
nz.webp


- `panorama-id` is derived from the **MD5 hash of the source URL**
- Images are optimized for fast delivery via CDN (jsDelivr)

---

## index.json

The index file is intentionally minimal:

```json
[
  "a3f9c1d0e6b24c...",
  "9b8d72e4a91f0c..."
]
```

This design allows:

- aggressive caching
- painless future format evolution
- reliable delivery via app updates (e.g. CapGo)
---
## Usage (example)

Via jsDelivr CDN:
```
https://cdn.jsdelivr.net/gh/<username>/cubemap-panoramas/<panorama-id>/px.webp
```

The library can be used in:
- WebGL / Three.js / A-Frame
- WebXR / immersive environments
- Experimental spatial interfaces
- Educational and artistic projects
---
## Attribution

This project deeply respects the work of panorama authors.

All original sources and credits are listed in:
- `sources.json`
- the GitHub Pages catalog

If you use these panoramas publicly, please include attribution where possible.
---
## License
### Content

All panoramas and generated cubemaps are licensed under:

**Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)**

You are free to:
- Share
- Adapt

Under the following terms:
- Attribution required
- Non-commercial use only

License text:
https://creativecommons.org/licenses/by-nc/4.0/
---
## Philosophy

Think of this project as a real-world library:
- the catalog is always nearby
- the content is fetched only when needed
- nothing unnecessary is duplicated
- authors are always acknowledged
---
## Status

🚧 Actively evolving
Features like tagging, semantic search, and voice-based selection may appear post-MVP.
---
If you are an author and would like your work credited differently — or removed — please open an issue.
