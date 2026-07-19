<script>
  import Icon from './Icon.svelte';
  const assetBase = `${import.meta.env.BASE_URL}assets/`;

  const steps = [
    ['01', 'Understand', 'Capture the customer intent.'],
    ['02', 'Ground', 'Anchor the answer in approved knowledge.'],
    ['03', 'Resolve', 'Answer clearly or take an approved action.'],
    ['04', 'Escalate', 'Bring in the right person with context.']
  ];
</script>

<div class="steps">
  {#each steps as step}
    <article><span>{step[0]}</span><div><strong>{step[1]}</strong><p>{step[2]}</p></div></article>
  {/each}
</div>

<div class="journey-rail">
  <div class="rail-line"></div>
  <article class="journey-node voice">
    <img src={`${assetBase}customer-avatar.webp`} alt="Customer" />
    <div><strong>Customer voice</strong><span class="mini-wave"><Icon name="wave" size={36} /></span></div>
  </article>
  <span class="connector-icon"><Icon name="mic" size={18} /></span>
  <article class="journey-node knowledge">
    <span class="node-icon"><Icon name="book" size={18} /></span>
    <div><strong>Approved knowledge</strong><small>Refund policy</small><small>Billing workflow</small></div>
  </article>
  <span class="connector-icon"><Icon name="sparkles" size={18} /></span>
  <article class="journey-node answer">
    <span class="node-icon brand">x</span>
    <div><strong>XIFI Assistant</strong><p>I found the approved path and prepared the next step.</p></div>
  </article>
  <span class="connector-icon"><Icon name="check" size={18} /></span>
  <article class="journey-node human">
    <img src={`${assetBase}specialist-avatar.webp`} alt="Support specialist" />
    <div><strong>Human handoff</strong><span>Context ready</span></div>
  </article>
</div>
