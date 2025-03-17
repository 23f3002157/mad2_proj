<template>
  <div class="container">
    <div class="d-flex flex-column align-items-center justify-content-center" style="height: 100vh;">
      <h1 class="text-center mb-4">Welcome to Our Service - Service Professionals</h1>
      <div class="d-flex gap-2">
        <router-link to="/servicer-login" class="btn btn-primary">Login</router-link>
        <router-link to="/servicer-signup" class="btn btn-secondary">Sign Up</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ServicerHome'
}
</script>
