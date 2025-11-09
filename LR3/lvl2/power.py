def power(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * power(base, exp - 1)
    else:
        return 1 / power(base, -exp)


b, e = 2, -3
print(f"{b}^{e} = {power(b, e)}")