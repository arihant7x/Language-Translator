from src.translator import translate_text

def main():
    print("Welcome to the Language Translator")
    text = input("Enter text: ").strip()
    destination = input("Target Language (en,es,fr...): ").strip().lower()
    result = translate_text(text, destination)
    print(f"\nTranslation: {result}")

if __name__ == "__main__":
    main()