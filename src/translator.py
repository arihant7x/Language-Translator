from deep_translator import GoogleTranslator 

def translate_text(text: str, destination: str) -> str:
    """
    Translates text into the destination language.
    
    Args:
    text: Text you want to translate.
    destination: Language code of the language you want to translate the text into (e.g., 'en' for English, 'es' for Spanish). 
    Returns:
    Translated text.
    """

    try:
        translation = GoogleTranslator(source="auto",target=destination).translate(text)
        return translation
    except Exception as e:
        return f"Error: {e}"