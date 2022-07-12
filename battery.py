from languages import Language
from limit_checker import LimitChecker
import constants as const
class Battery:
    def __init__(self, language = None) -> None:
        self.language = Language()
        self.language.set_language_preference(language)
        self.checker = LimitChecker(self.language)
        self.result = True

    def set_attribute(self, name, value):
        self.__setattr__(name, value)

    def get_converted_value(self, conversion, value, actual_unit, expected_unit):
        if conversion.get("From") == actual_unit and conversion.get("To") == expected_unit:
            value = eval(conversion.get("Formula").format(value))
        return value
    
    def unit_conversion(self, value, actual_unit, expected_unit):
        for conversion in const.UNIT_CONVERSIONS:
            value = self.get_converted_value(conversion, value, actual_unit, expected_unit)
        return value

    def is_temperature_ok(self):
        temperature =  self.__getattribute__(const.TEMPERATURE)
        value = temperature.get("value")
        actual_unit = temperature.get("unit")
        expected_unit = const.CELSIUS
        if not actual_unit in [expected_unit, None]:
            value = self.unit_conversion(value, actual_unit, expected_unit)
        return self.checker.check_param(value, const.TEMPERATURE, const.MIN_TEMP, const.MAX_TEMP)

    def is_soc_ok(self):
        soc =  self.__getattribute__(const.SOC)
        value = soc.get("value")
        return self.checker.check_param(value, const.SOC, const.MIN_SOC, const.MAX_SOC)

    def is_charge_rate_ok(self):
        charge_rate = self.__getattribute__(const.CHARGE_RATE)
        value = charge_rate.get("value")
        return self.checker.check_param(value, const.CHARGE_RATE, max = const.MAX_CHARGE_RATE)

    def is_battery_ok(self):
        self.result = all([self.is_temperature_ok(), self.is_soc_ok(), self.is_charge_rate_ok()])