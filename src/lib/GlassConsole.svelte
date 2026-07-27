<script>
  import Icon from './Icon.svelte';

  const conversations = [
    {
      title: 'Duplicate charge', initial: 'D', age: 'Now', customer: 'Jane Cooper', identity: 'Verified', channel: 'Voice',
      message: 'I was charged twice for my subscription.', time: '10:24 AM',
      reply: 'I found the approved refund policy and verified the account context.',
      sources: ['Refund policy', 'Billing guide'], action: 'Duplicate charge refund', specialist: 'Billing specialist'
    },
    {
      title: 'Refund request', initial: 'R', age: '2m', customer: 'Malik Johnson', identity: 'Verified', channel: 'Web chat',
      message: 'Can I cancel today and receive a refund?', time: '10:22 AM',
      reply: 'Your account is inside the approved cancellation window. I can prepare the next step.',
      sources: ['Cancellation policy', 'Refund eligibility'], action: 'Cancellation and refund', specialist: 'Retention specialist'
    },
    {
      title: 'Account access', initial: 'A', age: '4m', customer: 'Sofia Patel', identity: 'Pending', channel: 'Messaging',
      message: 'I cannot get back into my account.', time: '10:20 AM',
      reply: 'I found the approved recovery workflow. Identity verification is the next required step.',
      sources: ['Access recovery', 'Identity guide'], action: 'Secure recovery link', specialist: 'Access specialist'
    },
    {
      title: 'Order status', initial: 'O', age: '6m', customer: 'Noah Williams', identity: 'Verified', channel: 'Email',
      message: 'Where is order 4208? It was due yesterday.', time: '10:18 AM',
      reply: 'The carrier recorded a delay. I found the latest tracking event and notification policy.',
      sources: ['Fulfilment guide', 'Carrier event'], action: 'Tracking update', specialist: 'Delivery specialist'
    }
  ];

  let selectedIndex = 0;
  let actionComplete = false;
  let joined = false;
  let activeSource = 0;
  $: current = conversations[selectedIndex];

  function selectConversation(index) {
    selectedIndex = index;
    actionComplete = false;
    joined = false;
    activeSource = 0;
  }
</script>

<div class="support-console" aria-label="Interactive XIFI contact-center console">
  <header>
    <div class="live"><span></span> Live interaction</div>
    <div class="console-tools" aria-hidden="true"><i></i><i></i><i></i></div>
  </header>
  <div class="mobile-conversation-tabs" aria-label="Choose a conversation">
    {#each conversations as conversation, index}
      <button class:active={selectedIndex === index} aria-label={conversation.title} aria-pressed={selectedIndex === index} onclick={() => selectConversation(index)}>{conversation.initial}</button>
    {/each}
  </div>
  <div class="console-grid">
    <aside class="conversation-list">
      <small>Conversations</small>
      {#each conversations as conversation, index}
        <button class:active={selectedIndex === index} aria-pressed={selectedIndex === index} onclick={() => selectConversation(index)}>
          <span>{conversation.initial}</span>{conversation.title}<em>{conversation.age}</em>
        </button>
      {/each}
      <p>+3 in queue</p>
    </aside>

    {#key current.title}
      <section class="conversation-thread" aria-live="polite">
        <div class="customer-bubble">{current.message}<time>{current.time}</time></div>
        <div class="assistant-bubble">
          <strong><b>X</b> XIFI</strong>
          <p>{current.reply}</p>
          <small><Icon name="book" size={12} /> Source: {current.sources[activeSource]}</small>
        </div>
        <button class:complete={actionComplete} class="action-card" aria-pressed={actionComplete} onclick={() => actionComplete = !actionComplete}>
          <span><Icon name={actionComplete ? 'check' : 'shield'} size={21} /></span>
          <div><strong>{actionComplete ? 'Action completed' : 'Approved action'}</strong><p>{current.action} {actionComplete ? 'recorded' : 'prepared'}</p></div>
          <em>{actionComplete ? 'Done' : 'Run'}</em>
        </button>
        <div class:connected={joined} class="handoff-card">
          <img src={`${import.meta.env.BASE_URL}assets/specialist-avatar.webp`} alt="Support specialist" />
          <div><strong>{joined ? 'Specialist connected' : 'Specialist available'}</strong><p>{joined ? `${current.specialist} joined with full context.` : 'Conversation, sources, and action attached.'}</p></div>
          <button aria-pressed={joined} onclick={() => joined = !joined}>{joined ? 'Leave' : 'Join'}</button>
        </div>
      </section>
    {/key}

    <aside class="context-panel">
      <small>Context</small>
      <dl>
        <div><dt>Customer</dt><dd>{current.customer}</dd></div>
        <div><dt>Identity</dt><dd class:pending={current.identity === 'Pending'}><span></span> {current.identity}</dd></div>
        <div><dt>Channel</dt><dd>{current.channel}</dd></div>
      </dl>
      <small>Knowledge</small>
      {#each current.sources as source, index}
        <button class:active={activeSource === index} aria-pressed={activeSource === index} onclick={() => activeSource = index}>{source} <Icon name="arrow" size={12} /></button>
      {/each}
    </aside>
  </div>
  <div class="console-summary" aria-live="polite">
    <div><span>Session</span><strong>Active</strong></div>
    <div><span>Knowledge</span><strong>{current.sources.length} sources</strong></div>
    <div><span>Action</span><strong>{actionComplete ? 'Completed' : 'Prepared'}</strong></div>
    <div><span>Handoff</span><strong>{joined ? 'Connected' : 'Ready'}</strong></div>
  </div>
</div>
