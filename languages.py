import constants as const
class Language:
    def __init__(self) -> None:
        self.language_preference = const.ENGLISH

    def set_language_preference(self, value):
        if not value in const.LANGUAGES_SUPPORTED and value is not None:
            raise ValueError("Language not Supported")
        elif value is not None:
            self.language_preference = value
            return True

    def get_language_preference(self):
        return self.language_preference
