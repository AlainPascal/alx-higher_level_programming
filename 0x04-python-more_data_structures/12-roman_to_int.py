#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return (0)

    r_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    r_num = 0

    for i in range(len(roman_string)):
        if i > 0 and r_dict[roman_string[i]] > r_dict[roman_string[i - 1]]:
            r_num += r_dict[roman_string[i]] - 2 * r_dict[roman_string[i - 1]]
        else:
            r_num += r_dict[roman_string[i]]
    return (r_num)