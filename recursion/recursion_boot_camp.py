

# 1. greatest common divisor

def gcd(x, y):
    print("x: ", x)
    print("y: ", y)
    print("\n")
    return x if y == 0 else gcd(y, x % y)

print(gcd(36, 156))


















