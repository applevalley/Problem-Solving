'''
1부터 N까지 N개의 풍선이 원형으로 놓여있다 -> N번과 1번이 연결되어 있다
가장 처음엔 1번 풍선을 터트리는데, 그 안에서 나오는 종이의 수만큼 이동한다.

deque의 rotate() 메서드 안에 들어가는 int값만큼 deque의 이동이 가능하다...!
단순히 1과 -1을 횟수만큼 반복시키곤 했는데... 하나 깨달아간다 이렇게.
'''


from collections import deque

N = int(input())
balloon = deque([i for i in range(1, N + 1)])
steps = list(map(int, input().split()))
blown_up = []

while balloon:
    balloon_to_blow_up = balloon.popleft()
    blown_up.append(balloon_to_blow_up)
    distance_to_move = steps[balloon_to_blow_up - 1]

    if distance_to_move > 0:
        balloon.rotate(-(distance_to_move - 1))
    else:
        balloon.rotate(-distance_to_move)

print(*blown_up)