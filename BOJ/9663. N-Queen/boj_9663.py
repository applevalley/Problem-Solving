# N x N 크기인 체스판 위에 N개의 퀸을 놓는다.
# 한 자리에 위치한 퀸에 대해 같은 x축 선상, y축 선상, 그리고 대각선 방향에 대해 퀸이 존재할 수는 없다.

# 백트래킹을 사용해야 한다.
# 우선 모든 좌표에 대해 검사를 진행해야 한다.
# 한 좌표에다 놓고 다음 퀸을 놓는 과정에서 조건이 맞지 않으면 돌아가야 한다.

# 시간 제한이 10초다! 여태까지 만나본 문제중에 가장 시간이 널널한 문제인데, 막상 풀다보면 여유롭지 그럴거같다...
# 재귀를 이용할 것이기에 재귀의 깊이 초과, 시간 초과등을 조심해야 한다.

def check(x):
    for j in range(0, x):
        if arr[x] == arr[j]:
            return False
        elif abs(x - j) == abs(arr[x] - arr[j]):
            return False
    return True

def Queen(n, k):
    global cnt

    if n == k:
        cnt += 1
        return

    for i in range(0, N):
        arr[n] = i
        if check(n):
            Queen(n + 1, k)


N = int(input())
arr = [0] * N  # 체스판
cnt = 0

Queen(0, N)
print(cnt)