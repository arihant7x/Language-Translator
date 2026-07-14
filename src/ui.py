def display_header(title):
    print("\n" + "=" * 40)
    padding = (40 - len(title)) // 2
    print(" " * padding + title)
    print("=" * 40)

def display_separator():
    print("-" * 40)

def display_menu():
    print("\n1. Translate Text")
    print("2. View History")
    print("3. Clear History")
    print("4. Supported Languages")
    print("5. Exit")

def display_error(message):
    print(f"\n[ERROR] {message}")

def display_success(message):
    print(f"\n[SUCCESS] {message}")

def display_empty(message):
    print(f"\n{message}")