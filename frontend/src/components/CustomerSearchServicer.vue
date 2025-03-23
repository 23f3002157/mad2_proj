<template>
    <div>
      <h3>Customer Search - Service Professionals</h3>
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
            <option value="firstname">Firstname</option>
            <option value="city">City</option>
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
                <h5 class="card-title">{{ result.firstname }}  {{ result.lastname }}</h5>
                <p class="card-text">Email ID: {{ result.email }}</p>
                <p class="card-text">City: {{ result.city }}</p>
                <p class="card-text">State: {{ result.state }}</p>
                <p class="card-text">Experience: {{ result.experience }}</p>
                <p class="card-text">Rating: {{ result.rating }}</p>
                <p class="card-text"><a ref="link" target="_blank" :href="result.servicer_photo"><button class="btn btn-warning">View Photo</button></a></p>
                <!-- "servicer_ID" VARCHAR(40) NOT NULL,
  firstname VARCHAR(40) NOT NULL,
  lastname VARCHAR(40) NOT NULL,
  email VARCHAR(30) NOT NULL,
  pass_ VARCHAR(20) NOT NULL,
  address VARCHAR(150) NOT NULL,
  city VARCHAR(40) NOT NULL,
  state VARCHAR(40) NOT NULL,
  created_date DATETIME NOT NULL,
  modified_date DATETIME NOT NULL,
  "sCat_id" VARCHAR(40) NOT NULL,
  flag INTEGER,
  status INTEGER,
  experience INTEGER,
  rating FLOAT,
  servicer_photo VARCHAR(200),
  document_verify VARCHAR(200), -->
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
          method:"PUT",
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
  