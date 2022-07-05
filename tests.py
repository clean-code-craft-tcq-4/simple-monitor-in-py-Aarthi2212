from battery import Battery
from limit_checker import LimitChecker
class Test:
    def __init__(self) -> None:
        self.test_config = [{"Temperature": 50, "SOC": 85, "ChargeRate": 0, "Result": False},
        {"Temperature": 25, "SOC": 70, "ChargeRate": 0.7, "Result": True}]

        self.temperature_config = [{"Temperature":100, "Result": False},
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
            battery.temperature = config.get("Temperature")
            battery.soc = config.get("SOC")
            battery.charge_rate = config.get("ChargeRate")
            battery.is_battery_ok()
            assert(battery.result is config.get("Result"))

    def test_temperature(self):
        for config in self.temperature_config:
            battery = Battery()
            battery.temperature = config.get("Temperature")
            battery.is_temperature_ok()
            assert(battery.result is config.get("Result"))

    def test_soc(self):
        for config in self.soc_config:
            battery = Battery()
            battery.soc = config.get("SOC")
            battery.is_soc_ok()
            assert(battery.result is config.get("Result"))

    def test_charge_rate(self):
        for config in self.charge_rate_config:
            battery = Battery()
            battery.charge_rate = config.get("ChargeRate")
            battery.is_charge_rate_ok()
            assert(battery.result is config.get("Result"))

    def test_is_in_range(self):
        checker = LimitChecker()
        checker.param_name = "Test Param"
        checker.value = 30
        assert(checker.is_in_range(0, 70) is True)
        checker.value = 100
        assert(checker.is_in_range(0, 70) is False)

    def test_is_in_high_range(self):
        checker = LimitChecker()
        checker.param_name = "Test Param"
        checker.value = 30
        assert(checker.is_in_high_range(70) is True)
        checker.value = 100
        assert(checker.is_in_high_range(70) is False)
    
    def test_is_in_low_range(self):
        checker = LimitChecker()
        checker.param_name = "Test Param"
        checker.value = -1
        assert(checker.is_in_low_range(0) is False)
        checker.value = 100
        assert(checker.is_in_low_range(0) is True)

    def execute(self):
        self.test_battery()
        self.test_temperature()
        self.test_soc()
        self.test_charge_rate()
        self.test_is_in_range()
        self.test_is_in_high_range()
        self.test_is_in_low_range()