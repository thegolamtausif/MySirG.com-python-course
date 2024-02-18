def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

first = 54
second = 72
print('HCF of', first, 'and', second, 'is', hcf(first, second))