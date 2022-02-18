a = int(input())
b = int(input())
c = int(input())

n = a*b*c
tmp = 0
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while(n != 0):
    tmp += 1
    num = n % (10**tmp)
    newNum = int(num/(10**(tmp-1)))
    n = n - newNum*(10**(tmp-1))
    arr[newNum] += 1

for i in arr:
    print(i)
