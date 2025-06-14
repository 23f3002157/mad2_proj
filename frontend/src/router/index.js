import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/components/HomeView.vue'
import AdminLogin from '@/components/AdminLogin.vue'
import CustomerHome from '@/components/CustomerHome.vue'
import CustomerLogin from '@/components/CustomerLogin.vue'
import CustomerSignup from '@/components/CustomerSignup.vue'
import ServicerHome from '@/components/ServicerHome.vue'
import ServicerSignup from '@/components/ServicerSignup.vue'
import ServicerLogin from '@/components/ServicerLogin.vue'
import AdminDashboard from '@/components/AdminDashboard.vue'
import AdminCustomerDetails from '@/components/AdminCustomerDetails.vue'
import AdminServicerDetails from '@/components/AdminServicerDetails.vue'
import AdminServicesDetails from '@/components/AdminServicesDetails.vue'
import AdminNewService from '@/components/AdminNewService.vue'
import AdminSearch from '@/components/AdminSearch.vue'
import AdminSummary from '@/components/AdminSummary.vue'
import CustomerDashboard from '@/components/CustomerDashboard.vue'
import CustomerNewService from '@/components/CustomerNewService.vue'
import CustomerSearch from '@/components/CustomerSearch.vue'
import CustomerSummary from '@/components/CustomerSummary.vue'
import ServicerDashboard from '@/components/ServicerDashboard.vue'
import CustomerSearchServicer from '@/components/CustomerSearchServicer.vue'
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
      path: '/admin-dashboard',
      name: 'admin-dashboard',
      component: AdminDashboard,
    },
    {
      path: '/admin-dashboard/search',
      name: 'admin-search',
      component: AdminSearch,
    },
    {
      path: '/admin-dashboard/summary',
      name: 'admin-summary',
      component: AdminSummary,
    },
    {
      path: '/admin-dashboard/customerDetails',
      name: 'admin-customerDetails',
      component: AdminCustomerDetails,
    },
    {
      path: '/admin-dashboard/servicerDetails',
      name: 'admin-servicerDetails',
      component: AdminServicerDetails,
    },
    {
      path: '/admin-dashboard/servicesDetails',
      name: 'admin-servicesDetails',
      component: AdminServicesDetails,
    },
    {
      path: '/admin-dashboard/servicesDetails/newService',
      name: 'admin-servicesDetails-newService',
      component: AdminNewService,
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
      path: '/customerDashboard',
      name: 'customer-dashboard',
      component: CustomerDashboard
    },
    {
      path: '/customerDashboard/new_service',
      name: 'customer-dashboard-newService',
      component: CustomerNewService
    },
    {
      path: '/customerDashboard/search',
      name: 'customer-dashboard-search',
      component: CustomerSearch
    },
    {
      path: '/customerDashboard/search_2',
      name: 'customer-dashboard-search_2',
      component: CustomerSearchServicer
    },
    {
      path: '/customerDashboard/summary',
      name: 'customer-dashboard-summary',
      component: CustomerSummary
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
    {
      path: '/servicerDashboard',
      name: 'servicer-dashboard',
      component: ServicerDashboard
    },
  ],
})

export default router
