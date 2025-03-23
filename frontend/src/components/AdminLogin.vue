<template>
    <div class="container d-flex justify-content-center align-items-center vh-100">
      <div class="col-md-5">
        <div class="card shadow-lg p-4">
          <h2 class="text-center text-primary mb-4">Admin Login</h2>
          <form @submit.prevent="loginAdmin">
            <div class="mb-3">
              <label for="email" class="form-label">Email</label>
              <input type="email" class="form-control" id="email" v-model="email" placeholder="Enter email" required>
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" class="form-control" id="password" v-model="password" placeholder="Enter password" required>
            </div>
            <div v-if="errorMessage" class="alert alert-danger text-center py-2">
              {{ errorMessage }}
            </div>
            <button type="submit" class="btn btn-primary w-100">Login</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        password: '',
        errorMessage: null
      };
    },
    methods: {
      async loginAdmin() {
        this.errorMessage = null;
        const payload = {
          email: this.email,
          password: this.password
        };
        try {
          const response = await fetch('http://127.0.0.1:5000/adminLogin', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
          });
          const result = await response.json();
          if (result.login !== 1) {
            this.errorMessage = result.message || "Something went wrong";
          } else {
            alert("Login Successful!");
            localStorage.setItem('adminAuthToken', result.token);
            this.$router.push('/admin-dashboard');
          }
        } catch (error) {
          this.errorMessage = "Network error. Please try again.";
        }
      }
    }
  };
  </script>
  