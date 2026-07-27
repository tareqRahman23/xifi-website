import gsap from 'gsap';

export function liquidGlass(node, options = {}) {
  if (typeof window === 'undefined') return {};

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const coarse = window.matchMedia('(pointer: coarse)').matches;
  const size = options.size ?? 180;
  const state = { x: 50, y: 50, opacity: 0 };
  let frame = 0;

  node.classList.add('liquid-surface');
  const lens = document.createElement('span');
  lens.className = 'liquid-lens';
  lens.setAttribute('aria-hidden', 'true');
  lens.style.setProperty('--lens-size', `${size}px`);
  node.appendChild(lens);

  const render = () => {
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(() => {
      node.style.setProperty('--glass-x', `${state.x}%`);
      node.style.setProperty('--glass-y', `${state.y}%`);
      node.style.setProperty('--glass-opacity', state.opacity);
    });
  };

  const xTo = gsap.quickTo(state, 'x', { duration: 0.42, ease: 'power3.out', onUpdate: render });
  const yTo = gsap.quickTo(state, 'y', { duration: 0.42, ease: 'power3.out', onUpdate: render });
  const opacityTo = gsap.quickTo(state, 'opacity', { duration: 0.28, ease: 'power2.out', onUpdate: render });

  const move = (event) => {
    const bounds = node.getBoundingClientRect();
    xTo(((event.clientX - bounds.left) / bounds.width) * 100);
    yTo(((event.clientY - bounds.top) / bounds.height) * 100);
    opacityTo(0.44);
  };
  const enter = (event) => move(event);
  const leave = () => { opacityTo(0); xTo(50); yTo(50); };

  if (!reduced && !coarse) {
    node.addEventListener('pointerenter', enter);
    node.addEventListener('pointermove', move);
    node.addEventListener('pointerleave', leave);
  }

  return {
    destroy() {
      cancelAnimationFrame(frame);
      node.removeEventListener('pointerenter', enter);
      node.removeEventListener('pointermove', move);
      node.removeEventListener('pointerleave', leave);
      lens.remove();
    }
  };
}
