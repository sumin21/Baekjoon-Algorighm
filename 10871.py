x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = x[0]
b = x[1]
for i in y:
    if(i < b):
        print(i, end=' ')
