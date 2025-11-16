# core/todo.py
tasks = []
task_id_counter = 1

def add_task(description):
    global task_id_counter
    task = {"id": task_id_counter, "description": description, "completed": False}
    tasks.append(task)
    task_id_counter += 1
    print(f"Task added: {description}")

def get_tasks():
    return [f"{t['id']}: {t['description']} (Done: {t['completed']})" for t in tasks]

def complete_task(task_id):
    for t in tasks:
        if str(t["id"]) == str(task_id):
            t["completed"] = True
            print(f"Task {task_id} marked complete.")
            return
    print("Task not found.")
