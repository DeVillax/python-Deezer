import deezer
import sys

if len(sys.argv) > 1:
    album_id = sys.argv[1]
else:
    album_id = "72839592"

    # --- OR ----

    # album_id = "https://www.deezer.com/en/album/72839592"

dz = deezer.Deezer()
album = dz.get_album(album_id)
print(album)
