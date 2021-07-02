# 아파트 a층의 b호에 거주하려면 a-1층의 1호부터 b호까지 거주자의 합만큼 사람을 데려와야 한다.
# 이거 한 집에만 해당되는 것이 아니겠구나라는 생각이 든다.
# 2층의 3호 거주자는 1층의 1호부터 3호까지 거주자의 합만큼 사람을 데려와야 한다.
# 여기서 1층의 3호 거주자는 또 0층의 1호부터 3호까지 거주자의 합만큼 사람을 데리고 있어야 한다.
# 재귀로 가능할까? 최대 깊이와 최대 호수가 14로 작은 편이기에 가능할지도 모르겠다라는 생각이 들지만 깊이를 초과할 수도 있다.

import sys
sys.setrecursionlimit(10000)

def people_sum(k, n):
    if k == 0:                       # 0층인 경우
        for i in range(1, n + 1):
            apartment[k][i - 1] = i  # i - 1호에는 i의 값이 들어간다. 0층의 호수에는 1부터 n까지의 값이 차례대로 들어간다.

    else:
        people_sum(k - 1, n)         # k가 0이 아닌 경우 계속 재귀호출을 한다.
        cnt = 0                      # 매번 초기화해주어야 함
        for i in range(1, n + 1):
            cnt += apartment[k - 1][i - 1]  # (a - 1)층의 b호까지의 사람들을 전부 더한 값이
            apartment[k][i - 1] = cnt       # a층의 b호에 필요한 사람의 수가 된다.


for test_case in range(int(input())):
    k = int(input())                 # 아파트의 층 수
    n = int(input())                 # 대상이 되는 호수

    apartment = [[0] * n for _ in range(k + 1)]  # 0층이라는 존재가 있기 때문에 k + 1을 해주어야 한다.
    people_sum(k, n)

    print(apartment[k][n - 1])       # n에서 1을 빼주어야 제대로 호수를 찾아갈 수 있다.