class Converter:

    def convert(self, value, from_unit, to_unit):

        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        conversions = {

            # Length
            ("km", "m"): 1000,
            ("m", "km"): 0.001,

            ("cm", "m"): 0.01,
            ("m", "cm"): 100,

            ("km", "miles"): 0.621371,
            ("miles", "km"): 1.60934,

            # Weight
            ("kg", "g"): 1000,
            ("g", "kg"): 0.001,

            ("kg", "lbs"): 2.20462,
            ("lbs", "kg"): 0.453592,

            # Time
            ("hours", "minutes"): 60,
            ("minutes", "hours"): 1 / 60,

            ("minutes", "seconds"): 60,
            ("seconds", "minutes"): 1 / 60,
        }

        factor = conversions.get((from_unit, to_unit))

        if factor is None:
            return "Conversion not supported."

        return value * factor