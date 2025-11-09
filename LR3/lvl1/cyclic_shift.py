def cyclic_shift(lst, n, times):
    length = len(lst)
    for i in range(times):
        n_mod = n % length
        lst = lst[-n_mod:] + lst[:-n_mod]
        print(f"Після зсуву {i+1}: {lst}")
    return lst


lst = [1, 2, 3, 4, 5]
n = 2
times = 3
print(f"Циклічне зміщення масиву: {lst} на {n} кроків {times} рази")
cyclic_shift(lst, n, times)