from lib.tracks import *

def test_matches_returns_True_for_keyword():
    track1 = Track("Track 1","Artist 1")
    assert track1.matches("Track") == True

def test_matches_returns_False_for_keyword():
    track1 = Track("Track 1","Artist 1")
    assert track1.matches("Artist") == True

def test_no_match_returns_false():
    track1 = Track("Track 1","Artist 1")
    assert track1.matches("Song") == False