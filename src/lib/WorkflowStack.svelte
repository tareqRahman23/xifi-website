<script>
  import Icon from './Icon.svelte';
  import { liquidGlass } from './liquidGlass.js';
</script>

<div class="workflow-stack">
  <article class="workflow-card understand" use:liquidGlass={{ size: 240 }}>
    <div class="workflow-copy"><span>01 / Understand</span><h3>Find the intent beneath the interaction.</h3><p>XIFI carries the live transcript, identity signals, channel context, and session history into one authoritative state.</p></div>
    <div class="workflow-visual intent-visual">
      <div class="intent-person"><img src={`${import.meta.env.BASE_URL}assets/customer-avatar.webp`} alt="Customer" /><span><i></i> Voice interaction</span></div>
      <div class="intent-card"><small>Detected intent</small><strong>Duplicate subscription charge</strong><div><span>Confidence</span><b>High</b></div><div><span>Knowledge</span><b>2 approved sources</b></div></div>
    </div>
  </article>
  <article class="workflow-card resolve" use:liquidGlass={{ size: 240 }}>
    <div class="workflow-copy"><span>02 / Resolve</span><h3>Take the right action within guardrails.</h3><p>Ground the answer, verify policy and account state, then perform only the steps the business has explicitly permitted.</p></div>
    <div class="workflow-visual resolution-visual">
      <span class="resolution-icon"><Icon name="shield" size={28} /></span>
      <small>Suggested action</small><strong>Refund duplicate charge</strong>
      <dl><div><dt>Policy</dt><dd><Icon name="check" size={13} /> Verified</dd></div><div><dt>Customer</dt><dd><Icon name="check" size={13} /> Verified</dd></div><div><dt>Audit evidence</dt><dd><Icon name="check" size={13} /> Ready</dd></div></dl>
    </div>
  </article>
  <article class="workflow-card escalate" use:liquidGlass={{ size: 240 }}>
    <div class="workflow-copy"><span>03 / Escalate</span><h3>Bring in a person with the work already done.</h3><p>The right specialist receives the story, sources, policy checks, customer state, and completed actions—not an empty ticket.</p></div>
    <div class="workflow-visual handoff-visual">
      <div class="handoff-person"><img src={`${import.meta.env.BASE_URL}assets/specialist-avatar.webp`} alt="Support specialist" /><span><strong>Hannah Lee</strong><small>Billing specialist</small></span></div>
      <span class="availability"><i></i> Available now</span>
      <ul><li>Conversation summary</li><li>2 approved sources</li><li>Policy check complete</li><li>Action receipt attached</li></ul>
      <button>Join interaction <Icon name="arrow" size={15} /></button>
    </div>
  </article>
</div>
