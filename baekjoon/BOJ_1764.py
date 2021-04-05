# 듣보잡 (https://www.acmicpc.net/problem/1764)

import sys

n, m = map(int, sys.stdin.readline().split())
ans = list()
people_1 = set()
people_2 = set()

for i in range(n):
    p = sys.stdin.readline().strip()
    people_1.add(p)

for i in range(m):
    p = sys.stdin.readline().strip()
    people_2.add(p)

ans = sorted(people_1 & people_2)
print(len(ans))
for v in ans:
    print(v)
