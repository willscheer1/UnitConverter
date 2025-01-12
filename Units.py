"""
"""

unit_library = {
    "Area": {
        "Square kilometer": "km\u00B2",
        "Square meter": "m\u00B2",
        "Square mile": "mi\u00B2",
        "Square yard": "yd\u00B2",
        "Square foot": "ft\u00B2",
        "Square inch": "in\u00B2",
        "Hectare": "ha",
        "Acre": "ac"
    },
    "Data Transfer Rate": {
        "Bit per second": "b/s",
        "Kilobit per second": "Kb/s",
        "Kilobyte per second": "KB/s",
        "Kibibit per second": "Kib/s",
        "Megabit per second": "Mb/s",
        "Megabyte per second": "MB/s",
        "Mebibit per second": "Mib/s",
        "Gigabit per second": "Gb/s",
        "Gigabyte per second": "GB/s",
        "Gibibit per second": "Gib/s",
        "Terabit per second": "Tb/s",
        "Terabyte per second": "TB/s",
        "Tebibit per second": "Tib/s"
    },
    "Digital Storage": {
        "Bit": "b",
        "Kilobit": "Kb",
        "Kibibit": "Kib",
        "Megabit": "Mb",
        "Mebibit": "Mib",
        "Gigabit": "Gb",
        "Gibibit": "Gib",
        "Terabit": "Tb",
        "Tebibit": "Tib",
        "Petabit": "Pb",
        "Pebibit": "Pib",
        "Byte": "B",
        "Kilobyte": "KB",
        "Kibibyte": "KiB",
        "Megabyte": "MB",
        "Mebibyte": "MiB",
        "Gigabyte": "GB",
        "Gibibyte": "GiB",
        "Terabyte": "TB",
        "Tebibyte": "TiB",
        "Petabyte": "PB",
        "Pebibyte": "PiB"
    },
    "Energy": {
        "Joule": "J",
        "Kilojoule": "kJ",
        "Gram calorie": "cal",
        "Kilocalorie": "kcal",
        "Watt hour": "Wh",
        "Kilowatt hour": "kWh",
        "Electronvolt": "eV",
        "British thermal unit": "Btu",
        "US therm": "therm",
        "Foot-pound": "ft\u00B7lbs"
    },
    "Frequency": {
        "Hertz": "Hz",
        "Kilohertz": "kHz",
        "Megahertz": "MHz",
        "Gigahertz": "GHz"
    },
    "Fuel Economy": {
        "Miles per gallon": "mpg",
        "Miles per gallon (Imperial)": "mpg(I)",
        "Kilometer per liter": "km/L",
        "Liter per 100 kilometers": "L/100km"
    },
    "Length": {
        "Kilometer": "km",
        "Meter": "m",
        "Centimeter": "cm",
        "Millimeter": "mm",
        "Micrometer": "\u03BCm",
        "Nanometer": "nm",
        "Mile": "mi",
        "Yard": "yd",
        "Foot": "ft",
        "Inch": "in",
        "Nautical Mile": "M"
    },
    "Mass": {
        "Metric ton": "t",
        "Kilogram": "kg",
        "Gram": "g",
        "Milligram": "mg",
        "Microgram": "\u03BCg",
        "Imperial ton": "long ton",
        "US ton": "short ton",
        "Stone": "st",
        "Pound": "lb",
        "Ounce": "oz"
    },
    "Plane Angel": {
        "Arcsecond": "\"",
        "Degree": "d\u00B0",
        "Gradian": "gon",
        "Milliradian": "mrad",
        "Minute of Arc": "'",
        "Radian": "rad"
    },
    "Pressure": {
        "Bar": "bar",
        "Pascal": "Pa",
        "Pound-force per square inch": "psi",
        "Standard atmosphere": "atm",
        "Torr": "Torr"
    },
    "Speed": {
        "Miles per hour": "mph",
        "Foot per second": "ft/s",
        "Meter per second": "m/s",
        "Kilometer per hour": "km/h",
        "Knot": "kn"
    },
    "Temperature": {
        "Degree Celsius": "\u00B0C",
        "Fahrenheit": "\u00B0F",
        "Kelvin": "K"
    },
    "Time": {
        "Nanosecond": "ns",
        "Microsecond": "\u03BCs",
        "Millisecond": "ms",
        "Second": "s",
        "Minute": "min",
        "Hour": "h",
        "Day": "day(s)",
        "Week": "week(s)",
        "Month": "month(s)",
        "Calender year": "year(s)",
        "Decade": "dec",
        "Century": "c"
    },
    "Volume": {
        "US liquid gallon": "US gal",
        "US liquid quart": "US qt",
        "US liquid pint": "US pt",
        "US legal cup": "US cup",
        "US fluid ounce": "US fl oz",
        "US tablespoon": "US tbsp",
        "US teaspoon": "US tsp",
        "Cubic meter": "m\u00B3",
        "Liter": "L",
        "Milliliter": "mL",
        "Imperial Gallon": "imp gal",
        "Imperial quart": "imp qt",
        "Imperial pint": "imp pt",
        "Imperial cup": "imp cup",
        "Imperial fluid ounce": "imp fl oz",
        "Imperial tablespoon": "imp tbsp",
        "Imperial teaspoon": "imp tsp",
        "Cubic foot": "ft\u00B3",
        "Cubic inch": "in\u00B3"
    }
}

