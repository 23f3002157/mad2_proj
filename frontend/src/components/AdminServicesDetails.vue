<template>
  <div class="container mt-4">
    <h1 class="text-center mb-4">Services Dashboard</h1>
    <div class="text-center mb-3">
      <router-link to="/admin-dashboard/servicesDetails/newService" class="btn btn-primary">
        <i class="bi bi-plus-circle"></i> Add New Service
      </router-link>
    </div>
    <div class="table-responsive">
      <table class="table table-striped table-hover text-center">
        <thead class="table-dark">
          <tr>
            <th>Service ID</th>
            <th>Description</th>
            <th>Price</th>
            <th>Category</th>
            <th>Created Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="service in services" :key="service.service_ID">
            <td>{{ service.service_ID }}</td>
            <td>{{ service.service_description }}</td>
            <td>&#8377; {{ service.price.toFixed(2) }}</td>
            <td>{{ service.ser_desc }}</td>
            <td>{{ new Date(service.created_date).toLocaleDateString() }}</td>
            <td>
              <button class="btn btn-primary btn-sm mx-1" @click="openEditModal(service)">
                <i class="bi bi-pencil-square"></i> Edit
              </button>
              <button class="btn btn-danger btn-sm mx-1" @click="deleteDetails(service.service_ID)">
                <i class="bi bi-trash"></i> Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Edit Service Modal -->
    <div class="modal fade" id="editServiceModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header bg-primary text-white">
            <h5 class="modal-title"><i class="bi bi-pencil-square"></i> Edit Service</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="updateService">
              <div class="mb-3">
                <label class="form-label">Service Description</label>
                <input type="text" v-model="selectedService.service_description" class="form-control" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Price</label>
                <input type="number" v-model="selectedService.price" class="form-control" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Category</label>
                <select class="form-select" v-model="selectedService.sCat_id" required>
                  <option value="cat_1">Plumbing</option>
                  <option value="cat_2">Carpentry</option>
                  <option value="cat_3">Electricals</option>
                </select>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                  <i class="bi bi-x-circle"></i> Close
                </button>
                <button type="submit" class="btn btn-primary">
                  <i class="bi bi-save"></i> Save Changes
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from 'bootstrap';

export default {
  data() {
    return {
      services: [],
      selectedService: {},
      editModal: null
    };
  },
  mounted() {
    this.fetchServices();
    this.editModal = new Modal(document.getElementById('editServiceModal'));
  },
  methods: {
    fetchServices() {
      fetch("http://127.0.0.1:5000/getServicesAdmin")
        .then(response => response.json())
        .then(data => {
          this.services = data;
        })
        .catch(error => {
          console.error('Error fetching services:', error);
        });
    },
    openEditModal(service) {
      this.selectedService = { ...service };
      this.editModal.show();
    },
    async updateService() {
      const response = await fetch(`http://127.0.0.1:5000/adminDashboard/new_service/${this.selectedService.service_ID}`, {
        method: "PATCH",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem("adminAuthToken")}`
        },
        body: JSON.stringify(this.selectedService)
      });
      const result = await response.json();
      alert(result.message);
      this.fetchServices();
      this.editModal.hide();
    },
    async deleteDetails(service_ID) {
      const response = await fetch(`http://127.0.0.1:5000/adminDashboard/new_service/${service_ID}`, {
        method: "PUT",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem("adminAuthToken")}`
        }
      });
      const result = await response.json();
      alert(result.message);
      this.fetchServices();
    }
  }
};
</script>


