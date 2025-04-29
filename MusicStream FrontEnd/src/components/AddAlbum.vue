<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome to Add Album Page</h1>
    <form class="addAlbum">
        <input type="text" name="name" placeholder="Enter Album Name" v-model="Album.name">
        <input type="text" name="name" placeholder="Enter Album Artist" v-model="Album.artist">
        <button v-on:click="addAlbum" type="button">Add Album</button>
        <input type="reset" value="Reset"/>
    </form>
</template>
<script>
import axios from 'axios';
import AdminHeaderView from './AdminHeaderView.vue';
export default {
    name: 'AddAlbum',
    data(){
        return {
            name: '',
            user: '',
            Album: {
                name:'',
                artist:''
            }
        }
    },
    methods:{
        addAlbum(){
            console.log(this.Album.name, this.Album.artist);
            const myparams = {
            'auth_token':this.user.token
            }
            //console.log(myparams)
            axios.post("http://127.0.0.1:5000/music_stream/api/albums", {
                "name": this.Album.name,
                "artist":this.Album.artist
            }, {params: myparams}).then((response) => {
                console.log(response)
                alert(response.data.message)
            }).catch((error) => {
                if(error.response.status === 400){
                    alert(error.response.data.message);
                }
            })
            this.Album.name = ''
            this.Album.artist = ''
        }
    },
    components:{
        AdminHeaderView
    },
    mounted(){
        let user = localStorage.getItem('user-info')
        if(!user){
            this.$router.push({name: 'SignIn'}); 
        }
        else{
            this.name = JSON.parse(user).username;
            this.user = JSON.parse(user)
        }
    }
}
</script>
<style>
.addAlbum input[type=text]{
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
.addAlbum button{
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
.addAlbum button:hover{
    background: rgb(137, 142, 145);
}
</style>
