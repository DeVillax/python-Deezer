import deezer
import sys

if len(sys.argv) > 1:
    podcast_id = sys.argv[1]
else:
    podcast_id = "59898"

    # --- OR ----

    # podcast_id = "https://www.deezer.com/en/show/59898"

dz = deezer.Deezer()
podcast = dz.get_podcast(podcast_id)
print(podcast)