from SmartDevice import SmartDevice
from LegacyThermostat import LegacyThermostat

class ThermostatAdapter(SmartDevice):
    def __init__(self, thermostat: LegacyThermostat) -> None:
        if thermostat is None:
            raise ValueError("thermostat must not be None")
        self._thermostat = thermostat