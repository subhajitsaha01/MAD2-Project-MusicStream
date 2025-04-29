import AdminHomeView from './components/AdminHomeView.vue';
import UserSignUp from './components/UserSignUp.vue';
import UserSignIn from './components/UserSignIn.vue';
import { createRouter, createWebHistory } from 'vue-router';
import AddAlbum from './components/AddAlbum.vue';
import UpdateAlbum from './components/UpdateAlbum.vue';
import ViewAlbum from './components/ViewAlbums.vue';
import ViewUsers from './components/ViewUsers.vue';
import UpdateUser from './components/UpdateUser.vue';
import ViewSongs from './components/ViewSongs.vue';
import AddSong from './components/AddSong.vue';
import UpdateSong from './components/UpdateSong.vue';
import ViewPlaylist from './components/ViewPlaylist.vue';

const routes = [
    {
        name: 'AdminHome',
        component: AdminHomeView,
        path: '/admin'
    },
    {
        name: 'SignUp',
        component: UserSignUp,
        path: '/signup'
    },
    {
        name: 'SignIn',
        component: UserSignIn,
        path: '/signin'
    },
    {
        name: 'AddAlbum',
        component: AddAlbum,
        path: '/add/album'
    },
    {
        name: 'UpdateAlbum',
        component: UpdateAlbum,
        path: '/update/album/:id'
    },
    {
        name: 'ViewAlbum',
        component: ViewAlbum,
        path: '/view/album'
    },
    {
        name: 'ViewUsers',
        component: ViewUsers,
        path: '/view/users'
    },
    {
        name:'UpdateUser',
        component: UpdateUser,
        path: '/update/user/:id'
    },
    {
        name:'ViewSongs',
        component: ViewSongs,
        path: '/view/album/songs/:id'
    },
    {
        name:'AddSong',
        component: AddSong,
        path: '/add/song/album/:id'
    },
    {
        name:'UpdateSong',
        component: UpdateSong,
        path: '/update/song/:id'
    },
    {
        name:'ViewPlaylist',
        component: ViewPlaylist,
        path: '/view/playlist'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;