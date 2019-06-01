import deezer
import sys

if len(sys.argv) > 1:
    playlist_id = sys.argv[1]
else:
    playlist_id = "2098157264"

    # --- OR ----

    # podcast_id = "https://www.deezer.com/en/playlist/2098157264"

dz = deezer.Deezer()
playlist = dz.get_playlist(playlist_id)
print(playlist)
