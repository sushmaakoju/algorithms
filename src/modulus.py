def modulus(x, p):
    if x == 0:
        return 0
    return int(x % p)

def power_mod(x, y, p):
    result = 1
    x = modulus(x, p)
    while y > 0:
        if ((y & 1) == 1):
            result = modulus(result * x, p)
        y = int(y>>1)
        x = modulus(x*x, p)
    return result

print(power_mod(2,5,13))