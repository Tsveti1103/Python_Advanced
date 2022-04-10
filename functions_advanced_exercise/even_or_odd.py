def even_odd(*args):
    e_o = 0 if "even" in args else 1
    return [x for x in args[:-1] if x % 2 == e_o]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
