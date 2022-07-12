import constants as const
class Logger:
    def __init__(self, language) -> None:
        self.log_language = language.get_language_preference()

    def log(self, parameter_name, log_template):
        language_template = const.LANGUAGE_TEMPLATES.get(self.log_language)
        print(language_template.get(log_template).format(language_template.get(parameter_name)))

    def log_range_output(self, result, parameter_name):
        if not result:
            self.log(parameter_name, const.OUT_OF_RANGE)
        else:
            self.log(parameter_name, const.INRANGE)
    
    def log_higher_output(self, result, parameter_name):
        if not result:
            self.log(parameter_name, const.OUT_OF_HIGH_LIMIT)
        else:
            self.log(parameter_name, const.IN_HIGH_LIMIT)
    
    def log_lower_output(self, result, parameter_name):
        if not result:
            self.log(parameter_name, const.OUT_OF_LOW_LIMIT)
        else:
            self.log(parameter_name, const.IN_LOW_LIMIT)