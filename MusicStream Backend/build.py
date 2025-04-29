#   Python File for building the resources of the application - Initializing databases, api resources

#---External Packages import start---
from flask import Flask, request
from flask_security import Security, auth_required, logout_user, current_user
from flask_restful import Api
from datetime import datetime, timedelta
from flask_cors import CORS
#---External Packages import end---

#---Internal Packages import start---
from application.configuration import appConfig
from db.database import db
from models.models import datastore
from resources.user_register_resource import UserRegistrationApi
from resources.user_login_resource import UserLoginApi
from resources.user_activation_resource import UserActivationApi
from resources.user_deactivation_resource import UserDeactivationApi
from resources.creator_register_resource import CreatorRegistrationApi
from resources.user_logout_resource import UserLogoutApi
from resources.creator_user_profile_resource import CreatorUserProfileApi
from resources.general_user_profile_resource import GeneralUserProfileApi
from resources.albums_resource import AlbumsApi
from resources.album_individual_resource import AlbumIndividualApi
from resources.songs_resource import SongsApi
from resources.song_individual_resource import SongsIndividualApi
from resources.playlist_resource import PlaylistApi
from resources.playlist_individual_resource import PlaylistIndividualApi
from resources.playlist_song_individual_resource import PlaylistSongIndividualApi
from resources.users_resource import UsersApi
from resources.user_individual_resource import UsersIndividualApi
from resources.album_song_individual_resource import AlbumSongIndividualApi
from resources.listen_song import SongsListenApi
#from resources.upload_song import SongsUploadApi
from resources.user_album_rating_resource import AlbumRating
#---Internal Packages import end---

#---Flask App initialization Beginning---
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(appConfig)
    db.init_app(app)
    api = Api(app,prefix='/music_stream/api')
    app.app_context().push()

    #   integration of flask security
    app.security = Security(app, datastore)

    #   Creating the database and initializing the tables inside the database
    with app.app_context():
        db.create_all()

    return app, api
#---Flask App Initialization Ending---

#---Configuring the resources and building the app---
app, api = create_app()

#---API Resources Configuration---
api.add_resource(UserRegistrationApi, "/user-register")
api.add_resource(UserLoginApi, "/user-login")
api.add_resource(UserActivationApi, "/user-activate/<int:id>")
api.add_resource(UserDeactivationApi, "/user-deactivate/<int:id>")
api.add_resource(UsersApi, "/users")
api.add_resource(UsersIndividualApi, "/user/<int:id>")
api.add_resource(CreatorRegistrationApi, "/creator-register")
api.add_resource(UserLogoutApi, "/user-logout")
api.add_resource(CreatorUserProfileApi, '/creator-profile/<int:id>')
api.add_resource(GeneralUserProfileApi, '/general-user-profile/<int:id>')

api.add_resource(AlbumsApi, '/albums')
api.add_resource(AlbumIndividualApi, '/album/<int:id>')
api.add_resource(SongsApi, '/songs')
api.add_resource(SongsIndividualApi, '/song/<int:id>')
api.add_resource(AlbumSongIndividualApi, '/album/songs/<int:id>')
api.add_resource(SongsListenApi, '/listen/song/<filename>')
#api.add_resource(SongsUploadApi, '/upload/song')

api.add_resource(PlaylistApi, '/playlists')
api.add_resource(PlaylistIndividualApi, '/playlist/<int:id>')
api.add_resource(PlaylistSongIndividualApi, '/playlist/<int:playlist_id>/song/<int:song_id>')

api.add_resource(AlbumRating, '/user/<int:id>/album/<int:album_id>')