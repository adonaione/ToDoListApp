import models

#To-Do List Class
# Implement a ToDoList class to manage a list of tasks.
# Include methods for adding tasks, viewing tasks, editing task completion status, deleting tasks, and retrieving tasks by ID.
class ToDoList:
    def __init__(self):
        self.tasks = []
        

    # Private Method that will get a task by its ID or return None if no task with that ID
    def _get_task_from_id(self, task_id):
        # Loop through all of the tasks in the app
        for task in self.tasks:
            # If the task's ID matches the task_id argument
            if models.Task.is_same_task == task_id:
                # return the task instance
                return task
        # If we finish the loop, that means the task with that ID does not exist
            return None


    #Method for adding a task
    def create_task(self, task_id):
        #check to see if task exists already
        while task_id in self.tasks:
            print(f"The task {task_id} is already on the to-do list.")
        else:
            description = input('Please enter a description: ').lower()
            completion_status = input(f'Please enter "complete" or "incomplete": ').lower()
            # Create new instance of a task with the info provided
            new_task = models.Task(task_id, description, completion_status)
            # add the new task to the to-do list
            self.tasks.append(new_task)
            print(f'{task_id} has been added to the to-do list.')

    #method for viewing tasks
    def view_task(self):
        #check if there are any tasks
        if self.tasks:
            #Loop through the list
            for task in self.tasks:
                print(task)
        else:
            print("The to-do list is empty.")        

    #method for editing task completion status
    def edit_task(self, task_id):
        task = self._get_task_from_id(task_id)
        if task:
            if task.task_id == task_id:
                new_status = input("Enter new completion status for this task. Complete/Incomplete ")
                task.completion_status = new_status
            print(f'{task_id} has successfully been updated.')
        else:
            print('That is not on the to-do list.')
    

    #method for deleting task
    def delete_task(self, task_id):
        task = self._get_task_from_id(task_id)
        if task:
            confirmation = input(f'Are you sure you want to delete this task from the to-do list? This cannot be undone. Enter "yes" to delete: ').lower()
            if confirmation == "yes":
                #remove task from list
                self.tasks.remove(task)
                print(f'{task.task_id} has been deleted.')
            else:
                print('Canceled')
        else:
            print(f'Task with a name of {task_id} does not exist on the To-Do List.')

    #method for retrieving by ID
    def retrieve_task(self, task_id):
        task = self._get_task_from_id(task_id)
        if task:
            return models.Task()
        else:
            return "Does not exist."

# tasks = []
# new_task = Task('hw', 'code', 'inc')
# ne_task = Task('work', 'code', 'inc')
# tasks.append(new_task)
# tasks.append(new_task)
# print(tasks)
# print(type(tasks))
