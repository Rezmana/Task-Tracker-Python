import customtkinter as ctk
from tasks import add_task, completed_all_task, complete_task, get_tasks, delete_task

def refresh_tasks():
    for widget in frame.winfo_children():
        widget.destroy()
    tasks = get_tasks()
    for task in tasks:
        if(task["completed"]):
            continue
        else:
            checkbox = ctk.CTkCheckBox(frame, text=task["title"], command=lambda t=task: handle_completed(t["id"]))
            checkbox.pack(pady=5)
        
def handle_completed(task_id):
    complete_task(task_id)
    refresh_tasks()
def handle_add_task(task_title):
    add_task(task_title)
    entry.delete(0, ctk.END)
    refresh_tasks()
    

app = ctk.CTk()
app.title("CustomTkinter Example")
app.geometry("400x300")
# task_list = get_tasks() # Loads the tasks from JSON file when the application starts
frame = ctk.CTkScrollableFrame(app,width=380, height=200)
refresh_tasks()
label = ctk.CTkLabel(app, text="My Tasks")
label.pack(pady=10)
entry = ctk.CTkEntry(app, placeholder_text="Enter a task")
entry.pack(pady=10)
button = ctk.CTkButton(app, text="Add Task", command=lambda: handle_add_task(entry.get()))
button.pack(pady=10)
frame.pack(pady=10, fill="both", expand=True)

app.mainloop()

