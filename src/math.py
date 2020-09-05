
def gcd(a,b):
    """Greatest common divisor of a and b

    Args:
        a (number): first value
        b (number): second value

    Returns:
       gcd call : recursive gcd function
    """
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return (a*b) / gcd(a,b)

def add_fractions(a : list, b : list):
    denom = lcm(a[1],b[1])
    c = {denom/(a[1]*a[0]), denom/(b[1]*b[0])}
    return c

print(gcd(11,5))
print(gcd(8,6))
print(lcm(8,6))
print(add_fractions([3,4], [7,8]))