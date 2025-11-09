def sum_powers(x, n):
    total_sum = 0
    term_strings = []
    for i in range(n + 1):
        term = x ** i
        total_sum += term
        if i == 0:
            term_strings.append("1")
        elif i == 1:
            term_strings.append(str(x))
        else:
            term_strings.append(f"{x}^{i}")
    expression = " + ".join(term_strings)

    return expression, total_sum


x = 2; n = 5
expression_str, result_sum = sum_powers(x, n)
print(f"Обчислення виразу 1+x+x^2+....+x^n для x={x} та n={n}:")
print(f"{expression_str} = {result_sum}")