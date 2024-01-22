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
  import axios from 'axios'
  
  export default {
    name: 'AdminRequests',
    data() {
      return {
        sm_requests: [],
        sm_category_requests: [],
        product_requests: []
      }
    },
    methods: {
  
      // Store Managers Registration Section
      getRequests_for_SM_registration() {
        axios.get('http://localhost:5000/requests').then((response) => {
          this.sm_requests = response.data['sm_requests']
        })
      },
      deleteRequest_for_SM_registration(id) {
        //make a delete request to /requests/:id asynchronusly
        ; (async () => {
          let url = `http://localhost:5000/requests/` + id
          await axios.delete(url, {
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              Authorization: 'Bearer ' + localStorage.getItem('access_token')
            }
          })
          this.getRequests_for_SM_registration()
        })()
      },
      acceptRequest_for_SM_registration(id) {
        axios
          .post(`http://localhost:5000/requests/${id}`, {
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              Authorization: 'Bearer ' + localStorage.getItem('access_token')
            }
          })
          .then((response) => {
            this.getRequests_for_SM_registration()
          })
      },
  
  
  
      // Store Managers Category Requests Section
      async getRequests_for_SM_category() {
        try {
          const res = await axios.get('http://localhost:5000/category/pending', {
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              Authorization: 'Bearer ' + localStorage.getItem('access_token')
            }
          });
  
          this.sm_category_requests = Object.keys(res.data).map(key => {
            const item = res.data[key];
            let [storeManager, operation, newName, newImage] = item.created_by.split(',');
  
            operation = operation.trim();
            let operationType = operation.charAt(0).toUpperCase() + operation.slice(1); // Capitalize first letter
            let categoryName = operation == 'update' ? `${item.name} to ${newName}` : item.name;
  
  
            return {
              Category_Id: item.id,
              Store_Manager: storeManager,
              Operation: operationType,
              Category_Name: categoryName,
              NewImage: newImage,
              OldImage: item.image,
              OldName: item.name
            };
          });
        } catch (err) {
          console.error(err);
        }
      },
      deleteRequest_for_SM_category(id, operation) {
  
        operation = operation.toLowerCase();
        let cat = this.sm_category_requests.findIndex(item => item.Category_Id == id);
        if (operation == 'update' || operation == 'delete') {
          (async () => {
            try {
              await axios.put(`http://localhost:5000/category/${id}`, {
                name: this.sm_category_requests[cat].OldName,
                image: this.sm_category_requests[cat].OldImage,
                created_by: 'admin'
  
              }, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_SM_category()
            } catch (err) {
              console.log(err)
            }
          })();
        }
        if (operation == 'create') {
          (async () => {
            try {
              await axios.delete(`http://localhost:5000/category/${id}`, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_SM_category()
            } catch (err) {
              console.log(err)
            }
          })()
        }
      },
      acceptRequest_for_SM_category(id, operation) {
        //make operation to lower case
        operation = operation.toLowerCase();
        // if operation is update and delete, then update created_by field by admin
        if (operation == 'update') {
          let cat = this.sm_category_requests.findIndex(item => item.Category_Id == id);
          (async () => {
            try {
              await axios.put(`http://localhost:5000/category/${id}`, {
                name: this.sm_category_requests[cat].NewName,
                image: this.sm_category_requests[cat].NewImage,
                categoryId: this.sm_category_requests[cat].Category_Id,
                price: this.sm_category_requests[cat].NewPrice,
                quantity: this.sm_category_requests[cat].NewQuantity,
                si_unit: this.sm_category_requests[cat].NewSiUnit,
                best_before: this.sm_category_requests[cat].NewBestBefore,
  
                created_by: 'admin'
              }, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_SM_category()
            } catch (err) {
              console.log(err)
            }
          })();
        }
        if (operation == 'create') {
          (async () => {
            try {
              await axios.put(`http://localhost:5000/category/${id}`, {
  
                created_by: 'admin',
                is_approved: true
  
              }, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_SM_category()
            } catch (err) {
              console.log(err)
            }
          })();
        }
        if (operation == 'delete') {
          (async () => {
            try {
              await axios.delete(`http://localhost:5000/category/${id}`, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_SM_category()
            } catch (err) {
              console.log(err)
            }
          })();
        }
  
      },
  
  
      // Product Requests Section
      async getRequests_for_Products() {
        try {
          const res = await axios.get('http://localhost:5000/product/pending', {
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              Authorization: 'Bearer ' + localStorage.getItem('access_token')
            }
          })
          this.product_requests = Object.keys(res.data).map(key => {
            const item = res.data[key];
            let [storeManager, operation, newName, newImage, newCategoryId, newPrice, newQuantity, newSiUnit, newBestBefore] = item.created_by.split(',');
  
            operation = operation.trim();
            let operationType = operation.charAt(0).toUpperCase() + operation.slice(1); // Capitalize first letter
            let productName = (operation == 'update' && item.name !== newName) ? `${item.name} to ${newName}` : item.name;
            let categoryId = (operation == 'update' && item.category_id !== newCategoryId) ? `${item.category_id} to ${newCategoryId}` : item.category_id;
            let price = (operation == 'update' && item.price !== newPrice) ? `${item.price} to ${newPrice}` : item.price;
            let quantity = (operation == 'update' && item.quantity !== newQuantity) ? `${item.quantity} to ${newQuantity}` : item.quantity;
            let siUnit = (operation == 'update' && item.si_unit !== newSiUnit) ? `${item.si_unit} to ${newSiUnit}` : item.si_unit;
            let bestBefore = (operation == 'update' && item.best_before !== newBestBefore) ? `${item.best_before} to ${newBestBefore}` : item.best_before;
  
            return {
              id: item.id,
              name: productName,
              category_id: categoryId,
              price: price,
              quantity: quantity,
              si_unit: siUnit,
              best_before: bestBefore,
              created_by: storeManager,
              operation: operationType,
              newImage: newImage,
              oldImage: item.image,
              oldName: item.name,
              oldCategoryId: item.category_id,
              oldPrice: item.price,
              oldQuantity: item.quantity,
              oldSiUnit: item.si_unit,
              oldBestBefore: item.best_before
            };
          });
  
        }
        catch (err) {
          console.error(err);
        }
      },
      deleteProductRequest(id, operation) {
        // Delete request logic
        operation = operation.toLowerCase();
        let product = this.product_requests.findIndex(item => item.id == id);
        if (operation == 'update' || operation == 'delete') {
          (async () => {
            try {
              await axios.put(`http://localhost:5000/product/${id}`, {
                created_by: 'admin'
              }, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_Products()
            } catch (err) {
              console.log(err)
            }
          })();
        }
        if (operation == 'create') {
          (async () => {
            try {
              await axios.delete(`http://localhost:5000/product/${id}`, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_Products()
            } catch (err) {
              console.log(err)
            }
          })();
        }
      },
      acceptProductRequest(id, operation) {
        // Accept request logic
        operation = operation.toLowerCase();
  
        if (operation == 'update') {
          let product = this.product_requests.findIndex(item => item.id == id);
          (async () => {
            try {
              await axios.put(`http://localhost:5000/product/${id}`, {
                name: this.product_requests[product].newName,
                category_id: this.product_requests[product].newCategoryId,
                price: this.product_requests[product].newPrice,
                quantity: this.product_requests[product].newQuantity,
                si_unit: this.product_requests[product].newSiUnit,
                best_before: this.product_requests[product].newBestBefore,
                image: this.product_requests[product].newImage,
                created_by: 'admin'
              }, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_Products()
            } catch (err) {
              console.log(err)
            }
          })();
        }
  
        if (operation == 'create') {
          let product = this.product_requests.findIndex(item => item.id == id);
          (async () => {
            try {
              await axios.put(`http://localhost:5000/product/${id}`, {
                created_by: 'admin',
                is_approved: true
              }, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_Products()
            } catch (err) {
              console.log(err)
            }
          })();
        }
  
        if (operation == 'delete') {
          (async () => {
            try {
              await axios.delete(`http://localhost:5000/product/${id}`, {
                headers: {
                  'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': '*',
                  Authorization: 'Bearer ' + localStorage.getItem('access_token')
                }
              })
              this.getRequests_for_Products()
            } catch (err) {
              console.log(err)
            }
          })();
        }
  
      }
  
    },
  
    mounted() {
      this.getRequests_for_SM_registration()
      this.getRequests_for_SM_category()
      this.getRequests_for_Products()
    }
  }
  </script>