<template>
  <div class="container mt-4">
    <h3 class="mb-3 text-primary">Admin Search</h3>
    <form @submit.prevent="searchServicer">
      <div class="input-group input-group-sm mb-3 w-75">
        <input type="text" class="form-control" v-model="searchQuery" placeholder="Search by name or email" />
        <button class="btn btn-primary" type="submit" @click="searchFunction">SEARCH</button>
      </div>
      <div class="input-group input-group-sm mb-3 w-50">
        <label class="input-group-text">Search By:</label>
        <select class="form-select" v-model="searchBy">
          <option value="firstname">Firstname</option>
          <option value="city">City</option>
          <option value="category">Category</option>
        </select>
      </div>
    </form>
    <div v-if="stat === 1">
      <div class="row row-cols-1 row-cols-md-3 g-4" v-if="searchResults.length">
        <div v-for="result in searchResults" :key="result.service_ID" class="col">
          <div class="card h-100 shadow-sm">
            <div class="card-body">
              <h5 class="card-title">{{ result.firstname }} {{ result.lastname }}</h5>
              <p class="card-text">Email ID: {{ result.email }}</p>
              <p class="card-text">City: {{ result.city }}</p>
              <p class="card-text">State: {{ result.state }}</p>
              <p class="card-text">Experience: {{ result.experience }}</p>
              <p class="card-text">Rating: {{ result.rating }}</p>
              <p class="card-text">Approved Status: <span :class="{'text-success': result.status === 1, 'text-danger': result.status !== 1}">{{ result.status === 1 ? 'Approved' : 'Pending' }}</span></p>
              <p class="card-text">Blocked Status: <span :class="{'text-success': result.flag === 0, 'text-danger': result.flag !== 0}">{{ result.flag === 0 ? 'NO' : 'YES' }}</span></p>
              <div class="d-flex flex-wrap gap-2">
                <a ref="link" target="_blank" :href="result.servicer_photo" class="btn btn-success">View Photo</a>
                <a ref="link" target="_blank" :href="result.document_verify" class="btn btn-warning">View Document</a>
                <button class="btn btn-danger" @click="toggleServicer(result.servicer_ID)">Block/Unblock</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="stat === 0" class="alert alert-danger mt-3" role="alert">
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
