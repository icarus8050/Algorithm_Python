# 차집합 (https://www.acmicpc.net/problem/1822)

import sys

n, m = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
c = a - b
print(len(c))
print(*sorted(c))