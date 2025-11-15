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
    z = 0
    while z == 0:
        #check for empty name and description
        a = 1
        while a == 1:
            name_of_task = str(input("Enter a name for the task: ")).strip()
            if name_of_task == "":
                print("Task name cannot be empty. Please enter a valid name.")
            else:
                a = 2
        b = 1
        while b == 1:
            desc_of_task = str(input("Enter a brief description of the task: ")).strip()
            if desc_of_task == "":
                print("Task description cannot be empty. Please enter a valid description.")
            else:
                b = 2
        #try except for priority and deadline inputs
        #priority must be an integer between 1 and 5
        #deadline must be a date in the future
        y = 1
        while y == 1:
            try:
                priority = int(input("Enter the priority of the task, with 1 being the lowest and 5 being the highest: ")) 
                if 1 <= priority <= 5:
                    y = 2
                else:
                    print("Please enter a valid priority between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 5.")
                continue
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
        another = input("Would you like to add another task? (yes/no): ").strip().lower()
        if another != 'yes':
            z = 1

create_task()

#looop to allow multiple task creation
#check for empty name and descripton
#try e=xcept for priority and deadline inputs