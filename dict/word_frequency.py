from collections import Counter

sentence = "Linux is great and Linux is powerful"
words = sentence.lower().split()
freq = Counter(words)
print(freq)
for data,value in freq.items():
    print(data,value)
