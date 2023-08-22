#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculate

    a = 10
    b = 5

    add_result = calculate.add(a, b)
    sub_result = calculate.sub(a, b)
    mult_result = calculate.mul(a, b)
    div_result = calculate.div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, add_result))
    print("{:d} - {:d} = {:d}".format(a, b, sub_result))
    print("{:d} * {:d} = {:d}".format(a, b, mult_result))
    print("{:d} / {:d} = {:d}".format(a, b, div_result))
