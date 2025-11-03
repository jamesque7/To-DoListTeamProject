"""
okay so this function is to allow the user to create a task
each task is gonna have a name, and a description
and it will be stored in a dictionary
with the name being the key and the description the value
i will also include a priority, and a deadline value into the dictionary
this will make it easier when you guys make those functions

each task dictionary will then be stored in a list
and this list can be read through and output, or sorted in different ways

i think thats all the info needed
"""
from datetime import datetime
list_of_tasks = [] #defining the list outside the function so it can be accessed by other programds
def create_task():
    name_of_task = str(input("Enter a name for the task: "))
    desc_of_task = str(input("Enter a brief description of the task: "))
    y = 1
    while y == 1:
        priority = int(input("Enter the priority of the task, with 1 being the lowest and 5 being the highest: "))
        if 1 <= priority <= 5:
            y = 2
        else:
            print("Please enter a valid priority between 1 and 5.")
    x = 1
    while x == 1:
        user_input = input("Enter a deadline (DD-MM-YYYY): ")
        #the user is prompted to enter a date
        try:
            deadline = datetime.strptime(user_input, "%d-%m-%Y")
            #Check if it's in the future
            if deadline > datetime.now():
                # store a formatted string instead of the datetime object
                deadline_str = deadline.strftime("%d-%m-%Y") #'this makes it look nicer
                print(f"Deadline set for: {deadline_str}")
                x = 2
            else:
                print("Please enter a future date and time.")
        except ValueError:
            print("Invalid format. Please use DD-MM-YYYY (e.g. 31-12-2025)")
            continue
    task_dictionary = {
        "Name of Task: ": name_of_task,
        "Description of Task: ": desc_of_task,
        "Priority of Task: ": priority,
        "Deadline of Task: ": deadline_str
    }
    list_of_tasks.append(task_dictionary)
    print(list_of_tasks)

create_task()