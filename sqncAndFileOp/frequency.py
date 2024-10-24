s = input("Enter a sentence :: ")
l = len(s)

visited = [False] * l

for i in range(l):
    if visited[i]:
        continue

    count = 1
    for j in range(i+1, l):
        if(s[i]==s[j]):
            count += 1
            visited[j] = True

    print(f"{s[i]} :: {count}")

