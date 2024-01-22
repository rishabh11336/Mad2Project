<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">
                        {{ isLoginForm ? 'Login' : 'Register' }}
                    </div>
                    <div class="card-body">
                        <div class="mb-3 form-check form-switch">
                            <input class="form-check-input" type="checkbox" id="toggleForm" v-model="isLoginForm" />
                            <label class="form-check-label" for="toggleForm">
                                {{ isLoginForm ? 'Switch to Register' : 'Switch to Login' }}
                            </label>
                        </div>
                        <form @submit.prevent="isLoginForm ? login : register">
                            <div class="mb-3">
                                <label v-if="!isLoginForm" for="email" class="form-label">Email address</label>
                                <input v-if="!isLoginForm" v-model="email" type="email" class="form-control" id="email"
                                    required>
                            </div>
                            <div class="mb-3">
                                <label for="username" class="form-label">Username</label>
                                <input v-model="username" type="text" class="form-control" id="username" required>
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input v-model="password" type="password" class="form-control" id="password" required>
                            </div>
                            <div class="mb-3" v-if="!isLoginForm">
                                <label for="role" class="form-label">Role</label>
                                <select v-model="role" class="form-select" id="role" required>
                                    <option value="user">User</option>
                                    <option value="storemanager">Store Manager</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-primary" @click="login" v-if="isLoginForm">
                                Login
                            </button>
                            <button type="submit" class="btn btn-primary" @click="register" v-else>
                                Register
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'LoginView',
    data() {
        return {
            isLoginForm: true,
            email: '',
            username: '',
            password: '',
            role: 'user' // Default role is set to 'user'
        };
    },
    methods: {
        async login() {
            try {
                const response = await this.$axios.post('/api/auth/login', {
                    username: this.username,
                    password: this.password
                });
                console.log('Login successful:', response.data);
                this.saveUserInfo(response.data);
                this.redirectBasedOnRole(response.data.role);
            } catch (error) {
                alert(error.response.data.message)
                console.error('Login failed:', error);
            }
        },
        async register() {
            try {
                const response = await this.$axios.post('/api/auth/register', {
                    email: this.email,
                    username: this.username,
                    password: this.password,
                    role: this.role
                });
                alert(response.data.message);
                this.isLoginForm = true;
            } catch (error) {
                console.error('Registration failed:', error);
                alert(error.response.data.message);
            }
        },
        saveUserInfo(data) {
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('email', data.email);
            localStorage.setItem('username', data.username);
            localStorage.setItem('role', data.role);
            localStorage.setItem('id', data.id);
        },
        redirectBasedOnRole(role) {
            if (role === 'admin') {
                this.$router.push('/admin');
            } else if (role === 'user') {
                this.$router.push('/user');
            } else if (role === 'storemanager') {
                this.$router.push('/store_manager');
            }
        }
    }
};
</script>
<style scoped>
/* Add your custom styles here if needed */
</style>