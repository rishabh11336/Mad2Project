<template>
  <div>
    <!-- Button to show/hide product form -->
    <div class="d-flex justify-content-end mb-3 mx-2 my-2">
      <button @click="toggleForm" class="btn btn-primary">
        {{ showForm ? 'Hide Form' : 'Add New Product' }}
      </button>
    </div>

    <!-- Product Form -->
    <div v-if="showForm" class="mb-3">
      <h2>{{ editMode ? 'Edit Product' : 'Add New Product' }}</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="productName">Product Name:</label>
          <input v-model="formData.name" type="text" class="form-control" id="productName" required>
        </div>
        <div class="form-group">
          <label for="productImage">Product Image URL:</label>
          <input v-model="formData.image" type="text" class="form-control" id="productImage" required>
        </div>
        <div class="form-group">
          <label for="productPrice">Price:</label>
          <input v-model="formData.price" type="number" class="form-control" id="productPrice" required>
        </div>
        <div class="form-group">
          <label for="productsi_unit">SI Unit:</label>
          <input v-model="formData.si_unit" type="text" class="form-control" id="productsi_unit" required>
        </div>
        <div class="form-group">
          <label for="productQuantity">Quantity:</label>
          <input v-model="formData.quantity" type="number" class="form-control" id="productQuantity" required>
        </div>
        <div class="form-group">
          <label for="productQuantity">category_id:</label>
          <input v-model="formData.category_id" type="number" class="form-control" id="productcategory_id" required>
        </div>
        <div class="form-group">
          <label for="productExpDate">best_before:</label>
          <input v-model="formData.best_before" type="date" class="form-control" id="productbest_before" required>
        </div>
        <button type="submit" class="btn btn-success">
          {{ editMode ? 'Update Product' : 'Add Product' }}
        </button>
      </form>
    </div>

    <!-- Product Cards -->
    <div class="row row-cols-1 row-cols-md-4 g-4">
      <div class="col mb-4" v-for="product in products" :key="product.id">
        <div class="card h-100">
          <img :src="product.image" class="card-img-top" alt="Product Image">
          <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <p class="card-text">
              <strong>Price:</strong> ₹{{ product.price }}/{{ product.si_unit }}
            </p>
            <p class="card-text text-start">
              <strong>Quantity:</strong> {{ product.quantity }}
            </p>
            <p class="card-text">
              <strong>best_before:</strong>{{ product.best_before }}
            </p>
            <div class="d-grid gap-2">
              <button class="btn btn-info" @click="editProduct(product)">Edit</button>
              <button class="btn btn-danger" @click="deleteProduct(product.id)">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StoreManagerProducts',
  data() {
    return {
      showForm: false,
      editMode: false,
      formData: {
        id: null,
        name: '',
        image: '',
        price: 0,
        quantity: 0,
        si_unit: '',
        best_before: '',
        category_id: '',
      },
      products: [],
    };
  },
  async created() {
    await this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await this.$axios.get('/api/products');
        let result = response.data;

        if (Array.isArray(result)) {
          this.products = result.map(product => ({
            ...product,
            counter: 0,
          }));
        } else {
          console.error('API response is not an array:', result);
        }
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    },
    async submitForm() {
      try {
        if (this.editMode) {
          // Update product
          console.log('Updating product', this.formData);
          await this.$axios.put(`/api/products/${this.formData.id}`, this.formData);
        } else {
          // Add new product
          await this.$axios.post('/api/products', this.formData);
        }

        // Refresh products after update or add
        await this.fetchProducts();

        // Clear the form
        this.resetForm();
      } catch (error) {
        console.error('Error submitting form', error);
      }
    },
    async deleteProduct(productId) {
      if (window.confirm('Are you sure you want to delete this product?')) {
        try {
          await this.$axios.delete(`/api/products/${productId}`);
          // Refresh products after deletion
          await this.fetchProducts();
        } catch (error) {
          console.error('Error deleting product', error);
        }
      }
    },
    editProduct(product) {
      // Set form data for editing
      this.formData.id = product.id;
      this.formData.name = product.name;
      this.formData.image = product.image;
      this.formData.price = product.price;
      this.formData.quantity = product.quantity;
      this.formData.best_before = product.best_before;
      this.formData.si_unit = product.si_unit;
      this.formData.category_id = product.category_id;

      // Set edit mode to true
      this.editMode = true;

      // Show the form
      this.showForm = true;
    },
    toggleForm() {
      // Toggle showForm and reset the form if hidden
      this.showForm = !this.showForm;
      if (!this.showForm) {
        this.resetForm();
      }
    },
    resetForm() {
      // Reset form data and edit mode
      this.formData.id = null;
      this.formData.name = '';
      this.formData.image = '';
      this.formData.price = 0;
      this.formData.quantity = 0;
      this.formData.best_before = '';
      this.formData.si_unit = '';
      this.formData.category_id = '';
      this.editMode = false;
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here */
.card {
  transition: transform 0.2s;
  /* Add a smooth transition effect on hover */
}

.card:hover {
  transform: scale(1.05);
  /* Increase card size on hover */
}

/* Customize labels or add more styles as needed */
.card-text strong {
  color: #333;
}
</style>