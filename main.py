import sys
from core import todo, records, planner
from ai import models, validators
from db import db_manager



def show_menu():
    print("\n=== Project Manager AI ===")
    print("1. Manage To-Do List")
    print("2. Record Keeping")
    print("3. Future Planning (AI)")
    print("4. Exit")

def todo_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Back")

    choice = input("Select option: ")
    if choice == "1":
        task = input("Enter task description: ")
        todo.add_task(task)
    elif choice == "2":
        tasks = todo.get_tasks()
        for t in tasks:
            print(f"- {t}")
    elif choice == "3":
        task_id = input("Enter task ID to complete: ")
        todo.complete_task(task_id)
    elif choice == "4":
        return

def records_menu():
    print("\n--- Records ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Back")

    choice = input("Select option: ")
    if choice == "1":
        entry = input("Enter record entry: ")
        records.add_record(entry)
    elif choice == "2":
        for r in records.get_records():
            print(f"- {r}")
    elif choice == "3":
        return

def planning_menu():
    print("\n--- Future Planning ---")
    tasks = todo.get_tasks()
    if not tasks:
        print("No tasks available for planning.")
        return

    print("Generating plan using AI...")
    model = models.load_model()  # explicit opt-in in settings.yaml
    plan = planner.generate_plan(model, tasks)

    if validators.validate_plan(plan):
        print("\nSuggested Plan:")
        for step in plan:
            print(f"- {step}")
    else:
        print("AI plan failed validation. Please adjust tasks or constraints.")

def main():
    db_manager.init_db()  # ensure DB schema is ready

    while True:
        show_menu()
        choice = input("Select option: ")

        if choice == "1":
            todo_menu()
        elif choice == "2":
            records_menu()
        elif choice == "3":
            planning_menu()
        elif choice == "4":
            print("Exiting Project Manager AI. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
