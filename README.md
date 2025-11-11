 # To-Do List Application - Design Document

**Team Name**: _________________

**Team Members**: James, Dillon, Ismael, Sanuel

**Date**: 30/10/25

---

## 1. Requirements Analysis

### 1.1 Research Notes
After exploring existing to-do list applications (Microsoft To-Do, Trello, GitHub Projects, etc.), we observed the following common features:

**What can these applications do?**
-Allow users to create, edit and organize tasks
-Set deadlines for tasks, and provide notifications when said deadlines are upcoming
-Organize tasks by priority
-Allow tasks to be synced across devices

**What data do they store?**
- They tend to store simple text data for task descriptions and titles. - These may be stored in different data structures such as dictionaries. They may also be stored in text files and read using file I/O features.
- Time and date data is stored - This is may be for deadlines and having a calendar view of the tasks.
- Priorities of each task is stored. These tend to be stored as integers in lists.
- Boolean data is stored to check wether tasks are complete or not.

**How do they display data?**
- format: clean user friendly interface for readability, in a text format
- Priority: order tasks in order from highest to lowest priority or due date
- graphs and images to show task completion percentages and more

---

### 1.2 Essential Features
List the features your to-do list MUST have to be functional:

1. Allow user to enter a task
2. Allow user to set a deadline for the task and how long it will take 
3. Write users to do lists into .txt file
4. Sort tasks based on the task duration and deadline
5. 

**Why are these essential?**
Provides the user functionality to add tasks and organise their schedule. 

---

### 1.3 Desirable Features
List nice-to-have features that would enhance the application but aren't strictly necessary:

1. have a GUI displaying the tasks and their deadlines.
2. Display how long left you have to do your task 
3. prompt the user for a task description
4.

---
### 2.1 Task Data
What information does each individual task need to store?

| Data Field | Data Type | Purpose | Example |
|------------|-----------|---------|---------|
| task description | String | Describe the task | "Task A" |
| Task deadline | date/time | Give a deadline for the task | 3:00, 18/05/10 |
| task priority | integer | Allow us to sort tasks into most important tasks | 1 |

---

### 2.2 Task List Structure
How will you store the collection of tasks?

**Chosen Structure** (e.g., list of dictionaries, list of lists, list of tuples):
Dictionaries, .txt file, list 
