"""
This function is to write the task from enter task to as text file
takes the key and value of from dictionary and goes text file.
"""
def WriteToFile(list_of_tasks):
    try:
        with open("Todo.txt", 'w') as file:
            for task in list_of_tasks:
                for key, value in task.items():
                    file.write(f"{key}{value}\n") # write in key and value to file
                file.write("\n")  # Blank line between tasks
    except IOError:
        print("Error: file not found")


WriteToFile(list_of_tasks)