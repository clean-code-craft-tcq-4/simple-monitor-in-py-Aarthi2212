# def is_in_range(parameter, min_value, max_value):
#   return parameter < min_value or parameter > max_value

# def battery_is_ok(temperature, soc, charge_rate):
#   result = True
#   if is_in_range(temperature, 0, 45):
#     print('Temperature is out of range!')
#     result = False
#   elif is_in_range(soc, 20, 80):
#     print('State of Charge is out of range!')
#     result = False
#   elif charge_rate > 0.8:
#     print('Charge rate is out of range!')
#     result = False

#   return result
from battery import Battery

if __name__ == '__main__':
  battery = Battery()
  battery.temperature = 50
  battery.soc = 85
  battery.charge_rate = 0
  battery.is_battery_ok()
  assert(battery.result is False)
  battery.temperature = 25
  battery.soc = 70
  battery.charge_rate = 0.7
  battery.is_battery_ok()
  assert(battery.result is True)
  # assert(battery_is_ok(25, 70, 0.7) is True)
  # assert(battery_is_ok(50, 85, 0) is False)
