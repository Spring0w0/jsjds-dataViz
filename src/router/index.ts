import { createRouter, createWebHistory } from 'vue-router'
import ChinaView from '../views/ChinaView.vue'
import WorldView from '../views/WorldView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/china' },
    { path: '/china', component: ChinaView },
    { path: '/world', component: WorldView }
  ]
})

export default router
