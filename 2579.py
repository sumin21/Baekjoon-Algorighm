num = int(input())

arr = [0]
dp = [0 for i in range(num+1)]

for i in range(num):
    n = int(input())
    arr.append(n)

dp[1] = arr[1]
if(num > 1):
    dp[2] = arr[1] + arr[2]

if(num > 2):
    for i in range(3, num+1):
        a = dp[i-3] + arr[i-1] + arr[i]
        b = dp[i-2] + arr[i]
        dp[i] = max(a, b)

print(dp[num])

# 계단 개수가 1 or 2일때의 경우 체크해야함 (주의)
