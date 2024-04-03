# Task Class
# 1. Implement a Task class to represent individual tasks.
# 2. Each task should have a unique ID, a description, and a completion status
# 3. Include a method to display the task in a user-friendly format.



class Task:
    
    task_counter = 1

    def __init__(self, task_id, description, completion_status):
        self.id = Task.task_counter
        Task.task_counter += 1
        self.task_id = task_id
        self.description = description
        self.completion_status = completion_status
        

    def __str__(self):
        return f'The name of this task is {self.task_id}.\nTask description is: {self.description}.\nCompletion status is: {self.completion_status}'
    
    #write a function that takes in a task_id and checks if it matches self.task_id
    def is_same_task(self, task):
        if self.task_id == task:
            return self.task_id
