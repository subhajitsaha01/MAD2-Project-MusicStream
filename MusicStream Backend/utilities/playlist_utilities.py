#---External Packages import start---
#---External Packages import end---

#---Internal Packages import start---
from db.database import db
from models.models import Playlist, Playlist_Songs, Users, Songs
#---Internal Packages import end---

#---Utility function to view the list of playlist and its features---
def view_playlists():
    data = []
    playlists = Playlist.query.all()
    if playlists is None:
        return None
    else:
        for playlist in playlists:
            user = Users.query.filter_by(id=playlist.created_by_user).first()
            data_playlist = {"id":playlist.playlist_id,"name":playlist.playlist_name,"description":playlist.playlist_description,"date_created":str(playlist.date_created),"created_by_user":{"name":user.username},"songs":[]}
            for song in playlist.songs:
                data_playlist['songs'].append({"name":song.song_name, "genre":song.song_genre})
            data.append(data_playlist)
        return data
    
#---Utility function to extract the data for the playlist with it's id---
def view_playlist_by_id(id):
    playlist = Playlist.query.filter_by(playlist_id=id).first()
    if playlist is None:
        return None
    else:
        user = Users.query.filter_by(id=playlist.created_by_user).first()
        data_playlist = {"id":playlist.playlist_id,"name":playlist.playlist_name,"description":playlist.playlist_description,"date_created":str(playlist.date_created),"created_by_user":{"name":user.username},"songs":[]}
        for song in playlist.songs:
                data_playlist['songs'].append({"name":song.song_name, "genre":song.song_genre})
        return data_playlist
    
#---Utility function to update the name and description of a playlist by it's id---
def update_playlist_by_id(id,playlist_name=None, playlist_description=None):
    if playlist_name is not None and playlist_description is not None:
        Playlist.query.filter_by(playlist_id=id).update({'playlist_name':playlist_name,'playlist_description':playlist_description})
    if playlist_name is not None and playlist_description is None:
        Playlist.query.filter_by(playlist_id=id).update({'playlist_name':playlist_name})
    elif playlist_description is not None and playlist_name is None:
        Playlist.query.filter_by(playlist_id=id).update({'playlist_description':playlist_description})
    db.session.commit()
    
#---Utility function to delete a playlist by it's id---
def delete_playlist_by_id(id):
    playlist = Playlist.query.filter_by(playlist_id=id).first()
    playlist.songs = []
    playlist.created_by_user=0
    db.session.commit()
    db.session.delete(playlist)
    db.session.commit()
    
#---Utility function to add a song w.r.t. id to a playlist w.r.t. id---
def add_song_to_playlist(playlist_id, song_id):
    playlist = Playlist.query.filter_by(playlist_id=playlist_id).first()
    song = Songs.query.filter_by(song_id=song_id).first()
    if playlist is None or song is None:
        return None
    else:
        if song in playlist.songs:
            return False
        else:
            playlist.songs.append(song)
            db.session.commit()
            return True

#---Utility function to delete a song w.r.t id from a playlist w.r.t. id---
def delete_song_from_playlist(playlist_id, song_id):
    flag=0
    playlist = Playlist.query.filter_by(playlist_id=playlist_id).first()
    song = Songs.query.filter_by(song_id=song_id).first()
    if playlist is not None and song is not None:    
        for song_ind in playlist.songs:
            if song.song_id==song_ind.song_id:
                playlist.songs.remove(song)
                db.session.commit()
                flag=1
        if flag==1:
            return True
        else:
            return False
    else:
        return None