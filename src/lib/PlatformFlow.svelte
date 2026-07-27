<script>
  import Icon from './Icon.svelte';

  const layers = [
    {
      title: 'Every channel',
      subtitle: 'One session',
      icon: 'channels',
      items: ['Voice', 'Web chat', 'Email', 'Messaging']
    },
    {
      title: 'Intelligent orchestration',
      subtitle: 'One control plane',
      icon: 'route',
      items: ['Intent and identity', 'Routing and queues', 'Policy checkpoints', 'Session memory']
    },
    {
      title: 'Knowledgeable AI',
      subtitle: 'Controlled resolution',
      icon: 'brain',
      items: ['Approved knowledge', 'Reasoning and context', 'Permissioned actions', 'Source provenance']
    },
    {
      title: 'Human operations',
      subtitle: 'Context intact',
      icon: 'headset',
      items: ['Specialist handoff', 'Agent workspace', 'Quality evidence', 'Operational insight']
    }
  ];
</script>

<div class="platform-flow">
  {#each layers as layer, index}
    <article class="flow-layer">
      <header>
        <span class="flow-icon"><Icon name={layer.icon} size={22} /></span>
        <span class="flow-index">0{index + 1}</span>
      </header>
      <div class="flow-title"><h3>{layer.title}</h3><p>{layer.subtitle}</p></div>
      <ul>
        {#each layer.items as item}<li><Icon name="check" size={14} /> {item}</li>{/each}
      </ul>
    </article>
    {#if index < layers.length - 1}
      <span class="flow-connector" aria-hidden="true"><Icon name="arrow" size={19} /></span>
    {/if}
  {/each}
</div>
