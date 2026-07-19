import { LiquidGlass } from '@ybouane/liquidglass';

const reducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const compactViewport = () => window.matchMedia('(max-width: 820px)').matches;

export function liquidGlass(node, options = {}) {
  let instance;
  let cancelled = false;

  const start = async () => {
    const glassElements = [...node.children].filter((child) => child.hasAttribute('data-liquid-glass'));

    if (!glassElements.length || reducedMotion() || compactViewport()) {
      node.classList.add('liquidglass-fallback');
      return;
    }

    try {
      if (document.fonts?.ready) await document.fonts.ready;
      if (cancelled) return;

      const nextInstance = await LiquidGlass.init({
        root: node,
        glassElements,
        defaults: options.defaults ?? {}
      });

      if (cancelled) {
        nextInstance.destroy();
        return;
      }

      instance = nextInstance;
      node.classList.add('liquidglass-ready');
    } catch {
      node.classList.add('liquidglass-fallback');
    }
  };

  requestAnimationFrame(start);

  return {
    destroy() {
      cancelled = true;
      instance?.destroy();
    }
  };
}

export function parallax(node, options = {}) {
  const strength = options.strength ?? 1;
  const scrollStrength = options.scrollStrength ?? 1;
  let frame;
  let pointerX = 0;
  let pointerY = 0;
  let scrollValue = 0;

  const paint = () => {
    frame = undefined;
    node.style.setProperty('--parallax-x', String(pointerX * strength));
    node.style.setProperty('--parallax-y', String(pointerY * strength));
    node.style.setProperty('--parallax-scroll', String(scrollValue * scrollStrength));
  };

  const queuePaint = () => {
    if (!frame) frame = requestAnimationFrame(paint);
  };

  const onPointerMove = (event) => {
    if (reducedMotion() || event.pointerType === 'touch') return;
    const rect = node.getBoundingClientRect();
    pointerX = ((event.clientX - rect.left) / rect.width - 0.5) * 2;
    pointerY = ((event.clientY - rect.top) / rect.height - 0.5) * 2;
    queuePaint();
  };

  const onPointerLeave = () => {
    pointerX = 0;
    pointerY = 0;
    queuePaint();
  };

  const onScroll = () => {
    if (reducedMotion()) return;
    const rect = node.getBoundingClientRect();
    const center = rect.top + rect.height / 2;
    scrollValue = Math.max(-1, Math.min(1, (window.innerHeight / 2 - center) / window.innerHeight));
    queuePaint();
  };

  node.classList.add('parallax-scene');
  node.addEventListener('pointermove', onPointerMove, { passive: true });
  node.addEventListener('pointerleave', onPointerLeave, { passive: true });
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  return {
    destroy() {
      node.removeEventListener('pointermove', onPointerMove);
      node.removeEventListener('pointerleave', onPointerLeave);
      window.removeEventListener('scroll', onScroll);
      if (frame) cancelAnimationFrame(frame);
    }
  };
}

export function reveal(node) {
  node.classList.add('motion-reveal');

  if (reducedMotion() || !('IntersectionObserver' in window)) {
    node.classList.add('is-visible');
    return {};
  }

  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        node.classList.add('is-visible');
        observer.disconnect();
      }
    },
    { threshold: 0.14, rootMargin: '0px 0px -8% 0px' }
  );

  observer.observe(node);
  return { destroy: () => observer.disconnect() };
}

export function interactiveRoot(node) {
  const selector = '.button, [data-interactive]';

  const onPointerMove = (event) => {
    const target = event.target.closest?.(selector);
    if (!target || !node.contains(target)) return;
    const rect = target.getBoundingClientRect();
    target.style.setProperty('--glass-x', `${event.clientX - rect.left}px`);
    target.style.setProperty('--glass-y', `${event.clientY - rect.top}px`);
    target.classList.add('pointer-lit');
  };

  const onPointerOut = (event) => {
    const target = event.target.closest?.(selector);
    if (!target || target.contains(event.relatedTarget)) return;
    target.classList.remove('pointer-lit');
  };

  node.addEventListener('pointermove', onPointerMove, { passive: true });
  node.addEventListener('pointerout', onPointerOut, { passive: true });

  return {
    destroy() {
      node.removeEventListener('pointermove', onPointerMove);
      node.removeEventListener('pointerout', onPointerOut);
    }
  };
}
