'''
문제를 잘 읽자...!
4 6
1 2 3 4 5 6
6 5 4 3 2 1
3 2 7 9 2 5
4 5 6 3 2 1
위와 같은 데이터를 이해하지 못해 어려움을 겪었다.
최대 3개의 치킨을 고른다고 했기에, 처음엔 당연히 arr[i][j]에서 i를 3개 선택하고, 거기에서의 최댓값들을 고르는 것으로 생각했다.
그러다 보니 테스트 케이스의 답인 25가 나오질 않아 너무 당황스러웠다.
문제를 몇 번씩 다시 봐도 눈에 들어오지 않아서... 다른 사람들의 접근을 보고서야 아차싶은 생각이 들었다.
사람의 만족도가 아닌 "치킨"을 선택하는게 먼저였다.
위와 같은 케이스에서는 총 6가지의 치킨이 있고, 이 중 최대 3개의 치킨을 선택해 각 치킨에 대한 사람들의 만족도의 총합을 구하는 것이었다..!
2번, 4번, 6번 치킨을 고른다면 2(2/4번 사람, 5 + 5), 4(3번 사람, 9), 6(1번 사람, 6) -> 5 + 5 + 9 + 6으로 25가 나온다.
조합으로도 풀 수 있을 것 같지만... 치킨 M의 개수는 최대 30이다.
30으로 잡더라도 30 x 30 x 30 = 27000이다. O(N^3)의 완전 탐색이 가능했다!
'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_value = 0

for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            value_for_selected_chicken = sum([max(arr[l][i], arr[l][j], arr[l][k]) for l in range(N)])
            max_value = max(max_value, value_for_selected_chicken)

print(max_value)