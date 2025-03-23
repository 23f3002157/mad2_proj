<template>
  <div class="container mt-4">
    <div class="text-center">
      <h1 class="mb-4">Customer Details</h1>
    </div>
    <h2 class="mb-3 text-primary">Regular Active Customers</h2>
    <div class="table-responsive">
      <table class="table table-striped table-bordered">
        <thead class="table-dark">
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Address</th>
            <th>City</th>
            <th>Postcode</th>
            <th>Flags</th>
            <th>Block</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="customer in customers" :key="customer.cust_id">
            <td v-if="customer.flag != 1">{{ customer.name }}</td>
            <td v-if="customer.flag != 1">{{ customer.email }}</td>
            <td v-if="customer.flag != 1">{{ customer.address }}</td>
            <td v-if="customer.flag != 1">{{ customer.city }}</td>
            <td v-if="customer.flag != 1">{{ customer.postcode }}</td>
            <td v-if="customer.flag != 1">{{ customer.flag }}</td>
            <td v-if="customer.flag != 1"><button class="btn btn-danger btn-sm" @click="blockCustomer(customer.cust_id)">Block</button></td>
          </tr>
        </tbody>
      </table>
    </div>
    <h2 class="mt-4 mb-3 text-danger">Blocked Customers</h2>
    <div class="table-responsive">
      <table class="table table-striped table-bordered">
        <thead class="table-dark">
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Address</th>
            <th>City</th>
            <th>Postcode</th>
            <th>Flags</th>
            <th>Unblock</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="customer in customers" :key="customer.cust_id">
            <td v-if="customer.flag != 0">{{ customer.name }}</td>
            <td v-if="customer.flag != 0">{{ customer.email }}</td>
            <td v-if="customer.flag != 0">{{ customer.address }}</td>
            <td v-if="customer.flag != 0">{{ customer.city }}</td>
            <td v-if="customer.flag != 0">{{ customer.postcode }}</td>
            <td v-if="customer.flag != 0">{{ customer.flag }}</td>
            <td v-if="customer.flag != 0"><button class="btn btn-success btn-sm" @click="unblockCustomer(customer.cust_id)">Unblock</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminCustomerDetails',
  data() {
    return {
      customers: [],
    };
  },
  methods: {
    getCustomers() {
      fetch("http://127.0.0.1:5000/getCustomers", {
        method: "GET",
        headers: {
          'Content-Type': 'application/json'
        },
      })
      .then(response => response.json())
      .then(data => {
        this.customers = data;
      })
      .catch(error => console.error("Error fetching customers:", error));
    },
    async blockCustomer(customer_id) {
      try {
        const response = await fetch(`http://127.0.0.1:5000/adminDashboard/customerBlock/${customer_id}`, {
          method: "PUT",
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("adminAuthToken")}`
          },
        }).then(response => response.json());
        alert(response.message);
        this.getCustomers();
      } catch (e) {
        console.error(e);
      }
    },
    async unblockCustomer(customer_id) {
      try {
        const response = await fetch(`http://127.0.0.1:5000/adminDashboard/customerBlock/${customer_id}`, {
          method: "PATCH",
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("adminAuthToken")}`
          },
        }).then(response => response.json());
        alert(response.message);
        this.getCustomers();
      } catch (e) {
        console.error(e);
      }
    }
  },
  mounted() {
    this.getCustomers();
  }
};
</script>
