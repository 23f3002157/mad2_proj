<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">Admin Dashboard</h2>
        <div class="d-flex gap-2">
          <router-link to="/admin-dashboard/servicerDetails" class="btn btn-primary">Servicer Details</router-link>
          <router-link to="/admin-dashboard/servicesDetails" class="btn btn-secondary">Services</router-link>
          <router-link to="/admin-dashboard/customerDetails" class="btn btn-danger">Customer Details</router-link>
          <router-link to="/admin-dashboard/search" class="btn btn-warning">Search</router-link>
          <router-link to="/admin-dashboard/summary" class="btn btn-info">Summary</router-link>
          <button class="btn btn-warning" @click="download()">Download Report</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminDashboard',
  data(){
      return{
        status: 0
      }
  },
  methods: {
    async download() {
      const response = await fetch("http://127.0.0.1:5000/adminDashboard/exportReport",{
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem("adminAuthToken")}`
        },
      })
      alert("Mail sent successfully! Starting Download")
      const blob = await response.blob();
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = "dataExport.csv";  
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
  
}
</script>
