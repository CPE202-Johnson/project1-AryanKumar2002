import math

numbers = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}


#(int, int) -> number in different base
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if b <= 16:
        final = converter(num, b)

        #Checking for special case when empty string is output
        if final == "":
            return "0"
        else:
            return final
    
#(int, int) -> number in different base
#Converts base recursively
def converter(num, b):
    if num == 0:
        return ""

    q = num // b

    if b > 10 and num % b > 9:
        remainder = numbers[num % b] #convering to letters if remainder is in double digits
    else:
        remainder = num % b
    return str(converter(q, b)) + str(remainder) #recursively call function to have remainders in reverse

