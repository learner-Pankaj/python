
num = int(input('Enter a number : ')) #10
for i in range(1, num+1):
    if(num%i==0):
        if(i%2==0):
            print(i," is even")
        else:
            print(i," is odd")
            