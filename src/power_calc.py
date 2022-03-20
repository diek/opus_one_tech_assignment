#!/usr/bin/python
#
# Simple program for testing prospective Python developers

import json
import math
import sys

# Allowable names for voltage, current, and power factor
V_NAMES = {"v", "V", "Volts", "Voltage"}
I_NAMES = {"i", "I", "Amps", "Amperes", "Current"}
PF_NAMES = {"pf", "PF", "Power Factor"}

# If no key/value pair given for power factor, assume a value of 0.9
DEFAULT_PF = 0.9


def is_nan(value):
    try:
        float(value)
    except ValueError:
        return True
    return False


def get_data(in_file):
    cleaned_data = {}
    try:
        with open(in_file, "r") as json_file:
            power_data = json.load(json_file)
            for k, v in power_data.items():
                cleaned_data[k] = {}
                for key, value in v.items():
                    if is_nan(value):
                        value = "nan"
                    if key in V_NAMES:  # voltage
                        cleaned_data[k]["voltage"] = value
                    if key in I_NAMES:  # current
                        cleaned_data[k]["current"] = value
                    if key in PF_NAMES:  # power factor
                        cleaned_data[k]["power_factor"] = value

                if "power_factor" not in cleaned_data[k]:  # No power factor in current item
                    cleaned_data[k]["power_factor"] = DEFAULT_PF

            return cleaned_data

    except IOError:
        error_message = (
            "The json data file or path does not exist, confirm that the file exists"
            " and that the path is correct."
        )
        print(error_message)
        return 0


def calc_power(volts, amps, pf):
    """Returns tuple of (real_power, reactive power, apparent_power) powers from the inputs."""
    try:
        apparent_power = volts * amps
        real_power = apparent_power * pf
        reactive_power = volts * amps * math.sin(math.radians(pf))
        return (real_power, reactive_power, apparent_power)
    except (ValueError, TypeError):
        return (None, None, None)


def print_details(power_information):
    print(json.dumps(power_information, indent=2))


def add_power_calculations(in_data):
    for key, value in in_data.items():
        power = calc_power(
            in_data[key]["voltage"],
            in_data[key]["current"],
            in_data[key]["power_factor"],
        )
        in_data[key]["real_power"] = power[0]
        in_data[key]["reactive_power"] = power[1]
        in_data[key]["apparent_power"] = power[2]

    return in_data


def main(data_file):
    data = get_data(data_file)
    if data:
        power_data = add_power_calculations(data)
        print_details(power_data)
    else:
        print("There was an error as indicated, exiting")


# Run the program; expects a single argument which is the name of JSON file
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an Filename or Path/Filename to proceed.")
    else:
        in_file = sys.argv[1:][0]
        main(in_file)

    # Step 1: Read in the file "data1.json" and clean it so that we
    #       semantically understand and have known quantities for
    #       voltage, current, and power factor

    # Step 2: Create a new dictionary that has the same location
    #       as the primary key, but the value is three new
    #       calculated quantities:
    #           s = apparent power
    #           p = real power
    #           q = reactive power
    #
    #   Can use the "calc_power" function to help with this job

    # Step 3: Print out this new dictionary
