# 연속합 (https://www.acmicpc.net/problem/1912)

import sys

n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().split()))
dp = [0] * (len(l) + 1)

dp[1] = l[0]
ans = dp[1]
for i in range(2, n + 1):
    if dp[i - 1] + l[i - 1] > l[i - 1]:
        dp[i] = dp[i - 1] + l[i - 1]
    else:
        dp[i] = l[i - 1]

    ans = max(ans, dp[i])

print(ans)