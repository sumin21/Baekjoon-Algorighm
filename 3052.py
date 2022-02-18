arr = []
for i in range(10):
    a = int(input())
    arr.append(a)

# 0~ 41

list = [0 for i in range(42)]

for i in arr:
    k = i % 42
    list[k] = 1

count = 0
for i in list:
    if(i == 1):
        count += 1

print(count)
