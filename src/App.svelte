<script>
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import Icon from './lib/Icon.svelte';
  import Logo from './lib/Logo.svelte';
  import GlassConsole from './lib/GlassConsole.svelte';
  import FeatureBento from './lib/FeatureBento.svelte';
  import SolutionsRail from './lib/SolutionsRail.svelte';
  import WorkflowStack from './lib/WorkflowStack.svelte';
  import { reveal } from './lib/interactions.js';

  let menuOpen = false;
  let pilotOpen = false;
  let submitted = false;
  let email = '';
  const phrase = 'always ready.';
  let typedPhrase = '';
  let typingComplete = false;

  const openPilot = () => { pilotOpen = true; submitted = false; };
  const submitPilot = () => { if (email.trim()) submitted = true; };

  onMount(() => {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let typeTimer;
    if (reduced) {
      typedPhrase = phrase;
      typingComplete = true;
    } else {
      let index = 0;
      const type = () => {
        index += 1;
        typedPhrase = phrase.slice(0, index);
        if (index < phrase.length) typeTimer = window.setTimeout(type, 72);
        else typingComplete = true;
      };
      typeTimer = window.setTimeout(type, 550);
    }

    if (!reduced) {
      gsap.registerPlugin(ScrollTrigger);
      const context = gsap.context(() => {
        gsap.timeline({ defaults: { ease: 'power3.out' } })
          .from('.floating-nav', { y: -24, opacity: 0, duration: .8 })
          .from('.hero-copy > *', { y: 34, opacity: 0, duration: .85, stagger: .1 }, '-=.45')
          .from('.console-wrap', { x: 54, scale: .92, opacity: 0, duration: 1.05 }, '-=.78');

        gsap.utils.toArray('.media-scale').forEach((element) => {
          gsap.fromTo(element, { scale: .82, opacity: .28 }, {
            scale: 1,
            opacity: 1,
            ease: 'none',
            scrollTrigger: { trigger: element, start: 'top 92%', end: 'top 42%', scrub: true }
          });
        });

        const cards = gsap.utils.toArray('.workflow-card');
        cards.forEach((card, index) => {
          gsap.fromTo(card, { scale: .9, opacity: .45 }, {
            scale: 1,
            opacity: 1,
            ease: 'none',
            scrollTrigger: { trigger: card, start: 'top 88%', end: 'top 46%', scrub: true }
          });
          if (index < cards.length - 1) {
            gsap.to(card, {
              scale: .94,
              opacity: .5,
              ease: 'none',
              scrollTrigger: { trigger: cards[index + 1], start: 'top 75%', end: 'top 34%', scrub: true }
            });
          }
        });
      });
      return () => { window.clearTimeout(typeTimer); context.revert(); };
    }
    return () => window.clearTimeout(typeTimer);
  });
</script>

<svelte:head>
  <title>XIFI | Intelligent frontline support</title>
  <meta name="description" content="XIFI delivers grounded AI assistance, approved actions, and context-rich human handoff for modern support teams." />
</svelte:head>

