from battery import Battery
from languages import Language
from limit_checker import LimitChecker
import constants as const
class Test:
    def __init__(self) -> None:
        self.test_config = [{"Temperature": 50, "SOC": 85, "ChargeRate": 0, "Result": False},
        {"Temperature": 25, "SOC": 70, "ChargeRate": 0.7, "Result": True}]

        self.celsius_temperature_config = [{"Temperature":100, "Result": False},
         {"Temperature": -20, "Result": False},
         {"Temperature": 34, "Result": True}]
        
        self.farenheit_temperature_config = [{"Temperature":100, "Result": True},
         {"Temperature": -20, "Result": False},
         {"Temperature": 34, "Result": True}]
        
        self.soc_config = [{"SOC":120, "Result": False},
         {"SOC": -2, "Result": False},
         {"SOC": 25, "Result": True}]

        self.charge_rate_config = [{"ChargeRate":10, "Result": False},
         {"ChargeRate": 1, "Result": False},
         {"ChargeRate": 0.1, "Result": True}]

    def test_battery(self):
        for config in self.test_config:
            battery = Battery()
            battery.set_attribute(const.TEMPERATURE, {"value": config.get("Temperature"), "unit": const.CELSIUS})
            battery.set_attribute(const.SOC, {"value": config.get("SOC")})
            battery.set_attribute(const.CHARGE_RATE, {"value": config.get("ChargeRate")})
            battery.is_battery_ok()
            assert(battery.result is config.get("Result"))

    def test_temperature_in_celsius(self):
        for config in self.celsius_temperature_config:
            battery = Battery()
            battery.set_attribute(const.TEMPERATURE, {"value": config.get("Temperature")})
            
            assert(battery.is_temperature_ok() is config.get("Result"))

    def test_temperature_in_farenheit(self):
        for config in self.farenheit_temperature_config:
            battery = Battery()
            battery.set_attribute(const.TEMPERATURE, {"value": config.get("Temperature"), "unit": const.FARENHEIT})
            assert(battery.is_temperature_ok() is config.get("Result"))

    def test_soc(self):
        for config in self.soc_config:
            battery = Battery()
            battery.set_attribute(const.SOC, {"value": config.get("SOC")})
            assert(battery.is_soc_ok() is config.get("Result"))

    def test_charge_rate(self):
        for config in self.charge_rate_config:
            battery = Battery()
            battery.set_attribute(const.CHARGE_RATE, {"value": config.get("ChargeRate")})
            assert(battery.is_charge_rate_ok() is config.get("Result"))

    def test_is_in_range(self):
        checker = LimitChecker(Language())
        checker.param_name = "Test Param"
        checker.value = 30
        assert(checker.is_in_range(0, 70) is True)
        checker.value = 100
        assert(checker.is_in_range(0, 70) is False)

    def test_is_in_high_range(self):
        checker = LimitChecker(Language())
        checker.param_name = "Test Param"
        checker.value = 30
        assert(checker.is_in_high_range(70) is True)
        checker.value = 100
        assert(checker.is_in_high_range(70) is False)
    
    def test_is_in_low_range(self):
        checker = LimitChecker(Language())
        checker.param_name = "Test Param"
        checker.value = -1
        assert(checker.is_in_low_range(0) is False)
        checker.value = 100
        assert(checker.is_in_low_range(0) is True)

    def test_language_support(self):
        language = Language()
        assert(language.set_language_preference(const.GERMAN) is True)
        assert(language.set_language_preference("Tamil") is False)

    def test_unit_conversion(self):
        battery = Battery()
        assert(battery.unit_conversion(100, const.FARENHEIT, const.CELSIUS) == 37.77777777777778)
    
    def test_different_language(self):
        for config in self.test_config:
            battery = Battery(const.GERMAN)
            battery.set_attribute(const.TEMPERATURE, {"value": config.get("Temperature"), "unit": const.CELSIUS})
            battery.set_attribute(const.SOC, {"value": config.get("SOC")})
            battery.set_attribute(const.CHARGE_RATE, {"value": config.get("ChargeRate")})
            battery.is_battery_ok()
            assert(battery.result is config.get("Result"))

    def execute(self):
        self.test_battery()
        self.test_temperature_in_celsius()
        self.test_temperature_in_farenheit()
        self.test_soc()
        self.test_charge_rate()
        self.test_is_in_range()
        self.test_is_in_high_range()
        self.test_is_in_low_range()
        self.test_language_support()
        self.test_unit_conversion()
        self.test_different_language()