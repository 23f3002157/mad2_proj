<template>
  <div class="container my-5">
    <div class="text-center">
      <h1 class="text-primary fw-bold mb-4">Servicer Details</h1>
    </div>
    <div class="mb-5">
      <h2 class="text-success text-center mb-3">Approved Active Servicers</h2>
      <div class="table-responsive">
        <table class="table table-hover table-striped table-bordered text-center">
          <thead class="table-dark">
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Address</th>
              <th>City</th>
              <th>State</th>
              <th>Rating</th>
              <th>Status</th>
              <th>Experience</th>
              <th>Photograph</th>
              <th>Document</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="servicer in servicers" :key="servicer.servicer_ID">
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.firstname }} {{ servicer.lastname }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.email }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.address }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.city }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.state }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.rating }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.status }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.experience }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0"><a :href="servicer.servicer_photo" target="_blank" class="btn btn-warning">View Photo</a></td>
              <td v-if="servicer.flag != 1 && servicer.status != 0"><a :href="servicer.document_verify" target="_blank" class="btn btn-warning">Document</a></td>
              <td v-if="servicer.flag != 1 && servicer.status != 0"><button class="btn btn-danger" @click="toggleServicer(servicer.servicer_ID)">Block</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="mb-5">
      <h2 class="text-warning text-center mb-3">Pending Servicers</h2>
      <div class="table-responsive">
        <table class="table table-hover table-striped table-bordered text-center">
          <thead class="table-dark">
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Address</th>
              <th>City</th>
              <th>State</th>
              <th>Experience</th>
              <th>Photograph</th>
              <th>Document</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="servicer in servicers" :key="servicer.servicer_ID" >
              <td v-if="servicer.status != 1">{{ servicer.firstname }} {{ servicer.lastname }}</td>
              <td v-if="servicer.status != 1">{{ servicer.email }}</td>
              <td v-if="servicer.status != 1">{{ servicer.address }}</td>
              <td v-if="servicer.status != 1">{{ servicer.city }}</td>
              <td v-if="servicer.status != 1">{{ servicer.state }}</td>
              <td v-if="servicer.status != 1">{{ servicer.experience }}</td>
              <td v-if="servicer.status != 1"><a :href="servicer.servicer_photo" target="_blank" class="btn btn-warning">View Photo</a></td>
              <td v-if="servicer.status != 1"><a :href="servicer.document_verify" target="_blank" class="btn btn-warning">Document</a></td>
              <td v-if="servicer.status != 1">
                <button class="btn btn-success mx-1" @click="approveServicer(servicer.servicer_ID)">Approve</button>
                <button class="btn btn-danger mx-1" @click="rejectServicer(servicer.servicer_ID)">Reject</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="mb-5">
      <h2 class="text-danger text-center mb-3">Blocked Servicers</h2>
      <div class="table-responsive">
        <table class="table table-hover table-striped table-bordered text-center">
          <thead class="table-dark">
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Address</th>
              <th>City</th>
              <th>State</th>
              <th>Flags</th>
              <th>Rating</th>
              <th>Status</th>
              <th>Experience</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="servicer in servicers" :key="servicer.servicer_ID">
              <td v-if="servicer.flag != 0">{{ servicer.firstname }} {{ servicer.lastname }}</td>
              <td v-if="servicer.flag != 0">{{ servicer.email }}</td>
              <td v-if="servicer.flag != 0">{{ servicer.address }}</td>
              <td v-if="servicer.flag != 0">{{ servicer.city }}</td>
              <td v-if="servicer.flag != 0">{{ servicer.state }}</td>
              <td v-if="servicer.flag != 0">{{ servicer.flag }}</td>
              <td v-if="servicer.flag != 0">{{ servicer.rating }}</td>
              <td v-if="servicer.flag != 0">{{ servicer.status }}</td>
              <td v-if="servicer.flag != 0">{{ servicer.experience }}</td>
              <td v-if="servicer.flag != 0"><button class="btn btn-success" @click="toggleServicer(servicer.servicer_ID)">Unblock</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      servicers: []
    };
  },
  methods: {
    getServicers() {
      fetch("http://127.0.0.1:5000/getServicers", {
        method: "GET",
        headers: { "Content-Type": "application/json" }
      })
      .then(response => response.json())
      .then(data => {
        this.servicers = data;
      });
    },
    async toggleServicer(servicer_id) {
      const response = await fetch(`http://127.0.0.1:5000/adminDashboard/servicerToggle/${servicer_id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem("adminAuthToken")}`
        }
      }).then(response => response.json());
      alert(response.message);
      this.getServicers();
    },
    async approveServicer(servicer_id) {
      const response = await fetch(`http://127.0.0.1:5000/adminDashboard/servicerToggle/${servicer_id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem("adminAuthToken")}`
        }
      }).then(response => response.json());
      alert(response.message);
      this.getServicers();
    },
    async rejectServicer(servicer_id) {
      const response = await fetch(`http://127.0.0.1:5000/adminDashboard/servicerToggle/${servicer_id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem("adminAuthToken")}`
        }
      }).then(response => response.json());
      alert(response.message);
      this.getServicers();
    }
  },
  mounted() {
    this.getServicers();
  }
};
</script>