conversion_library = {
    # area
    "Square kilometer": {
        "Square kilometer": lambda value: value,
        "Square meter": lambda value: value * 10**6,
        "Square mile": lambda value: value / 2.59,
        "Square yard": lambda value: value * 1.196 * 10**6,
        "Sqaure foot": lambda value: value * 1.076 * 10**7,
        "Square inch": lambda value: value * 1.55 * 10**9,
        "Hectare": lambda value: value * 100,
        "Acre": lambda value: value * 247.1
    },
    "Square meter": {
        "Square kilometer": lambda value: value / 10**6,
        "Square meter": lambda value: value,
        "Square mile": lambda value: value / (2.59 * 10**6),
        "Square yard": lambda value: value * 1.196,
        "Sqaure foot": lambda value: value * 10.764,
        "Square inch": lambda value: value * 1550,
        "Hectare": lambda value: value / 10000,
        "Acre": lambda value: value / 4047
    },
    "Square mile": {
        "Square kilometer": lambda value: value * 2.59,
        "Square meter": lambda value: value * 2.59 * 10**6,
        "Square mile": lambda value: value,
        "Square yard": lambda value: value * 3.098 * 10**6,
        "Sqaure foot": lambda value: value * 2.788 * 10**7,
        "Square inch": lambda value: value * 4.014 * 10**9,
        "Hectare": lambda value: value * 259,
        "Acre": lambda value: value * 640
    },
    "Square yard": {
        "Square kilometer": lambda value: value / (1.196 * 10**6),
        "Square meter": lambda value: value / 1.196,
        "Square mile": lambda value: value / (3.098 * 10**6),
        "Square yard": lambda value: value,
        "Sqaure foot": lambda value: value * 9,
        "Square inch": lambda value: value * 1296,
        "Hectare": lambda value: value / 11960,
        "Acre": lambda value: value / 4840
    },
    "Square foot": {
        "Square kilometer": lambda value: value / (1.076 * 10**7),
        "Square meter": lambda value: value / 10.764,
        "Square mile": lambda value: value / (2.788 * 10**7),
        "Square yard": lambda value: value / 9,
        "Sqaure foot": lambda value: value,
        "Square inch": lambda value: value * 144,
        "Hectare": lambda value: value / 107600,
        "Acre": lambda value: value / 43560
    },
    "Square inch": {
        "Square kilometer": lambda value: value / (1.55 * 10**9),
        "Square meter": lambda value: value / 1550,
        "Square mile": lambda value: value / (4.014 * 10**9),
        "Square yard": lambda value: value / 1296,
        "Sqaure foot": lambda value: value / 144,
        "Square inch": lambda value: value,
        "Hectare": lambda value: value / (1.55 * 10**7),
        "Acre": lambda value: value / (6.273 * 10**6)
    },
    "Hectare": {
        "Square kilometer": lambda value: value / 100,
        "Square meter": lambda value: value * 10000,
        "Square mile": lambda value: value / 259,
        "Square yard": lambda value: value * 11960,
        "Sqaure foot": lambda value: value * 107600,
        "Square inch": lambda value: value * 1.55 * 10**7,
        "Hectare": lambda value: value,
        "Acre": lambda value: value * 2.471
    },
    "Acre": {
        "Square kilometer": lambda value: value / 247.1,
        "Square meter": lambda value: value * 4047,
        "Square mile": lambda value: value / 640,
        "Square yard": lambda value: value * 4840,
        "Sqaure foot": lambda value: value * 43560,
        "Square inch": lambda value: value * 6.273 * 10**6,
        "Hectare": lambda value: value / 2.471,
        "Acre": lambda value: value
    }
}

def types() -> list[str]:
    """
    Returns all unit types as a list.

    Returns:
        (list[str]): All unit types.
    """
    return list(unit_library.keys())


def units(unit_type: str) -> list[str]:
    """
    Returns all units for a given unit type.

    Parameters:
        unit_type (str): Type of unit.
    Returns:
        (list[str]): All units of the given type.
    """
    try:
        return list(unit_library[unit_type].keys())
    except:
        print("Given unit type not found in unit library.")
        return []


def symbol(unit: str) -> str:
    """
    Returns the unit symbol for the given unit.

    Parameters:
        unit: Name of the unit of measurement.
    Returns:
        (str): The unit symbol of the given unit. If unit not found, returns '--'.
    """
    # find given unit in library
    for type in unit_library:
        try:
            return unit_library[type][unit]
        except:
            continue

    # unit not found
    print("Given unit not found in unit library.")
    return "--"

