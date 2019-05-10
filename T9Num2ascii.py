#!/usr/bin/env python3

#use this to decode a T9Num string to ascii
#example: 222334477788 = CEHRU or something like that
#will not handle consecutive letters from the same number, so sry :(

from itertools import groupby
import sys

finalstring = ['Decoded: ']

def numbercheck(cipher):
    groups = groupby(cipher)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    joined_result = [(",".join("{}x{}".format(label, count) for label, count in result))]
    iterator(joined_result)

def iterator(joined_result):
    for lettermatcher in joined_result:
        lettermatcher = lettermatcher.split(",")
        print(f'Input: {lettermatcher}')
        for match in lettermatcher:
            num2text(match)

def num2text(match):
    decoded = ""
    if str(match) == str('2x1'):
        decoded = "A"
        fulltext(decoded)
    elif str(match) == str('2x2'):
        decoded = "B"
        fulltext(decoded)
    elif str(match) == str('2x3'):
        decoded = "C"
        fulltext(decoded)
    elif str(match) == str('3x1'):
        decoded = "D"
        fulltext(decoded)
    elif str(match) == str('3x2'):
        decoded = "E"
        fulltext(decoded)
    elif str(match) == str('3x3'):
        decoded = "F"
        fulltext(decoded)
    elif str(match) == str('4x1'):
        decoded = "G"
        fulltext(decoded)
    elif str(match) == str('4x2'):
        decoded = "H"
        fulltext(decoded)
    elif str(match) == str('4x3'):
        decoded = "I"
        fulltext(decoded)
    elif str(match) == str('5x1'):
        decoded = "J"
        fulltext(decoded)
    elif str(match) == str('5x2'):
        decoded = "K"
        fulltext(decoded)
    elif str(match) == str('5x3'):
        decoded = "L"
        fulltext(decoded)
    elif str(match) == str('6x1'):
        decoded = "M"
        fulltext(decoded)
    elif str(match) == str('6x2'):
        decoded = "N"
        fulltext(decoded)
    elif str(match) == str('6x3'):
        decoded = "O"
        fulltext(decoded)
    elif str(match) == str('7x1'):
        decoded = "P"
        fulltext(decoded)
    elif str(match) == str('7x2'):
        decoded = "Q"
        fulltext(decoded)
    elif str(match) == str('7x3'):
        decoded = "R"
        fulltext(decoded)
    elif str(match) == str('7x4'):
        decoded = "S"
        fulltext(decoded)
    elif str(match) == str('8x1'):
        decoded = "T"
        fulltext(decoded)
    elif str(match) == str('8x2'):
        decoded = "U"
        fulltext(decoded)
    elif str(match) == str('8x3'):
        decoded = "V"
        fulltext(decoded)
    elif str(match) == str('9x1'):
        decoded = "W"
        fulltext(decoded)
    elif str(match) == str('9x2'):
        decoded = "X"
        fulltext(decoded)
    elif str(match) == str('9x3'):
        decoded = "Y"
        fulltext(decoded)
    elif str(match) == str('9x4'):
        decoded = "Z"
        fulltext(decoded)

def fulltext(decoded):
    global finalstring
    finalstring.append(str(decoded))

def main():
    cipher = input("Paste cipher with no spaces: ")
    numbercheck(cipher)
    decoded_solution = ''.join(finalstring)
    print(decoded_solution)

main()





#Key

#('2', 1) == "A"
#('2', 2) == "B"
#('2', 3) == "C"
#('3', 1) == "D"
#('3', 2) == "E"
#('3', 3) == "F"
#('4', 1) == "G"
#('4', 2) == "H"
#('4', 3) == "I"
#('5', 1) == "J"
#('5', 2) == "K"
#('5', 3) == "L"
#('6', 1) == "M"
#('6', 2) == "N"
#('6', 3) == "O"
#('7', 1) == "P"
#('7', 2) == "Q"
#('7', 3) == "R"
#('7', 4) == "S"
#('8', 1) == "T"
#('8', 2) == "U"
#('8', 3) == "V"
#('9', 1) == "W"
#('9', 2) == "X"
#('9', 3) == "Y"
#('9', 4) == "Z"
