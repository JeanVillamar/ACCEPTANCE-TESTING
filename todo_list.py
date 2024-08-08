tasks = []

def add_task(description):
    tasks.append({'description': description, 'completed': False})

def list_tasks():
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['description']} - {'Completed' if task['completed'] else 'Incomplete'}")

def mark_completed(index):
    tasks[index - 1]['completed'] = True

def edit_task(index, new_description):
    tasks[index - 1]['description'] = new_description

def clear_tasks():
    tasks.clear()