n = int(input())

for i in range(n):
    s = list(input().split())
    arr = list(s[1])
    arr2 = ''
    for j in arr:
        for k in range(int(s[0])):
            arr2 += j
    print(arr2)
