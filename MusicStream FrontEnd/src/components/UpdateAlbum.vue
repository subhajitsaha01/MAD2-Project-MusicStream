<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome to Update Album Page</h1>
    <form class="addAlbum">
        <input type="text" name="name" placeholder="Enter Album Name" v-model="Album.name">
        <input type="text" name="name" placeholder="Enter Album Artist" v-model="Album.artist">
        <button v-on:click="updateAlbum" type="button">Update Album</button>
    </form>
</template>
<script>
import AdminHeaderView from './AdminHeaderView.vue';
import axios from 'axios';
export default {
    name: 'UpdateAlbum',
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
    components:{
        AdminHeaderView
    },
    methods:{
        async updateAlbum(){
            console.log(this.Album.name,this.Album.artist);
            const myparams = {
                'auth_token':this.user.token
            }
            axios.put("http://127.0.0.1:5000/music_stream/api/album/"+this.$route.params.id, {
                "name": this.Album.name,
                "artist":this.Album.artist
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
        axios.get('http://127.0.0.1:5000/music_stream/api/album/'+this.$route.params.id, {params:myparams})
        .then((response) => {
            this.Album.name = response.data.album_name
            this.Album.artist = response.data.album_artist
        })
        .catch((error) => {
            if(error.response.status === 400){
                alert(error.response.data.message);
            }
        })
    }
}
</script>