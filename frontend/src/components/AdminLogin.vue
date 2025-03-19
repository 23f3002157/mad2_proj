<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form @submit.prevent="loginAdmin">
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" class="form-control" id="email" v-model="email" aria-describedby="emailHelp" placeholder="Enter email">
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" class="form-control" id="password" v-model="password" placeholder="Password">
                    </div>
                    <div v-if="errorMessage">
                        <span>{{ errorMessage }}</span>
                    </div>
                    <button type="submit" class="btn btn-primary">Login</button>
                </form>
            </div>
        </div>
    </div>
    
</template>
<script>
export default{
    data(){
        return {
            email: '',
            password: '',
            errorMessage: null
        };
    },
    methods:{
        async loginAdmin(){
                //initailly why logging in, error message is null
                this.errorMessage = null;
                const payload = {
                    email : this.email,
                    password : this.password
                };
                try{
                    const response = await fetch('http://127.0.0.1:5000/adminLogin',{
                        method:'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(payload),
                    });
                    const result = await response.json();
                    console.log(result)
                    if(result.login !=1){
                        this.errorMessage = result.message || "Something really went wrong";
                    }else{
                        alert("Login Successful!");
                        console.log(result);
                        localStorage.setItem('adminAuthToken', result.token)
                        this.$router.push('/admin-dashboard');
                    }
                }catch (error){
                    this.errorMessage=error;
                }
                
        }
    }
}
</script>