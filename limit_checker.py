from logger import Logger
class LimitChecker:
    def __init__(self, language) -> None:
        self.logger = Logger(language)
        self.value = None
    
    def is_in_range(self, min, max):
        result = self.value > min and self.value < max
        self.logger.log_range_output(result, self.param_name)
        return result

    def is_in_high_range(self, max):
        result = self.value < max
        self.logger.log_higher_output(result, self.param_name)
        return result

    def is_in_low_range(self, min):
        result = self.value > min
        self.logger.log_lower_output(result, self.param_name)
        return result

    def check_param(self, value, param_name, min = 0, max = 0):
        self.value = value
        self.param_name = param_name
        result = self.is_in_range(min, max)
        if not result:
            result = all([self.is_in_high_range(max), self.is_in_low_range(min)])
        return result
