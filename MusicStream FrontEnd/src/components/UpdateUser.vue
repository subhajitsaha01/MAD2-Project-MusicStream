<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome to Users Page</h1>
    <form class="addAlbum">
        <input type="text" name="name" placeholder="Enter User's UserName" v-model="User_Details.username">
        <input type="text" name="name" placeholder="Enter User's Email" v-model="User_Details.email">
        <button v-on:click="updateUser" type="button" style="height:50px;width:150px;">Update User Details</button>
    </form>
</template>
<script>
import AdminHeaderView from './AdminHeaderView.vue';
import axios from 'axios';
export default {
    name: 'UpdateUser',
    data(){
        return {
            name: '',
            user: '',
            User_Details: {
                username:'',
                email:''
            }
        }
    },
    components:{
        AdminHeaderView
    },
    methods:{
        async updateUser(){
            console.log(this.User_Details.username,this.User_Details.email);
            const myparams = {
                'auth_token':this.user.token
            }
            axios.put("http://127.0.0.1:5000/music_stream/api/user/"+this.$route.params.id, {
                "username": this.User_Details.username,
                "email":this.User_Details.email,
                "password":""
            }, {params: myparams})
            .then((response) => {
                console.log(response)
                alert(response.data.message)
            }).catch((error) => {
                if(error.response.status === 400){
                    alert(error.response.data.message);
                }
            })
        }
    },
    async mounted(){
        let user = localStorage.getItem('user-info')
        if(!user){
            this.$router.push({name: 'SignIn'}); 
        }
        else{
            this.name = JSON.parse(user).username;
            this.user = JSON.parse(user)
        }
        console.log(this.$route.params.id)
        const myparams = {
            'auth_token':JSON.parse(user).token
        }
        axios.get('http://127.0.0.1:5000/music_stream/api//user/'+this.$route.params.id, {params:myparams})
        .then((response) => {
            console.log(response)
            this.User_Details.username = response.data.user.username
            this.User_Details.email = response.data.user.email
        })
        .catch((error) => {
            if(error.response.status === 400){
                alert(error.response.data.message);
            }
        })
    }
}
</script>