import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/LoginView.vue'

import AdminHome from '../views/admin/AdminHome.vue'
import AdminCategoryView from '../views/admin/AdminCategoryView.vue'
import AdminProductView from '../views/admin/AdminProductView.vue'
import AdminRequests from '../views/admin/AdminRequests.vue'
import AdminGraphView from '../views/admin/AdminGraphView.vue'


import StoreManagerHome from '../views/store_manager/StoreManagerHome.vue'
import StoreManagerProduct from '../views/store_manager/StoreManagerProduct.vue'
import StoreManagerCategory from '../views/store_manager/StoreManagerCategory.vue'


import UserHome from '../views/user/UserHome.vue'
import UserProductView from '../views/user/UserProductView.vue'
import UserCategoryView from '../views/user/UserCategoryView.vue'
import CartView from '../views/user/CartView.vue'

const routes = [
  {
    path: '/',
    alias: '/login',
    name: 'Login',
    component: Login,
    meta: {
      requireLogin: false
    }
  },
  {
    path: '/admin',
    name: 'Admin',
    component: AdminHome,
    meta: {
      requireLogin: true,
      role: 'admin'
    },
    children: [
      {
        path: 'graph',
        name: 'AdminGraphView',
        component: AdminGraphView
      },
      {
        path: 'products',
        name: 'AdminProductView',
        component: AdminProductView
      },
      {
        path: 'categories',
        name: 'AdminCategoryView',
        component: AdminCategoryView
      },
      {
        path: 'requests',
        name: 'AdminRequests',
        component: AdminRequests
      }
    ]
  },

  {
    // create store_manager
    path: '/store_manager',
    name: 'StoreManagerHome',
    component: StoreManagerHome,
    meta: {
      requireLogin: true,
      role: 'storemanager'
    },
    children: [

      {
        path: 'product',
        name: 'StoreManagerProduct',
        component: StoreManagerProduct
      },
      {
        path: 'category',
        name: 'StoreManagerCategory',
        component: StoreManagerCategory
      }
    ]

  },

  {
    path: '/user',
    name: 'UserHome',
    component: UserHome,
    meta: {
      requireLogin: true,
      role: 'user'
    },
    children: [

      {
        path: 'products',
        name: 'UserProductView',
        component: UserProductView
      },
      {
        path: 'category',
        name: 'UserCategoryView',
        component: UserCategoryView
      },
      {
        path: 'cart',
        name: 'CartView',
        component: CartView
      }
    ]
  },
  {
    path: '/logout',
    name: 'Logout',
    beforeEnter: (to, from, next) => {
      localStorage.clear()
      next('/login')
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  // Check if the route requires authentication
  if (to.meta.requireLogin) {
    const token = localStorage.getItem('access_token')
    const role = localStorage.getItem('role')

    if (to.meta.role === role) {
      next()
    } else {
      localStorage.clear()
      next('/login')
    }
  } else {
    next()
  }
})

export default router