<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">Admin Dashboard</h2>
        <div class="d-flex gap-2">
          <router-link to="/admin-login" class="btn btn-primary">Logout</router-link>
          <router-link to="/admin-new-service" class="btn btn-secondary">Add Service</router-link>
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
