<script>
  import Icon from './Icon.svelte';
  let selected = 'Duplicate charge';
  const conversations = ['Duplicate charge', 'Refund request', 'Account access'];
</script>

<div class="support-console glass-panel" aria-label="Interactive XIFI support console">
  <header>
    <div class="live"><span></span> Live support</div>
    <div class="console-tools"><i></i><i></i><i></i></div>
  </header>
  <div class="console-grid">
    <aside class="conversation-list">
      <small>Conversations</small>
      {#each conversations as conversation}
        <button class:active={selected === conversation} on:click={() => selected = conversation}>
          <span>{conversation.slice(0, 1)}</span>{conversation}<em>{conversation === 'Duplicate charge' ? 'Now' : '4m'}</em>
        </button>
      {/each}
    </aside>
    <section class="conversation-thread">
      <div class="customer-bubble">I was charged twice for my subscription.<time>10:24 AM</time></div>
      <div class="assistant-bubble"><strong><b>X</b> XIFI Assistant</strong><p>I found the approved refund policy and verified the account context.</p><small><Icon name="book" size={12} /> Source: Refund policy</small></div>
      <div class="action-card"><span><Icon name="shield" size={21} /></span><div><strong>Approved action</strong><p>Duplicate charge refund prepared</p></div><em>Ready</em></div>
      <div class="handoff-card"><img src={`${import.meta.env.BASE_URL}assets/specialist-avatar.webp`} alt="Support specialist" /><div><strong>Human handoff available</strong><p>Conversation and sources attached.</p></div><button>Connect</button></div>
    </section>
    <aside class="context-panel">
      <small>Context</small>
      <dl><div><dt>Customer</dt><dd>Jane Cooper</dd></div><div><dt>Status</dt><dd><span></span> Verified</dd></div><div><dt>Channel</dt><dd>Voice</dd></div></dl>
      <small>Knowledge</small>
      <a href="#product">Refund policy <Icon name="arrow" size={12} /></a>
      <a href="#product">Billing guide <Icon name="arrow" size={12} /></a>
    </aside>
  </div>
</div>
