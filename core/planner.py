# core/planner.py
def generate_plan(model, tasks):
    # For now, just return a simple sequential plan
    plan = []
    for idx, task in enumerate(tasks, start=1):
        plan.append(f"Step {idx}: Work on {task}")
    return plan
