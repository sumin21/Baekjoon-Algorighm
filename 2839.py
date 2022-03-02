n = int(input())

dp = [0 for i in range(5001)]
dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
    if(dp[i-3] == 0 or dp[i-5] == 0):
        dp[i] = max(dp[i-3], dp[i-5]) + 1
        if(dp[i] == 1):
            dp[i] = 0
    else:
        dp[i] = min(dp[i-3], dp[i-5]) + 1

if(dp[n] != 0):
    print(dp[n])
else:
    print(-1)
