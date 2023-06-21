from lib.diary import *

def test_read():
    diary = Diary("This is my diary entry.")
    assert diary.read() == "This is my diary entry."