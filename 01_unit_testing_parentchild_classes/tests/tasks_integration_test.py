from lib.task_list import TaskList
from lib.task import Task
from lib.task_formatter import *


def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]


def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert task_list.all_complete() == True

def test_task_incomplete_format():
    task = Task("Cleaning")
    formatted_task = TaskFormatter(task)
    assert formatted_task.format() == "- [ ] Cleaning"

def test_task_complete_format():
    task = Task("Cleaning")
    task.mark_complete()
    formatted_task = TaskFormatter(task)
    assert formatted_task.format() == "- [x] Cleaning"