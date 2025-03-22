<template>
    <div class="container">
      <h1 class="text-center mb-4">Select a Service</h1>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="service in allServices" :key="service.service_ID">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">{{ service.service_description }}</h5>
              <p class="card-text">Price: {{ service.price }}</p>
              <p class="card-text">Service ID: {{ service.service_ID }}</p>
              <p class="card-text">Category: {{ service.sCat_id }}</p>
              <button @click="openEditModal(service)" class="btn btn-primary">BOOK</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  
    <!-- Modal -->
    <div class="modal fade" id="editServiceModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Book Service</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="updateService">
                <div class="mb-3">
                <label class="form-label">Service ID</label>
                <input type="text" v-model="selectedService.service_ID" class="form-control" disabled>
              </div>
              <div class="mb-3">
                <label class="form-label">Service Description</label>
                <input type="text" v-model="selectedService.service_description" class="form-control" disabled>
              </div>
              <div class="mb-3">
                <label class="form-label">Price</label>
                <input type="number" v-model="selectedService.price" class="form-control" disabled>
              </div>
              <div class="mb-3">
                <label class="form-label">Category</label>
                <input type="text" v-model="selectedService.sCat_id" class="form-control" disabled>
              </div>
              <div class="mb-3">
                <label class="form-label">Select Professional</label>
                <select v-model="selectedService.servicer_ID" class="form-select">
                  <option v-for="temp in tempSer" :key="temp.servicer_ID" :value="temp.servicer_ID">
                    {{ temp.firstname + " " + temp.lastname }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Select Date</label>
                <input type="date" v-model="selectedService.service_date" class="form-control" />
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary">Confirm Booking</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { Modal } from 'bootstrap'
  
  export default {
    data() {
      return {
        allServices: [],
        tempSer: [],
        selectedService: {},
        editModal: null,
      }
    },
    mounted() {
      this.fetchServices();
      this.editModal = new Modal(document.getElementById('editServiceModal'), { keyboard: false });
    },
    methods: {
      async fetchServices() {
        try {
          const response = await fetch("http://127.0.0.1:5000/getServicesAdmin", {
            method: "GET", 
            headers: { 'Content-Type': 'application/json' }
          });
          if (!response.ok) throw new Error("Failed to fetch services");
          this.allServices = await response.json();
        } catch (error) {
          console.error("Error fetching services:", error);
        }
      },
  
      async fetchServicers(cat_id) {
        try {
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
  
      async openEditModal(service) {
        this.selectedService = { ...service }; 
        this.fetchServicers(service.sCat_id); 
        this.editModal.show(); 
      },
  
      async updateService() {
        console.log("Booking service:", this.selectedService);
        const response = await fetch("http://127.0.0.1:5000/customerDashboard/serviceRequest",{
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("customerAuthToken")}`
          },
          body: JSON.stringify(this.selectedService)
        }).then(response => response.json())
            alert(response.message)
            this.$router.push("/customerDashboard")
        alert()
        this.editModal.hide();
      }
    }
  }
  </script>
  
  <style>
  .modal-content {
    max-width: 500px;
    margin: auto;
  }
  </style>
  