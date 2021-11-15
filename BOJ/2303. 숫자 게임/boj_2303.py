from itertools import combinations

N = int(input())
maxIdx, maxV = 0, 0

for i in range(N):
    cards = list(map(int, input().split()))
    possible_list = list(combinations(cards, 3))
    biggest_value = max([sum(i) % 10 for i in possible_list])

    if biggest_value >= maxV:
        maxV = biggest_value
        maxIdx = i + 1

print(maxIdx)