num = range(1, 56)
word = "hello it is mine"

for item in zip(word, num, range(1, 56, 5)):
    print(item)