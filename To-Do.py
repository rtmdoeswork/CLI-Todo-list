import json

def See_Tasks(all_tasks):
    for i, task in enumerate(all_tasks, 1):
        print(f"{i}. {task['Task']} - {task['Status']}.")

def Add_Tasks(file_path, all_tasks, status):
    
    task_input = input("Enter the task: ")

    status_input = input(f"Enter the status 1, 2, 3 - {'|'.join(["Not Started", "In-Progress", "Done"])}: ")
    if status_input == "1":
        status = "Not Started"
    elif status_input == "2":
        status = "In-Progress"
    elif status_input == "3":
        status = "Done"
    else:
        print("Enter a integer between 1 - 3.")

    todo_list = {"Task": task_input, "Status": status}
    all_tasks.append(todo_list)
    with open(file_path, 'w') as file:
        json.dump(all_tasks, file, indent=5)   
        print(f"{task_input} was added")

def Modify_Status(all_tasks, file_path, status):
    for i, task in enumerate(all_tasks, 1):
        print(f"{i}. {task['Task']} - {task['Status']}.")
    
    index = int(input("Which status you like to modify?(enter the number): "))
    status_input = input(f"Enter the status 1, 2, 3 - {'|'.join(["Not Started", "In-Progress", "Done"])}: ")
    if status_input == "1":
            status = "Not Started"
    elif status_input == "2":
            status = "In-Progress"
    elif status_input == "3":
            status = "Done"
    else:
        print("Enter a integer between 1 - 3.")
    all_tasks[index - 1]['Status'] = status
    
    with open(file_path, 'w') as file:
        json.dump(all_tasks, file, indent=5)

def Remove_Tasks(all_tasks, file_path):
    for i, task in enumerate(all_tasks, 1):
        print(f"{i}. {task['Task']} - {task['Status']}.")
    index = int(input("Which would you like to remove?(enter the number): "))
    try:
        all_tasks.pop(index - 1)
        with open(file_path, 'w') as file:
            json.dump(all_tasks, file, indent=5)
    except IndexError:
        print("TASK DOES NOT EXIST") 

def main():
    status = "LAST INPUT WAS INVALID"
    running = True
    file_path = "PUT YOUR FILE PATH HERE"
    try:
        with open(file_path, 'r') as file:
            all_tasks = json.load(file)
    except:
        all_tasks = []
    while running:
        menu = input(f"What would you like to do (1, 2, 3, 4, 5)? - {'|'.join(["See Tasks", "Add Tasks", "Modify Status", "Remove Tasks", "Exit"])}: ")
        if menu == "1":
            See_Tasks(all_tasks)
        elif menu == "2":
            Add_Tasks(file_path, all_tasks, status)
        elif menu == "3":
            Modify_Status(all_tasks, file_path, status)
        elif menu == "4":
            Remove_Tasks(all_tasks, file_path)
        elif menu == "5":
            running = False
            print("Goodbye!")
        else:
            print("Enter a integer between 1 - 5.")

if __name__ == '__main__':
    main()