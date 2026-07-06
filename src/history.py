import json
import os
from datetime import datetime

HISTORY_FILE = "data/history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        return []


def save_history(original, translated, target_code, target_name):
    history = load_history()
    entry = {
        "original": original,
        "translated": translated,
        "target_code": target_code,
        "target_name": target_name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def clear_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f, indent=4)