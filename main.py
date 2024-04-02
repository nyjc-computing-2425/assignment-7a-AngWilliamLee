# Write a function to convert numbers to text numerals

def text_numeral(num):
    """
    Given a a positive integer less than 100, returns a string representing the number in text format

    Parameter
    ---------
    num: integer

    Returns
    -------
    string
        num in text format
    """

    NUM_WORD = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }


    if num <= 20:
        return NUM_WORD[num]

    count = 0
    if num > 20:
        check = False
        while not check:
            num += -10
            count += 1
            if num >= 10:
                check = False
            if num < 10:
                check = True

    if count != 0:
        tens = NUM_WORD[count*10]
    else:
        tens = ""
    return str(f"{tens} {NUM_WORD[num]}")







