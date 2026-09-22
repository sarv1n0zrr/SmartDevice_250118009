from typing import List
from SmartDevice import SmartDevice

# Client
class ModernHub:
    def __init__(self, devices: List[SmartDevice]) -> None:
        self._devices = devices

    def activate_all(self) -> None:
        for d in self._devices:
            d.turn_on()

    def emergency_shutdown(self) -> None:
        for d in self._devices:
            d.turn_off()

    def calculate_average_power_usage(self) -> float:
        if not self._devices:
            return 0.0
        total = 0
        for d in self._devices:
            total += d.get_power_percent()
        return total / len(self._devices)

