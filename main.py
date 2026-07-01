from src.translator import translate_text

def main():
    print("Welcome to the Language Translator")

    while True:
        print("\n1. Translate Text")
        print("2. Exit")
        choice = input("\n> ").strip()

        if choice == "1":
            text = input("Enter text: ").strip()
            if not text:
                print("Error: Text cannot be empty.")
                continue
            
            destination = input("Target Language (en,es,fr...): ").strip().lower()
            if not destination:
                print("Error: need a language code.")
                continue
    
            result = translate_text(text, destination)
            print(f"\nTranslation: {result}")
        elif choice == "2":
            print("Exiting the translator. Bye!")
            break
        else:
            print(f"'{choice}' isn't a valid option.")
if __name__ == "__main__":
    main()