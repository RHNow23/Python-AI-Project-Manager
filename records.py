# core/records.py
records = []

def add_record(entry):
    records.append(entry)
    print(f"Record added: {entry}")

def get_records():
    return records
