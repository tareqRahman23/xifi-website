import '@fontsource/inter/400.css';
import '@fontsource/inter/500.css';
import '@fontsource/inter/600.css';
import '@fontsource/sora/600.css';
import App from './App.svelte';
import './app.css';
import { mount } from 'svelte';

mount(App, {
  target: document.getElementById('app')
});
