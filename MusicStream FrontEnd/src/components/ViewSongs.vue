<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome to Songs Page of <i>{{ album_name }}</i> Album</h1>
    <div class="parent">
        <div class="header">Songs</div>
        <router-link :to="'/add/song/album/'+album_id" class="addSong">Add Song</router-link>
        <div class="song_check" v-for="item in song.songs" :key="item.id">
            <div class="songs_details">
                <div class="songs_name">{{ item.name }}</div>
                <div class="songs_artist">{{ item.genre }}</div>
                <div class="song_duration">{{ item.duration }} minutes</div>
                <p class="song_lyrics">{{ item.lyrics }}</p>
                <audio controls :id="item.id" v-on:mouseover="loadSong(item.link,item.id)"></audio>
            </div>
            <div class="songs">
                <div class="actions">
                    <button class="updateButton"><router-link :to="'/update/song/'+item.id" class="update">Update</router-link></button>
                    <button class="deleteButton" v-on:click="deleteSong(item.id)" type="button">Delete</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import AdminHeaderView from './AdminHeaderView.vue';
export default {
    name: 'ViewSongs',
    data(){
        return {
            album_name: '',
            name: '',
            song: [],
            srcEx: '',
            album_id: ''
        }
    },
    methods:{
        async deleteSong(id){
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
                axios.delete("http://127.0.0.1:5000/music_stream/api/song/"+id, {params:myparams})
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
        async loadSong(songFilename,id){
            let user = localStorage.getItem('user-info')
            if(!user){
                this.$router.push({name: 'SignIn'}); 
            }
            else{
                this.name = JSON.parse(user).username;
            }
            const myparams = {
                'auth_token':JSON.parse(user).token,
                responseType: 'blob'
            }
            let ele = document.getElementById(id)
            // try{
            // let response = await axios.get("http://127.0.0.1:5000/music_stream/api/listen/song/"+songFilename, {params:myparams})
            // console.log(response)
            // const buffer = await response.arrayBuffer();
            // const audioBlob = new Blob([buffer], {type: 'audio/mpeg'})
            ele.src = "http://127.0.0.1:5000/music_stream/api/listen/song/"+songFilename+"?auth_token="+myparams['auth_token']
            // }
            // catch(error){
            //     console.log("axios error"+error);
            // }
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
                let songs = await axios.get("http://127.0.0.1:5000/music_stream/api/album/songs/"+this.$route.params.id, {params:myparams})
                console.log(songs)
                this.song = songs.data;
                this.album_name = songs.data.name
                console.log(this.song)
                this.album_id = this.$route.params.id
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
    border-radius: 10px;
    border-style: outset;    
}
.header{
    margin: 15px;
    font-size: 40px;
    font-weight: 900;
    text-shadow: 4px 4px 10px rgb(148, 118, 118);
}
.song_check{
    border: 4px solid black;
    margin: 1%;
    padding: 5px;
    border-radius: 5px;
    position:relative;
    height: auto;
    display: inline-block;
    width: 95%;
    /*
    overflow: hidden;*/
    box-shadow: 0px 0px 10px rgb(29, 27, 31);
    background-color: rgb(234, 241, 241);
}
.songs_details{
    display: block;
}
.songs_name{
    font-size: 25px;
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
.songs_artist{
    font-size: 20px;
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
.song_lyrics{
    background-color: rgb(204, 219, 250);
    padding: 25px;
    margin: 30px;
    border-radius:20px;
    font-size: 17px;
}
audio{
    width: 50%;
    border: 2px solid rgb(25, 25, 92);
    border-radius: 20px;
}
.song_duration{
    font-style: italic;
    font-weight: 600;
    font-size: 15px;
}
.addSong{
    font-size: 20px;
}
</style>