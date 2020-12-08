import sys; sys.stdin = open('1476.txt')

E, S, M = map(int, input().split())
a, b, c, cnt = 0, 0, 0, 0

E -= 1
S -= 1
M -= 1

for i in range(15 * 28 * 19):
    if i % 15 == E and i % 28 == S and i % 19 == M:
        print(i + 1)
        break