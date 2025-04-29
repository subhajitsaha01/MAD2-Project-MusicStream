<template>
    <img class="logo" src="../assets/Music Streaming APP_transparent.png">
    <h1 class="heading">User Login</h1>
    <div class="register">
        <div class="role_select">
            <i>Role :</i> 
            <input type="radio" id="general_user_select" name="role" value="General_User" v-model="role">
            <label for="general_user_select">General User&nbsp;</label>
            <input type="radio" id="creator_select" name="role" value="Creator" v-model="role">
            <label for="creator_select">Creator&nbsp;</label>
            <input type="radio" id="admin_select" name="role" value="Admin" v-model="role">
            <label for="admin_select">Admin&nbsp;</label>
        </div>
        <input type="email" v-model="email" placeholder="Enter Email" required/>
        <input type="password" v-model="password" placeholder="Enter Password" required/>
        <router-link to="/signup" class="loginLink">If not registered, Please Register Here!!!</router-link>
        <button v-on:click="signIn">SignIn</button>
        <button v-on:click="reset">Reset</button>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    name: "UserSignIn",
    data(){
        return {
            email: '',
            password: '',
            role: ''
        }
    },
    methods: {
        reset(){
            this.email = '',
            this.password = '',
            this.role = ''
        },
        signIn(){
            //console.warn("signup",this.email,this.password,this.role)
            if(this.role==='General_User'){
                axios.post("http://127.0.0.1:5000/music_stream/api/user-login",{
                    "email":this.email,
                    "password":this.password
                }).then((response) => {
                    alert('General User Login successfully Done');
                    console.log(response);
                    localStorage.setItem("user-info",JSON.stringify(response.data));
                    // this.$router.push({name: 'Home'})
                })
                .catch((error) => {
                    if(error.response.status === 400){
                        alert(error.response.data.message);
                    }
                });
            }
            else if(this.role==='Creator'){
                axios.post("http://127.0.0.1:5000/music_stream/api/user-login",{
                    "email":this.email,
                    "password":this.password
                }).then((response) => {
                    alert('Creator Login Successfully Done');
                    console.log(response);
                    localStorage.setItem("user-info",JSON.stringify(response.data));
                    // this.$router.push({name: 'Home'})
                })
                .catch((error) => {
                    if(error.response.status === 400){
                        alert(error.response.data.message);
                    }
                });
            }
            else if(this.role==='Admin'){
                axios.post("http://127.0.0.1:5000/music_stream/api/user-login",{
                    "email":this.email,
                    "password":this.password
                }).then((response) => {
                    if(response.data.role===this.role){
                        alert('Admin Login Successfully Done');
                        console.log(response);
                        localStorage.setItem("user-info",JSON.stringify(response.data));
                        this.$router.push({name: 'AdminHome'})
                    }
                    else
                    {
                        alert("Role Selected is Wrong!");
                    }
                })
                .catch((error) => {
                    if(error.response.status === 400){
                        alert(error.response.data.message);
                    }
                });
            }
            else{
                alert("Role Not Selected");
            }
        }
    },  
    mounted(){
        let user = JSON.parse(localStorage.getItem('user-info'))
        console.log(user)
        if(user){
            if(user.role==='Admin'){
            this.$router.push({name: 'AdminHome'}); 
            }
        }
    }
}
</script>

<style>
.logo{
    width: 200px;
    margin-bottom: 0px;
}
.heading{
    margin-top: 0px;
}
.loginLink{
    display: block;
    margin: 5px;
    font-weight: 600;
}
.register input[type=text],.register input[type=email],.register input[type=password]{
    width: 300px;
    height: 40px;
    padding-left: 20px;
    display:block;
    margin-bottom: 30px;
    margin-left: auto;
    margin-right: auto;
    border: 3px solid rgb(72, 76, 78);
    border-radius: 10px;
    font-size: 15px;
}
.register button,input[type=reset]{
    width: 160px;
    height: 40px;
    border: 1px solid rgb(72, 76, 78);
    background: rgb(72, 76, 78);
    color: white;
    cursor: pointer;
    font-size: 20px;
    font-weight:bold;
    border-radius: 5px;
    margin: 5px;
}
.role_select{
    margin: 20px;
    font-family:Avenir, Helvetica, Arial, sans-serif;
    font-size: medium;
    color: rgb(72, 76, 78);
    font-weight: 600;
}
</style>