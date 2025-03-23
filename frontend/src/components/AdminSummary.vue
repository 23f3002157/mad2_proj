<template>
  <div class="container mt-4">
    <h1 class="text-center mb-4">Summary</h1>
    <div class="row text-center">
      <div class="col-md-4">
        <div class="card shadow-sm border-primary">
          <div class="card-body">
            <h5 class="card-title text-primary">Total Users</h5>
            <p class="display-6 fw-bold">{{ totalUsers }}</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card shadow-sm border-success">
          <div class="card-body">
            <h5 class="card-title text-success">Total Service Requests</h5>
            <p class="display-6 fw-bold">{{ totalServicers }}</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card shadow-sm border-danger">
          <div class="card-body">
            <h5 class="card-title text-danger">Total Customers</h5>
            <p class="display-6 fw-bold">{{ totalCustomers }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-center flex-wrap gap-4 mt-4">
      <div class="card shadow p-3" style="width: 500px">
        <Bar v-if="l" id="my-chart-id" :options="chartOptions" :data="chartData" />
      </div>
      <div class="card shadow p-3" style="width: 500px">
        <Bar v-if="l" id="my-chart-id-1" :options="chartOptions_1" :data="chartData_1" />
      </div>
    </div>
  </div>
<br><br>
  <div class="row">
      <div class="col-12">
        <h2 class="text-center mb-4">All Orders</h2>
        <table class="table table-striped">
          <thead>
            <tr>
              <th>serReq_id</th>
              <th>Service Name</th>
              <th>Service Date</th>
              <th>Service Status</th>
              <th>Servicer Name</th>
              <th>Customer Name</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in serReqDetails" :key="order.serReq_id">
              <td>{{ order.serReq_id }}</td>
              <td>{{ order.service_Description }}</td>
              <td>{{ order.service_date.slice(0, 10) }}</td>
              <td>{{ order.status }}</td>
              <td>{{ order.servicername }}</td>
              <td>{{ order.custname }}</td>
  
            </tr>
          </tbody>
        </table>
      </div>
    </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
export default {
  name: 'admin-summary',
  components: { Bar },
  data() {
    return {
      chartData: null,
      chartOptions: {
        responsive: true,
        plugins: {
          legend: {
            display: false
          },
          title: {
            display: true,
            text: "Status of Service Requests"
          }
        }
      },
      chartData_1: null,
      chartOptions_1: {
        responsive: true,
        plugins: {
          legend: {
            display: false
          },
          title: {
            display: true,
            text: "Status of Customers"
          }
        }
      },
      l: false,
      totalUsers: 0,
      totalServicers: 0,
      totalCustomers: 0,
      serReqDetails:[]
    }
  },
  methods: {
    async getData() {
      const response = await fetch("http://127.0.0.1:5000/adminDashboard/summary", {
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
          "Authorization": `Bearer ${localStorage.getItem("adminAuthToken")}`
        }
      }).then(response => response.json())
      console.log(response)
      this.chartData = {
        labels: ['Requested', 'Rejected', 'Accepted', 'Completed'],
        datasets: [{
          data: response.data_1,
          backgroundColor: ['rgba(255, 99, 132, 0.7)', 'rgba(54, 162, 235, 0.7)', 'rgba(255, 206, 86, 0.7)', 'rgba(75, 192, 192, 0.7)']
        }]
      }
      this.chartData_1 = {
        labels: ['Blocked Users', 'Active Users'],
        datasets: [{
          data: response.data_2,
          backgroundColor: ['rgba(255, 99, 132, 0.7)', 'rgba(54, 162, 235, 0.7)']
        }]
      }
      this.totalCustomers = response.data_3[0]
      this.totalServicers = response.data_1[0]+response.data_1[1]+response.data_1[2]+response.data_1[3]
      this.totalUsers = response.data_3[0]+response.data_3[1]
      this.l = true
      this.getRequests();
    },
    async getRequests(){
      const response = await fetch("http://127.0.0.1:5000//getServiceRequest",{
        method:"GET",
        headers:{
          'Content-Type': 'application/json',
          "Authorization": `Bearer ${localStorage.getItem("adminAuthToken")}`
        }
      }).then(response => response.json())
      this.serReqDetails = response.data;
      console.log(response)
    }
  },
  mounted() {
    this.l = false
    this.getData();
  }
}
</script>
