<template>
    <div class="nav">
        <router-link to="/admin">Admin Home</router-link>
        <router-link to="/view/users">Users</router-link>
        <router-link to="/view/album">Albums</router-link>
        <router-link to="/view/playlist">Playlist</router-link>
        <a v-on:click="logout" href="#">Logout</a>
    </div>
</template>

<script>
export default {
    name: 'AdminHeaderView',
    methods:{
        logout(){
            localStorage.clear();
            this.$router.push({name:'SignIn'});
        }
    }
}
</script>
<style>
.nav{
    background-color: rgb(72, 76, 78);
    overflow: hidden;

}
.nav a{
    float: left;
    color: whitesmoke;
    padding:14px 16px;
    text-align: center;
    font-size: 17px;
    text-decoration: none;
    margin-right: 5px;
}
.nav a:hover{
    background: #ddd;
    color: #333;
}
</style>