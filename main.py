from SmartDevice import SmartDevice
from LegacyThermostat import LegacyThermostat
from LegacyBulb import LegacyBulb
from BulbAdapter import BulbAdapter

if __name__ == "__main__":
    bulb = LegacyBulb()
    adapter = BulbAdapter(bulb)

    adapter.turn_on()
    assert bulb.read_brightness() == 255
    assert adapter.is_on() is True

    adapter.turn_off()
    assert bulb.read_brightness() == 0
    assert adapter.is_on() is False
    assert adapter.get_power_percent() == 0

    bulb.set_brightness(128)
    print("Power percent at 128:", adapter.get_power_percent())
    print("All Stage 1 checks passed.")