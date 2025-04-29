<template>
    <img class="logo" src="../assets/Music Streaming APP_transparent.png">
    <h1 class="heading">User Registration</h1>
    <div class="register">
        <input type="text" v-model="username" placeholder="Enter Username" required/>
        <input type="email" v-model="email" placeholder="Enter Email" required/>
        <input type="password" v-model="password" placeholder="Enter Password" required/>
        <router-link to="/signin" class="loginLink">If already registered, Please Login Here!!!</router-link>
        <button v-on:click="signUp">SignUp</button>
        <button v-on:click="reset">Reset</button>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    name: "UserSignUp",
    data(){
        return {
            username: '',
            email: '',
            password: ''
        }
    },
    methods: {
        reset(){
            this.username = '',
            this.email = '',
            this.password = ''
        },
        signUp(){
            //console.warn("signup",this.username,this.email,this.password)
            axios.post("http://127.0.0.1:5000/music_stream/api/user-register",{
                "username":this.username,
                "email":this.email,
                "password":this.password
            }).then((response) => {
                alert('Registration successfully done');
                console.log(response);
                this.$router.push({name: 'SignIn'})
            })
            .catch((error) => {
                if(error.response.status === 400){
                    alert(error.response.data.message);
                }
            });
        }
    },
    mounted(){
        let user = localStorage.getItem('user-info');
        if(user){
            // this.$router.push({name: 'Home'}); 
        }
    }
}
</script>

<style>
.logo{
    width: 200px;
    margin-bottom: 0px;
}
.loginLink{
    display: block;
    margin: 5px;
    font-weight: 600;
}
.heading{
    margin-top: 0px;
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
</style>