#   Python File for initializing the database models

#---External Packages import start---
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
#---External Packages import end---

#---Internal Packages import start---
from db.database import db
#---Internal Packages import end---

#---Creating the models for the Users Table and linking in the Roles Table via a secondary Table roles_users---
class Users(db.Model, UserMixin):
    __tablename__="Users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String,unique=True,nullable=False)
    email = db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    active = db.Column(db.Boolean,nullable=False,default=False)
    fs_uniquifier = db.Column(db.String(255), unique=True)
    remember_token = db.Column(db.String(100), unique=True)
    remember_token_expires = db.Column(db.DateTime)
    roles = db.relationship('Roles', secondary='roles_users', backref=db.backref('Users',lazy='dynamic'))
    playlists = db.relationship('Playlist', backref=db.backref('Users',cascade='all,delete'))

#---Creating the model for the Roles Table and getting it linked with the Users Table via a secondary Table roles_users---
class Roles(db.Model, RoleMixin):
    __tablename__="Roles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String(255))

#---Creating the table relation between Users table and the Roles table---
roles_users = db.Table("roles_users",
db.Column("id", db.Integer, primary_key=True),
db.Column("user_id", db.Integer, db.ForeignKey("Users.id")), 
db.Column("role_id", db.Integer, db.ForeignKey("Roles.id")))

#---Integration of Flask Security and Combining Users and Roles into a single User Datastore---
datastore = SQLAlchemyUserDatastore(db, Users, Roles)

#---Creating the model for the Album Table and linking it with the Songs table via a secondary table Album_Songs---
class Albums(db.Model):
    __tablename__="Albums"
    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_name = db.Column(db.String, nullable=False, unique=True)
    album_artist = db.Column(db.String, nullable=False)
    songs = db.relationship('Songs', secondary='Albums_Songs', backref=db.backref('Albums',lazy='dynamic',cascade='all,delete'))

#---Creating the model for the Songs Tabe and linking it with the Album table via a secondary table Album_Songs---
class Songs(db.Model):
    __tablename__="Songs"
    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_name = db.Column(db.String, nullable=False)
    song_lyrics = db.Column(db.Text, nullable=True)
    song_genre = db.Column(db.String, nullable=True)
    song_duration_mins = db.Column(db.Float, nullable=False)
    song_date_created = db.Column(db.Date, nullable=False)
    song_link = db.Column(db.String)
    album = db.relationship('Albums', secondary='Albums_Songs', backref=db.backref('Songs',lazy='dynamic',cascade='all,delete'))
    
#---Creating the table relation between Album and the Songs table---
class Albums_Songs(db.Model):
    __tablename__="Albums_Songs"
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey("Albums.album_id", ondelete='cascade'))
    song_id = db.Column(db.Integer, db.ForeignKey("Songs.song_id", ondelete='cascade'))
    
#---Creating the model for the Playlist table containing songs for a playlist---
class Playlist(db.Model):
    __tablename__="Playlist"
    playlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_name = db.Column(db.String, nullable=False)
    playlist_description = db.Column(db.String, nullable=False)
    date_created = db.Column(db.Date, nullable=False)
    created_by_user = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete='cascade'), nullable=False)
    songs = db.relationship('Songs', secondary='Playlist_Songs', backref=db.backref('Playlist',lazy='dynamic',cascade='all,delete'))

#---Creating the table for associating Playlist and Songs---
class Playlist_Songs(db.Model):
    __tablename__="Playlist_Songs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("Playlist.playlist_id", ondelete='cascade'))
    song_id = db.Column(db.Integer, db.ForeignKey("Songs.song_id", ondelete='cascade'))
    
#---Creating the table for Song Rating---
class Song_Rating(db.Model):
    __tablename__="Song_Rating"
    song_rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_id = db.Column(db.Integer, db.ForeignKey("Songs.song_id", ondelete='cascade'))
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete='cascade'))
    rating = db.Column(db.Float, nullable=True)
    
#---Creating the table for Album Rating---
class Album_Rating(db.Model):
    __tablename__='Album_Rating'
    album_rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_id = db.Column(db.Integer, db.ForeignKey("Albums.album_id", ondelete='cascade'))
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete='cascade'))
    rating = db.Column(db.Float, nullable=True)
    
    







