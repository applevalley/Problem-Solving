# 문제들을 파란색, 빨간색으로 칠해야 한다. 이를 효율적으로 처리해 작업 횟수를 최소한으로 줄이려면 어떻게 해야 할까?

# 빨파파빨파파빨 과 같은 문제들이 있다면, 빨/파파/빨/파파/빨 이렇게 5번 작업하는 것보다 1~7번까지 파란색/1번 빨/4번 빨/7번 빨 이렇게 색칠하는 것이 더 효율적이다.
# 입력으로 주어지는 배열을 순회하며 어떤 색이 더 많이 입력되는지를 확인한다.
# 더 많은 색상이 밑바탕이 되며, 적은 색상을 칠한 작업의 횟수에 1(많은 색상으로 전체 배열을 칠한 횟수 1)을 더한 값이 최솟값이 된다!

import sys
N = int(sys.stdin.readline())
color = sys.stdin.readline().rstrip()
total_red = color.count('R')
total_blue = color.count('B')
turns_red = 0
turns_blue = 0

for i in range(len(color)):
    if color[i] == 'R' and color[i] != color[i - 1]:
        turns_red += 1
    elif color[i] == 'B' and color[i] != color[i - 1]:
        turns_blue += 1

if total_red >= total_blue:
    cnt = turns_blue + 1
else:
    cnt = turns_red + 1

print(cnt)