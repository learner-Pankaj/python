str = input("Enter a String :: ")
for index, op in enumerate(str):
    if(index%2==0):
        print(op, end="")
