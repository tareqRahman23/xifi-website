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
  .logo-mark { width: 50px; height: 44px; object-fit: contain; flex: none; filter: drop-shadow(0 9px 16px rgba(47,99,245,.22)); }
  .wordmark { font-family: 'Sora', sans-serif; font-size: 1.45rem; font-weight: 600; letter-spacing: -.06em; font-style: italic; }
  .light { color: white; }
  .compact .logo-mark { width: 43px; height: 38px; }
</style>
