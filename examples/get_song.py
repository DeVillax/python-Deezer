import deezer
import sys

if len(sys.argv) > 1:
    track_id = sys.argv[1]
else:
    track_id = "653689002"

    # --- OR ----

    # podcast_id = "https://www.deezer.com/en/track/653689002"

dz = deezer.Deezer()
track = dz.get_track(track_id)
print(track)