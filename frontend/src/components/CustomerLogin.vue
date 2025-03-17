<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">Login</h2>
        <form @submit.prevent="handleLogin">
          <div class="form-group mb-3">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" v-model="email" placeholder="Enter email" required>
          </div>
          <div class="form-group mb-3">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" v-model="cust_password" placeholder="Enter password" required>
          </div>
          <div v-if="errorMessage" class="alert alert-danger">
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
      cust_password: '',
      errorMessage: null
    };
  },
  methods: {
    async handleLogin() {
      // Implement login logic here
      this.errorMessage = null;
                const payload = {
                    email : this.email,
                    cust_password : this.cust_password
                };
                try{
                    const response = await fetch('http://127.0.0.1:5000/customerLogin',{
                        method:'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(payload),
                    });
                    const result = await response.json();
                    console.log(result)
                    if(result.login !=1){
                        this.errorMessage = result.message || "Something really went wrong";
                    }else{
                        alert("Login Successful!");
                        console.log(result);
                        localStorage.setItem('customerAuthToken', result.token)
                        this.$router.push('/customer-dashboard');
                    }
                }catch (error){
                    this.errorMessage=error;
                }
    }
  }
};
</script>


