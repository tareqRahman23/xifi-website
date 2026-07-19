<script>
  import Icon from './lib/Icon.svelte';
  import Logo from './lib/Logo.svelte';
  import ProductPreview from './lib/ProductPreview.svelte';
  import Journey from './lib/Journey.svelte';
  import Handoff from './lib/Handoff.svelte';
  import Footer from './lib/Footer.svelte';

  let menuOpen = false;
  let pilotOpen = false;
  let submitted = false;
  let email = '';

  const openPilot = () => {
    pilotOpen = true;
    submitted = false;
  };

  const submitPilot = () => {
    if (email.trim()) submitted = true;
  };
</script>

<svelte:head>
  <meta property="og:title" content="Resolve the routine. Elevate every conversation." />
  <meta property="og:description" content="Meet XIFI, an AI-assisted frontline for grounded answers, controlled support actions, and seamless human handoffs." />
</svelte:head>

<main id="top">
  <div class="site-shell">
    <section class="hero" aria-labelledby="hero-title">
      <nav aria-label="Main navigation">
        <Logo />
        <div class:open={menuOpen} class="nav-links">
          <a href="#product" on:click={() => menuOpen = false}>Product</a>
          <a href="#solutions" on:click={() => menuOpen = false}>Solutions</a>
          <a href="#platform" on:click={() => menuOpen = false}>Platform</a>
          <a href="#trust" on:click={() => menuOpen = false}>Trust</a>
        </div>
        <button class="button nav-cta" on:click={openPilot}>Join the pilot</button>
        <button class="menu-button" on:click={() => menuOpen = !menuOpen} aria-label="Toggle menu" aria-expanded={menuOpen}><Icon name={menuOpen ? 'close' : 'menu'} /></button>
      </nav>

      <div class="hero-field">
        <div class="light-path path-one"></div><div class="light-path path-two"></div>
        <div class="hero-copy">
          <h1 id="hero-title">Resolve the routine.<br /><span>Elevate every conversation.</span></h1>
          <p>Grounded answers, approved actions, and a human path built into every support journey.</p>
          <div class="hero-actions">
            <button class="button primary" on:click={openPilot}>Join the pilot <Icon name="arrow" size={17} /></button>
            <a class="button secondary" href="#product">See how it works <Icon name="play" size={18} /></a>
          </div>
        </div>
        <ProductPreview />
      </div>
    </section>

    <section class="principles" id="product">
      <p class="section-lead">AI assistance where it counts.</p>
      <div class="principle-row">
        <div><span>01</span><strong>Ground every answer</strong><p>Use approved knowledge and keep source context attached.</p></div>
        <div><span>02</span><strong>Control every action</strong><p>Allow only defined, permissioned workflows with confirmed results.</p></div>
        <div><span>03</span><strong>Keep the human path</strong><p>Escalate with the conversation context already prepared.</p></div>
      </div>
    </section>

    <section class="journey-section section-pad" id="solutions">
      <header class="section-heading centered">
        <h2>From first contact to the right outcome.</h2>
        <p>One connected journey keeps customers moving without losing context.</p>
      </header>
      <Journey />
    </section>

    <section class="capabilities section-pad" id="platform">
      <div class="capability-copy">
        <h2>An intelligent frontline,<br />built around your business.</h2>
        <p>Coordinate conversation, knowledge, AI, voice, avatar, CRM actions, and human escalation through one support experience.</p>
        <a class="text-link" href="#human">Explore the support journey <Icon name="arrow" size={16} /></a>
      </div>
      <div class="capability-stack">
        <article><span class="cap-icon"><Icon name="book" /></span><h3>Grounded answers</h3><p>Anchor responses in approved knowledge and policies.</p></article>
        <article class="featured"><span class="cap-icon"><Icon name="shield" /></span><h3>Approved actions</h3><p>Take permitted steps with clear results and traceability.</p></article>
        <article><span class="cap-icon handoff-icon"><Icon name="people" /></span><h3>Context-rich handoff</h3><p>Give specialists the story, sources, and actions already completed.</p></article>
      </div>
    </section>

    <section class="trust-strip" id="trust">
      <div><Icon name="lock" size={22} /><strong>Control travels with the conversation.</strong></div>
      <p>Identity, consent, policy, source provenance, tenant boundaries, and audit evidence are designed into the support journey.</p>
    </section>

    <section class="human section-pad" id="human">
      <div class="human-copy"><h2>The best automated experience knows when to bring in a person.</h2><p>Escalate on customer request, policy, confidence, or service health - with the context already prepared.</p><a class="text-link" href="#pilot">Design your handoff journey <Icon name="arrow" size={16} /></a></div>
      <Handoff />
    </section>

    <section class="pilot" id="pilot">
      <div class="light-path path-three"></div>
      <div><h2>Make the first support interaction count.</h2><p>Bring us one support journey worth improving.</p><div><button class="button pilot-primary" on:click={openPilot}>Join the pilot <Icon name="arrow" size={17} /></button><a class="button pilot-secondary" href="mailto:hello@xifi.com">Talk to our team</a></div></div>
    </section>

    <Footer />
  </div>
</main>

{#if pilotOpen}
  <div class="modal-backdrop" role="presentation" on:click={() => pilotOpen = false}>
    <dialog open class="pilot-modal" aria-labelledby="pilot-title" on:click|stopPropagation>
      <button class="modal-close" aria-label="Close" on:click={() => pilotOpen = false}><Icon name="close" /></button>
      {#if submitted}
        <span class="success-mark"><Icon name="check" size={28} /></span>
        <h2 id="pilot-title">Thank you.</h2>
        <p>We received your request and will contact you to discuss the support journey, integrations, and next steps.</p>
        <button class="button primary full" on:click={() => pilotOpen = false}>Done</button>
      {:else}
        <Logo compact />
        <h2 id="pilot-title">Bring us one journey worth improving.</h2>
        <p>Tell us where your customers need a better first step.</p>
        <form on:submit|preventDefault={submitPilot}>
          <label>Work email<input type="email" bind:value={email} placeholder="you@company.com" required /></label>
          <label>Target support journey<textarea placeholder="For example: duplicate billing questions and refund handoff"></textarea></label>
          <button class="button primary full" type="submit">Request a pilot conversation <Icon name="arrow" size={17} /></button>
        </form>
        <small>Do not include customer personal data or confidential production content.</small>
      {/if}
    </dialog>
  </div>
{/if}
