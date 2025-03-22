<template>
  <div class="container">
    <div class="d-flex flex-column align-items-center">
      <h1 class="text-center mb-4">Servicer Dashboard</h1>
      
    </div>
  </div>
  <h2>Requested Services</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>serReq_id</th>
          <th>service_id</th>
          <th>service_date</th>
          <th>status</th>
          <th>customername</th>
          <th>ACTIONS</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in serReqDetails" :key="order.serReq_id">
          <td v-if="order.status === 'REQUESTED'">{{ order.serReq_id }}</td>
          <td v-if="order.status === 'REQUESTED'">{{ order.service_id }}</td>
          <td v-if="order.status === 'REQUESTED'">{{ order.service_date }}</td>
          <td v-if="order.status === 'REQUESTED'">{{ order.status }}</td>
          <td v-if="order.status === 'REQUESTED'">{{ order.custname }}</td>
          <td>
            <button class="btn btn-danger" v-if="order.status === 'REQUESTED'" @click="rejectRequest(order.serReq_id)">REJECT</button>
            <button class="btn btn-success" v-if="order.status === 'REQUESTED'" @click="acceptRequest(order.serReq_id)">ACCEPT</button>
          </td>
        </tr>
      </tbody>
    </table>
    <br><hr><br>
    <h2>Rejected Services</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>serReq_id</th>
          <th>service_id</th>
          <th>service_date</th>
          <th>status</th>
          <th>customername</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in serReqDetails" :key="order.serReq_id">
          <td v-if="order.status === 'REJECTED'">{{ order.serReq_id }}</td>
          <td v-if="order.status === 'REJECTED'">{{ order.service_id }}</td>
          <td v-if="order.status === 'REJECTED'">{{ order.service_date }}</td>
          <td v-if="order.status === 'REJECTED'">{{ order.status }}</td>
          <td v-if="order.status === 'REJECTED'">{{ order.custname }}</td>
        </tr>
      </tbody>
    </table>
    <br><hr><br>
    <h2>Accepted Services</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>serReq_id</th>
          <th>service_id</th>
          <th>service_date</th>
          <th>status</th>
          <th>customername</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in serReqDetails" :key="order.serReq_id">
          <td v-if="order.status === 'ACCEPTED'">{{ order.serReq_id }}</td>
          <td v-if="order.status === 'ACCEPTED'">{{ order.service_id }}</td>
          <td v-if="order.status === 'ACCEPTED'">{{ order.service_date }}</td>
          <td v-if="order.status === 'ACCEPTED'">{{ order.status }}</td>
          <td v-if="order.status === 'ACCEPTED'">{{ order.custname }}</td>
        </tr>
      </tbody>
    </table>
    <br><hr><br>
    <h2>Completed Services</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>serReq_id</th>
          <th>service_id</th>
          <th>service_date</th>
          <th>status</th>
          <th>customername</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in serReqDetails" :key="order.serReq_id">
          <td v-if="order.status === 'COMPLETED'">{{ order.serReq_id }}</td>
          <td v-if="order.status === 'COMPLETED'">{{ order.service_id }}</td>
          <td v-if="order.status === 'COMPLETED'">{{ order.service_date }}</td>
          <td v-if="order.status === 'COMPLETED'">{{ order.status }}</td>
          <td v-if="order.status === 'COMPLETED'">{{ order.custname }}</td>
        </tr>
      </tbody>
    </table>
</template>

<script>
export default {
  data(){
    return {
      serReqDetails: []
    }
  },
  methods : {
        async getServiceRequests(){
            const response =  await fetch("http://127.0.0.1:5000/servicerDashboard/serviceRequests",{
                method: "GET",
                headers:{
                    'Content-Type': 'application/json',
                    "Authorization": `Bearer ${localStorage.getItem("servicerAuthToken")}`
                }
            }).then(response => response.json())
            this.serReqDetails=response.data
        },
        async acceptRequest(serReq_i){
            const payload = {
                status:"ACCEPT",
                serReq_id:serReq_i
            }
            const response = await fetch("http://127.0.0.1:5000/servicerDashboard/updateRequestServicer",{
                method: "PUT",
                headers:{
                    'Content-Type': 'application/json',
                     "Authorization": `Bearer ${localStorage.getItem("servicerAuthToken")}`
                },
                body: JSON.stringify(payload)
            }).then(response => response.json())
            alert(response.message)
            this.getServiceRequests();
        },
        async rejectRequest(serReq_i){
            const payload = {
                status:"REJECT",
                serReq_id:serReq_i
            }
            const response = await fetch("http://127.0.0.1:5000/servicerDashboard/updateRequestServicer",{
                method: "PUT",
                headers:{
                    'Content-Type': 'application/json',
                     "Authorization": `Bearer ${localStorage.getItem("servicerAuthToken")}`
                },
                body: JSON.stringify(payload)
            }).then(response => response.json())
            alert(response.message)
            this.getServiceRequests();
        }
},
mounted(){
    this.getServiceRequests();
}
}
</script>
