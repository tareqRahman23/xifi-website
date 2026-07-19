# XIFI website

Responsive Svelte/Vite marketing website for XIFI, based on the supplied landing-page reference and XIFI brand sheet.

Live site: https://tareqrahman23.github.io/xifi-website/

The interface uses `@ybouane/liquidglass` for targeted WebGL refraction and a lightweight local motion layer for parallax, pointer lighting, scroll reveals, and reduced-motion fallbacks.

## Run locally

```powershell
npm.cmd install
npm.cmd run dev
```

Open `http://127.0.0.1:4173/`.

## Validate and build

```powershell
npm.cmd run check
npm.cmd run build
```

The production bundle is written to `dist/`.

## Brand system

- Heading type: Sora SemiBold
- Body type: Inter
- XIFI Blue Light: `#68BEFF`
- XIFI Blue: `#2F63F5`
- Deep Indigo: `#0E088C`
- Accent Magenta: `#F1065A`
- Soft Mist: `#ECEEF3`
- Graphite: `#5A5A5A`
- White: `#FFFFFF`

The generated design concepts are stored under `design/`. Production UI remains code-native. Generated avatar assets are stored under `public/assets/`.
