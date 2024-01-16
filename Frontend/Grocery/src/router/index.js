import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'

import AdminMain from '../views/admin/AdminMain.vue'
import AdminCategoryRequest from '../views/admin/Category.vue'
// import AdminDashboard from '../views/admin/Dashboard.vue'
// import AdminProductRequest from '../views/admin/Product.vue'
// import AdminRequests from '../views/admin/AdminRequests.vue'

// import SM_Main from '../views/store_manager/SM_Main.vue'
// import SM_Category from '../views/store_manager/Category.vue'
// import SM_Product from '../views/store_manager/Product.vue'

// import UserDashboard from '../views/user/Dashboard.vue'
// import UserProduct from '../views/user/Product.vue'
// import UserCategory from '../views/user/Category.vue'
// import UserCart from '../views/user/Cart.vue'
// import UserSearch from '../views/user/Search.vue'
// import User from '../views/user/User.vue'

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
    component: AdminMain,
    meta: {
      requireLogin: true,
      role: 'admin'
    },
    children: [
      // {
      //   path: '',
      //   name: 'AdminDashboard',
      //   component: AdminDashboard
      // },
      // {
      //   path: 'dashboard',
      //   name: 'AdminDashboard',
      //   component: AdminDashboard
      // },
      // {
      //   path: 'product',
      //   name: 'AdminProductRequest',
      //   component: AdminProductRequest
      // },
      {
        path: 'category',
        name: 'AdminCategoryRequest',
        component: AdminCategoryRequest
      }
      // {
      //   path: 'requests',
      //   name: 'AdminRequests',
      //   component: AdminRequests
      // }
    ]
  }
  // {
  //   // create store_manager
  //   path: '/store_manager',
  //   name: 'StoreManager',
  //   component: SM_Main,
  //   children: [

  //     {
  //       path: 'product',
  //       name: 'StoreManagerProduct',
  //       component: SM_Product
  //     },
  //     {
  //       path: 'category',
  //       name: 'StoreManagerCategory',
  //       component: SM_Category
  //     }
  //   ]

  // },
  // {
  //   path: '/user',
  //   name: 'User',
  //   component: User,
  //   meta: {
  //     requireLogin: true,
  //     role: 'user'
  //   },
  //   children: [
  //     {
  //       path: '/dashboard',
  //       name: 'UserDashboard',
  //       component: UserDashboard
  //     },
  //     {
  //       path: 'product',
  //       name: 'UserProduct',
  //       component: UserProduct
  //     },
  //     {
  //       path: 'category',
  //       name: 'UserCategory',
  //       component: UserCategory
  //     },
  //     {
  //       path: 'cart',
  //       name: 'UserCart',
  //       component: UserCart
  //     },
  //     {
  //       path: 'search',
  //       name: 'UserSearch',
  //       component: UserSearch
  //     }
  //   ]
  // },
  // {
  //   path: '/logout',
  //   name: 'Logout',
  //   beforeEnter: (to, from, next) => {
  //     localStorage.clear()
  //     next('/login')
  //   }
  // }
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
