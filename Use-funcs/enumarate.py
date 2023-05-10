sentence = "hey it is something called a sentence"

for index, item in enumerate(sentence):
    print(f"word {item} indexed at {index}")

split_sen= sentence.split()

print(f"\nsentence has {len(split_sen)} words in it")