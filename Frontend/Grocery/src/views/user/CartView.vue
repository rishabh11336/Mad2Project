<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h3>Cart</h3>
        <div class="table-responsive">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>Product</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Subtotal</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(product, index) in products" :key="index">
                <td>
                  <div class="row">
                    <div class="col-md-4">
                      <img :src="product.image" style="width: 100px;" />
                    </div>
                    <div class="col-md-8">
                      <p>{{ product.product_name }}</p>
                    </div>
                  </div>
                </td>
                <td>
                  <div class="row">
                    <div class="col-md-4">
                      <button
                        type="button"
                        class="btn btn-primary btn-sm"
                        @click="decreaseCounter(product)"
                      >
                        -
                      </button>
                      <span class="mx-1">{{ product.quantity }}</span>
                      <button
                        type="button"
                        class="btn btn-primary btn-sm"
                        @click="increaseCounter(product)"
                      >
                        +
                      </button>
                    </div>
                    <div class="col-md-8">
                      <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="removeProduct(product)"
                      >
                        Remove
                      </button>
                    </div>
                  </div>
                </td>
                <td>{{ product.price }}</td>
                <td>{{ product.price * product.quantity }}</td>
              </tr>
            </tbody>
            <tfoot>
              <tr>
                <td colspan="3" class="text-right">Total</td>
                <td>{{ total }}</td>
              </tr>
              <tr>
                <td colspan="4" class="text-right">
                  <div class="d-flex justify-content-end">
                    <button 
                    type="button" 
                    class="btn btn-primary"
                    @click="placeOrder(products)"
                    >
                      Place Order
                    </button>
                  </div>
                </td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductsView',
  data() {
    return {
      products: [],
      total: 0,
    };
  },
  async created() {
    try {
      const response = await this.$axios.get('/api/cart');
      this.products = response.data;
      this.calculateTotal();
    } catch (error) {
      console.error('Error fetching cart data:', error);
    }
  },
  methods: {
    async increaseCounter(product) {
    product.quantity++;
    const response = await this.$axios.post('/api/cart', {
      product_id: product.product_id,
      quantity: product.quantity,
      price: product.price
    });
    this.calculateTotal();
  },
  async decreaseCounter(product) {
    if (product.quantity > 1) {
      product.quantity--;
      const response = await this.$axios.post('/api/cart', {
        product_id: product.product_id,
        quantity: product.quantity,
        price: product.price
      });
      this.calculateTotal();
    }
  },
    async removeProduct(product) {
      const index = this.products.indexOf(product);
      if (index !== -1) {
        this.products.splice(index, 1);
        const response = await this.$axios.delete('/api/cart/'+product.id);
        this.calculateTotal();
      }
    },
    async placeOrder(products) {
      const response = await this.$axios.post('/api/orders', {
        products: products,
        total: this.total
      });
      this.$router.push('/orders');
    },
    calculateTotal() {
      this.total = this.products.reduce((acc, product) => acc + product.price * product.quantity, 0);
    },
  },
};
</script>
