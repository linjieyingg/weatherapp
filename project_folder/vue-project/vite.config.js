
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const backendPath = '../final'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/static/vite/',
  server: {
    watch: {
      irgnored: [],
    },
  },
  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: backendPath + '/core/static/vite/',
    rollupOptions: {
      input: {
        vue_weather_get: "./src/apps/weather_get/weather_get.js"
      },
    },
  }
})