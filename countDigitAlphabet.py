text = input("Enter Alphanumeric word : ")
alphabet = 0
digit = 0

for char in text:
    if char.isalpha():
        alphabet += 1
    elif char.isdigit():
        digit += 1

print("Alphabets : ", alphabet)
print("Digits : ", digit)