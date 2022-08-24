def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10

def from_decimal(n, b):
    result = 0
    multiplier = 1
    l = len(n)

    for i in range(l-1, -1, -1):
        if val(n[i]) < b:
            result += val(n[i])*multiplier
            multiplier = b * multiplier
    return result

def to_decimal(n, b):
    result = 0
    multiplier = 1
    while n>0:
        result += n%(10*multiplier)
        multiplier = b
        n/=10
    return int(result)
from_decimal('43', 10)
print(from_decimal('43', 10))
print(from_decimal('43', 10))

print(to_decimal(101011, 10))