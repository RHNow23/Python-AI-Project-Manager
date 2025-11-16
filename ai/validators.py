# ai/validators.py
def validate_plan(plan):
    # Simple validation: ensure plan is not empty
    if not plan:
        return False
    return True
    # More complex validation logic can be added here
# In a real implementation, this would check for feasibility, constraints, etc.
