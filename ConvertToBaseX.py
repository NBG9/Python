# Program to convert a decimal number to a number of any base.
def convertToBaseX(base, num: int) -> str:
    from math import log

    if num == 0:
        return str(0)

    # Storing converted value as a String.
    converted = ''

    # Dealing with the negative sign.
    if str(num)[0] == '-':
        num = int(str(num)[1::])
        converted += '-'

    # Creating a dictionary for storing conversion rates.
    dict = {i: '0123456789ABCDEF'[i] for i in range(16)}
    
    # 'power' is the power to which the 'base' must be raised
    # - in order to obtain 'num'
    power = int(log(num, base))

    # Iterating over a range of numbers.
    # Floor-dividing the passed-in value by the base raised to the iterator.
    # Using the result as index of the desired value in the dictionary.
    # Using modulo to reduce 'num' for the next iteration.
    for pow in range(power, -1, -1):
        converted += dict[num // (base ** pow)]
        num %= base ** pow

    return converted
  
