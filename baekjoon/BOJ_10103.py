# 주사위 게임 (https://www.acmicpc.net/problem/10103)

import sys

a = 100
b = 100

n = int(sys.stdin.readline().strip())
for i in range(n):
    aS, bS = map(int, sys.stdin.readline().split())

    if aS > bS:
        b -= aS
    elif bS > aS:
        a -= bS

print(a)
print(b)
