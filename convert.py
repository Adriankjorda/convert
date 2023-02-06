# convert.py

import sys

def convert_inches_to_metric(value, to_unit):
    if to_unit == 'mm':
        return value * 25.4
    elif to_unit == 'cm':
        return value * 2.54
    elif to_unit == 'm':
        return value * 0.0254
    else:
        raise ValueError(f"Invalid unit: {to_unit}")

def run_tests():
    test_cases = [
        (3, 'mm', 76.2),
        (3, 'cm', 7.62),
        (3, 'm', 0.0762),
    ]
    for value, to_unit, expected in test_cases:
        result = convert_inches_to_metric(value, to_unit)
        assert result == expected, f"For {value} inches to {to_unit}, expected {expected} but got {result}"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python convert.py VALUE UNIT [-t]")
        sys.exit(1)
    value = float(sys.argv[1])
    to_unit = sys.argv[2][1:]
    if len(sys.argv) == 4 and sys.argv[3] == '-t':
        run_tests()
    else:
        result = convert_inches_to_metric(value, to_unit)
        print(f"{result} {to_unit}")
