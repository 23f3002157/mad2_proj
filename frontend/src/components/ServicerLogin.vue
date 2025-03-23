<template>
  <div class="container min-vh-100 d-flex justify-content-center align-items-center">
    <div class="card shadow p-4" style="max-width: 400px; width: 100%;">
      <h2 class="text-center mb-4">Login - Service Professionals</h2>
      <form @submit.prevent="loginServicer">
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" v-model="email" placeholder="Enter email" required>
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input type="password" class="form-control" id="password" v-model="pass_" placeholder="Enter password" required>
        </div>
        <div v-if="errorMessage" class="alert alert-danger text-center">
          {{ errorMessage }}
        </div>
        <button type="submit" class="btn btn-primary w-100">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      pass_: '',
      errorMessage: null
    }
  },
  methods: {
    async loginServicer(){
      try{
        const response = await fetch('http://127.0.0.1:5000/servicerLogin',{
          method:'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: this.email, pass_: this.pass_ }),
        });
        const result = await response.json();
        if(result.login !== 1){
          this.errorMessage = result.message || "Something went wrong";
        }else{
          alert("Login Successful!");
          localStorage.setItem('servicerAuthToken', result.token);
          this.$router.push('/servicerDashboard');
        }
      } catch (error) {
        this.errorMessage = "Network error, please try again.";
      }
    }
  }
}
</script>
