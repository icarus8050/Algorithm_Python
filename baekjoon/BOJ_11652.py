# 카드 (https://www.acmicpc.net/problem/11652)

import sys

n = int(sys.stdin.readline().rstrip())
cards = {}

smallCard = 0
bigCount = 0
for i in range(n):
    card = int(sys.stdin.readline().rstrip())
    cards[card] = cards.get(card, 0) + 1

    if cards[card] > bigCount:
        bigCount = cards[card]
        smallCard = card
    elif cards[card] == bigCount and smallCard > card:
        smallCard = card

print(smallCard)
