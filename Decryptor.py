from collections import Counter

sentence = "how to count all the amount of each letter in a sentence"
counts = Counter(sentence)

for char, count in counts.items():
    print(f"{char}: {count}")
