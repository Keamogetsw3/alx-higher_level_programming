#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decs = [romans[num] for num  in roman_string]
    results = 0
    for i in range(len(decs)):
        results += decs[i]
        if decs[i - 1] < decs[i] and i != 0:
            results -= (decs[i - 1] + decs[i - 1])
    return results
