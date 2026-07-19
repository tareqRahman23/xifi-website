<script>
  import Icon from './Icon.svelte';
  import { liquidGlass, parallax } from './interactions.js';
  const assetBase = `${import.meta.env.BASE_URL}assets/`;

  const sources = [
    { title: 'Refund policy', detail: 'Eligible within 30 days', icon: 'book' },
    { title: 'Billing guidance', detail: 'Duplicate charge workflow', icon: 'check' },
    { title: 'Account context', detail: 'Identity verified', icon: 'shield' }
  ];
  let selected = 0;
  let sent = false;
</script>

<div class="preview-wrap" aria-label="Interactive XIFI support session preview" use:liquidGlass={{ defaults: { refraction: 0.34, edgeHighlight: 0.13, chromAberration: 0.018, shadowOpacity: 0.18 } }} use:parallax={{ strength: 0.72, scrollStrength: 0.7 }}>
  <div class="liquidglass-scene preview-glass-scene" aria-hidden="true"></div>
  <aside class="glass source-panel" data-liquid-glass data-config={JSON.stringify({ blurAmount: 0.18, cornerRadius: 22, zRadius: 18, brightness: 0.08 })}>
    <div class="panel-title"><span class="icon-disc"><Icon name="book" size={17} /></span>Approved knowledge</div>
    <div class="source-list">
      {#each sources as source, index}
        <button data-interactive class:active={selected === index} on:click={() => selected = index}>
          <span><strong>{source.title}</strong><small>{source.detail}</small></span>
          <span class="mini-check"><Icon name="check" size={15} /></span>
        </button>
      {/each}
    </div>
    <span class="panel-link">View source library <Icon name="arrow" size={14} /></span>
  </aside>

  <section class="glass conversation" data-liquid-glass data-config={JSON.stringify({ blurAmount: 0.22, cornerRadius: 27, zRadius: 22, brightness: 0.08 })}>
    <div class="conversation-top">
      <span class="live"><i></i> Live support</span>
      <span class="handoff-tag"><Icon name="people" size={14} /> Human handoff ready</span>
    </div>
    <div class="customer-row">
      <img src={`${assetBase}customer-avatar.webp`} alt="Customer avatar" />
      <div><strong>Jane Cooper</strong><p>I was charged twice for my subscription.</p></div>
      <button class="round-control" aria-label="Call customer"><Icon name="phone" size={17} /></button>
    </div>
    <div class="wave" aria-hidden="true">
      {#each Array(38) as _, i}<i style={`--h:${10 + ((i * 13) % 30)}px; --d:${i * 25}ms`}></i>{/each}
    </div>
    <div class="assistant-message">
      <span class="assistant-mark">x</span>
      <div>
        <strong>XIFI Assistant</strong>
        <p>{selected === 0 ? 'I found the approved refund policy. I can help resolve the duplicate charge.' : selected === 1 ? 'The billing workflow is approved. I can prepare the next action.' : 'Identity is verified. The account context is ready.'}</p>
        <span class="citation"><Icon name="book" size={13} /> Source: {sources[selected].title}</span>
      </div>
      <small>Just now</small>
    </div>
    <div class="composer">
      <span>{sent ? 'Action sent for confirmation' : 'Type a reply...'}</span>
      <button on:click={() => sent = !sent} aria-label="Send reply"><Icon name="send" size={18} /></button>
    </div>
  </section>

  <aside class="glass action-panel" data-liquid-glass data-config={JSON.stringify({ blurAmount: 0.18, cornerRadius: 22, zRadius: 18, brightness: 0.08 })}>
    <div class="panel-title"><span class="icon-disc success"><Icon name="check" size={17} /></span>Action confirmed</div>
    <div class="action-body">
      <div class="action-head"><strong>Duplicate charge refund</strong><span>Completed</span></div>
      <dl>
        <div><dt>Amount</dt><dd>$29.00</dd></div>
        <div><dt>Method</dt><dd>•••• 4242</dd></div>
        <div><dt>Receipt</dt><dd>RFD-839201</dd></div>
      </dl>
    </div>
    <span class="panel-link">View action details <Icon name="arrow" size={14} /></span>
  </aside>
</div>
