# 회사에 있는 사람 (https://www.acmicpc.net/problem/7785)

import sys

n = int(sys.stdin.readline().strip())
company = set()
for i in range(n):
    record = sys.stdin.readline().split()

    if record[1] == 'enter':
        company.add(record[0])
    else:
        company.remove(record[0])

ans = sorted(company, reverse=True)
for v in ans:
    print(v)
