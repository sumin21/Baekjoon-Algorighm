def emdck(a):
    k = list(str(a))
    n = 10
    dif2 = 10
    tmp = True
    for i in k:
        if (n != 10):
            dif1 = n - int(i)
            if (dif1 != dif2 and dif2 != 10):
                tmp = False
                break
            dif2 = dif1
        n = int(i)
    return tmp


n = int(input())
count = 0
for i in range(1, n+1):
    if(emdck(i)):
        count += 1

print(count)
