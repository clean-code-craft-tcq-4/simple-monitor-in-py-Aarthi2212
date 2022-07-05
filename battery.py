from limit_checker import LimitChecker
import constants as const
class Battery:
    def __init__(self) -> None:
        self.checker = LimitChecker()
        self.result = True
        self.temperature = None
        self.soc = None
        self.charge_rate = None

    def is_temperature_ok(self):
        self.result = self.checker.check_param(self.temperature, const.TEMPERATURE, const.MIN_TEMP, const.MAX_TEMP)

    def is_soc_ok(self):
        self.result = self.checker.check_param(self.soc, const.SOC, const.MIN_SOC, const.MAX_SOC)

    def is_charge_rate_ok(self):
        self.result = self.checker.check_param(self.charge_rate, const.CHARGE_RATE, max = const.MAX_CHARGE_RATE)

    def is_battery_ok(self):
        self.is_temperature_ok()
        self.is_soc_ok()
        self.is_charge_rate_ok()