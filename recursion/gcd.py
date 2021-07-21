"""
 Euclidean algorithm to find the Greatest Common Divisor/Denominator/Prime Factor
"""


def gdc(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers'
    if b == 0:
        return a
    return gdc(b, a % b)


print(gdc(48, 18))

