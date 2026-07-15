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

EXPORT_FILE = "data/history_export.txt"

def export_history():
    history = load_history()

    if not history:
        return False, "No history to export."

    try:
        with open(EXPORT_FILE, "w") as f:
            for i, entry in enumerate(history, start=1):
                f.write(f"Translation #{i}\n")
                f.write(f"Time       : {entry['timestamp']}\n")
                f.write(f"Original   : {entry['original']}\n")
                f.write(f"Translated : {entry['translated']}\n")
                f.write(f"Language   : {entry['target_name']} ({entry['target_code']})\n")
                f.write("-" * 40 + "\n")
        return True, EXPORT_FILE

    except Exception as e:
        return False, str(e)