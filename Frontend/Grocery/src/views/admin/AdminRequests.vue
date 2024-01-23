<template>
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h1 class="mt-2">Requests</h1>
          <hr />
  
  
          <!-- Store Managers Registration Section -->
          <h3 v-if="sm_requests.length != 0">Store Managers Registration Requests: </h3>
          <table class="table table-bordered" v-if="sm_requests.length != 0">
            <thead>
              <tr>
                <th>Id</th>
                <th>Username</th>
                <th>Email</th>
                <th>Role</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="sm_request in sm_requests" :key="sm_request.id">
                <td>{{ sm_request.id }}</td>
                <td>{{ sm_request.username }}</td>
                <td>{{ sm_request.email }}</td>
                <td>{{ sm_request.role.toUpperCase() }}</td>
                <td>
                  <button class="btn btn-danger m-1" @click="deleteRequest_for_SM_registration(sm_request.id)">
                    Delete
                  </button>
                  <button class="btn btn-success m-1" @click="acceptRequest_for_SM_registration(sm_request.id)">
                    Accept
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
          <div v-else>
  
            <h3>No Requests For Store Managers Registration.</h3>
          </div>
          <!-- End of Store Managers Registration Section -->
  
          <!-- Store Managers Category Requests Section -->
          <h3 v-if="sm_category_requests.length != 0">Store Managers Category Requests: </h3>
          <table class="table table-bordered table-striped table-hover" v-if="sm_category_requests.length != 0">
            <thead class="thead-dark">
              <tr>
                <th>Category_Id</th>
                <th>Category_Name</th>
                <th>Operation</th>
                <th>Store_Manager</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="request in sm_category_requests" :key="request.id">
                <td>{{ request.Category_Id }}</td>
                <td>{{ request.Category_Name }}</td>
                <td>{{ request.Operation }}</td>
                <td>{{ request.Store_Manager }}</td>
                <td>
                  <!-- Buttons for accept and delete -->
                  <button class="btn btn-danger m-1"
                    @click="deleteRequest_for_SM_category(request.Category_Id, request.Operation)">
                    Delete
                  </button>
                  <button class="btn btn-success m-1"
                    @click="acceptRequest_for_SM_category(request.Category_Id, request.Operation)">
                    Accept
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
          <div v-else>
            <h3>No Category Change Requests.</h3>
          </div>
          <!-- End of Store Managers Category Requests Section -->
  
          <!-- Product Requests Section -->
          <h3 v-if="product_requests.length != 0">Product Requests: </h3>
          <table class="table table-bordered table-striped table-hover" v-if="product_requests.length != 0">
            <thead class="thead-dark">
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Category ID</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>SI Unit</th>
                <th>Best Before</th>
                <th>Operation</th>
                <th>Created By</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="product in product_requests" :key="product.id">
                <td>{{ product.id }}</td>
                <td>{{ product.name }}</td>
                <td>{{ product.category_id }}</td>
                <td>{{ product.price }}</td>
                <td>{{ product.quantity }}</td>
                <td>{{ product.si_unit }}</td>
                <td>{{ product.best_before }}</td>
                <td>{{ product.created_by }}</td>
                <td>{{ product.operation }}</td>
                <td>
                  <!-- Buttons for accept and delete -->
                  <button class="btn btn-danger m-1" @click="deleteProductRequest(product.id, product.operation)">
                    Delete
                  </button>
                  <button class="btn btn-success m-1" @click="acceptProductRequest(product.id, product.operation)">
                    Accept
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
          <div v-else>
            <h3>No Product Requests.</h3>
          </div>
          <!-- End of Product Requests Section -->
  

        </div>
      </div>
    </div>
  </template>
<script>

