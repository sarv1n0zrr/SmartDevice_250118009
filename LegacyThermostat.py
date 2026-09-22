# Adaptee
class LegacyThermostat:
    # Valid dial states: "IDLE", "LOW", "MEDIUM", "MAX"
    def __init__(self) -> None:
        self._dial_position = "IDLE"

    def rotate_dial(self, position: str) -> None:
        self._dial_position = position

    def check_dial(self) -> str:
        return self._dial_position