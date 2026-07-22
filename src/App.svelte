<script>
  import Icon from './lib/Icon.svelte';
  import Logo from './lib/Logo.svelte';
  import ProductPreview from './lib/ProductPreview.svelte';
  import Journey from './lib/Journey.svelte';
  import Handoff from './lib/Handoff.svelte';
  import Footer from './lib/Footer.svelte';
  import LiquidButton from './lib/LiquidButton.svelte';
  import { parallax, reveal } from './lib/interactions.js';

  let menuOpen = false;
  let pilotOpen = false;
  let submitted = false;
  let email = '';
  const openPilot = () => { pilotOpen = true; submitted = false; };
  const submitPilot = () => { if (email.trim()) submitted = true; };
</script>

<svelte:head>
  <meta property="og:title" content="Tech support that is always ready to help." />
  <meta property="og:description" content="XIFI delivers instant, intelligent assistance across common support issues without adding pressure to your team." />
</svelte:head>

<main id="top">
  <div class="site-shell">
    <nav aria-label="Main navigation">
      <Logo />
      <div class:open={menuOpen} class="nav-links">
        <a href="#product" on:click={() => menuOpen = false}>Product</a>
        <a href="#solutions" on:click={() => menuOpen = false}>Solutions</a>
        <a href="#platform" on:click={() => menuOpen = false}>Platform</a>
      </div>
      <button class="button nav-cta" on:click={openPilot}>Join the pilot</button>
      <button class="menu-button" on:click={() => menuOpen = !menuOpen} aria-label="Toggle menu" aria-expanded={menuOpen}><Icon name={menuOpen ? 'close' : 'menu'} /></button>
    </nav>

    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-field" use:parallax={{ strength: .42, scrollStrength: .3 }}>
        <div class="hero-copy">
          <h1 id="hero-title">Tech support that is<br /><span>always ready</span> to help.</h1>
          <p>Deliver instant, intelligent assistance across common IT issues — without adding pressure to your support team.</p>
          <div class="hero-actions">
            <LiquidButton label="Ask for a demo" onpress={openPilot} />
            <a class="button secondary" href="#product">See how it works <Icon name="play" size={16} /></a>
          </div>
        </div>
        <ProductPreview />
      </div>
    </section>

    <section class="principles" id="product" use:reveal>
      <h2>AI assistance where it counts.</h2>
      <div class="principle-row">
        <div><span>01</span><strong>Ground every answer</strong><p>Use approved knowledge and keep source context attached.</p></div>
        <div><span>02</span><strong>Control every action</strong><p>Allow only defined, permissioned workflows with confirmed results.</p></div>
        <div><span>03</span><strong>Keep the human path</strong><p>Escalate with the conversation context already prepared.</p></div>
      </div>
    </section>

    <section class="journey-section section-pad" id="solutions" use:reveal>
      <header class="section-heading centered"><h2>Our Avatars are a bit different.</h2><p>Instead of a diffusion model we use 3D graphics that provide consistent results.</p></header>
      <Journey />
    </section>

    <section class="capabilities section-pad" id="platform" use:reveal>
      <div class="capability-copy"><h2>An intelligent frontline,<br />built around your business.</h2><p>Coordinate conversation, knowledge, AI, voice, avatar, CRM actions, and human escalation through one support experience.</p><a class="text-link" href="#human">Explore the support journey <Icon name="arrow" size={16} /></a></div>
      <div class="capability-stack">
        <article><span class="cap-icon"><Icon name="book" /></span><h3>Grounded answers</h3><p>Anchor responses in approved knowledge and policies.</p></article>
        <article class="featured"><span class="cap-icon"><Icon name="shield" /></span><h3>Approved actions</h3><p>Take permitted steps with clear results and traceability.</p></article>
        <article><span class="cap-icon handoff-icon"><Icon name="people" /></span><h3>Context-rich handoff</h3><p>Give specialists the story, sources, and actions already completed.</p></article>
      </div>
    </section>

    <section class="trust-strip" id="trust" use:reveal><div><Icon name="lock" size={20} /><strong>Control travels with the conversation.</strong></div><p>Identity, consent, policy, source provenance, tenant boundaries, and audit evidence are designed into the support journey.</p></section>

    <section class="human section-pad" id="human" use:reveal>
      <div class="human-copy"><h2>The best automated experience knows when to bring in a person.</h2><p>Escalate on customer request, policy, confidence, or service health — with the context already prepared.</p><a class="text-link" href="#pilot">Design your handoff journey <Icon name="arrow" size={16} /></a></div>
      <Handoff />
    </section>

    <section class="pilot" id="pilot" use:reveal><div><h2>We integrate to your Existing Solution</h2><p>So no hassle for you.</p><LiquidButton label="Join the pilot" tone="light" onpress={openPilot} /></div></section>
    <Footer />
  </div>
</main>

{#if pilotOpen}
  <div class="modal-backdrop" role="presentation" on:click={() => pilotOpen = false}>
    <dialog open class="pilot-modal" aria-labelledby="pilot-title" on:click|stopPropagation>
      <button class="modal-close" aria-label="Close" on:click={() => pilotOpen = false}><Icon name="close" /></button>
      {#if submitted}
        <span class="success-mark"><Icon name="check" size={28} /></span><h2 id="pilot-title">Thank you.</h2><p>We received your request and will contact you to discuss the support journey, integrations, and next steps.</p><button class="button primary full" on:click={() => pilotOpen = false}>Done</button>
      {:else}
        <Logo compact /><h2 id="pilot-title">Bring us one journey worth improving.</h2><p>Tell us where your customers need a better first step.</p>
        <form on:submit|preventDefault={submitPilot}><label>Work email<input type="email" bind:value={email} placeholder="you@company.com" required /></label><label>Target support journey<textarea placeholder="For example: duplicate billing questions and refund handoff"></textarea></label><button class="button primary full" type="submit">Request a pilot conversation <Icon name="arrow" size={17} /></button></form>
        <small>Do not include customer personal data or confidential production content.</small>
      {/if}
    </dialog>
  </div>
{/if}
