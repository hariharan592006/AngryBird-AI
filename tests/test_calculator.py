from core.tools.calculator import Calculator

calc = Calculator()

tests = [
    "25*18",
    "100/5",
    "20+40",
    "10**2",
    "50%6"
]

for expression in tests:

    print(expression)

    print(calc.calculate(expression))

    print("-" * 30)