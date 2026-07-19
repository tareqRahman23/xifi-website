<script>
  import Icon from './Icon.svelte';
  import { liquidGlass, parallax } from './interactions.js';
  const assetBase = `${import.meta.env.BASE_URL}assets/`;
</script>

<div class="handoff-console" use:liquidGlass={{ defaults: { refraction: 0.22, edgeHighlight: 0.1, chromAberration: 0.012, shadowOpacity: 0.13 } }} use:parallax={{ strength: 0.45, scrollStrength: 0.45 }}>
  <div class="liquidglass-scene handoff-glass-scene" aria-hidden="true"></div>
  <section class="handoff-side ai-side" data-liquid-glass data-config={JSON.stringify({ blurAmount: 0.14, cornerRadius: 24, zRadius: 18, brightness: 0.06 })}>
    <div class="identity"><img src={`${assetBase}customer-avatar.webp`} alt="Customer" /><div><span class="mini-brand">x</span><strong>XIFI Assistant</strong><small>Preparation complete</small></div></div>
    <dl>
      <div><dt>Summary</dt><dd>Customer reported a duplicate subscription charge.</dd></div>
      <div><dt>Consulted source</dt><dd><Icon name="book" size={14} /> Refund policy</dd></div>
      <div><dt>Completed action</dt><dd>Refund request initiated.</dd></div>
    </dl>
  </section>
  <div class="handoff-link"><span><Icon name="sparkles" size={18} /></span></div>
  <section class="handoff-side human-side" data-liquid-glass data-config={JSON.stringify({ blurAmount: 0.14, cornerRadius: 24, zRadius: 18, brightness: 0.06 })}>
    <div class="identity"><img src={`${assetBase}specialist-avatar.webp`} alt="Support specialist" /><div><strong>Support specialist</strong><small class="ready"><Icon name="people" size={13} /> Handoff ready</small></div></div>
    <dl>
      <div><dt>Customer</dt><dd>Jane Cooper</dd></div>
      <div><dt>Reason</dt><dd>Customer requested review</dd></div>
      <div><dt>Context</dt><dd>Conversation, actions, and sources attached.</dd></div>
    </dl>
  </section>
</div>
