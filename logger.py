class Logger:
    def __init__(self) -> None:
        pass

    def log_range_output(self, result, parameter_name):
        if not result:
            print("{} out of range".format(parameter_name))
        else:
            print("{} is in range".format(parameter_name))
    
    def log_higher_output(self, result, parameter_name):
        if not result:
            print("{} is too high".format(parameter_name))
        else:
            print("{} is in high limit".format(parameter_name))
    
    def log_lower_output(self, result, parameter_name):
        if not result:
            print("{} is too low".format(parameter_name))
        else:
            print("{} is in low limit".format(parameter_name))