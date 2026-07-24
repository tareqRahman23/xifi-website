<script>
  import Icon from './Icon.svelte';
  let active = 0;
  const solutions = [
    { title: 'Always-on frontline', body: 'Handle routine inquiries instantly with accurate, brand-aligned responses.', icon: 'sparkles' },
    { title: 'Secure by design', body: 'Identity, consent, policy, and tenant boundaries travel with every conversation.', icon: 'lock' },
    { title: 'Built to fit your stack', body: 'Connect knowledge, CRM, ticketing, voice, and existing operational workflows.', icon: 'shield' }
  ];
</script>

<div class="solutions-rail media-scale">
  {#each solutions as solution, index}
    <button class:active={active === index} on:mouseenter={() => active = index} on:focus={() => active = index} on:click={() => active = index} aria-expanded={active === index}>
      <span class="solution-number">0{index + 1}</span>
      <span class="solution-icon"><Icon name={solution.icon} size={24} /></span>
      <span class="solution-content"><strong>{solution.title}</strong><p>{solution.body}</p><em>Explore <Icon name="arrow" size={15} /></em></span>
    </button>
  {/each}
</div>
