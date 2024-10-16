for i in range(1000, 3001):
    flag = 0
    num = i
    while(num!=0):
        rem = num%10
        num = int (num/10)
        if rem%2==0:
            flag = 1
        else:
            flag = 0
            break
    if flag==1:
        print(i, end=", ")