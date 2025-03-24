<template>
    <div>
      <div class="container d-flex flex-column justify-content-center align-items-center vh-100">
        <h1 class="text-center mb-3">Welcome to the Household Services App</h1>
        <p><i>Services. Reimagined.</i></p>
        <p class="lead text-center mb-4">Select Your Role</p>
        <div class="d-flex gap-3">
          <router-link to="/admin-login" class="btn btn-primary px-4">Admin</router-link>
          <router-link to="/customer-home" class="btn btn-secondary px-4">Customer</router-link>
          <router-link to="/servicer-home" class="btn btn-danger px-4">Service Professional</router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'homeView'
  }
  </script>
  