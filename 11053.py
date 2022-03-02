n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dp = [1] * (n+1)
dp[0] = 0

max = 1

for i in range(1, n+1):
    min = 0
    if(i > 1):
        for j in range(0, i):
            if(arr[j] < arr[i]):
                if(min < dp[j]):
                    min = dp[j]
        dp[i] = min + 1

        if(max < dp[i]):
            max = dp[i]
print(max)
