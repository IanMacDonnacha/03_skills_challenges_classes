class TaskTracker:
    def __init__(self):
        #Parameters: no parameters
        #Side effects: will have a mutable list
        self.task_list = []

    def add_todo_tasks(self, task):
        #Parameters: task - input as string
        #Returns: a list of todo tasks
        #Side effects: add task to list
        self.task_list.append(task)
        return self.task_list

    def mark_as_complete(self, task_complete):
        #Parameters: task_complete - input as string
        #Returns: new list of uncomplete work
        #Side effects: remove tasks from list
        self.task_list.remove(task_complete)
        return self.task_list