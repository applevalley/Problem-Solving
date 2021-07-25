# 로프는 각자 들 수 있는 중량이 다를 수 있다. 여러 로프를 병렬로 연결하면 중량을 나눌 수 있는데, k개의 로프로 w만큼의 무게를 들어올릴 때 각 로프에 w/k만큼이 걸린다.
# 로프를 통해 들 수 있는 최대 중량은?

# 각각의 로프 중 가장 한계 중량이 낮은 로프를 기준으로 삼을 수 있을 것 같다.
# 각 로프에는 w/k만큼의 부하가 가해지는데, 이것이 각 로프가 가진 한계치를 넘을 수는 없다.
# 2개의 로프와 각 로프의 한계치가 10 / 40일 때, w/k(2)의 한계치는 10이다. 따라서 최대 중량은 20이 된다.

# 로프의 수치들을 정렬하고, w/k는 정렬된 첫 인덱스의 요소(가장 작은)라는 등식을 세워서 이를 풀어낸다.

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()
maximum_weight = 0

for i in range(N):
    temp = ropes[i] * (N - i)
    print(temp)
    if maximum_weight < temp:
        maximum_weight = temp

print(maximum_weight)