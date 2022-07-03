def convertToBaseX(base, num: int) -> str:
    from math import log

    if num == 0:
        return str(0)

    converted = ''

    if str(num)[0] == '-':
        num = int(str(num)[1::])
        converted += '-'

    dict = {i: '0123456789ABCDEF'[i] for i in range(16)}
    power = int(log(num, base))

    for pow in range(power, -1, -1):
        converted += dict[num // (base ** pow)]
        num %= base ** pow

    return converted
  
