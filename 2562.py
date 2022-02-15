arr = []
for i in range(9):
    a = int(input())
    arr.append(a)

tmp = max(arr)
tmpIndex = arr.index(tmp) + 1

print(tmp)
print(tmpIndex)
