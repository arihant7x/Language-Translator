from src.translator import translate_text
from src.history import save_history, load_history, clear_history, export_history
from src.utils import validate_language, SUPPORTED_LANGUAGES, CODE_TO_LANGUAGE
from src.ui import (
    display_header,
    display_separator,
    display_menu,
    display_error,
    display_success,
    display_empty,
)


def main():
    display_header("Language Translator")

    while True:
        display_menu()
        choice = input("\n> ").strip()

        if choice == "1":
            display_header("Translate Text")

            text = input("Enter text: ").strip()
            if not text:
                display_error("Text cannot be empty.")
                continue

            destination = input(
                "Target Language\nType 'languages' to see all: "
            ).strip().lower()

            if not destination:
                display_error("Need a language.")
                continue

            if destination == "languages":
                display_header("Supported Languages")
                for name, code in SUPPORTED_LANGUAGES.items():
                    print(f"  {name.capitalize()} → {code}")
                continue

            lang_code = validate_language(destination)
            if not lang_code:
                display_error(f"'{destination}' isn't a supported language.")
                continue

            lang_name = CODE_TO_LANGUAGE[lang_code].capitalize()
            result = translate_text(text, lang_code)

            if result.startswith("Error"):
                display_error(result)
                continue

            save_history(text, result, lang_code, lang_name)
            print(f"\nTranslation: {result}")
            display_success("Translation saved.")

        elif choice == "2":
            display_header("Translation History")
            history = load_history()

            if not history:
                display_empty("No translation history found.")
            else:
                for i, entry in enumerate(history, start=1):
                    display_separator()
                    print(f"Translation #{i}")
                    print(f"Time       : {entry['timestamp']}")
                    print(f"Original   : {entry['original']}")
                    print(f"Translated : {entry['translated']}")
                    print(f"Language   : {entry['target_name']} ({entry['target_code']})")
                display_separator()

        elif choice == "3":
            clear_history()
            display_success("History cleared.")

        elif choice == "4":
            display_header("Supported Languages")
            for name, code in SUPPORTED_LANGUAGES.items():
                print(f"  {name.capitalize()} → {code}")

        elif choice == "5":
            success, message = export_history()
            if success:
                display_success(f"History exported to {message}")
            else:
                display_error(message)
            
        elif choice == "6":
            print("\nExiting the translator. Bye!")
            break

        else:
            display_error(f"'{choice}' isn't a valid option.")


if __name__ == "__main__":
    main()