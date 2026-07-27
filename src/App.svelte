<script>
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import Icon from './lib/Icon.svelte';
  import Logo from './lib/Logo.svelte';
  import GlassConsole from './lib/GlassConsole.svelte';
  import PlatformFlow from './lib/PlatformFlow.svelte';
  import CcaasShift from './lib/CcaasShift.svelte';
  import WorkflowStack from './lib/WorkflowStack.svelte';

  let menuOpen = false;
  let pilotOpen = false;
  let submitted = false;
  let email = '';
  const phrase = 'rebuilt for AI.';
  let typedPhrase = '';
  let typingComplete = false;

  const capabilities = [
    ['channels', 'Voice + digital'],
    ['route', 'Routing + queues'],
    ['brain', 'Knowledge + reasoning'],
    ['shield', 'Approved actions'],
    ['headset', 'Human operations'],
    ['chart', 'Quality + insight']
  ];

  const openPilot = () => { pilotOpen = true; submitted = false; };
  const closePilot = () => { pilotOpen = false; };
  const submitPilot = () => { if (email.trim()) submitted = true; };

  onMount(() => {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let typeTimer;
    const onKeydown = (event) => { if (event.key === 'Escape') closePilot(); };
    window.addEventListener('keydown', onKeydown);

    if (reduced) {
      typedPhrase = phrase;
      typingComplete = true;
    } else {
      let index = 0;
      const type = () => {
        index += 1;
        typedPhrase = phrase.slice(0, index);
        if (index < phrase.length) typeTimer = window.setTimeout(type, 66);
        else typingComplete = true;
      };
      typeTimer = window.setTimeout(type, 480);
    }

    if (!reduced) {
      gsap.registerPlugin(ScrollTrigger);
      const context = gsap.context(() => {
        gsap.timeline({ defaults: { ease: 'power4.out' } })
          .from('.floating-nav', { y: -28, opacity: 0, duration: 0.9 })
          .from('.hero-overline, .hero-copy h1, .hero-copy > p', { y: 42, opacity: 0, duration: 0.9, stagger: 0.09 }, '-=0.48')
          .from('.hero-actions, .hero-proof', { y: 22, opacity: 0, duration: 0.72, stagger: 0.1 }, '-=0.54')
          .from('.console-wrap', { x: 70, rotateY: -7, scale: 0.9, opacity: 0, duration: 1.15 }, '-=0.95')
          .from('.capability-item', { y: 18, opacity: 0, duration: 0.65, stagger: 0.07 }, '-=0.5');

        gsap.to('.hero-copy', {
          yPercent: 12,
          opacity: 0.3,
          ease: 'none',
          scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom 28%', scrub: true }
        });
        gsap.to('.console-wrap', {
          yPercent: -8,
          rotateZ: 0.8,
          ease: 'none',
          scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom 20%', scrub: true }
        });
        gsap.to('.page-progress', {
          scaleX: 1,
          ease: 'none',
          scrollTrigger: { start: 0, end: 'max', scrub: 0.25 }
        });

        gsap.utils.toArray('.reveal-copy').forEach((element) => {
          gsap.from(element, {
            y: 42,
            opacity: 0,
            duration: 0.88,
            ease: 'power3.out',
            scrollTrigger: { trigger: element, start: 'top 86%', once: true }
          });
        });

        gsap.from('.flow-layer', {
          y: 58,
          opacity: 0,
          duration: 0.9,
          stagger: 0.12,
          ease: 'power3.out',
          scrollTrigger: { trigger: '.platform-flow', start: 'top 78%', once: true }
        });
        gsap.from('.flow-connector', {
          scale: 0,
          opacity: 0,
          duration: 0.5,
          stagger: 0.13,
          ease: 'back.out(1.8)',
          scrollTrigger: { trigger: '.platform-flow', start: 'top 70%', once: true }
        });

        gsap.from('.shift-card', {
          clipPath: 'inset(0 50% 0 50% round 28px)',
          opacity: 0,
          duration: 1.1,
          stagger: 0.18,
          ease: 'power4.inOut',
          scrollTrigger: { trigger: '.shift-grid', start: 'top 78%', once: true }
        });

        const cards = gsap.utils.toArray('.workflow-card');
        cards.forEach((card, index) => {
          gsap.fromTo(card, { scale: 0.9, opacity: 0.35 }, {
            scale: 1,
            opacity: 1,
            ease: 'none',
            scrollTrigger: { trigger: card, start: 'top 90%', end: 'top 46%', scrub: true }
          });
          if (index < cards.length - 1) {
            gsap.to(card, {
              scale: 0.945,
              opacity: 0.46,
              ease: 'none',
              scrollTrigger: { trigger: cards[index + 1], start: 'top 76%', end: 'top 35%', scrub: true }
            });
          }
        });

        gsap.to('.cta-glow', {
          xPercent: 44,
          rotate: 18,
          ease: 'none',
          scrollTrigger: { trigger: '.cta-section', start: 'top bottom', end: 'bottom top', scrub: true }
        });
      });

      return () => {
        window.clearTimeout(typeTimer);
        window.removeEventListener('keydown', onKeydown);
        context.revert();
      };
    }

    return () => {
      window.clearTimeout(typeTimer);
      window.removeEventListener('keydown', onKeydown);
    };
  });
