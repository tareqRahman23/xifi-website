<script>
  import Icon from './Icon.svelte';
  const assetBase = `${import.meta.env.BASE_URL}assets/`;
</script>

<div class="handoff-console">
  <section class="handoff-side ai-side">
    <div class="identity"><img src={`${assetBase}customer-avatar.webp`} alt="Customer" /><div><span class="mini-brand">x</span><strong>XIFI Assistant</strong><small>Preparation complete</small></div></div>
    <dl>
      <div><dt>Summary</dt><dd>Customer reported a duplicate subscription charge.</dd></div>
      <div><dt>Consulted source</dt><dd><Icon name="book" size={14} /> Refund policy</dd></div>
      <div><dt>Completed action</dt><dd>Refund request initiated.</dd></div>
    </dl>
  </section>
  <div class="handoff-link"><span><Icon name="sparkles" size={18} /></span></div>
  <section class="handoff-side human-side">
    <div class="identity"><img src={`${assetBase}specialist-avatar.webp`} alt="Support specialist" /><div><strong>Support specialist</strong><small class="ready"><Icon name="people" size={13} /> Handoff ready</small></div></div>
    <dl>
      <div><dt>Customer</dt><dd>Jane Cooper</dd></div>
      <div><dt>Reason</dt><dd>Customer requested review</dd></div>
      <div><dt>Context</dt><dd>Conversation, actions, and sources attached.</dd></div>
    </dl>
  </section>
</div>
