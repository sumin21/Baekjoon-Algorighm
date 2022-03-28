nn = input()
n = int(nn)


arr1 = list(nn)
lens = len(arr1)
a = 0

if(n > 9):
    a = n - (9*(lens))
if(a < 0):
    a = 0
result = 0
for i in range(a, n+1):
    arr = list(map(int, list(str(i))))
    k = i
    for j in arr:
        k += j
    if(k == n):
        result = i
        break

if(n == 1):
    result = 0
print(result)
