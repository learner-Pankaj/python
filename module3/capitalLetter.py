

# sentence = input("Enter a line : ")
# str = sentence.upper()
# print(str)

lines = []

print("Enter lines of text, to come out from the program type END.")

while True:
    line = input()
    if line == "END":
        break
    lines.append(line.upper())

for line in lines:
    print(line)
