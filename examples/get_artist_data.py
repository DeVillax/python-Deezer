import deezer
import sys

if len(sys.argv) > 1:
    artist_id = sys.argv[1]
else:
    artist_id = "3968561"

    # --- OR ----

    # podcast_id = "https://www.deezer.com/en/artist/3968561"

dz = deezer.Deezer()
artist = dz.get_artist(artist_id)
print(artist)
