#(int, int) -> number in different base
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""

    remainder = ''
    finish = ''

    if num == 0:
        finish += str(remainder)
        return finish

    remainder = num % b

    if b > 10 and remainder > 9:
        remainder = chr(remainder + 55) #convering to letters if remainder is in double digits

    return str(convert(num//b, b)) + str(remainder) #recursively call function to have remainders in reverse