from core.tools.converter import Converter

tool = Converter()

tests = [

    (10, "km", "m"),
    (5, "kg", "lbs"),
    (100, "cm", "m"),
    (2, "hours", "minutes"),
    (120, "minutes", "hours"),
]

for value, from_unit, to_unit in tests:

    result = tool.convert(value, from_unit, to_unit)

    print(f"{value} {from_unit} -> {to_unit}")

    print(result)

    print("-" * 30)