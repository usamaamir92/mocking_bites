from lib.diary import *
from lib.secret_diary import *


def test_read_function_when_locked():
    diary = Diary("This is my diary entry")
    secret_diary = SecretDiary(diary)
    assert secret_diary.read() == "Go away!"

def test_read_function_when_unlocked():
    diary = Diary("This is my diary entry.")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "This is my diary entry."

def test_read_function_locked_then_unlocked():
    diary = Diary("This is my diary entry.")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.read() == "Go away!"