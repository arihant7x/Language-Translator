from src.translator import translate_text
from src.history import save_history, load_history, clear_history


def main():
    print("Welcome to the Language Translator")

    while True:
        print("\n1. Translate Text")
        print("2. View History")
        print("3. Clear History")
        print("4. Exit")

        choice = input("\n> ").strip()

        if choice == "1":
            text = input("Enter text: ").strip()

            if not text:
                print("Error: Text cannot be empty.")
                continue

            destination = input(
                "Target Language (en,es,fr...): "
            ).strip().lower()

            if not destination:
                print("Error: Need a language code.")
                continue

            result = translate_text(text, destination)

            if result.startswith("Error"):
                print(result)
                continue

            save_history(text, result, destination)

            print(f"\nTranslation: {result}")

        elif choice == "2":
            history = load_history()

            if not history:
                print("No history yet.")

            else:
                print()

                for i, entry in enumerate(history, start=1):
                    print("-" * 50)
                    print(f"Translation #{i}")
                    print(f"Time       : {entry['timestamp']}")
                    print(f"Original   : {entry['original']}")
                    print(f"Translated : {entry['translated']}")
                    print(f"Target     : {entry['target']}")

                print("-" * 50)

        elif choice == "3":
            clear_history()
            print("History cleared.")

        elif choice == "4":
            print("Exiting the translator. Bye!")
            break

        else:
            print(f"'{choice}' isn't a valid option.")


if __name__ == "__main__":
    main()