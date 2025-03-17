<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">Sign Up - Customers</h2>
        <div v-if="successMessage" class="alert alert-success">
          {{ successMessage }}  
        </div>
        <form @submit.prevent="handleSignup">
          <div class="form-group mb-3">
            <label for="name">Name</label>
            <input type="text" class="form-control" id="name" v-model="name" placeholder="Enter name" required>
          </div>
          <div class="form-group mb-3">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" v-model="email" placeholder="Enter email" required>
          </div>
          <div class="form-group mb-3">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="cust_password" v-model="cust_password" placeholder="Enter password" required>
          </div>
          <div class="form-group mb-3">
            <label for="location">Address</label>
            <input type="text" class="form-control" id="location" v-model="address" placeholder="Enter location" required>
          </div>
          <div class="form-group mb-3">
            <label for="city">Postcode</label>
            <input type="text" class="form-control" id="city" v-model="postcode" placeholder="Enter city" required>
          </div>
          <div class="form-group mb-3">
            <label for="state">City</label>
            <input type="text" class="form-control" id="state" v-model="city" placeholder="Enter state" required>
          </div>
          <button type="submit" class="btn btn-primary w-100">Sign Up</button>
        </form>
      </div>
    </div>
  </div>
</template>
<!-- if data.get('name') and data.get('email') and data.get('cust_password') and data.get('address') and data.get("postcode") and data.get("city"): -->
<script>
export default {
  data() {
    return {
      name: '',
      email: '',
      cust_password: '',
      address: '',
      city: '',
      postcode: '',
      successMessage: null
    }
  },
  methods: {
    async handleSignup() {
        this.successMessage=null
      const payload ={
        name: this.name,
        email: this.email,
        cust_password: this.cust_password,
        address: this.address,
        postcode: this.postcode,
        city: this.city,
        state: this.state
      }
      const response = await fetch("http://127.0.0.1:5000/customerSignUp", {
        method: 'POST',
        headers:{
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });
      const result = await response.json(); console.log(result);
      if(result.status != 1){
        alert(result.message);
      }
      else{
        this.successMessage="Registered Successfully, login to continue";
        alert(result.message);
        this.$router.push('/customer-login');
      }
    }
  }
}
</script>
