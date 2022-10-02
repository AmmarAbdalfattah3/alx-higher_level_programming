#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roma = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_res = 0
    for x in range(len(roman_string)):

        if roma.get(roman_string[x], -1) == -1:
            return 0
        if x != len(roman_string) - 1 and\
            roma[roman_string[x]] < roma[roman_string[x + 1]]:
            roman_res -= roma[roman_string[x]]
        else:
            roman_res += roma[roman_string[x]]
    return roman_res
