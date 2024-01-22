<template>
<div>
      <!-- Button to show/hide category form -->
      <div class="d-flex justify-content-end mb-3 my-2 mx-2">
        <button @click="toggleForm" class="btn btn-primary">
          {{ showForm ? 'Hide Form' : 'Add New Product' }}
        </button>
      </div>

      <!-- Category Form -->
      <div v-if="showForm" class="mb-3">
        <h2>{{ editMode ? 'Edit Category' : 'Add New Category' }}</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="categoryName">Category Name:</label>
            <input v-model="formData.name" type="text" class="form-control" id="categoryName" required>
          </div>
          <div class="form-group">
            <label for="categoryDescription">Category Description:</label>
            <textarea v-model="formData.description" class="form-control" id="categoryDescription" rows="3" required></textarea>
          </div>
          <div class="form-group">
            <label for="categoryImage">Category Image URL:</label>
            <input v-model="formData.image" type="text" class="form-control" id="categoryImage" required>
          </div>
          <button type="submit" class="btn btn-success">
            {{ editMode ? 'Update Category' : 'Add Category' }}
          </button>
        </form>
      </div>

      <!-- Category Cards -->
      <div class="row row-cols-1 row-cols-md-4 g-4">
        <div class="col mb-4" v-for="category in categories" :key="category.id">
          <div class="card h-100">
            <img :src="category.image" class="card-img-top" alt="category Image">
            <div class="card-body">
              <h5 class="card-title">{{ category.name }}</h5>

              <!-- Buttons for update and delete operations -->
              <button @click="editCategory(category)" class="btn btn-info mr-2 mx-2">
                Edit
              </button>
              <button @click="deleteCategory(category.id)" class="btn btn-danger">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>

  <script>
  export default {
    name: 'AdminCategoryView',
    data() {
      return {
        showForm: false,
        editMode: false,
        formData: {
          id: null,
          name: '',
          description: '',
          image: '',
        },
        categories: [],
      };
    },
    async created() {
      await this.fetchCategories();
    },
    methods: {
      async fetchCategories() {
        try {
          const response = await this.$axios.get('/api/categories');
          this.categories = response.data;
        } catch (error) {
          console.error('Error fetching categories', error);
        }
      },
      async submitForm() {
        try {
          if (this.editMode) {
            // Update category
            console.log('Updating category', this.formData);
            await this.$axios.put(`/api/categories/${this.formData.id}`, this.formData);
          } else {
            // Add new category
            await this.$axios.post('/api/categories', this.formData);
          }
  
          // Refresh categories after update or add
          await this.fetchCategories();
  
          // Clear the form
          this.resetForm();
        } catch (error) {
          console.error('Error submitting form', error);
        }
      },
      async deleteCategory(categoryId) {
        if (window.confirm('Are you sure you want to delete this category?')) {
          try {
            await this.$axios.delete(`/api/categories/${categoryId}`);
            // Refresh categories after deletion
            await this.fetchCategories();
          } catch (error) {
            console.error('Error deleting category', error);
          }
        }
      },
      editCategory(category) {
        // Set form data for editing
        this.formData.id = category.id;
        this.formData.name = category.name;
        this.formData.description = category.description;
        this.formData.image = category.image;
  
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
        this.formData.description = '';
        this.formData.image = '';
        this.editMode = false;
      },
    },
  };
  </script>
