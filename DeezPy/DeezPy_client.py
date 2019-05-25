import sys
import requests


class Deezer(object):

    def __init__(self, auth=None, client_credentials_manager=None):
        self.base_url = "https://api.deezer.com/"
        self._auth = auth
        self.client_credentials_manager = client_credentials_manager

    def _auth_headers(self):
        if self._auth:
            return {"access_token": self._auth}
        elif self.client_credentials_manager:
            return {"access_token": self.client_credentials_manager.token}
        else:
            token = self.client_credentials_manager.get_access_token()
            return {"access_token": token}

    def album(self, album_id, method=""):
        """
        :param album_id: ID or URL
        :param method: Album methods:
                        'comments': Return a list of album's comments
                        'fans': Return a list of album's fans
                        'tracks': Return a list of album's tracks
        :return: return information about the album if no method is provided.
        """
        albid = self._get_id("album", album_id)
        album = self._get(f"album/{albid}/{method}")
        return album

    def artist(self, artist_id, method=""):
        """
        :param artist_id: ID or URL
        :param method: :param album_id: ID or URL
        :param method: Artist methods accepted:
                        'albums': Return a list of artist's albums
                        'comments': Return a list of artist's comments
                        'fans': Return a list of artist's fans
                        'playlists': Return a list of artist's playlists
                        'radio': Return a list of tracks
                        'related': Return a list of related artists
                        'top': Get the top 5 tracks of an artist
        :return: information related to the artist if no method is provided
        """
        artid = self._get_id("artist", artist_id)
        artist = self._get(f"artist/{artid}/{method}")
        return artist

    def chart(self, type):
        """
        Retrieve the top 10 items in the category provided.

        :param type: chart to retrieve. Params can be:
                'tracks': returns list of object of type track of the Top 10 tracks
                'albums': returns list of object of type album of the Top 10 album
                'artists': returns list of object of type artist of the Top 10 artists
                'playlists': returns list of object of type playlist of the Top 10 playlists
                'podcasts': returns list of object of type podcast of the Top 10 podcasts
        :return: Depends on the category provided. (See above)
        """
        chart = self._get(f"chart/0/{type}")
        return chart

    def comment(self, comment_id):
        """

        :param comment_id: ID of the comment
        :return: Information regarding the comment
        """
        comment = self._get(f"comment/{comment_id}")
        return comment

    def editorial(self, method=""):
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

    def episode(self, episode_id):
        """
        :param episode_id: ID or URL of the episode
        :return: information regarding the episode
        """
        epid = self._get_id("episode", episode_id)
        episode = self._get(f"episode/{epid}")
        return episode

    def infos(self):
        """
        :return: Get information about the API in the current country
        """
        information = self._get("infos")
        return information

    def me(self, method=""):
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

    def options(self):
        """

        :return: Get the user's options
        """
        options = self._get("options")
        return options

    def playlist(self, playlist_id, method=""):
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

    def podcast(self, show_id, method=""):
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

    def track(self, track_id):
        """

        :param track_id: ID or URL
        :return: return information about a track
        """
        trid = self._get_id("track", track_id)
        track = self._get(f"track/{trid}")
        return track

    def user(self, user_id):
        """

        :param user_id: ID or URL
        :return: information related to the user
        """
        userid = self._get_id("user", user_id)
        user = self._get(f"user/{userid}")
        return user

    def _get_id(self, type, id):
        fields = id.split("/")
        if len(fields) >= 3:
            if type != fields[-2]:
                self._warn_message(f"Expecting '{type}', found '{fields[-2]}' instead. ")
            return fields[-1]
        return id

    def _get(self, url):
        if not url.startswith("http"):
            url = self.base_url + url

        if self._auth or self.client_credentials_manager:
            headers = self._auth_headers()
            result = requests.get(url, params=headers)
        else:
            result = requests.get(url)
        return result

    def _warn_message(self, message):
        print(f"warning: {message}", file=sys.stderr)
