import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const backendPath = '../manager'

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
        vue_student_edit: "./src/apps/weather_edit/weather_edit.js"
      },
    },
  }
})