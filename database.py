import json
task_file = "tasks.json"
def load_tasks(): # load tasks from json file
    try:    
        with open(task_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(data): # save tasks to json file
    with open(task_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)