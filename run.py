# User Interactions
# Create a simple user interface for the To-Do List Manager using a loop.
# Provide options for users to:
# 1. Add a new task.
# 2. View all tasks.
# 3. Edit the completion status of a task.
# 4. Delete a task.
# 5. Quit the manager.
# Implement appropriate data validation to handle user input and prevent errors.




import to_do_list


def run_app():
    print("Welcome to the To-Do List App by Adonai Romero")
    #create an instance of the to-do list class
    to_do = to_do_list.ToDoList()


    # start running the app until user quits
    while True:
        # include methods for adding tasks, viewing tasks, editing task completion status, deleting tasks, and retrieving tasks by ID.
        print(f"Please enter a number:\n1. Add Task\n2. View To_do List\n3. Edit Task Completion Status\n4. Delete Task\n5. Retrieve Task by Name\n6. Quit")
        # ask the user what they would like to do
        option = input("What would you like to do today? ")
        # handling user input error
        while option not in ('1', '2', '3', '4', '5', '6'):
            #redefine
            option = input("Not a valid option, please enter 1, 2, 3, 4, 5, or 6. ")
        
        if option == '6':
            break
        elif option == '1':
            task_id = input('What would you like to add to the to-do list? ').lower()
            # Call the add task method from the app
            to_do.create_task(task_id)
        elif option == '2':
            # Call the view task function
            to_do.view_task()
        elif option == '3':
            task_id = input('Which task would you like to edit? ')
            # call the edit task completion function
            to_do.edit_task(task_id)
            # call the delete task function
        elif option == '4':
            task = input('What would you like to delete from the to-do list? ')
            to_do.delete_task(task)
            # call the retrieve task ID function
        elif option == '5':
            task = input("Which task would you like to fetch? ")
            to_do.retrieve_task(task)

if __name__ == "__main__":
    run_app()
