<template>
  <div class="container">
    <h1 class="text-center mb-4">Services Dashboard</h1>
    <div class="text-center my-3">
      <router-link to="/admin-dashboard/servicesDetails/newService" class="btn btn-primary">Add New Service</router-link>
    </div>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Service ID</th>
          <th>Description</th>
          <th>Price</th>
          <th>Category</th>
          <th>Created Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="service in services" :key="service.service_ID">
          <td>{{ service.service_ID }}</td>
          <td>{{ service.service_description }}</td>
          <td>{{ service.price }}</td>
          <td>{{ service.sCat_id }}</td>
          <td>{{ service.created_date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<!-- "service_ID" INTEGER NOT NULL,
  "service_Description" VARCHAR(40) NOT NULL,
  price FLOAT NOT NULL,
  "sCat_id" VARCHAR(40) NOT NULL,
  created_date DATETIME NOT NULL,
  modified_date DATETIME, -->
<script>
export default {
  data() {
    return {
      services: [] // This should be populated with service data from your backend
    }
  },
  mounted() {
    this.fetchServices();
  },
  methods: {
    fetchServices() {
      // Fetch service data from the backend and populate the services array
      const response = fetch("http://127.0.0.1:5000/getServicesAdmin")
        .then(response => response.json())
        .then(data => {
          this.services = data;
        })
        .catch(error => {
          console.error('Error fetching services:', error);
        });
    }
  }
}
</script>

