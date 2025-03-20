<template>
  <div class="container">
    <div class="d-flex flex-column align-items-center">
      <h1 class="text-center mb-4">Servicer Details</h1>
      <h2>Approved Activer Servicers</h2>
      <table class="table table-striped">
        <thead>
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
          </tr>
        </thead>
        <tbody>
          <tr v-for="servicer in servicers" :key="servicer.servicer_ID">
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.firstname }} {{ servicer.lastname }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.email }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.address }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.city }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.state }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.flag }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.rating }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.status }}</td>
              <td v-if="servicer.flag != 1 && servicer.status != 0">{{ servicer.experience }}</td>
            <td v-if="servicer.flag != 1 && servicer.status != 0"><button class="btn btn-danger" @click="toggleServicer(servicer.servicer_ID)">Block</button></td>
          </tr>
        </tbody>
      </table>
      <h2>Pending Servicers</h2>
      <table class="table table-striped">
        <thead>
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
          </tr>
        </thead>
        <tbody>
          <tr v-for="servicer in servicers" :key="servicer.servicer_ID">
              <td v-if="servicer.status != 1">{{ servicer.firstname }} {{ servicer.lastname }}</td>
              <td v-if="servicer.status != 1">{{ servicer.email }}</td>
              <td v-if="servicer.status != 1">{{ servicer.address }}</td>
              <td v-if="servicer.status != 1">{{ servicer.city }}</td>
              <td v-if="servicer.status != 1">{{ servicer.state }}</td>
              <td v-if="servicer.status != 1">{{ servicer.flag }}</td>
              <td v-if="servicer.status != 1">{{ servicer.rating }}</td>
              <td v-if="servicer.status != 1">{{ servicer.status }}</td>
              <td v-if="servicer.status != 1">{{ servicer.experience }}</td>
            <td v-if="servicer.status != 1"><button class="btn btn-success" @click="approveServicer(servicer.servicer_ID)">Approve</button></td>

            <!-- firstname VARCHAR(40) NOT NULL,
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
  document_verify VARCHAR(200) -->
          </tr>
        </tbody>
      </table>
      <h2>Blocked Servicers</h2>
      <table class="table table-striped">
        <thead>
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

            <!-- firstname VARCHAR(40) NOT NULL,
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
  document_verify VARCHAR(200) -->
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            servicers: []
        }
    },
    methods : {
        getServicers(){
            const response = fetch("http://127.0.0.1:5000/getServicers",{
            method:"GET",
            headers:{
                'Content-Type': 'application/json'
            },
        }).then(response => response.json())
        .then(data => {
            this.servicers = data;
            console.log(this.servicers);
        })
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
                this.getServicers();

    },
    async approveServicer(servicer_id) {
            const response = await fetch(`http://127.0.0.1:5000/adminDashboard/servicerToggle/${servicer_id}`, {
                method:"PATCH",
                headers:{
                    'Content-Type': 'application/json',
                    "Authorization": `Bearer ${localStorage.getItem("adminAuthToken")}`
                }
            }).then(response => response.json())
                alert(response.message);
                this.getServicers();
    }
},
    mounted(){
        this.getServicers();
    }
}
</script>