def avg(*args):
    return [sum(args)/len(args), [num for num in args]]


test = avg(10, 10, 12)
print(f" avg of is/are{test[0]}")
