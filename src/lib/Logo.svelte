<script>
  export let light = false;
  export let compact = false;
  const logoUrl = `${import.meta.env.BASE_URL}assets/xifi-logo.svg`;
</script>

<a class:light class:compact class="logo" href="#top" aria-label="XIFI home">
  <img class="logo-mark" src={logoUrl} alt="" aria-hidden="true" />
  {#if !compact}<span class="wordmark">xifi</span>{/if}
</a>

<style>
  .logo { display: inline-flex; align-items: center; gap: .72rem; text-decoration: none; color: #10122f; }
  .logo-mark { width: 38px; height: 34px; object-fit: contain; flex: none; filter: drop-shadow(0 7px 13px rgba(205,52,120,.18)); }
  .wordmark { font-family: 'Outfit', sans-serif; font-size: 1.45rem; font-weight: 700; letter-spacing: -.06em; }
  .light { color: white; }
  .compact .logo-mark { width: 36px; height: 32px; }
</style>
