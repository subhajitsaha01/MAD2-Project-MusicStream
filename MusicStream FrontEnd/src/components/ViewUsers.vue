<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome to Users Page</h1>
    <table border="2">
        <tr>
            <th>Id</th>
            <th>Username</th>
            <th>Email</th>
            <th>Role</th>
            <th>Active Status</th>
            <th>Actions</th>
        </tr>
        <tr v-for="item in users.users" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.username }}</td>
            <td>{{ item.email }}</td>
            <td>{{ item.role }}</td>
            <td>{{ item.active }}</td>
            <td>
                <button class="updateButton"><router-link :to="'/update/user/'+item.id" class="update">Update</router-link></button>
                <button class="deleteButton" v-on:click="deleteUser(item.id)" type="button">Delete</button>
                <button class="deleteButton" v-on:click="activateUser(item.id)" type="button">Activate</button>
                <button class="deleteButton_new" v-on:click="deactivateUser(item.id)" type="button">Deactivate</button>
            </td>
        </tr>
    </table>
</template>
<script>
import axios from 'axios';
import AdminHeaderView from './AdminHeaderView.vue';
export default {
    name: 'ViewAlbum',
    data(){
        return {
            name: '',
            users: [],
        }
    },
    methods:{
        async deleteUser(id){
            console.log(id);
            let user = localStorage.getItem('user-info')
            if(!user){
                this.$router.push({name: 'SignIn'}); 
            }
            else
            {
                this.name = JSON.parse(user).username;
            }
            const myparams = {
                'auth_token':JSON.parse(user).token
            }
            if(confirm("Do you want to delete?")==true){
                axios.delete("http://127.0.0.1:5000/music_stream/api/user/"+id, {params:myparams})
                .then((response) => {
                    console.log(response)
                    alert(response.data.message)
                    this.loadData();
                })
                .catch((error) => {
                    console.log(error);
                })
            }
            else{
                alert("You cancelled!!!");
            }
        },
        async activateUser(id){
            console.log(id);
            let user = localStorage.getItem('user-info')
            if(!user){
                this.$router.push({name: 'SignIn'}); 
            }
            else
            {
                this.name = JSON.parse(user).username;
            }
            const myparams = {
                'auth_token':JSON.parse(user).token
            }
            if(confirm("Do you want to activate the user?")==true){
                axios.put("http://127.0.0.1:5000/music_stream/api/user-activate/"+id, null, {params:myparams})
                .then((response) => {
                    console.log(response)
                    alert(response.data.message)
                    this.loadData();
                })
                .catch((error) => {
                    console.log(error);
                })
            }
            else{
                alert("You cancelled!!!");
            }
        },
        async deactivateUser(id){
            console.log(id);
            let user = localStorage.getItem('user-info')
            if(!user){
                this.$router.push({name: 'SignIn'}); 
            }
            else
            {
                this.name = JSON.parse(user).username;
            }
            const myparams = {
                'auth_token':JSON.parse(user).token
            }
            console.log(myparams)
            if(confirm("Do you want to deactivate the user?")==true){
                axios.put("http://127.0.0.1:5000/music_stream/api/user-deactivate/"+id, null, {params:myparams})
                .then((response) => {
                    console.log(response)
                    alert(response.data.message)
                    this.loadData();
                })
                .catch((error) => {
                    console.log(error);
                })
            }
            else{
                alert("You cancelled!!!");
            }
        },
        async loadData(){
            let user = localStorage.getItem('user-info')
            if(!user){
                this.$router.push({name: 'SignIn'}); 
            }
            else
            {
                this.name = JSON.parse(user).username;
            }
            const myparams = {
                'auth_token':JSON.parse(user).token
            }
            try{
                let users = await axios.get("http://127.0.0.1:5000/music_stream/api/users", {params:myparams})
                console.log(users)
                this.users = users.data;
                console.log(this.users)
            }
            catch{
                alert("Please Logout and Login Again to access the data!!!");
                this.$router.push({name: 'AdminHome'});
            }
        }
    },
    components:{
        AdminHeaderView
    },
    async mounted(){
        this.loadData()
    }
}
</script>
<style>
table {
  border-collapse: collapse;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {background-color: #f2f2f2;}

.deleteButton_new{
    width: 90px;
    height: 30px;
    border: 1px solid rgb(72, 76, 78);
    background: rgb(72, 76, 78);
    color: greenyellow;
    cursor: pointer;
    font-size: 15px;
    font-weight:bold;
    border-radius: 5px;
    margin: 5px;
}
.deleteButton_new:hover{
    background-color: rgb(0, 0, 0);
    font-weight: 600;
    color: greenyellow;
}
</style>