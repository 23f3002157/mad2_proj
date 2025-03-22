<template>
    <div class="container">
      <h1 class="text-center mb-4">Summary</h1>
      <div class="row justify-content-center">
        <div class="col-md-4">
          <div class="card mb-3">
            <div class="card-body">
              <h5 class="card-title">Total Service Requests</h5>
              <p class="card-text">{{ totalRequests }}</p>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card mb-3">
            <div class="card-body">
              <h5 class="card-title">Requested Services</h5>
              <p class="card-text">{{ totalPending }}</p>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card mb-3">
            <div class="card-body">
              <h5 class="card-title">Completed Services</h5>
              <p class="card-text">{{ totalCompleted }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-center gap-3"> 
    <div style="width: 500px">
      <Bar v-if="l"
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
      />
    </div>
  
    <div style="width: 500px">
      <Bar v-if="0"
        id="my-chart-id-1"
        :options="chartOptions_1"
        :data="chartData_1"
      />
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
    data(){
      return{
        chartData: null,
        chartOptions: {
          responsive: true,
          plugins: {
              legend: {
                  display: false
              }
    }
        },
        chartData_1: null,
        chartOptions_1: {
          responsive: true,
          plugins: {
              legend: {
                  display: false
              }
          }
        },
        l:false,
        totalRequests:0,
        totalPending:0,
        totalCompleted:0,
      }
    },
    methods:{
      async getData(){
          const response = await fetch("http://127.0.0.1:5000/customerDashboard/summary",{
              method:"GET",
              headers:{
                  'Content-Type': 'application/json',
                  "Authorization": `Bearer ${localStorage.getItem("customerAuthToken")}`
              }
          }).then(response => response.json())
          console.log(response)
          this.chartData = {
          labels: [ 'Pending', 'Completed', 'Total Requests' ],
          datasets: [ { data: response.data_1,
              backgroundColor: [ 'rgba(255, 99, 132, 0.7)',  'rgba(54, 162, 235, 0.7)',  'rgba(255, 206, 86, 0.7)']
           } ]
          }
          this.chartData_1 = {
              labels : ['Blocked Users', 'Active Users'],
              datasets: [ { data: response.data_2,
                  backgroundColor: [ 'rgba(255, 99, 132, 0.7)',  'rgba(54, 162, 235, 0.7)' ]
               } ]
          }
          this.totalRequests=response.data_1[0]
          this.totalPending=response.data_1[1]
          this.totalCompleted=response.data_1[2]
          this.l=true
      }
    },
    mounted(){
      this.l=false
      this.getData();
    }
  }
  </script>
  