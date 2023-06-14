# Constants
ROD_TO_METERS = 5.0292
METER_TO_FEET = 1 / 0.3048
METER_TO_MILES = 1 / 1609.34
ROD_TO_FURLONGS = 1 / 40
WALKING_SPEED_MPH = 3.1
WALKING_SPEED_MPM = WALKING_SPEED_MPH * (1 / 60) # miles per minute


if __name__ == '__main__':
    # Input
    num_str = input("Input rods: ")
    num_float = float(num_str)

    # Calculations
    meters = num_float * ROD_TO_METERS
    feet = meters * METER_TO_FEET
    miles = meters * METER_TO_MILES
    furlongs = num_float * ROD_TO_FURLONGS
    minutes = (miles / WALKING_SPEED_MPM)

    # Output

    print("You input", round(num_float, 3), "rods.")
    print("Conversions")
    print("Meters:", round(meters, 3))
    print("Feet:", round(feet, 3))
    print("Miles:", round(miles, 3))
    print("Furlongs:", round(furlongs, 3))
    print("Minutes to walk", round(num_float, 3), "rods:", round(minutes, 3))
