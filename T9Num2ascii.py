#!/usr/bin/env python3

#use this to decode a T9Num string to ascii
#does not print spaces and could contain a few errors. still beats doing it by hand
#example from hackthebox.eu challenge 'bank heist'
#python T9Num2ascii.py
#Paste cipher with no spaces: 44433399966688277733777332344466484433222444744337779996668827773366655299999966688777777744277733666333844334433444777784447777444669996668877744666887777338443355339998666844335556662225544477772233555666946668666727774447777
#Input: ['4x3', '3x3', '9x3', '6x3', '8x2', '2x1', '7x3', '3x2', '7x3', '3x2', '2x1', '3x1', '4x3', '6x2', '4x1', '8x1', '4x2', '3x2', '2x3', '4x3', '7x1', '4x2', '3x2', '7x3', '9x3', '6x3', '8x2', '2x1', '7x3', '3x2', '6x3', '5x2', '2x1', '9x6', '6x3', '8x2', '7x7', '4x2', '2x1', '7x3', '3x2', '6x3', '3x3', '8x1', '4x2', '3x2', '4x2', '3x2', '4x3', '7x4', '8x1', '4x3', '7x4', '4x3', '6x2', '9x3', '6x3', '8x2', '7x3', '4x2', '6x3', '8x2', '7x4', '3x2', '8x1', '4x2', '3x2', '5x2', '3x2', '9x3', '8x1', '6x3', '8x1', '4x2', '3x2', '5x3', '6x3', '2x3', '5x2', '4x3', '7x4', '2x2', '3x2', '5x3', '6x3', '9x1', '4x1', '6x3', '8x1', '6x3', '7x1', '2x1', '7x3', '4x3', '7x4']
#Decoded: IFYOUAREREADINGTHECIPHERYOUAREOKAOUHAREOFTHEHEISTISINYOURHOUSETHEKEYTOTHELOCKISBELOWGOTOPARIS

from itertools import groupby

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
