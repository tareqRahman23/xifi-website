import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import { resolve } from 'node:path';

export default defineConfig({
  base: '/xifi-website/',
  plugins: [svelte()],
  build: {
    rollupOptions: {
      input: {
        main: resolve(process.cwd(), 'index.html'),
        branding: resolve(process.cwd(), 'branding-guidelines/index.html')
      }
    }
  },
  server: {
    host: '127.0.0.1',
    port: 4173
  }
});
