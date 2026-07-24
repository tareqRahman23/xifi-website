<script>
  import Icon from './Icon.svelte';
</script>

<div class="workflow-stack">
  <article class="workflow-card understand">
    <div class="workflow-copy"><span>Understand</span><h3>Capture the real customer intent.</h3><p>XIFI listens across voice and chat, preserving the conversation and the signals that matter.</p></div>
    <div class="workflow-visual"><img src={`${import.meta.env.BASE_URL}assets/customer-avatar.webp`} alt="Customer" /><div class="voice-ring"><Icon name="wave" size={44} /></div><span>Customer voice</span></div>
  </article>
  <article class="workflow-card resolve">
    <div class="workflow-copy"><span>Resolve</span><h3>Move with confidence.</h3><p>Ground the response, verify policy, and take only the actions your team has approved.</p></div>
    <div class="workflow-visual shield-visual"><Icon name="shield" size={76} /><strong>Action confirmed</strong><span>Receipt and audit trail attached</span></div>
  </article>
  <article class="workflow-card escalate">
    <div class="workflow-copy"><span>Escalate</span><h3>Bring in the right person, fully briefed.</h3><p>When the moment calls for a human, specialists receive the story, sources, and completed work.</p></div>
    <div class="workflow-visual handoff-visual"><img src={`${import.meta.env.BASE_URL}assets/customer-avatar.webp`} alt="Customer" /><i><Icon name="arrow" size={19} /></i><img src={`${import.meta.env.BASE_URL}assets/specialist-avatar.webp`} alt="Support specialist" /><strong>Context ready</strong></div>
  </article>
</div>
