"""
Base Unit: meter

kilometer:
    Actual Value: 100       -from chatgpt
    Calculated Value: 100   -from Units.py
    Displayed Value: 100    -from UnitConverter.py

repeat for each sister unit

"""
import Units
from UnitConverter import UnitConverter
import test_dict
from decimal import Decimal

def test(unit_type: str) -> None:
    """
    Prints the actual conversion value of 1 base unit, the UnitConverter's calculated value,
    and the value displayed after formatting.
    """ 
    # set up UnitConverter class
    uc = UnitConverter()
    uc.input_value.set("1")
    # iterate through units for unit_type
    for key in test_dict.units[unit_type].keys():
        print("\n\n")
        print(f"Base Unit: {key}\n")
        # iterate through sister units
        for subkey in test_dict.units[unit_type][key].keys():
            print(f"{subkey}:")
            print(f"\tActual Value: {test_dict.units[unit_type][key][subkey]}")
            calculated_value = Units.conversion_library[key][subkey](1)
            print(f"\tCalculated Value: {calculated_value}")
            print(f"\tDisplayed Value: {uc.format_result(Decimal(calculated_value))}\n")
        # # wait for next unit
        print(f"({key})")
        inpt = input("Press 'Enter' to display next unit or 'e' to exit. ")
        if inpt == "e":
            exit()
        
area = "Area"
dtr = "Data Transfer Rate"
ds = "Digital Storage"
e = "Energy"
f = "Frequency"
fe = "Fuel Economy"
l = "Length"
m = "Mass"
pa = "Plane Angle"
p = "Pressure"
s = "Speed"
temp = "Temperature"
t = "Time"
v = "Volume"

test(ds)
