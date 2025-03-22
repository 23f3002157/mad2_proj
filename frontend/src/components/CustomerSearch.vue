<template>
    <div>
      <h3>Customer Search</h3>
      <form @submit.prevent="searchServicer">
        <div class="input-group mb-3 input-group-sm" style="width: 1000px;">
          <input type="text" class="form-control" v-model="searchQuery" placeholder="Search by name or email" />
          <br>
              <br>
            <button class="btn btn-primary" type="submit" @click="searchFunction()">SEARCH</button>
        </div>
        <div class="input-group mb-3 input-group-sm" style="width: 400px;">
          <label>Search By:</label>
          <select class="form-control" v-model="searchBy">
            <option value="service_description">Service Name</option>
            <option value="price">Price</option>
            <option value="category">Service Category</option>
          </select>
          </div>
      </form>
    </div>
      <div v-if="stat === 1">
        <div class="row row-cols-1 row-cols-md-3 g-4" v-if="searchResults.length">
          <div v-for="result in searchResults" :key="result.service_ID" class="col">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">{{ result.service_description }}</h5>
                <p class="card-text">Price: {{ result.price }}</p>
                <p class="card-text">Category: {{ result.sCat_id }}</p>
                <p class="card-text">Created Date: {{ result.created_date }}</p>
              </div>
            </div>
          </div>
        </div>        
      </div>
      <div v-if="stat === 0">
        <div class="alert alert-danger" role="alert">
          No results found.
        </div>
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
        searchQuery: "",
        searchBy: "",
        stat :-1,
        searchResults:[]
      };
    },
    methods: {
      async searchFunction() {
        console.log("searchQuery: ", this.searchBy, this.searchQuery);
        const payload = {
          searchQuery : this.searchQuery,
          searchBy : this.searchBy
        }
        const response = await fetch("http://127.0.0.1:5000/customerDashboard/search", {
          method:"POST",
          headers:{
              'Content-Type': 'application/json',
               "Authorization": `Bearer ${localStorage.getItem("customerAuthToken")}`
          },
          body: JSON.stringify(payload)
        }).then(response => response.json())
         this.searchResults = response.data; this.stat=response.stat; console.log(this.searchResults);
      },
    }
  };
  </script>
  