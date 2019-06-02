import sys
import requests


class Deezer:

    def __init__(self, auth=None, credentials_manager=None):
        self.base_url = "https://api.deezer.com/"
        self._auth = auth
        self.credentials_manager = credentials_manager

# ------------------- GET Methods ------------------------------------

    def get_album(self, album_id, method=""):
        """
        Retrieve information about an album
        :param album_id: ID or URL of the album
        :param method: Allows to access information related to the album such as :
                       - 'fans',
                       - 'comments'
                       - 'tracks'
        """
        albid = self._get_id("album", album_id)
        album = self._get(f"album/{albid}/{method}")
        return album

    def get_artist(self, artist_id, method=""):
        """
        Information about a given artist
        :param artist_id: ID or URL of the artist
        :param method: To access further information related to artist:
                        - 'albums'
                        - 'comments'
                        - 'fans'
                        - 'playlists'
                        - 'radio'
                        - 'related'
                        - 'top'
        """
        artid = self._get_id("artist", artist_id)
        artist = self._get(f"artist/{artid}/{method}")
        return artist

    def get_chart(self, ty):
        """
        Retrieve the top 10 items in the category provided.
        :param ty: type of chart to retrieve. Params can be:
                -'tracks'
                -'albums'
                -'artists'
                -'playlists'
                -'podcasts'
        """
        chart = self._get(f"chart/0/{ty}")
        return chart

    def get_comment(self, comment_id):
        """
        Get a comment
        :param comment_id: ID of the comment
        """
        comment = self._get(f"comment/{comment_id}")
        return comment

    def get_editorial(self, method=""):
        """
        :param method: Editorial methods accepted:
                        'selection': Return a list of albums selected every week by the Deezer Team
                        'charts': Return four lists: Top track, Top album, Top artist and Top playlist
                        'releases': This method returns the new releases per genre for the current country
        """
        if method == "":
            editorial = self._get(f"editorial")
        else:
            editorial = self._get(f"editorial/0/{method}")
        return editorial

    def get_episode(self, episode_id):
        """
        :param episode_id: ID or URL of the episode
        """
        epid = self._get_id("episode", episode_id)
        return self._get(f"episode/{epid}")

    def get_all_genres(self):
        """
        Retrieve information about all genres available
        """
        return self._get("genre")

    def get_genre_details(self, id, method=""):
        """
        Retrieve further details of a given genre by the ID or name provided.
        :param id: Genre's ID
        :param method: Retrieve details of genre's 'artists', 'podcasts', or 'radios'
        """
        return self._get(f"genre/{id}/{method}")

    def get_infos(self):
        """
        Get information about the API in the current country
        """
        return self._get("infos")

    def get_me(self, method=""):
        """
        Get information about the current user.
        :param method: Me methods accepted:
                'albums': Return a list of user's favorite albums
                'artists': Return a list of user's favorite artists
                'flow': Returns a list of user's flow tracks
                'folders': Return a list of user's Folder
                'followings': Return a list of user's Friends
                'followers': Return a list of user's followers
                'history': Returns a list of the recently played tracks
                'permissions': Return the user's Permissions granted to the application
                'options': Return user's options
                'personal_songs': Return a list of user's personal song
                'playlists': Return a list of user's public Playlist. Permission is needed to return private playlists
                'podcasts': Return a list of user's favorite podcasts
                'radios': Return a list of user's favorite Radio
                'recommendations':
                    -'/albums': Return a list of albums recommendations
                    -'/artists': Return a list of artists recommendations
                    -'/playlists': Return a list of playlists recommendations
                    -'/tracks': Return a list of tracks recommendations
                    -'/radios': Return a list of radios recommendation
                'tracks': Return a list of user's favorite tracks
        """
        if method == "":
            user = self._get("user/me")
        else:
            user = self._get(f"user/me/{method}")
        return user

    def get_me_top_tracks(self):
        """
        Retrieve information about the current user's top tracks.
        It will retrieve the top 25 tracks
        """
        return self._get("user/me/charts/tracks")

    def get_me_top_albums(self):
        """
        Retrieve information about the current user's top albums
        """
        return self._get("user/me/charts/albums")

    def get_me_top_playlists(self):
        """
        Retrieve information about the current user's top playlists
        """
        return self._get("user/me/charts/playlists")

    def get_me_top_artists(self):
        """
        Fetch information about the current user's top artists
        """
        return self._get("user/me/charts/artists")

    def get_options(self):
        """
        Get the user's options
        """
        return self._get("options")

    def get_playlist(self, playlist_id, method=""):
        """
        Return information about a playlist
        :param playlist_id: ID or URL
        :param method: Playlist's methods accepted:
                        'comments': Return a list of playlist's comments
                        'fans': Return a list of playlist's fans
                        'tracks': Return a list of playlist's tracks
                        'radio': Return a list of playlist's recommendation tracks
        """
        playid = self._get_id("playlist", playlist_id)
        playlist = self._get(f"playlist/{playid}/{method}")
        return playlist

    def get_podcast(self, show_id, method=""):
        """
        Information regarding a show
        :param show_id: ID or URL
        :param method: Podcast accepted methods:
                        'episodes': Return the list of episodes about the podcast
        """
        showid = self._get_id("podcast", show_id)
        show = self._get(f"podcast/{showid}/{method}")
        return show

    def get_track(self, track_id):
        """
        Information related to a track
        :param track_id: ID or URL
        """
        trid = self._get_id("track", track_id)
        track = self._get(f"track/{trid}")
        return track

    def get_user(self, user_id):
        """
        Information related to a user
        :param user_id: ID or URL
        """
        userid = self._get_id("user", user_id)
        user = self._get(f"user/{userid}")
        return user

