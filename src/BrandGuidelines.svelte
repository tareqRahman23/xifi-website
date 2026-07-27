<script>
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import Logo from './lib/Logo.svelte';
  import Icon from './lib/Icon.svelte';

  const baseUrl = import.meta.env.BASE_URL;
  const homeUrl = baseUrl;
  const logoUrl = `${baseUrl}assets/xifi-logo.svg`;
  const pngUrl = `${baseUrl}assets/xifi-app-icon.png`;
  const pdfUrl = `${baseUrl}assets/XIFI-Brand-Guidelines-v1.0.pdf`;

  let menuOpen = false;
  let copied = '';
  let copiedTimer;

  const colors = [
    { name: 'XIFI Pink', hex: '#D83F9B', role: 'Primary signal', dark: true },
    { name: 'Electric Blue', hex: '#2F63F5', role: 'Technology + focus', dark: true },
    { name: 'Signal Violet', hex: '#7552ED', role: 'Intelligence + depth', dark: true },
    { name: 'Warm Coral', hex: '#FF6E73', role: 'Human energy', dark: true },
    { name: 'Deep Ink', hex: '#101239', role: 'Authority + contrast', dark: true },
    { name: 'Cloud White', hex: '#FAFBFF', role: 'Space + clarity', dark: false }
  ];

  const principles = [
    ['Precise', 'Say exactly what the system knows, did, or needs next.'],
    ['Human', 'Use natural language without pretending the technology is a person.'],
    ['Composed', 'Make complex operations feel calm, ordered, and trustworthy.'],
    ['Progressive', 'Show forward movement from customer intent to a useful outcome.']
  ];

  const copyColor = async (hex) => {
    try {
      await navigator.clipboard.writeText(hex);
      copied = hex;
      window.clearTimeout(copiedTimer);
      copiedTimer = window.setTimeout(() => { copied = ''; }, 1400);
    } catch {
      copied = '';
    }
  };

  onMount(() => {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const onKeydown = (event) => {
      if (event.key === 'Escape') menuOpen = false;
    };
    window.addEventListener('keydown', onKeydown);

    if (!reduced) {
      gsap.registerPlugin(ScrollTrigger);
      const context = gsap.context(() => {
        gsap.timeline({ defaults: { ease: 'power4.out' } })
          .from('.brand-nav', { y: -24, opacity: 0, duration: 0.8 })
          .from('.brand-hero-copy > *', { y: 38, opacity: 0, duration: 0.82, stagger: 0.08 }, '-=0.42')
          .from('.hero-mark-shell', { x: 54, rotate: 5, scale: 0.9, opacity: 0, duration: 1.1 }, '-=0.82')
          .from('.journey-point', { scale: 0, opacity: 0, duration: 0.45, stagger: 0.08 }, '-=0.45');

        gsap.utils.toArray('.brand-reveal').forEach((element) => {
          gsap.from(element, {
            y: 36,
            opacity: 0,
            duration: 0.82,
            ease: 'power3.out',
            scrollTrigger: { trigger: element, start: 'top 88%', once: true }
          });
        });

        gsap.to('.journey-ribbon', {
          xPercent: 7,
          ease: 'none',
          scrollTrigger: { trigger: '.brand-hero', start: 'top top', end: 'bottom top', scrub: true }
        });

        gsap.to('.expression-ribbon', {
          xPercent: -10,
          rotate: -3,
          ease: 'none',
          scrollTrigger: { trigger: '.expression-section', start: 'top bottom', end: 'bottom top', scrub: true }
        });
      });

      return () => {
        window.clearTimeout(copiedTimer);
        window.removeEventListener('keydown', onKeydown);
        context.revert();
      };
    }

    return () => {
      window.clearTimeout(copiedTimer);
      window.removeEventListener('keydown', onKeydown);
    };
  });
</script>

<svelte:head>
  <title>XIFI Brand Guidelines | Intelligence in motion</title>
  <meta name="description" content="The XIFI identity system: logo, color, typography, voice, visual language, and practical brand applications." />
</svelte:head>

