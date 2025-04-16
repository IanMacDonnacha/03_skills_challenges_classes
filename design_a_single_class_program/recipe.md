## 1. Describe the Problem

*Put or write the user story here. Add any clarifying notes you might have.*



    As a user
    So that I can keep track of my tasks
    I want a program that I can add todo tasks to and see a list of them.

    As a user
    So that I can focus on tasks to complete
    I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

*Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.*

```python

class TaskTracker:
    def __init__(self)
        #Parameters: no parameters
        #Side effects: will have a mutable list

    def add_todo_tasks(self, task)
        #Parameters: task - input as string
        #Returns: a list of todo tasks
        #Side effects: add task to list

    def mark_as_complete(self, task_complete)
        #Parameters: task_complete - input as string
        #Returns: new list of uncomplete work
        #Side effects: remove tasks from list



```

## 3. Create Examples as Tests

*Make a list of examples of how the class will behave in different situations.*

```python

"""
Given a task to input
Action to add input to a list
"""
task_tracker = TaskTracker()
task_tracker.add_todo_list("Walk the dog")
assert task_tracker == ["Walk the dog"]

"""
Given a task to input
Action to add input to a list
"""
task_tracker = TaskTracker()
task_tracker.mark_as_complete("Walk the dog")
assert task_tracker == []

"""
Given a name and no task
#task_tracker raises an exception
"""
task_tracker = TaskTracker()
task_tracker.add_todo_list()
assert task_tracker == "No task added" # raises an error with the message "No task added."


```

*Encode each example as a test. You can add to the above list as you go.*

## 4. Implement the Behaviour

*After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.*