<main id="top">
  <div class="ambient ambient-one"></div>
  <div class="ambient ambient-two"></div>

  <nav class="floating-nav" aria-label="Main navigation">
    <Logo />
    <div class:open={menuOpen} class="nav-links">
      <a href="#product" on:click={() => menuOpen = false}>Product</a>
      <a href="#solutions" on:click={() => menuOpen = false}>Solutions</a>
      <a href="#platform" on:click={() => menuOpen = false}>Platform</a>
      <a href="#integrations" on:click={() => menuOpen = false}>Integrations</a>
    </div>
    <button class="button button-primary nav-cta" on:click={openPilot}>Ask for a demo <Icon name="arrow" size={16} /></button>
    <button class="menu-button" on:click={() => menuOpen = !menuOpen} aria-label="Toggle menu" aria-expanded={menuOpen}>
      <Icon name={menuOpen ? 'close' : 'menu'} />
    </button>
  </nav>

  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-copy">
      <h1 id="hero-title" aria-label="Tech support, always ready.">
        Tech support,
        <span class="typed-line" aria-hidden="true">
          <span class:typing-complete={typingComplete} class="typewriter">
            <span class="typewriter-reserve">{phrase}</span>
            <span class="typewriter-text">{typedPhrase}</span>
          </span>
        </span>
      </h1>
      <p>Deliver instant, intelligent assistance across common support issues—grounded in your knowledge, controlled by your policies, and ready to hand off.</p>
      <div class="hero-actions">
        <button class="button button-primary" on:click={openPilot}>Ask for a demo <Icon name="arrow" size={17} /></button>
        <a class="button button-secondary" href="#product"><Icon name="play" size={17} /> See how it works</a>
      </div>
      <div class="trust-note"><span></span> Grounded answers. Approved actions. Human when it matters.</div>
    </div>
    <div class="console-wrap media-scale"><GlassConsole /></div>
  </section>

  <section class="section product-section" id="product" use:reveal>
    <div class="section-intro">
      <h2>AI assistance where it counts.</h2>
      <p>One support layer coordinates conversation, knowledge, action, and escalation without losing control.</p>
    </div>
    <FeatureBento />
  </section>

  <section class="integration-band" id="integrations" aria-label="Integration partners">
    <p>Built to meet your existing stack.</p>
    <div class="marquee-mask">
      <div class="marquee-track">
        {#each ['Salesforce', 'Zendesk', 'HubSpot', 'Freshdesk', 'ServiceNow', 'Microsoft Dynamics', 'Salesforce', 'Zendesk', 'HubSpot', 'Freshdesk', 'ServiceNow', 'Microsoft Dynamics'] as partner}
          <span>{partner}</span>
        {/each}
      </div>
    </div>
  </section>

  <section class="section solutions-section" id="solutions" use:reveal>
    <div class="section-intro split-intro">
      <h2>An intelligent frontline,<br />built around your business.</h2>
      <p>Shape the support journey around your knowledge, permissions, systems, and people.</p>
    </div>
    <SolutionsRail />
  </section>

  <section class="section workflow-section" id="platform">
    <div class="workflow-heading" use:reveal>
      <h2>Great automation knows<br />when to bring in a person.</h2>
      <p>Every answer is grounded. Every action is controlled. Every handoff arrives with context intact.</p>
    </div>
    <WorkflowStack />
  </section>

  <section class="cta-section" id="pilot" use:reveal>
    <div class="cta-orbit cta-orbit-one"></div>
    <div class="cta-orbit cta-orbit-two"></div>
    <h2>Ready to elevate your<br />frontline support?</h2>
    <p>Bring us one support journey worth improving.</p>
    <button class="button button-light" on:click={openPilot}>Ask for a demo <Icon name="arrow" size={17} /></button>
  </section>

  <footer>
    <div class="footer-brand"><Logo /><p>Grounded answers.<br />Approved actions.<br />Human when it matters.</p></div>
    <div><strong>Product</strong><a href="#product">Overview</a><a href="#platform">AI frontline</a><a href="#integrations">Integrations</a></div>
    <div><strong>Solutions</strong><a href="#solutions">Guided support</a><a href="#solutions">Ticket workflows</a><a href="#platform">Human handoff</a></div>
    <div><strong>Trust</strong><a href="#product">Security approach</a><a href="#product">Data privacy</a><a href="#product">Responsible AI</a></div>
    <div><strong>Company</strong><a href="#pilot">Pilot program</a><a href="mailto:hello@xifi.com">Contact</a><a href="#top">Back to top</a></div>
    <div class="footer-bottom"><span>© 2026 XIFI. All rights reserved.</span><span>Selected pilot engagements.</span></div>
  </footer>
</main>

{#if pilotOpen}
  <div class="modal-backdrop" role="presentation" on:click={() => pilotOpen = false}>
    <dialog open class="pilot-modal" aria-labelledby="pilot-title" on:click|stopPropagation>
      <button class="modal-close" aria-label="Close" on:click={() => pilotOpen = false}><Icon name="close" /></button>
      {#if submitted}
        <span class="success-mark"><Icon name="check" size={28} /></span>
        <h2 id="pilot-title">Your journey is on our radar.</h2>
        <p>We received your request and will contact you to discuss integrations, guardrails, and next steps.</p>
        <button class="button button-primary button-full" on:click={() => pilotOpen = false}>Done</button>
      {:else}
        <Logo compact />
        <h2 id="pilot-title">Bring us one journey worth improving.</h2>
        <p>Tell us where your customers need a better first step.</p>
        <form on:submit|preventDefault={submitPilot}>
          <label>Work email<input type="email" bind:value={email} placeholder="you@company.com" required /></label>
          <label>Target support journey<textarea placeholder="For example: duplicate billing questions and refund handoff"></textarea></label>
          <button class="button button-primary button-full" type="submit">Request a pilot conversation <Icon name="arrow" size={17} /></button>
        </form>
        <small>Do not include customer personal data or confidential production content.</small>
      {/if}
    </dialog>
  </div>
{/if}