</script>

<svelte:head>
  <title>XIFI | The contact center, rebuilt for AI</title>
  <meta name="description" content="XIFI is an AI-native contact-center platform designed to replace the traditional CCaaS operating model with first-party services for channels, orchestration, knowledge, actions, handoff, quality, and operations." />
</svelte:head>

<div class="page-progress" aria-hidden="true"></div>

<main id="top">
  <nav class="floating-nav" aria-label="Main navigation">
    <Logo />
    <div class:open={menuOpen} class="nav-links">
      <a href="#product" onclick={() => menuOpen = false}>Platform</a>
      <a href="#model" onclick={() => menuOpen = false}>Why XIFI</a>
      <a href="#experience" onclick={() => menuOpen = false}>Experience</a>
      <a href="#pilot" onclick={() => menuOpen = false}>Pilot</a>
    </div>
    <button class="button button-primary nav-cta" onclick={openPilot}>Design your pilot <Icon name="arrow" size={16} /></button>
    <button class="menu-button" onclick={() => menuOpen = !menuOpen} aria-label="Toggle menu" aria-expanded={menuOpen}>
      <Icon name={menuOpen ? 'close' : 'menu'} />
    </button>
  </nav>

  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-backdrop" aria-hidden="true"><i></i><i></i></div>
    <div class="hero-copy">
      <span class="hero-overline">AI-native contact-center platform</span>
      <h1 id="hero-title" aria-label="The contact center, rebuilt for AI.">
        The contact center,
        <span class="typed-line" aria-hidden="true">
          <span class:typing-complete={typingComplete} class="typewriter">
            <span class="typewriter-text">{typedPhrase}</span>
          </span>
        </span>
      </h1>
      <p>One system for voice, digital channels, intelligent routing, approved knowledge, controlled actions, human handoff, quality, and operations.</p>
      <div class="hero-actions">
        <button class="button button-primary" onclick={openPilot}>Design your pilot <Icon name="arrow" size={17} /></button>
        <a class="text-link" href="#product"><Icon name="play" size={18} /> See the platform in action</a>
      </div>
      <div class="hero-proof">
        <span><Icon name="layers" size={16} /> First-party services</span>
        <span><Icon name="shield" size={16} /> Policy controlled</span>
        <span><Icon name="people" size={16} /> Human in the loop</span>
      </div>
    </div>
    <div class="console-wrap"><GlassConsole /></div>
  </section>

  <section class="capability-rail" aria-label="XIFI platform capabilities">
    {#each capabilities as capability}
      <div class="capability-item"><Icon name={capability[0]} size={20} /><span>{capability[1]}</span></div>
    {/each}
  </section>

  <section class="section platform-section" id="product">
    <div class="statement reveal-copy">
      <span class="section-kicker">Built different</span>
      <h2>Not another <em>bot on top</em> of your CCaaS.</h2>
      <p>Traditional CCaaS moved the contact center to the cloud. XIFI is designed for the next shift: an AI-native operating model that connects the interaction from first contact to final resolution.</p>
    </div>
    <PlatformFlow />
  </section>

  <section class="section model-section" id="model">
    <div class="section-heading reveal-copy">
      <span class="section-kicker">A new operating model</span>
      <h2>From fragmented CCaaS to one intelligent platform.</h2>
      <p>XIFI coordinates the session while bounded services own the capabilities that need to scale, fail, and evolve independently.</p>
    </div>
    <CcaasShift />
  </section>

  <section class="section workflow-section" id="experience">
    <div class="workflow-heading reveal-copy">
      <div><span class="section-kicker">The XIFI experience</span><h2>Automation with a human path built in.</h2></div>
      <p>Every interaction stays grounded in approved information, constrained by policy, and ready to move to the right person with context intact.</p>
    </div>
    <WorkflowStack />
  </section>

  <section class="cta-section" id="pilot">
    <div class="cta-glow" aria-hidden="true"></div>
    <span class="section-kicker">Selected pilot engagements</span>
    <h2>Ready to design your <em>pilot?</em></h2>
    <p>Choose one queue or customer journey. We’ll scope the channels, policies, systems, human path, and proof plan together.</p>
    <button class="button button-light" onclick={openPilot}>Design your pilot <Icon name="arrow" size={17} /></button>
  </section>

  <footer>
    <div class="footer-brand"><Logo /><p>AI-native contact-center infrastructure for modern customer operations.</p></div>
    <div><strong>Platform</strong><a href="#product">Service layers</a><a href="#model">Operating model</a><a href="#experience">Experience</a></div>
    <div><strong>Use cases</strong><a href="#pilot">Selected queues</a><a href="#pilot">Guided resolution</a><a href="#pilot">Human handoff</a></div>
    <div><strong>Company</strong><a href="#pilot">Pilot program</a><a href="mailto:hello@getxifi.com">Contact</a><a href="#top">Back to top</a></div>
    <div class="footer-note"><strong>Product status</strong><p>XIFI is currently offered through selected, scoped pilot engagements.</p></div>
    <div class="footer-bottom"><span>© 2026 XIFI. All rights reserved.</span><span>Simple. Controlled. Connected.</span></div>
  </footer>
</main>

{#if pilotOpen}
  <div class="modal-backdrop" role="presentation" onclick={closePilot}>
    <dialog open class="pilot-modal" aria-labelledby="pilot-title" onclick={(event) => event.stopPropagation()}>
      <button class="modal-close" aria-label="Close" onclick={closePilot}><Icon name="close" /></button>
      {#if submitted}
        <span class="success-mark"><Icon name="check" size={28} /></span>
        <h2 id="pilot-title">Your journey is on our radar.</h2>
        <p>We received your request and will contact you to discuss scope, integrations, guardrails, and proof criteria.</p>
        <button class="button button-primary button-full" onclick={closePilot}>Done</button>
      {:else}
        <Logo compact />
        <h2 id="pilot-title">Bring us one journey worth rebuilding.</h2>
        <p>Start with a queue, a channel, and an outcome your team can measure.</p>
        <form onsubmit={(event) => { event.preventDefault(); submitPilot(); }}>
          <label>Work email<input type="email" bind:value={email} placeholder="you@company.com" required /></label>
          <label>Target journey<textarea placeholder="For example: billing calls that require account verification, policy lookup, and specialist handoff"></textarea></label>
          <button class="button button-primary button-full" type="submit">Request a pilot conversation <Icon name="arrow" size={17} /></button>
        </form>
        <small>Do not include customer personal data or confidential production content.</small>
      {/if}
    </dialog>
  </div>
{/if}
