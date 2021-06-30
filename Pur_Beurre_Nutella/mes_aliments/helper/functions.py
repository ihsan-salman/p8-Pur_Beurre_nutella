'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


def parse_request(url):
    parsed_letter = []
    for letter in url:
        if letter not in ("'", "(", ",", ")"):
            parsed_letter.append(letter)
    parsed_info = ''.join(parsed_letter)
    return parsed_info