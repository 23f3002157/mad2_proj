<template>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="col-md-6">
      <div class="card shadow-lg p-4">
        <h2 class="text-center text-primary mb-4">Add New Service</h2>
        <form @submit.prevent="addNewService">
          <div class="mb-3">
            <label for="service_description" class="form-label">Service Description</label>
            <input type="text" class="form-control" id="service_description" v-model="service_description" placeholder="Enter service description" required>
          </div>
          <div class="mb-3">
            <label for="price" class="form-label">Price</label>
            <input type="number" class="form-control" id="price" v-model="price" placeholder="Enter price" required>
          </div>
          <div class="mb-3">
            <label for="sCat_id" class="form-label">Service Category</label>
            <select class="form-select" id="sCat_id" v-model="sCat_id" required>
              <option v-for="service in allServices" :value="service.sCat_id">{{ service.ser_desc }}</option>
            </select>
          </div>
          <div v-if="errorMessage" class="alert alert-danger text-center">
            {{ errorMessage }}
          </div>
          <button type="submit" class="btn btn-primary w-100">Add Service</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      service_description: '',
      price: 0,
      sCat_id: '',
      allServices: [],
      errorMessage: ''
    }
  },
  methods: {
    async addNewService() {
      const payload = {
        service_Description: this.service_description,
        price: this.price,
        sCat_id: this.sCat_id
      }
      try {
        const response = await fetch('http://127.0.0.1:5000/adminDashboard/new_service', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("adminAuthToken")}`
          },
          body: JSON.stringify(payload)
        }).then(response => response.json())
        if (response.status === 1) {
          alert("Service Created Successfully!");
          this.$router.push('/admin-dashboard/servicesDetails');
        } else {
          this.errorMessage = response.data.message;
        }
      } catch (error) {
        this.errorMessage = "Network error. Please try again.";
      }
    },
    getServices() {
      fetch("http://127.0.0.1:5000/getServices", {
        method: "GET",
        headers: { 'Content-Type': 'application/json' },
      })
      .then(response => response.json())
      .then(data => {
        this.allServices = data;
      });
    }
  },
  mounted() {
    this.getServices();
  }
}
</script>
