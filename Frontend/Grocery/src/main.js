import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import axiosInstance from './axios_config'

const app = createApp(App)

// Set up Axios as a plugin with the configured instance
app.config.globalProperties.$axios = axiosInstance

app.use(router)

app.mount('#app')
