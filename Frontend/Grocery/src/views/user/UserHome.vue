<!-- Home.vue -->

<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <router-link to="/user" class="navbar-brand"><img src="@/assets/logo.svg" alt="Grocery" height="40" /> Home</router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link to="/user/products" class="nav-link">Products</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/user/category" class="nav-link">Categories</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/user/cart" class="nav-link">Cart</router-link>
                    </li>
                </ul>
                
                <form class="d-flex ms-auto mx-2" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
               
                <button @click="logout" class="btn btn-outline-danger">Logout</button>
            </div>
        </nav>
        <router-view></router-view>
        <div v-if="$route.path === '/user'">
        <div>
            <h3 class="text-center mb-4"><u>Recent Products</u></h3>
            <div class="row row-cols-1 row-cols-md-5 g-4">
            <div class="col mb-4" v-for="product in products" :key="product.id">
                <div class="card h-100">
                <img :src="`${product.image}`" class="card-img-top" alt="Product Image" width="262.64" height="350.19">
                <div class="card-body">
                    <div class="d-flex justify-content-between">
                    <div>
                        <h5 class="card-title">{{ product.name }}</h5>
                        <p class="card-text">
                        <strong>Price:</strong> ₹{{ product.price }}/{{ product.si_unit }}
                        </p>
                    </div>
                    <div class="text-end">
                        <p class="card-text">
                        <strong>Brand:</strong> {{ product.brand }}
                        </p>
                        <p class="card-text text-start">
                        <strong>Quantity:</strong> {{ product.quantity }}
                        </p>
                    </div>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                    <button class="btn btn-outline-secondary btn-sm me-2" @click="decreaseCounter(product)">-</button>
                    <span>{{ product.counter }}</span>
                    <button class="btn btn-outline-secondary btn-sm ms-2" @click="increaseCounter(product)">+</button>
                    </div>
                    <p class="card-text">
                    <strong>Exp:</strong> {{ product.best_before }}
                    </p>
                    <div class="d-grid gap-2">
                    <button class="btn btn-primary" type="button">Add to cart</button>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>

        <hr />

        <div>
            <h3 class="text-center mb-4"><u>Categories</u></h3>
            <div class="row row-cols-1 row-cols-md-5 g-4">
                <div class="col mb-4" v-for="category in categories" :key="category.id">
                <div class="card h-100">
                    <RouterLink
                    class="nav-link active"
                    :to="{ name: 'UserProductView', query: { categoryId: category.id } }">
                        <img :src="`${category.image}`" class="card-img-top" alt="category Image">
                    </RouterLink>
                    <div class="card-body">
                    <h5 class="card-title">{{ category.name }}</h5>
                    </div>
                </div>
                </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>

  export default {
    name: 'HomeView',
    data() {
      return {
        products: [],
        categories: []

      }
    },
    beforeCreate() {
      // IIFE - Immediately Invoked Function Expression
      (async () => {
        const Productresponse = await this.$axios.get('/api/products')
        
        let productresult = Productresponse.data
        let required_keys_product = Object.keys(productresult).splice(-10)
        let required_values_product = Object.values(productresult).splice(-10)
        let required_products = {}
        for (let i = 0; i < required_keys_product.length; i++) {
          required_products[required_keys_product[i]] = required_values_product[i]
          required_products[required_keys_product[i]]['counter'] = 0
        }
        this.products = required_products

      })();
      (async () => {
        const Categoryresponse = await this.$axios.get('/api/categories')

        let categoryresult = Categoryresponse.data
        let required_keys_category = Object.keys(categoryresult).splice(-10)
        let required_values_category = Object.values(categoryresult).splice(-10)
        let required_category = {}
        for (let i = 0; i < required_keys_category.length; i++) {
          required_category[required_keys_category[i]] = required_values_category[i]
        }
        this.categories = required_category

      })();
    },
    methods: {
        logout() {
            // Add your logout logic here
            localStorage.clear();
            this.$router.push('/login');
            console.log('Logged out');
        },
        increaseCounter(product) {
        product.counter++
        product.quantity--
      },
      decreaseCounter(product) {
        if (product.counter > 0) {
          product.counter--
          product.quantity++
        }
      }
    }
};
</script>
  
<style scoped>
/* Add your custom styles here */
</style>