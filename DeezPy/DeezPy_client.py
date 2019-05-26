import sys
import requests


class Deezer:

    def __init__(self, auth=None, client_credentials_manager=None):
        self.base_url = "https://api.deezer.com/"
        self._auth = auth
        self.client_credentials_manager = client_credentials_manager

    def get_album(self, album_id, method=""):
        """
        Retrieve information about an album
        :param album_id: ID or URL of the album
        :param kwargs: Allows to access information related to the album such as :
                       - 'fans',
                       - 'comments'
                       - 'tracks'
        :return: response from the API
        """
        albid = self._get_id("album", album_id)
        album = self._get(f"album/{albid}/{method}")
        return album

    def get_artist(self, artist_id, method=""):
        """
        :param artist_id: ID or URL of the artist
        :param **kwargs: To access further information related to artist:
                        - 'albums'
                        - 'comments'
                        - 'fans'
                        - 'playlists'
                        - 'radio'
                        - 'related'
                        - 'top'
        :return: response from the API
        """
        artid = self._get_id("artist", artist_id)
        artist = self._get(f"artist/{artid}/{method}")
        return artist

    def get_chart(self, type):
        """
        Retrieve the top 10 items in the category provided.
        :param type: chart to retrieve. Params can be:
                -'tracks'
                -'albums'
                -'artists'
                -'playlists'
                -'podcasts'
        :return: Depends on the category provided. (See above)
        """
        chart = self._get(f"chart/0/{type}")
        return chart

    def get_comment(self, comment_id):
        """
        Retrieve informatio 
        :param comment_id: ID of the comment
        :return: Information regarding the comment
        """
        comment = self._get(f"comment/{comment_id}")
        return comment

    def get_editorial(self, method=""):
        """

        :param method: Editorial methods accepted:
                        'selection': Return a list of albums selected every week by the Deezer Team
                        'charts': Return four lists: Top track, Top album, Top artist and Top playlist
                        'releases': This method returns the new releases per genre for the current country
        :return:
        """
        if method == "":
            editorial = self._get(f"editorial")
        else:
            editorial = self._get(f"editorial/0/{method}")
        return editorial

    def get_episode(self, episode_id):
        """
        :param episode_id: ID or URL of the episode
        :return: information regarding the episode
        """
        epid = self._get_id("episode", episode_id)
        episode = self._get(f"episode/{epid}")
        return episode

    def get_infos(self):
        """
        :return: Get information about the API in the current country
        """
        information = self._get("infos")
        return information

    def get_me(self, method=""):
        """
        :param method: Me methods accepted:
                'albums': Return a list of user's favorite albums
                'artists': Return a list of user's favorite artists
                'charts':
                    -'/albums': Returns a list of the user's top albums
                    -'/artists': Returns a list of the user's top artists
                    -'/playlists': Returns a list of the user's top playlists
                    -'/tracks': Returns a list of the user's top 25 tracks
                'flow': Returns a list of user's flow tracks
                'folders': Return a list of user's Folder
                'followings': Return a list of user's Friends
                'followers': Return a list of user's followers
                'history': Returns a list of the recently played tracks
                'permissions': Return the user's Permissions granted to the application
                'options': Return user's options
                'personal_songs': Return a list of user's personnal song
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

        :return: Get information about the current user. Requires authentication token.
        """
        if method == "":
            user = self._get("user/me")
        else:
            user = self._get(f"user/me/{method}")
        return user

    def get_options(self):
        """
        Get the user's options
        :return: API response
        """
        options = self._get("options")
        return options

    def get_playlist(self, playlist_id, method=""):
        """

        :param playlist_id: ID or URL
        :param method: Playlist's methods accepted:
                        'comments': Return a list of playlist's comments
                        'fans': Return a list of playlist's fans
                        'tracks': Return a list of playlist's tracks
                        'radio': Return a list of playlist's recommendation tracks
        :return: return information about the playlist
        """
        playid = self._get_id("playlist", playlist_id)
        playlist = self._get(f"playlist/{playid}/{method}")
        return playlist

    def get_podcast(self, show_id, method=""):
        """
        :param show_id: ID or URL
        :param method: Podcast accepted methods:
                        'episodes': Return the list of episodes about the podcast
        :return: information regarding the show
        """
        showid = self._get_id("podcast", show_id)
        show = self._get(f"podcast/{showid}/{method}")
        return show

    def search(self, keyword, method=""):
        """
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
        :return: Information related to the keyword. Using a method helps to narrow down the search and,
                 therefore obtain more accurate results.
        """
        if method == "":
            results = self._get(f"search?q={keyword}")
        else:
            results = self._get(f"search/{method}?q={keyword}")
        return results

    def get_track(self, track_id):
        """

        :param track_id: ID or URL
        :return: return information about a track
        """
        trid = self._get_id("track", track_id)
        track = self._get(f"track/{trid}")
        return track

    def get_user(self, user_id):
        """

        :param user_id: ID or URL
        :return: information related to the user
        """
        userid = self._get_id("user", user_id)
        user = self._get(f"user/{userid}")
        return user

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
        Add one or more albums to the user's library

        :param user_id: ID or URL
        :param album_id:  list of albums IDs or URLs
        """
        userid = self._get_id("user", user_id)
        albid = self._get_id("album", album_id)
        return self._post(f"user/{userid}/albums", "album_id", albid)

    def follow_artist(self, user_id, artist_id):
        """
        Add one or more artists to the user's library
        :param user_id: ID or URL
        :param artist_ids: list of artists IDs or URLs
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
        return self._delete(f"playlist/{plistid}")

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
        Remove an artist from the user's favorities
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
        Remove a playlist from the folder
        :param folder_id: ID or URL
        :param playlist_id: ID or URL
        """
        fldid = self._get_id("folder", folder_id)
        plid = self._get_id("playlist", playlist_id)
        return self._delete(f"folder/{fldid}/items", "playlist_id", plid)

    def delete_album_from_folder(self, folder_id, album_id):
        """
        Remove an album from the folder
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
        elif self.client_credentials_manager:
            return {"access_token": self.client_credentials_manager.token}
        else:
            token = self.client_credentials_manager.get_access_token()
            return {"access_token": token}

    def _get_id(self, type, id):
        fields = id.split("/")
        if len(fields) >= 3:
            if type != fields[-2]:
                self._warn_message(f"Expecting '{type}', found '{fields[-2]}' instead. ")
            return fields[-1]
        return id

    def _get(self, url, **kwargs):
        result = self._call("GET", url, **kwargs)
        return result

    def _post(self, url, param, id):
        result = self._call("POST", url, param, id)
        return result

    def _delete(self, url, param=None, id=None):
        result = self._call("DELETE", url, param, id)
        return result

    def _call(self, call_method, url, param=None, id=None, **kwargs):
        if not url.startswith("http"):
            url = self.base_url + url

        if len(kwargs) == 1:
            url = f"{url}/{kwargs.get('method')}"

        if self._auth or self.client_credentials_manager:
            headers = self._auth_headers()
            if param and id:
                headers[f"{param}"] = id
                result = requests.request(call_method, url, params=headers)
            else:
                result = requests.request(call_method, url, params=headers)
        else:
            result = requests.request(call_method, url)
        return result

    def _warn_message(self, message):
        print(f"warning: {message}", file=sys.stderr)
