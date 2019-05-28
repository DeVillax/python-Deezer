import unittest
import deezer


class TestDeezerClient(unittest.TestCase):

    # Data to test

    # ----------- Albums ------------------------
    skin_album_url = "https://www.deezer.com/en/album/13095256"
    flume_album_id = "7112591"

    # ----------- Artists -----------------------
    flume_artist_url = "https://www.deezer.com/en/artist/1164295"
    deadmau5_artist_id = "142381"

    # ----------- Playlist ----------------------
    summer_hits_playlist_url = "https://www.deezer.com/en/playlist/1283499335"
    summer_sounds_playlist_id = "4793446724"

    # ----------- Tracks ------------------------
    iremember_track_url = "https://www.deezer.com/en/track/3582295"
    ghostsnstuff_track_id = "89844257"

    def setUp(self):
        self.dz = deezer.Deezer()

    # ----------- Albums Tests -------------------

    def test_album_id(self):
        album = self.dz.get_album(self.flume_album_id)
        self.assertTrue(album["title"] == "Flume (Deluxe Edition)")

    def test_album_url(self):
        album = self.dz.get_album(self.skin_album_url)
        self.assertTrue(album["title"] == "Skin")

    def test_album_fans(self):
        fans = self.dz.get_album(self.skin_album_url, method="fans")
        self.assertTrue(fans["data"][0]["type"] == "user")

    def test_album_tracks(self):
        tracks = self.dz.get_album(self.skin_album_url, method="tracks")
        self.assertTrue(tracks["total"] == 16)

    def test_album_comments(self):
        comments = self.dz.get_album(self.flume_album_id, method="comments")
        self.assertTrue(comments["data"][0]["type"] == "comment")

    # ----------- Artists Tests ------------------

    def test_artist_id(self):
        artist = self.dz.get_artist(self.deadmau5_artist_id)
        self.assertTrue(artist["name"] == "Deadmau5")

    def test_artist_url(self):
        artist = self.dz.get_artist(self.flume_artist_url)
        self.assertTrue(artist["name"] == "Flume")

    def test_artist_albums(self):
        albums = self.dz.get_artist(self.deadmau5_artist_id, "albums")
        self.assertTrue(len(albums["data"]) > 0)

        album_found = False
        for album in albums["data"]:
            if "stuff i used to do" in album["title"]:
                album_found = True
        self.assertTrue(album_found)

    def test_artist_comments(self):
        comments = self.dz.get_artist(self.deadmau5_artist_id, "comments")
        self.assertTrue(len(comments["data"]) > 0)

        comment_found = False
        for comment in comments["data"]:
            if "Deadmau5 is a very original artist. He just keeps it cool." in comment["text"]:
                comment_found = True
        self.assertTrue(comment_found)

    """
    def test_artist_fans(self):
        # Need to finish this one
        fans = self.dz.get_artist(self.deadmau5_artist_id, "fans")
        self.assertTrue(len(fans["data"]) > 0)

        fan_found = False
        while fans.get("next"):
            for fan in fans["data"]:
                if fan["name"] == "Gatlock":
                    fan_found = True
                    break
            if fan_found:
                break
            fans = self.dz.next(fans)
        self.assertTrue(fan_found)
    """
    def test_artist_playlists(self):
        playlists = self.dz.get_artist(self.deadmau5_artist_id, "playlists")
        self.assertTrue(len(playlists) > 0)

        playlist_found = False
        while 1:
            for playlist in playlists["data"]:
                if playlist["title"] == "Fitness Unlimited":
                    playlist_found = True
                    break
            if playlist_found:
                break
            playlists = self.dz.next(playlists)
        self.assertTrue(playlist_found)

    def test_artist_radio(self):
        radios = self.dz.get_artist(self.deadmau5_artist_id, "radio")
        self.assertTrue(len(radios) > 0)

        radio_found = False
        for radio in radios["data"]:
            if radio["title"] == "Ghosts 'n' Stuff":
                radio_found = True
                break
        self.assertTrue(radio_found)

    def test_artist_related(self):
        related = self.dz.get_artist(self.deadmau5_artist_id, "related")
        self.assertTrue(len(related) > 0)

        content_found = False
        while 1:
            for content in related["data"]:
                if content["name"] == "Martin Garrix":
                    content_found = True
                    break

            if content_found:
                break
            related = self.dz.next(related)
        self.assertTrue(content_found)

    def test_artist_top(self):
        top = self.dz.get_artist(self.deadmau5_artist_id, "top")
        self.assertTrue(len(top) > 0)

        track_found = False
        for track in top["data"]:
            if track["title"] == "I Remember":
                track_found = True
        self.assertTrue(track_found)

    # ------------- Playlist Tests -------------------

    def test_playlist_id(self):
        playlist = self.dz.get_playlist(self.summer_sounds_playlist_id)
        self.assertTrue(playlist["creator"]["name"] == "Spinnin Records")

    def test_playlist_url(self):
        playlist = self.dz.get_playlist(self.summer_hits_playlist_url)
        self.assertTrue(playlist["title"] == "Summer Hits 2019")

    def test_playlist_comments(self):
        comments = self.dz.get_playlist(self.summer_hits_playlist_url, "comments")
        self.assertTrue(len(comments) > 0)

        comment_found = False
        for comment in comments["data"]:
            if comment["text"] == "goooooooood":
                comment_found = True
                break
        self.assertTrue(comment_found)

    def test_playlist_fans(self):
        fans = self.dz.get_playlist(self.summer_hits_playlist_url, "fans")
        self.assertTrue(len(fans) > 0)
        print(fans)
        fan_found = False
        for fan in fans["data"]:
            if fan["name"] == "mikadov":
                fan_found = True
                break
        self.assertTrue(fan_found)

    def test_playlist_tracks(self):
        tracks = self.dz.get_playlist(self.summer_hits_playlist_url, "tracks")
        self.assertTrue(len(tracks) > 0)

        track_found = False
        while 1:
            for track in tracks["data"]:
                if track["title"] == "WOW":
                    track_found = True
                    break
            if track_found:
                break
            tracks = self.dz.next(tracks)
        self.assertTrue(track_found)

    # ---------- Track Tests ----------------------------

    def test_track_id(self):
        track = self.dz.get_track(self.ghostsnstuff_track_id)
        self.assertTrue(track["title"] == "Ghosts 'n' Stuff")

    def test_track_url(self):
        track = self.dz.get_track(self.iremember_track_url)
        self.assertTrue(track["title"] == "I Remember")

    # ---------- Search Test ----------------------------

    def test_search(self):
        search = self.dz.search("eminem")
        self.assertTrue(len(search) > 0)

        data_found = False
        for data in search["data"]:
            if data["title"] == "The Real Slim Shady":
                data_found = True
                break
        self.assertTrue(data_found)

    def test_advanced_search(self):
        params = {"artist": "Red Hot Chili Peppers", "track": "Snow"}
        search = self.dz.advanced_search(params)

        item_found = False
        for item in search["data"]:
            if item["title"] == "Snow (Hey Oh)":
                item_found = True
                break
        self.assertTrue(item_found)

