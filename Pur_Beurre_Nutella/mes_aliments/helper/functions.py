'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


def parse_request(info):
    '''parse the information given in entry'''
    parsed_letter = []
    for letter in info:
        if letter not in ("'", "(", ",", ")"):
            parsed_letter.append(letter)
    parsed_info = ''.join(parsed_letter)
    return parsed_info
    
