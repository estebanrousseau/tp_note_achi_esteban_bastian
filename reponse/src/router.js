import { createWebHistory, createRouter } from 'vue-router'
import AppJeu from './Jeu.vue'
import AppEdit from './Edit.vue'

const routes = [
    { path: '/', component: AppJeu },
    { path: '/edit', component: AppEdit },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router