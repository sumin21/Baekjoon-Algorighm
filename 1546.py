n = int(input())
arr = list(map(int, input().split()))

m = max(arr)

# 0-2
for i in range(len(arr)):
    arr[i] = arr[i]/m*100
sum = 0
for i in arr:
    sum += i

avr = sum/len(arr)

print(avr)
