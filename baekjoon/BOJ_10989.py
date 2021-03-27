# 수 정렬하기 3 (https://www.acmicpc.net/problem/10989)

import sys

n = int(sys.stdin.readline())
l = [0] * 10001

for _ in range(n):
    l[int(sys.stdin.readline().strip())] += 1

for i in range(10001):
    if l[i] > 0:
        sys.stdout.write((str(i) + "\n") * l[i])
