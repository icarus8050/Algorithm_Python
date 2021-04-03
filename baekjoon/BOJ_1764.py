# 듣보잡 (https://www.acmicpc.net/problem/1764)

import sys

n, m = map(int, sys.stdin.readline().split())
ans = list()
people = set()

for i in range(n):
    p = sys.stdin.readline().strip()
    people.add(p)

for i in range(m):
    p = sys.stdin.readline().strip()
    if p in people:
        ans.append(p)

ans = sorted(ans)
print(len(ans))
for v in ans:
    print(v)
