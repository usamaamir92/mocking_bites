from lib.music_library import *
from lib.tracks import *
from unittest.mock import Mock

def test_add_track():
    music_library = MusicLibrary()
    track_1 = ("Track 1", "Artist 1")
    music_library.add(track_1)
    assert music_library.track_list == [track_1]

def test_search_returns_correct():
    music_library = MusicLibrary()
    track_1 = Track("Track 1", "Artist 1")
    song_1 = Track("Song 1", "Singer 1")
    music_library.add(track_1)
    music_library.add(song_1)
    assert music_library.search("Track") == [track_1]