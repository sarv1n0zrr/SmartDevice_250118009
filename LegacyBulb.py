# Adaptee
class LegacyBulb:
    def __init__(self) -> None:
        self._brightness_level = 0  # Raw range: 0 to 255
        self._filament_connected = True

    def set_brightness(self, level: int) -> None:
        if level < 0:
            self._brightness_level = 0
        elif level > 255:
            self._brightness_level = 255
        else:
            self._brightness_level = level

    def read_brightness(self) -> int:
        return self._brightness_level

    def break_filament(self) -> None:
        self._filament_connected = False

    def has_power(self) -> bool:
        return self._filament_connected and (self._brightness_level > 0)