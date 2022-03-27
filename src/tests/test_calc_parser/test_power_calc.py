import json
import math

import pytest
from power_calc import calc_power, is_nan

SAMPLE_DATA = {
    "Empty House": {"V": 120.0, "I": 0.0},
    "My House": {"V": 120.0, "i": 4.5},
    "Industrial #1": {"voltage": 4160, "current": 25, "power_factor": 0.75}
}


def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n * multiplier) / multiplier


def calc_reactive_power():
    return 25 * 4160 * 0.01308959557134197


def test_reactive_power():
    volts = 4160
    amps = 25
    pf = 0.75
    reactive_power_1 = volts * amps * math.sin(math.radians(pf))
    reactive_power_2 = calc_reactive_power()
    assert truncate(reactive_power_1, 8) == truncate(reactive_power_2, 8)


def test_valid_json():
    try:
        json.dumps(SAMPLE_DATA)
    except ValueError as err:
        assert False
    assert True


def test_is_nan():
    assert is_nan(5) is False
    assert is_nan('five') is True


def test_calc_power():
    voltage = SAMPLE_DATA["Industrial #1"]["voltage"]
    current = SAMPLE_DATA["Industrial #1"]["current"]
    power_factor = SAMPLE_DATA["Industrial #1"]["power_factor"]
    power = calc_power(voltage, current, power_factor)
    # powers = calc_power(4160, 25, 0.75)
    assert isinstance(power, tuple)
    assert len(power) == 3
    assert power[1] == 1361.3179394198219