export default {
  name: 'AdminRequests',
  data() {
    return {
      sm_requests: [],
      sm_category_requests: [],
      product_requests: []
    };
  },
  methods: {
    // Store Managers Registration Section
    async getRequests_for_SM_registration() {
      try {
        const response = await this.$axios.get('/api/admin/request/storemanager');
        this.sm_requests = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    deleteRequest_for_SM_registration(id) {
      (async () => {
        try {
          await this.$axios.delete(`/api/admin/request/storemanager/${id}`);
          this.getRequests_for_SM_registration();
        } catch (error) {
          console.error(error);
        }
      })();
    },
    async acceptRequest_for_SM_registration(id) {
      try {
        await this.$axios.put(`/api/admin/request/storemanager/${id}`, {
          approved: true
        });
        this.getRequests_for_SM_registration();
      } catch (error) {
        console.error(error);
      }
    },


    // Store Managers Category Requests Section
    async getRequests_for_SM_category() {
      try {
        const res = await this.$axios.get('/api/admin/request/category');
        this.sm_category_requests = Object.keys(res.data).map(key => {
          const item = res.data[key];
          const { approved, createdBy, dateCreated, description, id, image, name } = item;
          let [storeManager, operation, newName, newImage] = createdBy.split(',');

          operation = operation.trim();
          let operationType = operation.charAt(0).toUpperCase() + operation.slice(1);

          let categoryName = operation === 'update' ? `${name} to ${newName}` : name;

          return {
            Category_Id: id,
            Store_Manager: storeManager.trim(),
            Operation: operationType,
            Category_Name: categoryName,
            NewImage: newImage.trim(),
            OldImage: image.trim(),
            OldName: name.trim(),
            Approved: approved,
            Date_Created: dateCreated,
            Description: description
          };
        });
      } catch (error) {
        console.error(error);
      }
    },
    deleteRequest_for_SM_category(id, operation) {
      (async () => {
        try {
          await this.$axios.delete(`/api/admin/request/category/${id}`);
          this.getRequests_for_SM_category();
        } catch (error) {
          console.error(error);
        }
      })();
    },
    acceptRequest_for_SM_category(id, operation) {
      (async () => {
        try {
          await this.$axios.put(`/api/admin/request/category/${id}`, {
            approved: true
          });
          this.getRequests_for_SM_category();
        } catch (error) {
          console.error(error);
        }
      })();
    },

    // Product Requests Section
    async getRequests_for_Products() {
  try {
    const res = await this.$axios.get('/api/admin/request/product');
    this.product_requests = res.data.map(item => {
      let storeManager = item.createdBy; // Assuming createdBy is the store manager
      let operation = 'create'; // Assuming there is no explicit operation in the API output

      let productName = item.name;
      let categoryId = item.category_id;
      let price = item.price;
      let quantity = item.quantity;
      let siUnit = item.si_unit;
      let bestBefore = item.best_before;

      return {
        id: item.id,
        name: productName,
        category_id: categoryId,
        price: price,
        quantity: quantity,
        si_unit: siUnit,
        best_before: bestBefore,
        created_by: storeManager,
        operation: operation,
        newImage: item.image,
        oldImage: item.image, // Assuming no old image is provided in the API output
        oldName: item.name,
        oldCategoryId: item.category_id,
        oldPrice: item.price,
        oldQuantity: item.quantity,
        oldSiUnit: item.si_unit,
        oldBestBefore: item.best_before
      };
    });
  } catch (error) {
    console.error(error);
  }
},
    deleteProductRequest(id, operation) {
      (async () => {
        try {
          await this.$axios.delete(`/api/admin/request/product/${id}`);
          this.getRequests_for_Products();
        } catch (error) {
          console.error(error);
        }
      })();
    },
    acceptProductRequest(id, operation) {
      (async () => {
        try {
          await this.$axios.put(`/api/admin/request/product/${id}`, {
            approved: true
          });
          this.getRequests_for_Products();
        } catch (error) {
          console.error(error);
        }
      })();
    },

  },
  mounted() {
    this.getRequests_for_SM_registration();
    this.getRequests_for_SM_category();
    this.getRequests_for_Products();
  }
};
</script>
