<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome to Albums Page</h1>
    <div class="parent">
        <div class="header">Albums</div>
        <router-link to="/add/album" class="addAlbum">Add Album</router-link>
        <div class="album" v-for="item in album.albums" :key="item.id">
            <div class="album_details">
                <div class="album_name">{{ item.album_name }}</div>
                <div class="album_artist">{{ item.album_artist }}</div>
            </div>
            <div class="songs">
                <div class="song" v-for="item_song in item.album_songs" :key="item_song.id">
                    <div class="song_name">{{ item_song.song_name }}</div>
                </div>
            <div class="actions">
                <button class="viewSongButton"><router-link :to="'/view/album/songs/'+item.id" class="update">View Songs</router-link></button>
                <button class="updateButton"><router-link :to="'/update/album/'+item.id" class="update">Update</router-link></button>
                <button class="deleteButton" v-on:click="deleteAlbum(item.id)" type="button">Delete</button>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import AdminHeaderView from './AdminHeaderView.vue';
export default {
    name: 'ViewAlbum',
    data(){
        return {
            name: '',
            album: [],
        }
    },
    methods:{
        async deleteAlbum(id){
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
                axios.delete("http://127.0.0.1:5000/music_stream/api/album/"+id, {params:myparams})
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
                let albums = await axios.get("http://127.0.0.1:5000/music_stream/api/albums", {params:myparams})
                console.log(albums)
                this.album = albums.data;
                console.log(this.album)
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
.parent{
    border: 10px;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    border-radius: 5px;
    border-style: outset;    
}
.header{
    margin: 5px;
    font-size: 35px;
    font-weight: 900;
    text-shadow: 4px 4px 10px rgb(148, 118, 118);
}
.album{
    border: 4px solid black;
    margin: 5px;
    padding: 5px;
    border-radius: 5px;
    position:relative;
    height: auto;
    display: inline-block;
    width: 95%;
    /*
    overflow: hidden;*/
}
.album_details{
    display: block;
}
.album_name{
    font-size: 22px;
    font-weight: bold;
    overflow: hidden;
    position:relative;
    height: auto;
    display: block;
    margin-top: 1%;
    margin-bottom: 1%;
    text-shadow: 2px 2px 5px rgb(168, 146, 146);
    color: rgb(54, 54, 138);
}
.album_artist{
    font-size: 18px;
    overflow: hidden;
    position:relative;
    height: auto;
    display: block;
    font-style:italic;
    margin-top: 1%;
    margin-bottom: 1%;
    text-shadow: 2px 2px 5px rgb(161, 135, 135);
    color: rgb(51, 112, 102);
}
.actions{
    display: block;
    position: relative;
    float:right;
}
.songs{
    display: block;
    position: relative;
}
.song{
    float: left;
    display: block;
    border: 3px solid black;
    margin: 5px;
    border-radius: 10px;
    padding: 3px;
}
.deleteButton{
    width: 70px;
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
.deleteButton:hover{
    background-color: rgb(0, 0, 0);
    font-weight: 600;
    color: greenyellow;
}
.updateButton{
    width: 70px;
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
.updateButton:hover{
    background-color: rgb(0, 0, 0);
    font-weight: 600;
    color: greenyellow;
}
.update{
    text-decoration: none;
    color: greenyellow;
    margin: 0;
    padding: 0;
}
.update:hover{
    color: greenyellow;
}
.addAlbum{
    color: blue;
    font-size:18px;
}
.addAlbum:hover{
    color: rgb(1, 1, 78);
    font-weight: 900;
}
.viewSongButton{
    width: 100px;
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
.viewSongButton:hover{
    background-color: rgb(0, 0, 0);
    font-weight: 600;
    color: greenyellow;
}
</style>