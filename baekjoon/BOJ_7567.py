# 그릇 (https://www.acmicpc.net/problem/7567)

s = input()

ans = 10
for i, c in enumerate(s[1:]):
    if s[i] == c:
        ans += 5
    else:
        ans += 10

print(ans)
