import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  base: '/xifi-website/',
  plugins: [svelte()],
  server: {
    host: '127.0.0.1',
    port: 4173
  }
});
