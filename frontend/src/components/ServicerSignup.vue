<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">Service Professional Signup</h2>
        <form @submit.prevent="handleSignup">
          <div class="form-group mb-3">
            <label for="firstname" class="form-label">First Name</label>
            <input type="text" class="form-control" id="firstname" v-model="firstname" placeholder="Enter first name" required>
          </div>
          <div class="form-group mb-3">
            <label for="lastname" class="form-label">Last Name</label>
            <input type="text" class="form-control" id="lastname" v-model="lastname" placeholder="Enter last name" required>
          </div>
          <div class="form-group mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email" v-model="email" placeholder="Enter email" required>
          </div>
          <div class="form-group mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" v-model="pass_" placeholder="Enter password" required>
          </div>
          <div class="form-group mb-3">
            <label for="state" class="form-label">State</label>
            <input type="text" class="form-control" id="state" v-model="state" placeholder="Enter state" required>
          </div>
          <div class="form-group mb-3">
            <label for="experience" class="form-label">Experience</label>
            <input type="number" class="form-control" id="experience" v-model="experience" placeholder="Enter experience" required>
          </div>
          <div class="form-group mb-3">
            <label for="city" class="form-label">City</label>
            <input type="text" class="form-control" id="city" v-model="city" placeholder="Enter city" required>
          </div>
          <div class="form-group mb-3">
            <label for="address" class="form-label">Address</label>
            <input type="text" class="form-control" id="address" v-model="address" placeholder="Enter address" required>
          </div>
          <div class="form-group mb-3">
            <label for="lastname" class="form-label">Service Category</label>
            <select class="form-select" id="service" v-model="sCat_id" required>
                <option v-for="service in allServices" :value="service.sCat_id">{{ service.ser_desc }}</option>
            </select>
          </div>
          <div class="form-group mb-3">
            <label for="document1" class="form-label">Document Link 1</label>
            <input type="text" class="form-control" id="document1" v-model="document_verify" placeholder="Enter document link 1" required>
          </div>
          <div class="form-group mb-3">
            <label for="document2" class="form-label">Servicer Photo</label>
            <input type="text" class="form-control" id="document2" v-model="servicer_photo" placeholder="Enter servicer photo" required>
          </div>
          <div v-if="errorMessage" class="alert alert-danger">
            {{ errorMessage }}
          </div>
          <button type="submit" class="btn btn-primary w-100">Sign Up</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstname: '',
      lastname: '',
      email: '',
      pass_: '',
      city: '',
      state: '',
      address: '',
      experience: 0,
      sCat_id: "",
      document_verify: '',
      servicer_photo: '',
      errorMessage: null,
      allServices: [],
    };
  },
  methods: {
    async handleSignup() {
      this.errorMessage = null;
      const payload = {
        firstname : this.firstname,
        lastname: this.lastname,
        email: this.email,
        pass_:this.pass_,
        city:this.city,
        state:this.state,
        sCat_id:this.sCat_id,
        address:this.address,
        experience:this.experience,
        document_verify:this.document_verify,
        servicer_photo : this.servicer_photo
      }
      const response = await fetch("http://127.0.0.1:5000/servicerSignUp",{
        method:"POST",
        headers: {
                    'Content-Type': 'application/json',
                },
        body: JSON.stringify(payload)
      })
      const result = await response.json();
      console.log(result);
      alert(result.message)
      if(result.status!=1){
            this.errorMessage= result.message;
      }else{
        alert(result.message)
        this.$router.push('/servicer-login')
      }
    },
    fetchServices: function(){
      const response = fetch("http://127.0.0.1:5000/getServices", {
        method:"GET",
        headers:{
          'Content-Type': 'application/json'
        },
      }).then(response => response.json())
      .then(data => {
        this.allServices = data;
        const iterator = this.allServices.values();
            for (let value of iterator) {
                console.log(value.ser_desc);
            }
      }).catch(error => {console.log(error)})
    }
  },
  mounted(){
    this.fetchServices();
  }
}
</script>



