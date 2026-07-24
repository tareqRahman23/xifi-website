<script>
  import Icon from './Icon.svelte';
</script>

<div class="feature-bento media-scale">
  <article class="feature-card feature-main">
    <div class="feature-copy"><span class="feature-icon"><Icon name="book" /></span><h3>Ground every answer.</h3><p>Anchor responses in approved knowledge and keep source context attached from question to resolution.</p><a href="#solutions">Explore grounded support <Icon name="arrow" size={15} /></a></div>
    <div class="knowledge-visual">
      <div class="source source-one"><span>Policy</span><strong>Refund eligibility</strong><i></i></div>
      <div class="source source-two"><span>Account</span><strong>Identity verified</strong><i></i></div>
      <div class="answer-orb"><b>X</b><span>Grounded answer</span></div>
    </div>
  </article>
  <article class="feature-card feature-action">
    <span class="feature-icon coral"><Icon name="shield" /></span><div><h3>Control every action.</h3><p>Permissioned workflows with clear confirmation and a complete audit trail.</p></div><span class="status-line"><i></i> Refund prepared <b>Approved</b></span>
  </article>
  <article class="feature-card feature-human">
    <span class="feature-icon violet"><Icon name="people" /></span><div><h3>Keep the human path.</h3><p>Escalate with the conversation, sources, and completed steps already attached.</p></div><div class="avatar-line"><img src={`${import.meta.env.BASE_URL}assets/customer-avatar.webp`} alt="Customer" /><span></span><img src={`${import.meta.env.BASE_URL}assets/specialist-avatar.webp`} alt="Specialist" /></div>
  </article>
</div>