# -------------- Search -------------------------------------------------------
    def search(self, keyword, method=""):
        """
        Information related to the given keyword. Using a method helps to narrow down the search
        and, therefore obtain more accurate results.
        :param keyword: keyword for searching related content. Spaces are allowed.
        :param method: Search methods accepted:
                        'album': Search albums
                        'artist': Search artists
                        'history': Get user search history. Authentication token is needed
                        'playlist': Search playlists
                        'podcast': Search podcasts
                        'radio': Search radio
                        'track': Search tracks
                        'user': Search users
        """
        if method == "":
            results = self._get(f"search?q={keyword}")
        else:
            results = self._get(f"search/{method}?q={keyword}")
        return results

    def advanced_search(self, params):
        """
        Advanced search to find artists, albums or tracks
        :param params: Search parameters. Must be a dictionary
        """
        if isinstance(params, dict):
            query = " ".join(f"{key}:'{value}'" for key, value in params.items())
            result = self._get(f"search?q={query}")
            return result
        else:
            self._warn_message("Please revise your search parameters. A dictionary must be used.")

    def next(self, response):
        """
        Retrieve the next section of the data, if any
        :param response: previous response from the API
        """
        if response.get("next"):
            return self._get(response["next"])
        else:
            return None

# -------------- Create/Edit Methods (POST) -----------------------------------

    def follow_playlist(self, user_id, playlist_id):
        """
        Add a playlist to the user's favorite
        :param user_id: ID or URL
        :param playlist_id: ID or URL
        """
        userid = self._get_id("user", user_id)
        plistid = self._get_id("playlist", playlist_id)
        operation = self._post(f"user/{userid}/playlists", "playlist_id", plistid)
        return operation

    def follow_podcast(self, user_id, podcast_id):
        """
        Add a podcast to the user's favorite
        :param user_id: ID or URL
        :param podcast_id:  ID or URL
        """
        userid = self._get_id("user", user_id)
        pdcastid = self._get_id("show", podcast_id)
        operation = self._post(f"user/{userid}/podcasts", "podcast_id", pdcastid)
        return operation

    def follow_album(self, user_id, album_id):
        """
        Add a album to the user's library
        :param user_id: ID or URL
        :param album_id:  list of albums IDs or URLs
        """
        userid = self._get_id("user", user_id)
        albid = self._get_id("album", album_id)
        return self._post(f"user/{userid}/albums", "album_id", albid)

    def follow_artist(self, user_id, artist_id):
        """
        Add an artist to the user's library
        :param user_id: ID or URL
        :param artist_id: list of artists IDs or URLs
        """
        userid = self._get_id("user", user_id)
        artid = self._get_id("artist", artist_id)
        return self._post(f"user/{userid}/artists", "artist_id", artid)

    def follow_user(self, user_id, user_to_follow):
        """
        Follow an user
        :param user_id: ID or URL
        :param user_to_follow: ID or URL
        """
        userid = self._get_id("user", user_id)
        userfollowid = self._get_id("user", user_to_follow)
        return self._post(f"user/{userid}/followings", "user_id", userfollowid)

    def user_post_notification(self, user_id, message):
        """
        Post a notification in the user feed
        :param user_id: ID or URL
        :param message: string with the content of the notification
        """
        userid = self._get_id("user", user_id)
        return self._post(f"user/{userid}/notifications", "message", message)

    def create_folder(self, user_id, title):
        """
        Create a folder
        :param user_id: ID or URL
        :param title: The title of the new folder
        """
        userid = self._get_id("user", user_id)
        return self._post(f"user/{userid}/folders", "title", title)

    def create_playlist(self, user_id, title):
        """
        Create a playlist
        :param user_id: ID or URL
        :param title: Title of the new playlist
        """
        userid = self._get_id("user", user_id)
        return self._post(f"user/{userid}/playlists", "title", title)

    def add_track_favorite(self, user_id, track_id):
        """
        Add a track to the user's favorites
        :param user_id: ID or URL
        :param track_id: ID or URL
        """
        userid = self._get_id("user", user_id)
        trackid = self._get_id("track", track_id)
        return self._post(f"user/{userid}/tracks", "track_id", trackid)

