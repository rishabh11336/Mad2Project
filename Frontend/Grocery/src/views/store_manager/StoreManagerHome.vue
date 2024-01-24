<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <router-link to="/store_manager" class="navbar-brand"><img src="@/assets/logo.svg" alt="Grocery" height="40" /> Home</router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link to="/store_manager/product" class="nav-link">Products</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/store_manager/category" class="nav-link">Categories</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/store_manager/request" class="nav-link">Requests</router-link>
                    </li>
                </ul>
                
            
               
                <button @click="logout" class="d-flex ms-auto mx-2 btn btn-outline-danger">Logout</button>
            </div>
        </nav>
        <router-view></router-view>
        <div v-if="$route.path === '/store_manager'">
            <h1>StoreManagerHome</h1>
        </div>
    </div>
</template>

<script>
export default {
    name: "StoreManagerHome",
    data(){

    },
    methods: {
        logout() {
            // Add your logout logic here
            localStorage.clear();
            this.$router.push('/login');
            console.log('Logged out');
        }
    }
};
</script>

<style scoped>
.store-manager-home {
    text-align: center;
}
</style>