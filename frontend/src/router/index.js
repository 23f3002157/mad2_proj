import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/components/HomeView.vue'
import AdminLogin from '@/components/AdminLogin.vue'
import CustomerHome from '@/components/CustomerHome.vue'
import CustomerLogin from '@/components/CustomerLogin.vue'
import CustomerSignup from '@/components/CustomerSignup.vue'
import ServicerHome from '@/components/ServicerHome.vue'
import ServicerSignup from '@/components/ServicerSignup.vue'
import ServicerLogin from '@/components/ServicerLogin.vue'
// import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homeView',
      component: HomeView,
    },
    {
      path: '/admin-login',
      name: 'admin-login',
      component: AdminLogin,
    },
    {
      path: '/customer-home',
      name: 'customer-home',
      component: CustomerHome,
    },
    {
      path: '/customer-login',
      name: 'customer-login',
      component: CustomerLogin
    },
    {
      path: '/customer-signup',
      name: 'customer-signup',
      component: CustomerSignup
    },
    {
      path: '/servicer-home',
      name: 'servicer-home',
      component: ServicerHome
    },
    {
      path: '/servicer-signup',
      name: 'servicer-signup',
      component: ServicerSignup
    },
    {
      path: '/servicer-login',
      name: 'servicer-login',
      component: ServicerLogin
    },
  ],
})

export default router
