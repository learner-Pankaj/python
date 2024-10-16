sentence = input()
#split() changes the sentence into list of words
word = sentence.split()
word.sort(key=lambda word: word.lower())
#join back words and make sentence for the user
print(" ".join(word))