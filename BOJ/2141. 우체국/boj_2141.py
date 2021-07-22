# 수직선상에 N개의 마을이 있고, i번째 마을에 x명의 사람이 산다.
# 각 사람들까지의 거리의 합(마을까지 거리의 합이 아님)이 최소가 되는 위치에 우체국을 세운다. 어디에다 세우면 될까?

# 각 사람들까지의 거리의 합이 의미하는게 뭘까? 이걸 이해하는데 너무 오랜 시간이 걸렸고, 결국 다른 풀이를 참고하였다.
# 마을 사람들의 합에 대한 중간값을 계산하고, 정렬된 리스트 안에서 인구수를 하나씩 순회해 중간값과 가장 근접한 마을을 선택해야 한다.
# 시간을 두고서 다시 풀어봐야겠다.


import sys

N = int(sys.stdin.readline())
value = 0
ans = 0
arr = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

for i in arr:
    value += i[1]

mid_value = (value // 2)

if value % 2:
    mid_value += 1

temp = 0
for i in range(N):
    temp += arr[i][1]

    if temp >= mid_value:
        print(arr[i][0])
        break