from deep_translator import GoogleTranslator

SUPPORTED_LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)

CODE_TO_LANGUAGE = {
    code: language
    for language, code in SUPPORTED_LANGUAGES.items()
}


def validate_language(user_input):
    """
    Validates a language entered by the user.

    Accepts either a language name (e.g. 'english')
    or a language code (e.g. 'en').

    Returns:
        str: Valid language code.
        None: If the language is unsupported.
    """

    user_input = user_input.strip().lower()

    if user_input in SUPPORTED_LANGUAGES:
        return SUPPORTED_LANGUAGES[user_input]

    if user_input in SUPPORTED_LANGUAGES.values():
        return user_input

    return None