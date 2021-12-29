'''
N개의 노드 중에서 두 개의 치킨집을 정했을 때, 전체 노드들에 대한 왕복 거리의 최솟값을 구하자!
노드가 4개라고 한다면, (1, 2)부터 (3, 4)까지 비교해야 하기에 필연적으로 O(N^2) 이상의 복잡도가 발생할 것이다.
다행히도 노드 N의 최댓값은 100이기에 문제를 해결하는 데에는 문제가 없을 것이라 생각했다!
모든 노드를 비교해가며 선택된 두 치킨집 각각에 대해 BFS를 돌렸고, 방문한 노드들의 거리가 담긴 배열을 반환하게 하였다.
반환된 두 배열을 가지고 각 n번째 원소의 최솟값만을 담은 최소 거리 배열을 다시 만들어주었다!

5 4
1 3
4 2
2 5
3 2
테스트 케이스로 비교하면...
1, 2번 치킨집을 선택했을 때, 각 치킨집을 대상으로 BFS를 돌린 결과 배열은....
[0, 0, 2, 1, 3, 3]
[0, 2, 0, 1, 1, 1] 와 같다.
여기서 최솟값들만 남기면
[0, 0, 0, 1, 1, 1]이다!
1, 2번은 치킨집 자체이기 때문에 거리가 0이고, 3번은 1번 치킨집에서 바로 갈 수 있기에 거리가 1, 4/5번은 2번 치킨집에서 바로 갈 수 있어서 1이다.
이렇게 만들어진 최소 거리 배열의 모든 원소를 더한 합에 2를 곱한 값이(왕복이니까) 두 치킨집을 통한 거리의 합이다.
거리 합의 최솟값을 담기 위해 선언한 변수 min_value가 두 치킨집의 거리 합보다 더 커서 변경이 일어날 때, 두 치킨집의 번호와 변경된 거리를 리스트로 묶어 저장했고,
마지막에 정렬을 해주었다.

이렇게 답을 구했는데.... 개선할 점이 많을 것 같다.
플로이드-와셜 알고리즘을 통해 풀이가 가능하다고 한다! 이 쪽이 시간이 더 적게 걸린다고 한다.
알고리즘을 공부한 후 다시 풀어봐야겠다.
'''

from collections import deque

def search(x, arr):
    start_point = x
    Q = deque()
    Q.append(x)

    while Q:
        p = Q.popleft()
        for w in G[p]:
            if w != start_point and not arr[w]:
                arr[w] = arr[p] + 1
                Q.append(w)

    return arr


N, M = map(int, input().split())
G = [[] * (M + 1) for _ in range(N + 1)]
min_value = 0xffffff
answer_list = []

for _ in range(M):
    start, end = map(int, input().split())
    G[start].append(end)
    G[end].append(start)

for i in range(1, N):
    for j in range(i + 1, N + 1):
        first_chicken_shop = search(i, [0] * (N + 1))
        second_chicken_shop = search(j, [0] * (N + 1))
        selected_minimum_distance = [min(i, j) for i, j in zip(first_chicken_shop, second_chicken_shop)]
        sum_of_distance = sum(selected_minimum_distance) * 2

        if min_value >= sum_of_distance:
            min_value = min(min_value, sum(selected_minimum_distance) * 2)
            answer_list.append([i, j, min_value])

answer_list.sort(key=lambda x: (x[2], x[0], x[1]))
print(*answer_list[0])


