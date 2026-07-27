<script>
  import Icon from './Icon.svelte';
  import { liquidGlass } from './liquidGlass.js';

  let selected = 'Duplicate charge';
  const conversations = [
    ['Duplicate charge', 'Now'],
    ['Refund request', '2m'],
    ['Account access', '4m'],
    ['Order status', '6m']
  ];
  const summary = [
    ['Session', 'Active'],
    ['Knowledge', '2 sources'],
    ['Action', 'Prepared'],
    ['Handoff', 'Ready']
  ];
</script>

<div class="support-console" aria-label="Interactive XIFI contact-center console" use:liquidGlass={{ size: 260 }}>
  <header>
    <div class="live"><span></span> Live interaction</div>
    <div class="console-tools"><i></i><i></i><i></i></div>
  </header>
  <div class="console-grid">
    <aside class="conversation-list">
      <small>Conversations</small>
      {#each conversations as conversation}
        <button class:active={selected === conversation[0]} onclick={() => selected = conversation[0]}>
          <span>{conversation[0].slice(0, 1)}</span>{conversation[0]}<em>{conversation[1]}</em>
        </button>
      {/each}
      <p>+3 in queue</p>
    </aside>
    <section class="conversation-thread">
      <div class="customer-bubble">I was charged twice for my subscription.<time>10:24 AM</time></div>
      <div class="assistant-bubble">
        <strong><b>X</b> XIFI</strong>
        <p>I found the approved refund policy and verified the account context.</p>
        <small><Icon name="book" size={12} /> Source: Refund policy</small>
      </div>
      <div class="action-card"><span><Icon name="shield" size={21} /></span><div><strong>Approved action</strong><p>Duplicate charge refund prepared</p></div><em>Ready</em></div>
      <div class="handoff-card"><img src={`${import.meta.env.BASE_URL}assets/specialist-avatar.webp`} alt="Support specialist" /><div><strong>Specialist available</strong><p>Conversation, sources, and action attached.</p></div><button>Join</button></div>
    </section>
    <aside class="context-panel">
      <small>Context</small>
      <dl><div><dt>Customer</dt><dd>Jane Cooper</dd></div><div><dt>Identity</dt><dd><span></span> Verified</dd></div><div><dt>Channel</dt><dd>Voice</dd></div></dl>
      <small>Knowledge</small>
      <a href="#product">Refund policy <Icon name="arrow" size={12} /></a>
      <a href="#product">Billing guide <Icon name="arrow" size={12} /></a>
    </aside>
  </div>
  <div class="console-summary">
    {#each summary as item}<div><span>{item[0]}</span><strong>{item[1]}</strong></div>{/each}
  </div>
</div>
