#int -> boolean
def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""

    if n == 42:
        return True
    elif n < 42:
        return False
    else:
        if n % 5 == 0:
            if bears(n - 42):
                return True
        if n % 2 == 0:
            if bears(n // 2):
                return True
        if n % 3 == 0 or n % 4 == 0:
            digit1 = int(str(n)[-1:])
            digit2 = int(str(n)[len(str(n)) - 2])

            print(digit1)
            print(digit2)
            print(n - digit1*digit2)

            if digit1 * digit2 != 0:
                if bears(n - digit1*digit2):
                  return True
        return False