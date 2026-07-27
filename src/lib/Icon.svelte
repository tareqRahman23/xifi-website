<script>
  export let name;
  export let size = 20;
  export let stroke = 1.8;
</script>

<svg
  width={size}
  height={size}
  viewBox="0 0 24 24"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  aria-hidden="true"
  stroke="currentColor"
  stroke-width={stroke}
  stroke-linecap="round"
  stroke-linejoin="round"
>
  {#if name === 'arrow'}
    <path d="M5 12h14M14 7l5 5-5 5" />
  {:else if name === 'play'}
    <circle cx="12" cy="12" r="9" />
    <path d="m10 8 6 4-6 4Z" fill="currentColor" stroke="none" />
  {:else if name === 'menu'}
    <path d="M4 7h16M4 12h16M4 17h16" />
  {:else if name === 'close'}
    <path d="m6 6 12 12M18 6 6 18" />
  {:else if name === 'book'}
    <path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11v16H6.5A2.5 2.5 0 0 0 4 21.5v-16Z" />
    <path d="M20 5.5A2.5 2.5 0 0 0 17.5 3H13v16h4.5a2.5 2.5 0 0 1 2.5 2.5v-16Z" />
  {:else if name === 'check'}
    <circle cx="12" cy="12" r="9" />
    <path d="m8 12 2.5 2.5L16 9" />
  {:else if name === 'people'}
    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
    <circle cx="9" cy="7" r="4" />
    <path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75" />
  {:else if name === 'sparkles'}
    <path d="m12 3-1.2 3.4L7.5 7.5l3.3 1.2L12 12l1.2-3.3 3.3-1.2-3.3-1.1L12 3Z" />
    <path d="m18 14-.8 2.2L15 17l2.2.8L18 20l.8-2.2L21 17l-2.2-.8L18 14Z" />
    <path d="m5 12-.6 1.6-1.4.5 1.4.5L5 16l.5-1.4 1.5-.5-1.5-.5L5 12Z" />
  {:else if name === 'mic'}
    <rect x="9" y="3" width="6" height="11" rx="3" />
    <path d="M5 11a7 7 0 0 0 14 0M12 18v3M9 21h6" />
  {:else if name === 'send'}
    <path d="m22 2-7 20-4-9-9-4 20-7Z" />
    <path d="M22 2 11 13" />
  {:else if name === 'chat'}
    <path d="M21 15a4 4 0 0 1-4 4H8l-5 3v-7a4 4 0 0 1-1-2.7V7a4 4 0 0 1 4-4h11a4 4 0 0 1 4 4v8Z" />
    <path d="M7 9h10M7 13h6" />
  {:else if name === 'download'}
    <path d="M12 3v12M7 10l5 5 5-5M5 21h14" />
  {:else if name === 'phone'}
    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.9.33 1.78.62 2.63a2 2 0 0 1-.45 2.11L8 9.73a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.85.29 1.73.5 2.63.62A2 2 0 0 1 22 16.92Z" />
  {:else if name === 'lock'}
    <rect x="4" y="10" width="16" height="11" rx="2" />
    <path d="M8 10V7a4 4 0 0 1 8 0v3" />
  {:else if name === 'shield'}
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z" />
    <path d="m9 12 2 2 4-4" />
  {:else if name === 'wave'}
    <path d="M3 12h2l2-5 3 10 3-14 3 9h5" />
  {:else if name === 'channels'}
    <path d="M7 4h10a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-5l-4 4v-4H7a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3Z" />
    <path d="M8 9h8M8 12h5" />
  {:else if name === 'route'}
    <circle cx="6" cy="5" r="2" /><circle cx="18" cy="19" r="2" />
    <path d="M8 5h3a3 3 0 0 1 3 3v8a3 3 0 0 0 3 3M14 10l-3 3-3-3" />
  {:else if name === 'brain'}
    <path d="M9.5 4A3.5 3.5 0 0 0 6 7.5v.3A3.5 3.5 0 0 0 5 14.5 3.5 3.5 0 0 0 9.5 20H12V4H9.5Z" />
    <path d="M14.5 4A3.5 3.5 0 0 1 18 7.5v.3a3.5 3.5 0 0 1 1 6.7 3.5 3.5 0 0 1-4.5 5.5H12V4h2.5ZM8 9h4M12 15h4" />
  {:else if name === 'headset'}
    <path d="M4 14v-2a8 8 0 0 1 16 0v2" /><path d="M6 13H4a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h2v-7ZM18 13h2a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-2v-7ZM18 20c0 1.1-.9 2-2 2h-3" />
  {:else if name === 'chart'}
    <path d="M4 20V10M10 20V4M16 20v-7M22 20H2" />
  {:else if name === 'layers'}
    <path d="m12 2 9 5-9 5-9-5 9-5Z" /><path d="m3 12 9 5 9-5M3 17l9 5 9-5" />
  {:else}
    <circle cx="12" cy="12" r="9" />
  {/if}
</svg>
