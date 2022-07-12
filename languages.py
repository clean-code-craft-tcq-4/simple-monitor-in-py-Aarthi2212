import constants as const
class Language:
    def __init__(self) -> None:
        self.language_preference = const.ENGLISH

    def is_language_supported(self, value):
        if value in const.LANGUAGES_SUPPORTED:
            return True

    def set_language_preference(self, value):
        result = False
        if value is not None and self.is_language_supported(value):
            self.language_preference = value
            result = True
        return result

    def get_language_preference(self):
        return self.language_preference
