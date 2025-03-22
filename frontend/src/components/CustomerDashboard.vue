<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-12 text-center">
        <h1 v-if="cust_details.length">Welcome {{ cust_details[0].name }}</h1>
      </div>
    </div>
    <div class="row justify-content-center mt-4 mb-5">
      <div class="col-auto">
        <router-link to="/customerDashboard/new_service" class="btn btn-secondary mx-2">Create new Service</router-link>
        <router-link to="/customerDashboard/search" class="btn btn-success mx-2">Search</router-link>
        <router-link to="/customer-support" class="btn btn-info mx-2">Summary</router-link>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <h2 class="text-center mb-4">Your Orders</h2>
        <table class="table table-striped">
          <thead>
            <tr>
              <th>serReq_id</th>
              <th>service_id</th>
              <th>service_date</th>
              <th>status</th>
              <th>servicername</th>
              <th>ACTIONS</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in serReqDetails" :key="order.serReq_id">
              <td>{{ order.serReq_id }}</td>
              <td>{{ order.service_id }}</td>
              <td>{{ order.service_date }}</td>
              <td>{{ order.status }}</td>
              <td>{{ order.servicername }}</td>
              <td><button class="btn btn-primary" v-if="order.status === 'REQUESTED'" @click="openEditModal_1(order)">EDIT</button>
                <button class="btn btn-danger" v-if="order.status === 'REQUESTED'" @click="deleteDetails(order.serReq_id)">DELETE</button>
                <button class="btn btn-warning" v-if="order.status === 'COMPLETED'" @click="openEditModal_2(order)">FEEDBACK</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="modal fade" id="editServiceModal_1" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Edit Service Request</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="updateService">
                <div class="mb-3">
                <label class="form-label">Service Request ID</label>
                <input type="text" v-model="selectedServiceReq.serReq_id" class="form-control" disabled>
              </div>
                <div class="mb-3">
                  <label class="form-label">Service ID</label>
                  <input type="text" v-model="selectedServiceReq.service_id" class="form-control" disabled>
                </div>
                <div class="mb-3">
                  <label class="form-label">Service Date</label>
                  <input type="date" v-model="selectedServiceReq.service_date" class="form-control" required>
                </div>
                <div class="mb-3">
                  <label class="form-label">Servicer Name</label>
                  <input type="text" v-model="selectedServiceReq.servicername" class="form-control" disabled>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  <button type="submit" class="btn btn-primary">Save Changes</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
</template>

<script>
import { Modal } from 'bootstrap';
export default {
  name: 'CustomerDashboard',
  data() {
    return {
      cust_details: [],
      serReqDetails: [],
      servicers: [],
      selectedServiceReq: {},
      editModal: null,
      tempSer: []
    }
  },
  methods: {
    async getDetails() {
      const response = await fetch("http://127.0.0.1:5000/customerDashboard/getDetails", {
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem("customerAuthToken")}`
        }
      })
      const data = await response.json();
      this.cust_details = data.data
    },
    getServicers() {
      fetch("http://127.0.0.1:5000/getServicers", {
        method: "GET",
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => response.json())
        .then(data => {
          this.servicers = data;
          console.log(this.servicers);
        })
    },
    getServiceRequests() {
      fetch("http://127.0.0.1:5000/getServiceRequest", {
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem("customerAuthToken")}`
        }
      }).then(response => response.json())
        .then(data => {
          this.serReqDetails = data;
          console.log(this.serReqDetails);
        })
    },
    deleteDetails(serReq_id){
        const response = fetch(`http://127.0.0.1:5000//customerDashboard/deleteRequest/${serReq_id}`,{
            method:"PUT",
            headers:{
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem("customerAuthToken")}`
            }
        }).then(response => response.json())
            alert("Deleted successfully");
            this.getServiceRequests();
    },
    async fetchServicers(cat_id) {
        try {
          console.log(cat_id);
          const response = await fetch(`http://127.0.0.1:5000/getServicersCustomer/${cat_id}`, {
            method: "GET", 
            headers: { 'Content-Type': 'application/json' }
          });
          if (!response.ok) throw new Error("Failed to fetch servicers");
          this.tempSer = await response.json();
        } catch (error) {
          console.error("Error fetching servicers:", error);
        }
      },
    openEditModal_1(order) {
        this.selectedServiceReq = { ...order };
        console.log(this.selectedServiceReq);
        // this.fetchServicers(order.sCat_id)
        this.editModal.show();
      },
      async updateService(){
          const response = await fetch('http://127.0.0.1:5000//customerDashboard/updateRequest',{
            method:"PUT",
            headers:{
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${localStorage.getItem("customerAuthToken")}`
            },
            body: JSON.stringify(this.selectedServiceReq)
          }).then(response => response.json())
          alert("Updated successfully");
          this.getServiceRequests();
      }
  },
  mounted() {
    this.getDetails()
    this.getServicers()
    this.getServiceRequests()
    this.editModal = new Modal(document.getElementById('editServiceModal_1'));
  }
}
</script>

