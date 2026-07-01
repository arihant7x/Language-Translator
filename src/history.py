import json
import os
from datetime import datetime

history_file = "data/history.json"

def load_history():
    if not os.path.exists(history_file):
        return []
    with open(history_file, "r") as f:
        return json.load(f)
    
def save_history(original,translated,target):
    history = load_history()
    entry = {
        "original" : original,
        "translated" : translated,
        "target" : target,
        "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M")

    }
    history.append(entry)
    with open(history_file, "w") as f:
        json.dump(history, f, indent=2)

def clear_history():
    with open(history_file,"w") as f:
        json.dump([], f)
        