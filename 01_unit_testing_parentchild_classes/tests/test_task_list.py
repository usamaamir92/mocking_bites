from lib.task_list import TaskList
from unittest.mock import *


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_tasks_list():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.all() == [task1,task2]

def test_all_complete_true():
    task_list = TaskList()
    task1 = Mock()
    task1.is_complete.return_value = True
    task2 = Mock()
    task1.is_complete.return_value = True
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.all_complete() == True

def test_all_complete_false():
    task_list = TaskList()
    task1 = Mock()
    task1.is_complete.return_value = True
    task2 = Mock()
    task1.is_complete.return_value = False
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.all_complete() == False


# Unit test `#tasks` and `#all_complete` behaviour