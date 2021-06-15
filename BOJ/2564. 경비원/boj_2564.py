# 풀이중! 아직 통과 못함

# 직사각형 모양의 배열
# 가운데로는 질러갈 수 없고 테두리 선을 따라서만 이동할 수 있다(델타를 사용해 이동하는 방식이 아니다)
# 따라서 시계방향, 반시계방향 2가지의 이동 방법이 있다.

# 가로, 세로의 길이와 상점의 수는 전부 100 이하
# 1은 북, 2는 남, 3은 서, 4는 동
# 북/남쪽의 경우 블록의 왼쪽 경계로부터의 거리, 동/서쪽의 경우 블록의 위쪽 경계로부터의 거리가 주어진다.
# 마지막에는 경비원의 위치가 주어진다.
# 각 상점들 사이의 최단 거리의 합은?

# 다행히 각 상점들을 하나의 체크포인트로 쓰지 않는다.
# 단순히 출발 지점에서 상점으로의 시계방향/반시계방향에 따른 최단 거리의 합만 더해주면 된다.

# 만약 경비원과 상점의 x값이 같은 경우, 상점과 경비원의 y값을 뺀 절댓값이 최단 거리가 된다.
# 경비원이 남/북에 있는 경우, 상점이 서쪽에 있다면 경비원의 x값만큼 왼쪽으로 이동하고, 블록의 y값과 상점의 y값의 차만큼을 더한다.
# 상점이 동쪽에 있다면 블록의 x값과 경비원의 x값의 차만큼 오른쪽으로 이동하고, 블록의 y값과 상점의 y값의 차만큼을 더한다.
# 상점이 북/남쪽에 있는 경우, 경비원과 강점의 x값이 다르다면 상점의 y값을 본다.
# 상점의 y값이 0에 가깝다면 왼쪽으로, 블록의 x값에 가깝다면 오른쪽으로 간다.

# 경비원이 동/서에 있는 경우
# 경비원이 서쪽에 있고 상점이 동쪽이라면, 상점의 y값이 0에 가깝다면 북쪽을 경유해서, 블록의 y값에 가깝다면 남쪽을 경유해서 가야 한다.
# 반대의 경우에도 동일하다
# 경비원이 동/서쪽에 있고 상점이 남/북쪽이라면, 경비원의 y값에서 상점의 x값 방향만큼(위/아래)의 값을 더하고, 상점의 y값을 더한다


def distance_check(x, y):
    global security_x, security_y

    if security_x == x:
        return abs(security_y - y)

    if security_x == 1:
        if x == 3:
            return security_y + y
        elif x == 4:
            return (width - security_x) +



width, height = map(int, input().split())
stores = int(input())
store_location = [list(map(int, input().split())) for _ in range(stores)]
security_x, security_y = map(int, input().split())
temp = 0
cnt = 0

print(store_location)
print(security_x, security_y)

for i in range(len(store_location)):
    store_x, store_y = store_location[i][0], store_location[i][1]
    print(store_x, store_y)