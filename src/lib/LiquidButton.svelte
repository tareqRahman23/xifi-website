<script>
  // Adapted from danilofiumi/liquid-glass-svelte's Svelte glass button technique.
  export let label = '';
  export let tone = 'pink';
  export let onpress = () => {};
  const filterId = `xifi-liquid-${label.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`;
</script>

<span class:light={tone === 'light'} class="liquid-button">
  <span class="tint" aria-hidden="true"></span>
  <span class="glass-filter" style={`filter:url(#${filterId}) saturate(120%)`} aria-hidden="true"></span>
  <button type="button" on:click={onpress} aria-label={label}>{label}<span aria-hidden="true">→</span></button>
</span>

<svg aria-hidden="true" width="0" height="0">
  <filter id={filterId} x="-12%" y="-20%" width="124%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.012 0.01" numOctaves="2" seed="92" result="noise" />
    <feGaussianBlur in="noise" stdDeviation="1.7" result="blurred" />
    <feDisplacementMap in="SourceGraphic" in2="blurred" scale="34" xChannelSelector="R" yChannelSelector="G" />
  </filter>
</svg>

<style>
  @property --glass-angle { syntax: '<angle>'; inherits: false; initial-value: -70deg; }
  .liquid-button { --glass-angle:-70deg; position:relative; display:inline-grid; min-width:150px; min-height:46px; border-radius:15px; isolation:isolate; overflow:hidden; background:linear-gradient(135deg,#e45294,#cf3478); box-shadow:0 10px 24px rgba(204,45,117,.22),inset 0 1px rgba(255,255,255,.35); transition:transform .3s cubic-bezier(.25,1,.5,1),box-shadow .3s ease,--glass-angle .5s ease; }
  .liquid-button.light { background:rgba(255,255,255,.72); border:1px solid rgba(255,255,255,.76); box-shadow:0 9px 24px rgba(91,35,67,.1),inset 0 1px rgba(255,255,255,.85); }
  .tint,.glass-filter,button { grid-area:1/1; }
  .tint { z-index:0; background:linear-gradient(var(--glass-angle),rgba(255,255,255,.06),rgba(255,255,255,.27) 48%,rgba(255,255,255,.05)); }
  .glass-filter { z-index:1; margin:-4px; border-radius:inherit; pointer-events:none; backdrop-filter:blur(3px); opacity:.34; }
  button { z-index:2;width:100%;min-height:46px;border:0;padding:0 21px;display:inline-flex;align-items:center;justify-content:center;gap:9px;color:white;background:transparent;font:650 .86rem/1 'Inter',sans-serif;cursor:pointer;text-shadow:0 1px rgba(91,19,51,.14); }
  .light button { color:#b82b69;text-shadow:none; }
  .liquid-button:hover { --glass-angle:-125deg; transform:translateY(-2px) scale(.985); box-shadow:0 14px 29px rgba(204,45,117,.25),inset 0 1px rgba(255,255,255,.42); }
  .liquid-button:active { transform:translateY(0) scale(.97) rotateX(4deg); }
  button:focus-visible { outline:3px solid rgba(255,255,255,.7);outline-offset:-4px; }
  svg { position:absolute;pointer-events:none; }
  @media (prefers-reduced-motion:reduce) { .liquid-button { transition:none; } }
</style>
