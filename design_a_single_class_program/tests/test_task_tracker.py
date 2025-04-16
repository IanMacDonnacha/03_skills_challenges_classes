from lib.task_tracker import *

"""
Given an empty string as input
return an empty string in list
"""
def test_task_tracker_for_empty_string_in_list():
    task_tracker = TaskTracker()
    result = task_tracker.add_todo_tasks("")
    assert result == [""]

"""
Given a task to input
Action to add input to a list
"""
def test_task_tracker_add_a_single_task():
    task_tracker = TaskTracker()
    result = task_tracker.add_todo_tasks("Walk the dog")
    assert result == ["Walk the dog"]

"""
Given multiple tasks to input
Action to add inputs to a list
"""
def test_task_tracker_add_multiple_tasks():
    task_tracker = TaskTracker()
    result = task_tracker.add_todo_tasks("Walk the dog")
    result = task_tracker.add_todo_tasks("Walk the dog")
    assert result == ["Walk the dog", "Walk the dog"]


"""
Given a task to input
Action to remove input from a list
"""
def test_task_tracker_remove_a_single_task_as_complete():
    task_tracker = TaskTracker()
    task_tracker.add_todo_tasks("Walk the dog")
    result = task_tracker.mark_as_complete("Walk the dog")
    assert result == []


"""
Given a name and no task
#task_tracker raises an exception
"""

# task_tracker = TaskTracker()
# task_tracker.add_todo_list()
# assert task_tracker == "No task added" # raises an error with the message "No task added."