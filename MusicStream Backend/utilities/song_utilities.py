#---External Packages import start---
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from db.database import db
from models.models import Songs, Albums, Albums_Songs, Song_Rating
#---Internal Packages import end---

#---Utility function to get the songs from the database---
def view_songs():
    data = []
    songs = Songs.query.all()
    if songs is None:
        return None
    else:
        for song in songs:
            data_song = {'id':song.song_id,'name':song.song_name, 'lyrics':song.song_lyrics, 'genre':song.song_genre, 'duration_mins':song.song_duration_mins, 'date':str(song.song_date_created), 'album':{'id':song.album[0].album_id, 'name':song.album[0].album_name,'artist':song.album[0].album_artist}}
            data.append(data_song)
        return data

#---Utility function to insert the songs data into the database---
def insert_song(song_name, song_lyrics, song_genre, song_duration_mins, song_date_created, album_id):
    album = Albums.query.filter_by(album_id=album_id).first()
    song = Songs(song_name=song_name, song_lyrics=song_lyrics, song_genre=song_genre, song_duration_mins=song_duration_mins, song_date_created = song_date_created, album=[album])
    db.session.add(song)
    db.session.commit()

#---Utility function to fetch a song by song_id and return that song object---
def view_song_by_its_id(id):
    song = Songs.query.filter_by(song_id=id).first()
    if song is None:
        return None
    else:
        data_song = {"id":song.song_id, "name":song.song_name, "lyrics":song.song_lyrics, "genre":song.song_genre, "duration_mins":song.song_duration_mins,"date":str(song.song_date_created),"link":song.song_link,"album":{"name":song.album[0].album_name,"artist":song.album[0].album_artist}}
        return data_song
    
#---Utility function to update a song by it's id---
def update_song_by_its_id(id,song_name=None,song_lyrics=None,song_genre=None,song_duration_mins=None,song_date_created=None,album_id=None):
    song = Songs.query.filter_by(song_id=id)
    if song is None:
        return None
    else:
        if song_name is not None:
            song.update({'song_name':song_name})
        if song_lyrics is not None:
            song.update({'song_lyrics':song_lyrics})
        if song_genre is not None:
            song.update({'song_genre':song_genre})
        if song_duration_mins is not None:
            song.update({'song_duration_mins':song_duration_mins})
        if song_date_created is not None:
            song.update({'song_date_created':date.fromisoformat(song_date_created)})
        if album_id is not None:
            album = Albums.query.filter_by(album_id=album_id).first()
            song.update({'album':[album]})
        db.session.commit()
        return True
    
#---Utility function to delete a song by it's id---
def delete_song_by_its_id(id):
    song = Songs.query.filter_by(song_id=id).first()
    song.album = []
    db.session.commit()
    db.session.delete(song)
    db.session.commit()
    
#---Utility function to update the song link by searching it by it's name---
def update_song_link_by_name(name, filename):
    song = Songs.query.filter_by(song_name=name).first()
    if song is None:
        return None
    else:
        song.song_link = filename
        db.session.commit()
        return True
    
#---Utility function to add rating to the song by the user---
def add_rating_song_by_user(id, song_id, rating):
    song_rating = Song_Rating.query.filter_by(user_id=id).filter_by(song_id=song_id).first()
    if song_rating is None:
        song_rating_new = Song_Rating(song_id=song_id,user_id=id,rating=rating)
        db.session.add(song_rating_new)
        db.session.commit()
        return True
    else:
        return False
    
#---Utility function to update rating to the song by the user---
def update_rating_song_by_user(id, song_id, rating):
    song_rating = Song_Rating.query.filter_by(user_id=id).filter_by(song_id=song_id).first()
    if song_rating is None:
        return False
    else:
        Song_Rating.query.filter_by(user_id=id).filter_by(song_id=song_id).update({'rating':rating})
        db.session.commit()
        return True
    
#---Utility function to get a rating for an song by a user---
def get_rating_song_by_user(id,song_id):
    song_rating = Song_Rating.query.filter_by(user_id=id).filter_by(song_id=song_id).first()
    if song_rating is None:
        return False
    else:
        data = {"rating_id":song_rating.song_rating_id,"song_id":song_rating.song_id,"user_id":song_rating.user_id,"rating":song_rating.rating}
        return data
    
#---Utility function to delete rating for an song by a user---
def delete_rating_song_by_user(id, song_id):
    song_rating = Song_Rating.query.filter_by(user_id=id).filter_by(song_id=song_id).first()
    if song_rating is None:
        return False
    else:
        db.session.delete(song_rating)
        db.session.commit()
        return True