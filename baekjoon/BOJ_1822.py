# 차집합 (https://www.acmicpc.net/problem/1822)

import sys

n, m = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

for v in b:
    if v in a:
        a.remove(v)

l = len(a)
print(l)
if l != 0:
    print(*sorted(a))
