<template>
  <div class="container mt-4">
    <h3 class="mb-3 text-primary">Customer Search - Services</h3>
    <form @submit.prevent="searchServicer">
      <div class="input-group input-group-sm mb-3 w-75">
        <input type="text" class="form-control" v-model="searchQuery" placeholder="Search by name or email" />
        <button class="btn btn-primary" type="submit" @click="searchFunction">SEARCH</button>
      </div>
      <div class="input-group input-group-sm mb-3 w-50">
        <label class="input-group-text">Search By:</label>
        <select class="form-select" v-model="searchBy">
          <option value="service_description">Service Name</option>
          <option value="price">Price</option>
          <option value="category">Service Category</option>
        </select>
      </div>
    </form>

    <div v-if="stat === 1">
      <div class="row row-cols-1 row-cols-md-3 g-4" v-if="searchResults.length">
        <div v-for="result in searchResults" :key="result.service_ID" class="col">
          <div class="card h-100 shadow-sm">
            <div class="card-body">
              <h5 class="card-title">{{ result.service_description }}</h5>
              <p class="card-text"><strong>Price:</strong> {{ result.price }}</p>
              <p class="card-text"><strong>Category:</strong> {{ result.ser_desc }}</p>
              <p class="card-text"><strong>Created Date:</strong> {{ result.created_date }}</p>
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
      stat: -1,
      searchResults: [],
    };
  },
  methods: {
    async searchFunction() {
      const payload = {
        searchQuery: this.searchQuery,
        searchBy: this.searchBy,
      };
      const response = await fetch("http://127.0.0.1:5000/customerDashboard/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("customerAuthToken")}`,
        },
        body: JSON.stringify(payload),
      }).then((response) => response.json());

      this.stat = response.stat;
      this.searchResults = response.data;
    },
  },
};
</script>
