<!-- Home.vue -->

<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <router-link to="/" class="navbar-brand"><img src="@/assets/logo.svg" alt="Grocery" height="40" />   Home</router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link to="/admin/products" class="nav-link">Products</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/admin/categories" class="nav-link">Categories</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/admin/requests" class="nav-link">Requests</router-link>
                    </li>
                </ul>
                
                <!-- Updated search form -->
                <form class="d-flex ms-auto mx-2" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
                
                <!-- Updated logout button -->
                <button @click="logout" class="btn btn-outline-danger">Logout</button>
            </div>
        </nav>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
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
/* Add your custom styles here */
</style>
  