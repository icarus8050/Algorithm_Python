# 풍선 터뜨리기 (https://www.acmicpc.net/problem/2346)

import sys

n = int(sys.stdin.readline().strip())

balloons = [(index + 1, val) for index, val in enumerate(map(int, sys.stdin.readline().split()))]
deleted = []
location = 0

while len(balloons) != 1:
    balloon = balloons.pop(location)
    deleted.append(balloon[0])
    length = len(balloons)

    move = balloon[1]
    if move > 0:
        move -= 1

    location += move

    if location < 0:
        location = length + (location % length)

    location %= length

deleted.append(balloons.pop(0)[0])
print(*deleted)