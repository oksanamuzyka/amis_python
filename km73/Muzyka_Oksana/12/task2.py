a = float(input('Enter number: '))
n = int(input('Enter degree of number: '))
def power(a,n):
    if n < 0:
        a = 1.0/a
        n = -n
    res = 1
    while n > 0:
        res = res * a
        n = n-1
    return res
print(power(a,n))
