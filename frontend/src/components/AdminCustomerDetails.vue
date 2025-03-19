<template>
  <div class="container">
    <div class="d-flex flex-column align-items-center">
      <h1 class="text-center mb-4">Customer Details</h1>
      <h2>Regular Active Cutomers</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Address</th>
            <th>City</th>
            <th>Postcode</th>
            <th>Flags</th>
            <th>Rating</th>
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
              <td v-if="customer.flag != 1">{{ customer.rating }}</td>
            <td v-if="customer.flag != 1"><button class="btn btn-danger" @click="blockCustomer(customer.cust_id)">Block</button></td>

          </tr>
        </tbody>
      </table>
  </div>
  <br><br>
  <h2>Blocked Customers</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Address</th>
            <th>City</th>
            <th>Postcode</th>
            <th>Flags</th>
            <th>Rating</th>
            <th>Block</th>
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
              <td v-if="customer.flag != 0">{{ customer.rating }}</td>
              <td v-if="customer.flag != 0"><button class="btn btn-success" @click="unblockCustomer(customer.cust_id)">Unblock</button></td>
          </tr>
        </tbody>
      </table>
  </div>
</template>

<script>
export default {
  name: 'AdminCustomerDetails',
  data(){
    return {
        customers:[],
    }
  },
  methods : {
    getCustomers : function(){
        const response = fetch("http://127.0.0.1:5000/getCustomers",{
            method:"GET",
            headers:{
                'Content-Type': 'application/json'
            },
        }).then(response => response.json())
        .then(data => {
            this.customers = data;
            console.log(this.customers);
        })
    },
    async blockCustomer(customer_id){
    try{
      
      console.log(customer_id);
      const response = await fetch(`http://127.0.0.1:5000/adminDashboard/customerBlock/${customer_id}`,{
        method:"PUT",
        headers:{
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("adminAuthToken")}`
        },
      }).then(response => response.json())
      alert(response.message);
      this.getCustomers();
    }catch(e){
      console.log(e);
    }
  },
  async unblockCustomer(customer_id){
    try{
      console.log(customer_id);
      const response = await fetch(`http://127.0.0.1:5000/adminDashboard/customerBlock/${customer_id}`,{
        method:"PATCH",
        headers:{
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("adminAuthToken")}`
        },
      }).then(response => response.json())
      alert(response.message);
      this.getCustomers();
    }catch(e){
      console.log(e);
    }
  }
  },
    mounted(){
    this.getCustomers();
  }

}
</script>
