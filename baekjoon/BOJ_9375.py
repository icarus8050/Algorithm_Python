# 패션왕 신해빈 (https://www.acmicpc.net/problem/9375)

import sys

t = int(sys.stdin.readline().strip())

while t > 0:
    t -= 1

    n = int(sys.stdin.readline().strip())
    closet = {}
    ans = 1

    for i in range(n):
        clothes = sys.stdin.readline().split()
        closet[clothes[1]] = closet.get(clothes[1], 0) + 1

    for i in closet.values():
        ans *= (i + 1)

    print(ans - 1)
