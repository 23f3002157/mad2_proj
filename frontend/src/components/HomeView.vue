<template>
    <div class="container">
        <div class="d-flex justify-content-center">
            
        </div>
        <h1 class="text-center">Welcome to the Household Services app</h1>
        <p class="lead text-center">Select role</p>
        <div class="d-flex justify-content-center">
            <router-link to="/admin" class="btn btn-primary">ADMIN</router-link>
            <router-link to="/register" class="btn btn-secondary">CUSTOMER</router-link>
            <router-link to="/register" class="btn btn-danger">Service Professional</router-link>
        </div>
    </div>
</template>

<script>
export default{
    name:'homeView'
}
</script>