<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome to Update Song Page</h1>
    <form class="addSong">
        <input type="text" name="name" placeholder="Enter Song Name" v-model="Song.name">
        <input type="text" name="genre" placeholder="Enter Song Genre" v-model="Song.genre">
        <input type="number" name="duration" placeholder="Enter Song Duration" v-model="Song.duration">
        <textarea name="lyrics" placeholder="Enter Song Lyrics" v-model="Song.lyrics" rows="10"></textarea>
        <label for="creation_date">Enter Song Creation Date</label>
        <input type="date" name="creation_date" id="creation_date" v-model="Song.date">
        <audio controls :id="Song.id" v-on:mouseover.once="loadSong(Song.link,Song.id)"></audio>
        <input type="file" id="audioFile" name="audioFile" @change="handleFileUpload" accept=".mp3,audio/*">
        <button v-on:click="updateSong" type="button">Update Song</button>
        <input type="reset" value="Reset"/>
    </form>
</template>
<script>
import axios from 'axios';
import AdminHeaderView from './AdminHeaderView.vue';
export default {
    name: 'UpdateSong',
    data(){
        return {
            name: '',
            user: '',
            Song: {
                id:'',
                name:'',
                genre:'',
                duration: '',
                lyrics: '',
                date: '',
                file: null,
                link:''
            }
        }
    },
    methods:{
        handleFileUpload(event){
            this.Song.file = event.target.files[0]
            console.log(this.Song.file)
        },
        updateSong(){
            console.log(this.Song.name, this.Song.genre, this.Song.duration, this.Song.lyrics, this.Song.date);
            const myparams = {
            'auth_token':this.user.token
            }
            //console.log(myparams)
            axios.put("http://127.0.0.1:5000/music_stream/api/song/"+this.$route.params.id, {
                    "name": this.Song.name,
                    "lyrics":this.Song.lyrics,
                    "genre":this.Song.genre,
                    "duration_mins":this.Song.duration,
                    "date":this.Song.date
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
            formData.append('audioFile',this.Song.file)
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
                if(error.response.status !== 400){
                    alert(error.response.data.message)
                }
            })
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
        }
    },
    components:{
        AdminHeaderView
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
        axios.get('http://127.0.0.1:5000/music_stream/api/song/'+this.$route.params.id, {params:myparams})
        .then((response) => {
            console.log(response)
            this.Song.id = response.data.id
            this.Song.name = response.data.name
            this.Song.lyrics = response.data.lyrics
            this.Song.genre = response.data.genre
            this.Song.duration = response.data.duration_mins
            this.Song.date = response.data.date
            this.Song.link = response.data.link
        })
        .catch((error) => {
            if(error.response.status === 400){
                alert(error.response.data.message);
            }
        })
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
