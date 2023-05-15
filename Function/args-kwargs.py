def avg(*args):
    return [sum(args)/len(args), [num for num in args]]


test = avg(10, 10, 12)
print(f" avg of {test[1]} is/are {test[0]}")


def example(**kwarg):
    if 'numbers' in kwarg:
        [sum(kwarg['numbers'])/len(kwarg['numbers']),[values for values in kwarg['numbers']]]

ask=input("please enter some numbers to get avg").split()
test2 = avg([int(any) for any in ask])

print(f" avg of {test2[1]} is/are {test2[0]}")