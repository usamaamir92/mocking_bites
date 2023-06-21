from lib.task_formatter import *
from unittest.mock import *

def test_complete_task_format():
    task = Mock()
    task.return_value = "Cleaning"
    task.format.return_value = "- [ ] Cleaning"
    assert task.format() == "- [ ] Cleaning"

def test_incomplete_task_format():
    task = Mock()
    task.return_value = "Cleaning"
    task.format.return_value = "- [x] Cleaning"
    assert task.format() == "- [x] Cleaning"