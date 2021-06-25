# R x C 사이즈의 공간이 있고, 좌상단에 말이 있다.
# 인접한 4방향으로 이동하는데, 이동한 좌표에 있는 알파벳은 그 동안 지나온 알파벳과는 달라야 한다.
# 좌상단까지 포함했을 때, 최대 몇 칸까지 갈 수 있는가?

# 시간초과가 발생한 코드
# 처음에는 리스트로 저장했었는데, 각 방향이 리스트에 담겨있는지를 확인하는 과정에서 
# 매 시도마다 리스트의 요소 개수만큼의 연산이 이루어지기에 시간초과가 난다 생각하여 집합으로 변경하였다.
# 그럼에도 시간초과는 발생하였다. 리스트에서 집합으로 바꾼 만큼 약간의 시간 절약은 있었을 수 있다.
# 하지만 여전히 시간초과가 나는 점에서 문제가 그것이 아니라는 생각이 들었다.

import sys
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    global cnt
#
    alpha.add(arr[x][y])
    visited[x][y] = 1
    cnt = max(cnt, len(alpha))

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] not in alpha and not visited[tx][ty]:
            DFS(tx, ty)
            alpha.remove(arr[tx][ty])
            visited[tx][ty] = 0


R, C = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(R)]
alpha = set()
visited = [[0] * C for _ in range(R)]
cnt = 1

DFS(0, 0)

print(cnt)



# 통과한 코드
# DFS가 아닌 BFS로 구성하였다.
# 아래와 같이 집합에 좌표와 해당 좌표의 알파벳을 같이 저장하면 (3, 0, 'A')와 같이 저장된다.
# 글자는 좌표들을 지날수록 합쳐져 (1, 0, 'ACBDE')와 같이 늘어난다.
# 아래와 같이 저장하면, 이전의 시도들과 같이 요소 확인을 위해 순회를 여러 번 할 필요가 없게 된다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    cnt = 1       # !!!!! 0으로 했더니 1 1 A 와 같은 데이터에서 1이 아닌 0이 나와버렸다

    while alpha:
        x, y, check = alpha.pop()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] not in check:
                check_plus = check + arr[tx][ty]
                alpha.add((tx, ty, check_plus))
                cnt = max(cnt, len(check_plus))

    return cnt

R, C = map(int, input().split())
arr = [input() for _ in range(R)]
alpha = set([(0, 0, arr[0][0])])

print(BFS())