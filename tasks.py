from storage import load_tasks, save_tasks

def add_task(task):
    loadedtasks = load_tasks()
    task_create = {
        "id" : len(loadedtasks) + 1,
        "title" : task,
        "completed" : False
    }
    loadedtasks.append(task_create)
    save_tasks(loadedtasks)
    
def completed_task():
    loadedtasks = load_tasks()
    for task in loadedtasks:
        task["completed"] = True
    save_tasks(loadedtasks)
    
def complete_task(task_id):
    loadedtasks = load_tasks()
    for task in loadedtasks:
        if task["id"] == task_id:
            task["completed"] = True
    save_tasks(loadedtasks)
    
def get_tasks():
    return load_tasks()

def delete_task(task_id):
    loadedtasks = load_tasks()
    for task in loadedtasks:
        if task["id"] == task_id:
            loadedtasks.remove(task)
    save_tasks(loadedtasks)

# This is built using list comprehension example 
# def delete_task(task_id):
#     tasks = load_tasks()
#     tasks = [t for t in tasks if t["id"] != task_id]
#     save_tasks(tasks)