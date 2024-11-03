
sentence = input("Enter a Sentence : ")
Upper_count, Lower_count = 0, 0

for char in sentence:
    if char.isupper():
        Upper_count += 1
    elif char.islower():
        Lower_count += 1

print("Upper Case : ", Upper_count)
print("Lower Case : ", Lower_count)