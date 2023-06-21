from lib.music_library import *
from unittest.mock import Mock

def test_search_by_keyword():
     music_library = MusicLibrary()
     fake_track1 = Mock()
     fake_track1.matches.return_value = True
     music_library.add(fake_track1)
     fake_track2 = Mock()
     fake_track2.matches.return_value = False
     music_library.add(fake_track2)
     assert music_library.search("hello") == [fake_track1]