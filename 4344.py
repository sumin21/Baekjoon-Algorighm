n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    avr = sum(arr[1:]) / arr[0]
    tmp = 0
    for j in arr[1:]:
        if(j > avr):
            tmp += 1
    result = round((tmp/arr[0])*100, 3)
    print(str(format(result, ".3f")) + '%')
