<template>
    <div class="container my-4">
      <div class="text-bg-info p-2" style="font-family: Algerian;">
        <h1><center><u>SHOPPING CART</u></center></h1>
      </div>
      <div class="table-responsive">
        <table class="table table-bordered table-hover">
          <thead>
            <tr>
              <th scope="col">Product</th>
              <th scope="col">Quantity</th>
              <th scope="col">Price</th>
              <th scope="col">Category</th>
              <th scope="col">Image</th>
              <th scope="col">Brand</th>
              <th scope="col">Total Price</th>
              <th scope="col">Remove from Cart</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in product_list" :key="item[7]">
              <td>{{ item[0] }}</td>
              <td>{{ item[1] }}</td>
              <td>{{ item[2] }}</td>
              <td>{{ item[3] }}</td>
              <td><img :src="item[4]" height="100px"></td>
              <td>{{ item[5] }}</td>
              <td>{{ item[6] }}</td>
              <td>
                <center>
                  <button @click="removeFromCart(item[7])" class="btn btn-danger btn-sm">Remove</button>
                </center>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="text-center">
        <form @submit.prevent="applyPromocode">
          <div class="container w-25 p-3 d-flex flex-row">
            <input v-model="promocode" class="form-control me-2" type="text" placeholder="PROMOCODE">
            <button type="submit" class="btn btn-dark">Apply</button>
          </div>
        </form>
        <div v-if="messages.length > 0">
          <b v-for="message in messages" :key="message">{{ message }}</b>
        </div>
        <h4>Total: ₹{{ cartTotal }}</h4>
        <button @click="createOrder" class="btn btn-success btn-lg">Buy Now</button>
      </div>
    </div>
  </template>

  <style scoped>
    
  </style>
  
  <script>
 
  </script>