# <-------------------------- Delete Methods ----------------------------->

    def delete_playlist(self, playlist_id):
        """
        Delete the playlist
        :param playlist_id: ID or URL
        """
        plistid = self._get_id("playlist", playlist_id)
        return self._delete(f"user/me/playlists", "playlist_id", plistid)

    def delete_tracks_from_playlist(self, playlist_id, tracks_ids):
        """
        Remove tracks from the playlist
        :param playlist_id: ID or URL
        :param tracks_ids: A comma separated list of track IDs or URLS
        """
        plistid = self._get_id("playlist", playlist_id)
        ids = []
        for track in tracks_ids:
            ids.append(self._get_id("track", track))
        return self._delete(f"playlist/{plistid}/tracks", "songs", ids)

    def delete_comment(self, comment_id):
        """
        Remove a comment
        :param comment_id: ID
        """
        cmmtid = self._get_id("comment", comment_id)
        return self._delete(f"comment/{cmmtid}")

    def delete_album(self, album_id):
        """
        Remove an album from the user's library
        :param album_id: ID or URL
        """
        albid = self._get_id("album", album_id)
        return self._delete(f"user/me/albums", "album_id", albid)

    def delete_artist(self, artist_id):
        """
        Remove an artist from the user's favourites
        :param artist_id: ID or URL
        """
        artid = self._get_id("artist", artist_id)
        return self._delete(f"user/me/artists", "artist_id", artid)

    def unfollow_user(self, user_id):
        """
        Unfollow an user
        :param user_id: ID or URL
        """
        userid = self._get_id("profile", user_id)
        return self._delete(f"user/me/followings", "user_id", userid)

    def delete_podcast(self, podcast_id):
        """
        Remove a podcast from the user's favorite
        :param podcast_id: ID or URL
        """
        podid = self._get_id("show", podcast_id)
        return self._delete(f"user/me/podcasts", "podcast_id", podid)

    def delete_favorite_track(self, track_id):
        """
        Remove a track from the user's favorites
        :param track_id: ID or URL
        """
        trackid = self._get_id("track", track_id)
        return self._delete(f"user/me/tracks", "track_id", trackid)

    def delete_folder(self, folder_id):
        """
        Delete a folder
        :param folder_id: ID
        """
        return self._delete(f"folder/{folder_id}")

    def delete_playlist_from_folder(self, folder_id, playlist_id):
        """
        Remove a playlist from a folder
        :param folder_id: ID or URL
        :param playlist_id: ID or URL
        """
        fldid = self._get_id("folder", folder_id)
        plid = self._get_id("playlist", playlist_id)
        return self._delete(f"folder/{fldid}/items", "playlist_id", plid)

    def delete_album_from_folder(self, folder_id, album_id):
        """
        Remove an album from a folder
        :param folder_id: ID or URL
        :param album_id: ID or URL
        """
        fldid = self._get_id("folder", folder_id)
        albid = self._get_id("album", album_id)
        return self._delete(f"folder/{fldid}/items", "album_id", albid)

# --------------------- Private Methods -------------------------------

    def _auth_headers(self):
        if self._auth:
            return {"access_token": self._auth}
        elif self.credentials_manager:
            return {"access_token": self.credentials_manager.token}
        else:
            token = self.credentials_manager.get_access_token()
            return {"access_token": token}

    def _get_id(self, type, id):
        fields = id.split("/")
        if len(fields) >= 3:
            if type != fields[-2]:
                self._warn_message(f"Expecting '{type}', found '{fields[-2]}' instead. ")
            return fields[-1]
        return id

    def _get(self, url):
        result = self._call("GET", url)
        return result

    def _post(self, url, param, id):
        result = self._call("POST", url, param, id)
        return result

    def _delete(self, url, param=None, id=None):
        result = self._call("DELETE", url, param, id)
        return result

    def _call(self, call_method, url, param=None, id=None):
        if not url.startswith("http"):
            url = self.base_url + url

        if self._auth or self.credentials_manager:
            headers = self._auth_headers()
            if param and id:
                headers[f"{param}"] = id
                result = requests.request(call_method, url, params=headers)
            else:
                result = requests.request(call_method, url, params=headers)
        else:
            result = requests.request(call_method, url)

        result = result.json()

        try:
            if "error" in result:
                ty = result["error"]["type"]
                message = result["error"]["message"]
                code = result["error"]["code"]
                return DeezerException(ty, message, code)
        except:
            pass
        return result

    def _warn_message(self, message):
        print(f"warning: {message}", file=sys.stderr)


class DeezerException(Exception):

    def __init__(self, ty, message, code):
        self.type = ty
        self.msg = message
        self.code = code

    def __str__(self):
        return f"An error has occurred:\n{self.type}\n{self.msg}\nCode: {self.code}"

