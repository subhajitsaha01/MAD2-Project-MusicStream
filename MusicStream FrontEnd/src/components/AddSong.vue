<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome to Add Song Page</h1>
    <form class="addSong">
        <input type="text" name="name" placeholder="Enter Song Name" v-model="Song.name">
        <input type="text" name="genre" placeholder="Enter Song Genre" v-model="Song.genre">
        <input type="number" name="duration" placeholder="Enter Song Duration" v-model="Song.duration">
        <textarea name="lyrics" placeholder="Enter Song Lyrics" v-model="Song.lyrics" rows="10"></textarea>
        <label for="creation_date">Enter Song Creation Date</label>
        <input type="date" name="creation_date" id="creation_date" v-model="Song.date">
        <input type="file" id="audioFile" name="audioFile" @change="handleFileUpload" accept=".mp3,audio/*">
        <button v-on:click="addSong" type="button">Add Song</button>
        <input type="reset" value="Reset"/>
    </form>
</template>
<script>
import axios from 'axios';
import AdminHeaderView from './AdminHeaderView.vue';
export default {
    name: 'AddSong',
    data(){
        return {
            name: '',
            user: '',
            Song: {
                name:'',
                genre:'',
                duration: '',
                lyrics: '',
                date: '',
                file: null
            }
        }
    },
    methods:{
        handleFileUpload(event){
            this.file = event.target.files[0]
            console.log(this.file)
        },
        addSong(){
            console.log(this.Song.name, this.Song.genre, this.Song.duration, this.Song.lyrics, this.Song.date);
            const myparams = {
            'auth_token':this.user.token
            }
            //console.log(myparams)
            axios.post("http://127.0.0.1:5000/music_stream/api/songs", {
                    "name": this.Song.name,
                    "lyrics":this.Song.lyrics,
                    "genre":this.Song.genre,
                    "duration_mins":this.Song.duration,
                    "date":this.Song.date,
                    "album_id":this.$route.params.id
            }, {params: myparams})
            .then((response) => {
                console.log(response)
                alert(response.data.message)
            }).catch((error) => {
                if(error.response.status === 400){
                    alert(error.response.data.message);
                }
            })
            const formData = new FormData()
            formData.append('audioFile',this.file)
            formData.append('name',this.Song.name)
            // const myparams_new = {
            //     'auth_token':this.user.token
            // }
            axios.post(`http://127.0.0.1:5000/music_stream/api/upload/song?auth_token=${this.user.token}`,formData, {
                headers:{
                    'Content-Type':'multipart/form-data'
                },
                responseType: 'text'})
            .then((response)=> {
                console.log(response)
                alert(response.data.message)
            })
            .catch((error) => {
                if(error.response.status === 400){
                    alert(error.response.data.message)
                }
            })
            this.Song.name = ''
            this.Song.genre = ''
            this.Song.duration = ''
            this.Song.lyrics = ''
            this.Song.date = ''
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
.addSong input[type=text],input[type=date]{
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
.addSong input[type=file]{
    width: 300px;
    height: 30px;
    padding-left: 20px;
    display:block;
    margin-bottom: 30px;
    margin-left: auto;
    margin-right: auto;
    font-size: 18px;
}
.addSong input[type=number]{
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
.addSong textarea{
    width: 300px;
    padding-left: 20px;
    display:block;
    margin-bottom: 30px;
    margin-left: auto;
    margin-right: auto;
    border: 3px solid rgb(72, 76, 78);
    border-radius: 10px;
    font-size: 15px;
}
.addSong button{
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
.addSong button:hover{
    background: rgb(137, 142, 145);
}
</style>
