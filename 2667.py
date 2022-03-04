

n = int(input())
arr = []


xx = [0, 0, -1, 1]
yy = [-1, 1, 0, 0]


def homeNumber(x, y):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False

    if(arr[x][y] == '1'):
        global count
        count += 1
        arr[x][y] = '0'
        for i in range(4):
            homeNumber(x+xx[i], y+yy[i])
        return True
    return False


count = 0

for i in range(n):
    s = input()
    arr1 = list(s)
    arr.append(arr1)

numArr = []
total = 0
for i in range(n):
    for j in range(n):
        if(homeNumber(i, j)):
            numArr.append(count)
            count = 0
            total += 1
print(total)
numArr.sort()
for i in numArr:
    print(i)
