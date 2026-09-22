from SmartDevice import SmartDevice
from LegacyBulb import LegacyBulb

class BulbAdapter(SmartDevice):
    STUDENT_ID_LAST_DIGIT = 9

    def __init__(self, bulb: LegacyBulb) -> None:
        if bulb is None:
            raise ValueError("bulb must not be None")
        self._bulb = bulb

    def turn_on(self) -> None:
        self._bulb.set_brightness(255)

    def turn_off(self) -> None:
        self._bulb.set_brightness(0)

    def is_on(self) -> bool:
        return self._bulb.has_power() and self._bulb.read_brightness() > 0

    def get_power_percent(self) -> int:
        raw_brightness = self._bulb.read_brightness()

        if raw_brightness == 0:
            return 0

        raw_percent = (raw_brightness * 100) // 255  # floor division
        calibrated_percent = raw_percent + self.STUDENT_ID_LAST_DIGIT

        if calibrated_percent > 100:
            return 100
        return calibrated_percent