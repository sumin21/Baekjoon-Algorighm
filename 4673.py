li = [0 for i in range(20001)]

for i in range(1, 10000):
    arr = list(str(i))
    sum = 0
    for k in arr:
        sum += int(k)
    a = i + sum  # a : index

    li[a] = 1

for j in range(1, 10001):
    if(li[j] == 0):
        print(j)
