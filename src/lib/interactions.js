const reduced = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export function reveal(node) {
  node.classList.add('motion-reveal');
  if (reduced() || !('IntersectionObserver' in window)) {
    node.classList.add('is-visible');
    return {};
  }
  const observer = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) { node.classList.add('is-visible'); observer.disconnect(); }
  }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
  observer.observe(node);
  return { destroy: () => observer.disconnect() };
}

export function parallax(node, options = {}) {
  if (reduced() || window.matchMedia('(pointer: coarse)').matches) return {};
  const strength = options.strength ?? 0.3;
  const scrollStrength = options.scrollStrength ?? 0.25;
  let frame = 0;
  node.classList.add('parallax-scene');
  const render = (x = 0, y = 0) => {
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(() => {
      node.style.setProperty('--parallax-x', `${x * strength}`);
      node.style.setProperty('--parallax-y', `${y * strength}`);
      const bounds = node.getBoundingClientRect();
      const scroll = Math.max(-1, Math.min(1, (innerHeight / 2 - (bounds.top + bounds.height / 2)) / innerHeight));
      node.style.setProperty('--parallax-scroll', `${scroll * scrollStrength}`);
    });
  };
  const move = (event) => {
    const bounds = node.getBoundingClientRect();
    render(((event.clientX - bounds.left) / bounds.width - .5) * 2, ((event.clientY - bounds.top) / bounds.height - .5) * 2);
  };
  const leave = () => render(0, 0);
  const scroll = () => render(0, 0);
  node.addEventListener('pointermove', move);
  node.addEventListener('pointerleave', leave);
  window.addEventListener('scroll', scroll, { passive: true });
  return { destroy() { cancelAnimationFrame(frame); node.removeEventListener('pointermove', move); node.removeEventListener('pointerleave', leave); window.removeEventListener('scroll', scroll); } };
}
