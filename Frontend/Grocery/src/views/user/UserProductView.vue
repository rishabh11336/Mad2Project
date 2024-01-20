<template>
  <div v-if="filteredProducts.length > 0">
    <h1 class="text-center mb-4">Products</h1>
    <div  class="row row-cols-1 row-cols-md-5 g-4">
      <div class="col mb-4" v-for="product in filteredProducts" :key="product.id">
        <div class="card h-100">
          <img :src="`${product.image}`" class="card-img-top" alt="Product Image" width="262.64" height="350.19">
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <div>
                <h5 class="card-title">{{ product.name }}</h5>
                <p class="card-text">
                  <strong>Price:</strong> ₹{{ product.price }}/{{ product.unit }}
                </p>
              </div>
              <div class="text-end">
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
              <button class="btn btn-primary" @click="addtocart(product)">Add to cart</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
      <h1 class="text-center mb-4">No Products</h1>
    </div>
</template>

<script>
export default {
  name: 'ProductsView',
  data() {
    return {
      products: [],
      categoryId: null, // Added categoryId to store the parameter value
    };
  },
  beforeCreate() {
    // IIFE - Immediately Invoked Function Expression
    (async () => {
    try {
      const response = await this.$axios.get('/api/products');
      let result = response.data;

      // Check if the result is an array before mapping
      if (Array.isArray(result)) {
        this.products = result.map(product => ({
          ...product,
          counter: 0,  // Initialize counter property
        }));
      } else {
        console.error('API response is not an array:', result);
      }

      this.categoryId = this.$route.query.categoryId;
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  })();
  },
  computed: {
    filteredProducts() {
      if (this.categoryId) {
        return this.products.filter(product => product.category_id == this.categoryId);
      } else {
        return this.products;
      }
    },
  },
  methods: {
    increaseCounter(product) {
      product.counter++;
      product.quantity--;
    },
    decreaseCounter(product) {
      if (product.counter > 0) {
        product.counter--;
        product.quantity++;
      }
    },
    addtocart(product) {
      if (product.counter > 0) {
        (async () => {
          const response = await this.$axios.post('/api/cart', {
            product_id: product.id,
            product_name: product.name,
            quantity: product.counter,
            price: product.price
          });
          alert("Added to cart")
        })();
        // alert("Added to cart")
        product.counter = 0;
        product.quantity = product.quantity - product.counter;
      }
    },
  },
};
</script>

  
  <style scoped>
    /* Add your custom styles here */
    .card {
      transition: transform 0.2s; /* Add a smooth transition effect on hover */
    }
  
    .card:hover {
      transform: scale(1.05); /* Increase card size on hover */
    }
  
    /* Customize labels or add more styles as needed */
    .card-text strong {
      color: #333;
    }
  </style>