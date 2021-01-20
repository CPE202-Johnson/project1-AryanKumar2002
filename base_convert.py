#(int, int) -> number in different base
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if b < 17:
        final = converter(num, b)
    
        #Checking for special case when empty string is output
        if final == '':
            return '0'
    
        return final

    
#(int, int) -> number in different base
#Converts base recursively
def converter(num, b):
    remainder = ''

    if num == 0:
        return ''

    remainder = num % b

    if b > 10 and remainder > 9:
        remainder = chr(remainder + 55) #convering to letters if remainder is in double digits

    return str(converter(num//b, b)) + str(remainder) #recursively call function to have remainders in reverse
