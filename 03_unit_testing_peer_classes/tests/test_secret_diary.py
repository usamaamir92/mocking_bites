from lib.secret_diary import *
from unittest.mock import *

def test_read_diary_entry_when_locked():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    assert secret_diary.read() == "Go away!"
    diary.read.assert_not_called()

def test_read_diary_entry_when_unlocked():
    diary = Mock()
    diary.read.return_value = "This is my diary entry."
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "This is my diary entry."
    diary.read.assert_called()

def test_read_diary_unlocked_then_locked():
    diary = Mock()
    diary.read.return_value = "This is my diary entry."
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.read() == "Go away!"
    diary.read.assert_not_called()

