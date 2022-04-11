def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ""
    for name, quantities in sorted_cheeses:
        sort = sorted(quantities, reverse=True)
        # print(name, end="\n")
        # print(*sort, sep="\n")
        result += name + "\n"
        result += "\n".join([str(el) for el in sort]) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
