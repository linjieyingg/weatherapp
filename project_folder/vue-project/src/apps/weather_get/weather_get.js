import 'vite/modulepreload-polyfill';
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { createApp } from 'vue';
import App from './WeatherGET.vue'

createApp(App).mount("#app")