

def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    q = num
    r = ''
    n = ''
    if q == 0: #base case
        n += str(r)
        return n
    q = num // b #dividing the quotient by the base
    r = num % b
    if b > 10 and r > 9:
        r = chr(r +55)
    n = str(convert(q,b)) + str(r)
    return n
