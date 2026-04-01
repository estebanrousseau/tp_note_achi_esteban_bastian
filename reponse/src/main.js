import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')



// import { createApp } from 'vue'
// import './style.css'
// import { createMemoryHistory, createRouter } from 'vue-router'
// import AppJeu from './App.vue'
// // import AppEdit from './AboutView.vue'

// const routes = [
//     { path: '/', component: AppJeu },
//     // { path: '/edit', component: AppEdit },
// ]

// const router = createRouter({
//     history: createMemoryHistory(),
//     routes,
// })

// export default router