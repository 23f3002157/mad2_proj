<template>
  <div class="container mt-4">
    <div class="text-center mb-4">
      <h1 class="text-primary fw-bold">Servicer Dashboard</h1>
    </div>

    <div class="mb-4">
      <h2 class="text-secondary">Requested Services</h2>
      <table class="table table-bordered table-hover">
        <thead class="table-primary">
          <tr>
            <th>Service Request ID</th>
            <th>Service ID</th>
            <th>Service Description</th>
            <th>Service Date</th>
            <th>Status</th>
            <th>Customer Name</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in serReqDetails" :key="order.serReq_id" >
            <td v-if="order.status === 'REQUESTED'">{{ order.serReq_id }}</td>
            <td v-if="order.status === 'REQUESTED'">{{ order.service_id }}</td>
            <td v-if="order.status === 'REQUESTED'">{{ order.service_Description }}</td>
            <td v-if="order.status === 'REQUESTED'">{{ order.service_date }}</td>
            <td v-if="order.status === 'REQUESTED'" class="fw-bold text-warning">{{ order.status }}</td>
            <td v-if="order.status === 'REQUESTED'">{{ order.custname }}</td>
            <td v-if="order.status === 'REQUESTED'">
              <button class="btn btn-danger me-2" @click="rejectRequest(order.serReq_id)">Reject</button>
              <button class="btn btn-success" @click="acceptRequest(order.serReq_id)">Accept</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mb-4">
      <h2 class="text-danger">Rejected Services</h2>
      <table class="table table-bordered table-hover">
        <thead class="table-danger">
          <tr>
            <th>Service Request ID</th>
            <th>Service ID</th>
            <th>Service Description</th>
            <th>Service Date</th>
            <th>Status</th>
            <th>Customer Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in serReqDetails" :key="order.serReq_id" >
            <td v-if="order.status === 'REJECTED'">{{ order.serReq_id }}</td>
            <td v-if="order.status === 'REJECTED'">{{ order.service_id }}</td>
            <td v-if="order.status === 'REJECTED'">{{ order.service_Description }}</td>
            <td v-if="order.status === 'REJECTED'">{{ order.service_date }}</td>
            <td v-if="order.status === 'REJECTED'" class="fw-bold text-danger">{{ order.status }}</td>
            <td v-if="order.status === 'REJECTED'">{{ order.custname }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mb-4">
      <h2 class="text-success">Accepted Services</h2>
      <table class="table table-bordered table-hover">
        <thead class="table-success">
          <tr>
            <th>Service Request ID</th>
            <th>Service ID</th>
            <th>Service Description</th>
            <th>Service Date</th>
            <th>Status</th>
            <th>Customer Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in serReqDetails" :key="order.serReq_id">
            <td v-if="order.status === 'ACCEPTED'">{{ order.serReq_id }}</td>
            <td v-if="order.status === 'ACCEPTED'">{{ order.service_id }}</td>
            <td v-if="order.status === 'ACCEPTED'">{{ order.service_Description }}</td>
            <td v-if="order.status === 'ACCEPTED'">{{ order.service_date }}</td>
            <td v-if="order.status === 'ACCEPTED'" class="fw-bold text-success">{{ order.status }}</td>
            <td v-if="order.status === 'ACCEPTED'">{{ order.custname }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mb-4">
      <h2 class="text-info">Completed Services</h2>
      <table class="table table-bordered table-hover">
        <thead class="table-info">
          <tr>
            <th>Service Request ID</th>
            <th>Service ID</th>
            <th>Service Description</th>
            <th>Service Date</th>
            <th>Status</th>
            <th>Customer Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in serReqDetails" :key="order.serReq_id" >
            <td v-if="order.status === 'COMPLETED'">{{ order.serReq_id }}</td>
            <td v-if="order.status === 'COMPLETED'">{{ order.service_id }}</td>
            <td v-if="order.status === 'COMPLETED'">{{ order.service_Description }}</td>
            <td v-if="order.status === 'COMPLETED'">{{ order.service_date }}</td>
            <td v-if="order.status === 'COMPLETED'" class="fw-bold text-info">{{ order.status }}</td>
            <td v-if="order.status === 'COMPLETED'">{{ order.custname }}</td>
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
            console.log(this.serReqDetails)
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
