<template>
    <div>
      <h1 class="text-center mb-4">Categories</h1>
      <div class="row row-cols-1 row-cols-md-5 g-4">
        <div class="col mb-4" v-for="category in categories" :key="category.id">
          <div class="card h-100">
            <RouterLink
            class="nav-link active"
            :to="{ name: 'UserProductView', query: { categoryId: category.id } }"
          >
              <img :src="`${category.image}`" class="card-img-top" alt="category Image">
            </RouterLink>
            <div class="card-body">
              <h5 class="card-title">{{ category.name }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
  
  <style scoped>
/* Add your custom styles here */
    .card {
      transition: transform 0.2s; /* Add a smooth transition effect on hover */
      box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    }
  
    .card:hover {
      transform: scale(1.05); /* Increase card size on hover */
    }
  
    /* Customize labels or add more styles as needed */
    .card-text strong {
      color: #333;
    }
  </style>
  
  
  
  <script>
    export default {
      name: 'UserCategoryView',
      data() {
        return {
          categories: []
        }
      },
      beforeCreate() {
        // iife - immediately invoked function expression
        (async () => {
          const response = await this.$axios.get('/api/categories')
          this.categories = response.data
        })()
      }
    }
  </script>