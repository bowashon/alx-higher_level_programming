#!/usr/bin/python3
"""function that converts Roman numeral to an integer"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    dic_roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
    result = 0
    prev_value = 0

    for roman_symbol in reversed(roman_string):
        value = dic_roman_to_int.get(roman_symbol, 0)
        if value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value
    return result
