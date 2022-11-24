
def GCD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)
a = 50
b = 130
print(GCD(a,b))