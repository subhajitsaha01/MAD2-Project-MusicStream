#---External Packages import start---
from flask import send_from_directory
#---External Packages import end---

#---Internal Packages import start---
from db.database import db
from models.models import Albums, Albums_Songs, Album_Rating
#---Internal Packages import end---

#---Utility function to check whether album name exists in the db or not---
def album_name_exists(name):
    album = Albums.query.filter_by(album_name=name).first()
    if not album:
        return False
    else:
        return True

#--Utility function to add an album into the database Table Albums---
def insert_album(name,artist):
    album = Albums(album_name=name, album_artist=artist)
    db.session.add(album)
    db.session.commit()

#---Utility function to view the list of albums and its features---
def view_albums():
    data = []
    albums = Albums.query.all()
    if albums is None:
        return None
    else:
        for album in albums:
            data_album = {"id":album.album_id, "album_name":album.album_name,"album_artist":album.album_artist, "album_songs":[]}
            for song in album.songs:
                data_album['album_songs'].append({"id":song.song_id,"song_name":song.song_name})
            data.append(data_album)
        return data
    
#---Utility function to view an album by it's id---
def view_album_by_id(id):
    album = Albums.query.filter_by(album_id=id).first()
    if album is None:
        return None
    else:
        data_album = {"id":album.album_id, "album_name":album.album_name,"album_artist":album.album_artist, "album_songs":[]}
        for song in album.songs:
            data_album['album_songs'].append({"id":song.song_id,"song_name":song.song_name})
        return data_album
    
#---Utility function to update the album data by it's id---
def update_album_data(id,album_name=None,album_artist=None):
    if album_name is not None and album_artist is not None:
        Albums.query.filter_by(album_id=id).update({'album_name':album_name,'album_artist':album_artist})
    if album_name is not None and album_artist is None:
        Albums.query.filter_by(album_id=id).update({'album_name':album_name})
    elif album_artist is not None and album_name is None:
        Albums.query.filter_by(album_id=id).update({'album_artist':album_artist})
    db.session.commit()

#---Utility function to delete the album data by it's id---
def delete_album_by_its_id(id):
    album = Albums.query.filter_by(album_id=id).first()
    songs = album.songs
    album.songs = []
    db.session.commit()
    db.session.delete(album)
    for song in songs:
        db.session.delete(song)
    db.session.commit()
    
#---Utility function to get the songs by album id---
def get_songs_by_album(id):
    album = Albums.query.filter_by(album_id=id).first()
    if album is None:
        return None
    else:
        songs = []
        for song in album.songs:
            songs.append({"id":song.song_id,"name":song.song_name,"lyrics":song.song_lyrics,"genre":song.song_genre,"duration":song.song_duration_mins,"date_created":str(song.song_date_created),"link":song.song_link})
        return songs, album.album_name
    
#---Utility function to add a rating for an album by a user---
def add_rating_album_by_user(id, album_id, rating):
    album_rating = Album_Rating.query.filter_by(user_id=id).filter_by(album_id=album_id).first()
    if album_rating is None:
        album_rating_new = Album_Rating(album_id=album_id,user_id=id,rating=rating)
        db.session.add(album_rating_new)
        db.session.commit()
        return True
    else:
        return False
    
#---Utility function to get a rating for an album by a user---
def get_rating_album_by_user(id,album_id):
    album_rating = Album_Rating.query.filter_by(user_id=id).filter_by(album_id=album_id).first()
    if album_rating is None:
        return False
    else:
        data = {"rating_id":album_rating.album_rating_id,"album_id":album_rating.album_id,"user_id":album_rating.user_id,"rating":album_rating.rating}
        return data
    
#---Utility function to update rating for an album by a user---
def update_rating_album_by_user(id, album_id, rating):
    album_rating = Album_Rating.query.filter_by(user_id=id).filter_by(album_id=album_id).first()
    if album_rating is None:
        return False
    else:
        Album_Rating.query.filter_by(user_id=id).filter_by(album_id=album_id).update({'rating':rating})
        db.session.commit()
        return True
    
#---Utility function to delete rating for an album by a user---
def delete_rating_album_by_user(id, album_id):
    album_rating = Album_Rating.query.filter_by(user_id=id).filter_by(album_id=album_id).first()
    if album_rating is None:
        return False
    else:
        db.session.delete(album_rating)
        db.session.commit()
        return True