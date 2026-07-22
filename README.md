# XIFI website

Responsive Svelte/Vite marketing website for XIFI, based on the supplied landing-page reference and XIFI brand sheet.

Live site: https://tareqrahman23.github.io/xifi-website/

The interface uses a restrained Svelte liquid-glass button adapted from [`danilofiumi/liquid-glass-svelte`](https://github.com/danilofiumi/liquid-glass-svelte), plus a lightweight local motion layer for subtle parallax, scroll reveals, and reduced-motion fallbacks.

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
- Support Pink: `#DF4C8D`
- Deep Rose: `#CB3478`
- Soft Pink: `#F9D4E8`
- Deep Navy: `#11132F`
- Signal Blue: `#4168EE`
- Cool Mist: `#EEF2F8`
- White: `#FFFFFF`

The generated design concepts are stored under `design/`. Production UI remains code-native. Generated avatar assets are stored under `public/assets/`.