<div class="brand-page" id="top">
  <nav class="brand-nav" aria-label="Brand guidelines navigation">
    <Logo href={homeUrl} />
    <div class:open={menuOpen} class="brand-nav-links">
      <a href="#foundation" onclick={() => menuOpen = false}>Identity</a>
      <a href="#mark" onclick={() => menuOpen = false}>Mark</a>
      <a href="#system" onclick={() => menuOpen = false}>Color & type</a>
      <a href="#expression" onclick={() => menuOpen = false}>Voice</a>
      <a href="#use" onclick={() => menuOpen = false}>Applications</a>
      <a class="brand-nav-pdf" href={pdfUrl} download>Download PDF</a>
    </div>
    <a class="brand-home-link" href={pdfUrl} download>PDF <Icon name="download" size={15} /></a>
    <button class="brand-menu-button" aria-label="Toggle navigation" aria-expanded={menuOpen} onclick={() => menuOpen = !menuOpen}>
      <Icon name={menuOpen ? 'close' : 'menu'} />
    </button>
  </nav>

  <main>
    <section class="brand-hero" aria-labelledby="brand-hero-title">
      <div class="brand-hero-copy">
        <div class="chapter-line"><span>XIFI / Brand guidelines</span><span>Version 1.0 — 2026</span></div>
        <h1 id="brand-hero-title">Brand<br />system</h1>
        <p class="brand-hero-tagline"><span>Intelligence</span> <em>in motion.</em></p>
      </div>

      <div class="hero-mark-stage" aria-hidden="true">
        <div class="hero-orbit"></div>
        <div class="hero-mark-shell"><img src={logoUrl} alt="" /></div>
        <div class="journey-ribbon"></div>
        <span class="journey-point journey-point-one"><Icon name="chat" size={18} /></span>
        <span class="journey-point journey-point-two"><Icon name="brain" size={18} /></span>
        <span class="journey-point journey-point-three"><Icon name="check" size={18} /></span>
        <span class="journey-point journey-point-four"><Icon name="people" size={18} /></span>
      </div>

      <div class="hero-index"><span>01</span><i></i><span>05</span></div>
    </section>

    <section class="foundation-section" id="foundation">
      <div class="chapter-heading brand-reveal">
        <div class="chapter-number"><strong>00</strong><span>Foundation</span></div>
        <div>
          <h2>A system built around<br /><em>one useful outcome.</em></h2>
          <p>The brand should make sophisticated contact-center infrastructure feel understandable. Every composition begins with intent, shows controlled intelligence at work, and ends with a clear next step.</p>
        </div>
      </div>

      <div class="outcome-rail brand-reveal" aria-label="XIFI interaction outcomes">
        <article><span>01</span><Icon name="chat" size={29} /><h3>Grounded answer</h3><p>Approved knowledge, expressed with clarity and source-aware confidence.</p></article>
        <i aria-hidden="true"><Icon name="arrow" size={18} /></i>
        <article><span>02</span><Icon name="check" size={29} /><h3>Approved action</h3><p>Permissioned work with visible control, verification, and a receipt.</p></article>
        <i aria-hidden="true"><Icon name="arrow" size={18} /></i>
        <article><span>03</span><Icon name="people" size={29} /><h3>Human handoff</h3><p>A calm transition with customer context intact and no forced restart.</p></article>
      </div>

      <div class="personality-grid brand-reveal">
        <div class="personality-intro"><span>Brand character</span><h3>Capable without being cold.</h3></div>
        {#each principles as principle, index}
          <article><span>0{index + 1}</span><h4>{principle[0]}</h4><p>{principle[1]}</p></article>
        {/each}
      </div>
    </section>

    <section class="mark-section" id="mark">
      <div class="chapter-heading brand-reveal">
        <div class="chapter-number"><strong>01</strong><span>The mark</span></div>
        <div>
          <h2>A coordinated<br /><em>handoff.</em></h2>
          <p>Two forms approach, meet, and continue together. The XIFI mark holds the product promise in one gesture: intelligence and human judgment working as one continuous system.</p>
        </div>
      </div>

      <div class="mark-story brand-reveal">
        <div class="mark-display"><img src={logoUrl} alt="XIFI app icon" /></div>
        <div class="mark-journey" aria-label="Two paths approach, resolve, and continue together">
          <div class="story-paths">
            <span class="story-line story-line-pink"></span>
            <span class="story-line story-line-blue"></span>
            <img src={logoUrl} alt="" aria-hidden="true" />
            <span class="story-line story-line-out-pink"></span>
            <span class="story-line story-line-out-blue"></span>
          </div>
          <div class="story-labels"><span>Two paths<br />approach.</span><span>They meet,<br />resolve, and align.</span><span>Together,<br />they continue.</span></div>
        </div>
      </div>

      <div class="mark-rules brand-reveal">
        <article class="rule-copy"><span>Core mark</span><h3>Keep it recognizable.</h3><p>Use the full-color app icon whenever the format allows. Its rounded field, pink spectrum, and white symbol are one protected unit.</p></article>
        <article class="clearspace-card">
          <span>Clear space</span>
          <div class="clearspace-demo"><b>x</b><b>x</b><b>x</b><b>x</b><img src={logoUrl} alt="XIFI mark with clear-space boundary" /></div>
          <p>Keep a minimum clear space equal to one quarter of the icon width on every side.</p>
        </article>
        <article class="size-card">
          <span>Minimum size</span>
          <div class="size-demo"><img src={logoUrl} alt="XIFI mark shown at its recommended minimum digital size" /><i></i><strong>24 px</strong></div>
          <p>For digital use, keep the icon at 24 px or larger. Use the wordmark lockup at 120 px or larger.</p>
        </article>
      </div>

      <div class="usage-strip brand-reveal">
        <div class="usage-heading"><span>Approved applications</span><h3>One mark.<br />Three environments.</h3></div>
        <article class="usage-light"><img src={logoUrl} alt="XIFI icon on Cloud White" /><span>Cloud White</span></article>
        <article class="usage-dark"><img src={logoUrl} alt="XIFI icon on Deep Ink" /><span>Deep Ink</span></article>
        <article class="usage-spectrum"><img src={logoUrl} alt="XIFI icon on the brand spectrum" /><span>Brand spectrum</span></article>
        <aside><strong>Never</strong><p>stretch or skew</p><p>recolor the symbol</p><p>add outlines or effects</p><p>place on visual noise</p></aside>
      </div>
    </section>

    <section class="system-section" id="system">
      <div class="system-intro brand-reveal">
        <div class="chapter-number light"><strong>02</strong><span>The system</span></div>
        <h2>Color carries<br />the conversation.</h2>
        <p>The spectrum represents the journey from signal to understanding to human resolution. Use it directionally, with restraint, and always beside generous neutral space.</p>
      </div>

      <div class="palette" aria-label="XIFI color palette">
        {#each colors as color}
          <button
            class:light-swatch={!color.dark}
            class="color-swatch"
            style={`--swatch:${color.hex}`}
            aria-label={`Copy ${color.name} ${color.hex}`}
            onclick={() => copyColor(color.hex)}
          >
            <span>{color.name}</span><strong>{copied === color.hex ? 'Copied' : color.hex}</strong><small>{color.role}</small>
          </button>
        {/each}
      </div>

      <div class="gradient-recipe brand-reveal">
        <div><span>Spectrum gradient</span><h3>Signal → intelligence → human</h3></div>
        <div class="gradient-bar"><i></i><i></i><i></i><i></i></div>
        <code>90deg · #2F63F5 0% · #7552ED 38% · #D83F9B 70% · #FF6E73 100%</code>
      </div>

      <div class="type-section brand-reveal">
        <div class="type-name"><span>Primary typeface</span><h3>Outfit</h3><p>Geometric enough for technology. Open enough for people.</p></div>
        <div class="type-specimen"><h4>Human clarity.<br />Machine precision.</h4><p class="alphabet">ABCDEFGHIJKLMNOPQRSTUVWXYZ</p><p class="alphabet lowercase">abcdefghijklmnopqrstuvwxyz</p><p class="alphabet">0123456789 · !@#$%&amp;*()+</p></div>
      </div>

      <div class="type-scale brand-reveal">
        <article><span>Display / 72–120</span><strong>Move with purpose.</strong></article>
        <article><span>Heading / 40–72</span><strong>Clear at every turn.</strong></article>
        <article><span>Body / 16–20</span><p>Use sentence case, a relaxed line height, and short paragraphs that make a complex system easier to navigate.</p></article>
        <article><span>Label / 11–13</span><b>APPROVED ACTION · SESSION ACTIVE</b></article>
      </div>
    </section>

    <section class="expression-section" id="expression">
      <div class="expression-ribbon" aria-hidden="true"></div>
      <div class="expression-intro brand-reveal">
        <div class="chapter-number dark"><strong>03</strong><span>Expression</span></div>
        <h2>Simple.<br />Controlled.<br /><em>Connected.</em></h2>
        <p>Use dark fields for concentrated moments: campaign statements, product proof, and decisive transitions. Let one luminous path carry the composition.</p>
      </div>

      <div class="expression-flow brand-reveal" aria-label="XIFI product outcome sequence">
        <article><Icon name="chat" size={31} /><span>Grounded<br />answer</span></article>
        <i><Icon name="arrow" size={19} /></i>
        <article><Icon name="check" size={31} /><span>Approved<br />action</span></article>
        <i><Icon name="arrow" size={19} /></i>
        <article><Icon name="people" size={31} /><span>Human<br />handoff</span></article>
      </div>

      <div class="voice-grid brand-reveal">
        <article class="say-card"><span>Say</span><ul><li>“Here’s what I found.”</li><li>“Based on your account context…”</li><li>“Here’s what we can do next.”</li><li>“I’ll connect you with a person who can help.”</li></ul></article>
        <article class="avoid-card"><span>Don’t say</span><ul><li>“I think…”</li><li>“You need to…”</li><li>“As an AI model…”</li><li>“Please hold while I transfer you.”</li></ul></article>
      </div>

      <div class="visual-language brand-reveal">
        <article><span>Imagery</span><h3>Show the journey, not the robot.</h3><p>Favor purposeful paths, quiet environments, human-scale interface moments, and atmospheric material light. Avoid generic AI faces, headset stock photography, and decorative tech clichés.</p></article>
        <article><span>Motion</span><h3>Move forward, then settle.</h3><p>Use motion to reveal sequence, confirm state, or connect one outcome to the next. Keep easing composed, respect reduced-motion preferences, and avoid movement without meaning.</p></article>
      </div>
    </section>

    <section class="applications-section" id="use">
      <div class="chapter-heading brand-reveal">
        <div class="chapter-number"><strong>04</strong><span>In use</span></div>
        <div>
          <h2>Recognizable at<br /><em>every scale.</em></h2>
          <p>The identity should remain calm and exact whether it appears as an app icon, a product surface, or a single campaign statement.</p>
        </div>
      </div>

      <div class="application-stage brand-reveal">
        <div class="app-tile"><img src={logoUrl} alt="XIFI app icon" /><span>XIFI</span><small>Customer operations</small></div>
        <div class="product-surface">
          <header><span><i></i>XIFI session</span><small>Policy controlled</small></header>
          <div class="surface-message customer">Help me understand my billing change.</div>
          <div class="surface-state"><Icon name="brain" size={17} /><span><strong>Intent understood</strong><small>Account + policy context resolved</small></span></div>
          <div class="surface-message assistant"><strong>Here’s what changed.</strong><p>Your plan moved to the current rate at renewal. I can show the line items or connect you with billing.</p></div>
          <footer><span><Icon name="shield" size={15} /> Grounded response</span><button>Continue <Icon name="arrow" size={14} /></button></footer>
        </div>
        <div class="campaign-tile"><span>XIFI</span><h3>Clarity moves<br />the conversation.</h3><div></div><small>Simple. Controlled. Connected.</small></div>
      </div>

      <div class="asset-bar brand-reveal">
        <div><span>Core assets</span><h3>Start with the source.</h3><p>Use the supplied files without redrawing, tracing, or applying additional effects.</p></div>
        <div class="asset-actions">
          <a class="brand-button brand-button-primary" href={pdfUrl} download>Download PDF <Icon name="download" size={16} /></a>
          <a class="brand-button brand-button-primary" href={logoUrl} download>Download SVG <Icon name="download" size={16} /></a>
          <a class="brand-button brand-button-secondary" href={pngUrl} download>Download PNG <Icon name="download" size={16} /></a>
        </div>
      </div>
    </section>
  </main>

  <footer class="brand-footer">
    <div><Logo href={homeUrl} /><p>AI-native contact-center infrastructure for modern customer operations.</p></div>
    <div><span>Brand system</span><strong>Version 1.0</strong></div>
    <div><span>Last updated</span><strong>July 2026</strong></div>
    <a href="#top">Back to top <Icon name="arrow" size={14} /></a>
    <p class="brand-footer-bottom"><span>© 2026 XIFI. All rights reserved.</span><span>Simple. Controlled. Connected.</span></p>
  </footer>
</div>
