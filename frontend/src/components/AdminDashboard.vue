<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">Admin Dashboard</h2>
        <div class="d-flex gap-2">
          <router-link to="/admin-dashboard/servicerDetails" class="btn btn-primary">Servicer Details</router-link>
          <router-link to="/admin-dashboard/servicesDetails" class="btn btn-secondary">Services</router-link>
          <router-link to="admin-dashboard/customerDetails" class="btn btn-danger">Customer Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminDashboard'
}
</script>
