<template>
  <div>
    <h3>Admin Search</h3>
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
          <option value="customer">Customer</option>
          <option value="servicer">Servicer</option>
        </select>
        </div>
    </form>
  </div>
    <div v-if="stat === 1">
      <div v-if="searchBy === 'customer'">
        <div class="card mb-3">
          <div class="card-header">Customer Results</div>
          <div class="card-body">
            <ul class="list-group">
              <li class="list-group-item" v-for="customer in searchResults" :key="customer.cust_id">
                {{ customer.name }} ({{ customer.email }})
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div v-if="searchBy === 'servicer'" style="display: flex; justify-content: center;">
        <div class="card mb-3" style="max-width: 840px;">
          <div class="row g-0">
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title">{{ searchResults.firstname }} {{ searchResults.lastname }}</h5>
                <p class="card-text">Email: {{ searchResults.email }}</p>
                <p class="card-text">Address: {{ searchResults.address }}, {{ searchResults.city }}, {{ searchResults.state }}</p>
                <p class="card-text">Approved Status: <span v-if="searchResults.status === 1">YES</span><span v-else>NO</span></p>
                <p class="card-text">Block (Yes/No): <span v-if="searchResults.flag === 1">YES</span><span v-else>NO</span></p>
                <p class="card-text">Modified Date: {{ searchResults.modified_date }}</p>
                <a ref="link" target="_blank" :href="searchResults.document_verify"><button @click="$refs.link.href = searchResults.document_verify" class="btn btn-success">View Documents</button></a>
                <a ref="link" target="_blank"><button @click="$refs.link.href = searchResults.servicer_photo" class="btn btn-warning">View Photograph</button></a>
                <button @click="toggleServicer(searchResults.servicer_ID)" class="btn btn-primary">Block/Unblock</button>
              </div>
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
      const response = await fetch("http://127.0.0.1:5000/adminDashboard/search", {
        method:"POST",
        headers:{
            'Content-Type': 'application/json',
                    "Authorization": `Bearer ${localStorage.getItem("adminAuthToken")}`
        },
        body: JSON.stringify(payload)
      }).then(response => response.json())
      console.log(response); this.stat = response.stat;this.searchResults=response.data
    },
    async toggleServicer(servicer_id) {
            const response = await fetch(`http://127.0.0.1:5000//adminDashboard/servicerToggle/${servicer_id}`, {
                method:"PUT",
                headers:{
                    'Content-Type': 'application/json',
                    "Authorization": `Bearer ${localStorage.getItem("adminAuthToken")}`
                }
            }).then(response => response.json())
                alert(response.message);
                this.searchFunction()

    }
  }
};
</script>
