<!-- Home.vue -->

<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <router-link to="/admin" class="navbar-brand"><img src="@/assets/logo.svg" alt="Grocery" height="40" />   Home</router-link>
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
        <div v-if="$route.path === '/admin'">
            <div class="container">
                <canvas id="myChart"></canvas>
            </div>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
    name: 'AdminHome',
    mounted() {
        const ctx = document.getElementById('myChart');

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                datasets: [{
                    label: '# of Votes',
                    data: [12, 19, 3, 5, 2, 3],
                    borderWidth: 1,
                }],
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
            },
        });
    },
    methods: {
        logout() {
            // Add your logout logic here
            localStorage.clear();
            this.$router.push('/login');
            console.log('Logged out');
        },
    },
};
</script>

  
<style scoped>
/* Add your custom styles here */
</style>
  