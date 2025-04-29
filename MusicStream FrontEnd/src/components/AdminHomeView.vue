<template>
    <AdminHeaderView />
    <h1>Hello {{ name }}, Welcome on Music-Stream App</h1>
</template>
<script>
import AdminHeaderView from './AdminHeaderView.vue';
export default {
    name: 'AdminHomeView',
    data(){
        return {
            name: ''
        }
    },
    components:{
        AdminHeaderView
    },
    mounted(){
        let user = localStorage.getItem('user-info');
        this.name = JSON.parse(user).username;
        if(!user){
            this.$router.push({name: 'SignIn'}); 
        }
    }
}
</script>