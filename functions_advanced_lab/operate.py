from functools import reduce

def operate(opr, *args):
    result = None
    if opr == "+":
        result = reduce(lambda x, y: x + y, args)
    elif opr == "-":
        result = reduce(lambda x, y: x - y, args)
    elif opr == "*":
        result = reduce(lambda x, y: x * y, args)
    else:
        result = reduce(lambda x, y: x / y, args)
    return result

# from functools import reduce
#
#
# def operate(opr, *args):
#     result = reduce(lambda x, y: eval(f"{x} {opr} {y}"), args)
#     return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
