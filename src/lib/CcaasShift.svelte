<script>
  import Icon from './Icon.svelte';
</script>

<div class="shift-grid">
  <article class="shift-card legacy">
    <header><span>Traditional CCaaS</span><small>Cloud delivery, fragmented intelligence</small></header>
    <div class="legacy-map" aria-label="A fragmented contact-center model">
      <span>Channels</span><span>IVR / routing</span><span>Knowledge</span>
      <i></i>
      <span>Agent desktop</span><span>QA / analytics</span>
    </div>
    <p>Capabilities live in separate tools. Context is repeatedly copied, reinterpreted, or lost between them.</p>
  </article>

  <div class="shift-arrow" aria-hidden="true"><Icon name="arrow" size={22} /></div>

  <article class="shift-card xifi-shift">
    <header><span>XIFI platform</span><small>AI-native, session-first orchestration</small></header>
    <div class="shift-content">
      <ul>
        <li><Icon name="check" size={15} /> One interaction state across channels</li>
        <li><Icon name="check" size={15} /> Routing informed by intent and policy</li>
        <li><Icon name="check" size={15} /> Knowledge, actions, and provenance connected</li>
        <li><Icon name="check" size={15} /> Human handoff with the work already attached</li>
        <li><Icon name="check" size={15} /> Quality and operations designed into the session</li>
      </ul>
      <div class="mini-platform" aria-hidden="true">
        <div class="mini-rail"><i></i><i></i><i></i><i></i></div>
        <div class="mini-thread"><span></span><b></b><em></em></div>
        <div class="mini-chart"><i></i><i></i><i></i><i></i></div>
      </div>
    </div>
    <p>Legacy platforms can remain as migration adapters while XIFI progressively takes ownership of selected queues and journeys.</p>
  </article>
</div>
