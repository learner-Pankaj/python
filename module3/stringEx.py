

words = input().split(" ")
words.sort()
sorted_words = sorted(set(words))
print(" ".join(sorted_words))