# 알파벳 찾기 (https://www.acmicpc.net/problem/10809)

s = input()
alphabets = [-1] * 26
cache = set()

for idx, ch in enumerate(s):
    if ch not in cache:
        cache.add(ch)
        alphabets[ord(ch) - 97] = idx

print(*alphabets)
