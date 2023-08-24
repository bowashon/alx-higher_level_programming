#!/usr/bin/python3
import sys
if __name__ == "__main__":
    import calculator_1 as calculator

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        result = calculator.add(a, b)
    elif operator == '-':
        result = calculator.sub(a, b)
    elif operator == '*':
        result = calculator.mul(a, b)
    elif operator == '/':
        result = float(calculator.div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result), end='\n')
