'''
N, M이 주어지고 그 다음 줄에 M개만큼의 수가 온다.
큐에는 1부터 N까지의 수가 들어있다!
M개만큼의 수 각각에 대해 큐의 첫 원소가 해당 수라면 0번만에, 해당 수가 아닌 경우 왼쪽 또는 오른쪽으로 회전시킨다.
이 때 왼쪽으로 돌려서 찾은 경우, 오른쪽으로 돌려 찾은 경우가 있을 것이고 각각에 대해 최솟값을 누적시켜나간다.
해당 수를 찾는다면 뽑아내야 하는 것에 주의하자!

큐 안에서 수를 찾아낸 뒤 어느 방향으로 돌려야 할지 어떻게 알 수 있을까?
큐 내에서 index() 메서드를 이용해보자. 만약 인덱스 값이 큐의 길이 / 2보다 크다면, 오른쪽에 있는 것이기에 큐를 오른쪽으로 미는게 최솟값에 가까워진다.
길이 / 2보다 작다면, 왼쪽으로 밀어야 한다.

큐를 회전시키는 과정에서... 매 루프마다
popleft() -> append() (왼쪽으로 미는 경우)
pop() -> appendleft() (오른쪽으로 미는 경우)
이렇게 두번의 연산을 통해 큐를 회전시키는 것과
rotate() 메서드를 통해 회전시키는 경우
두 방법간의 시간 차이는 얼마나 날지도 관건!

두 방법 사이에 유의미한 시간 차이는 없었다..!
'''


from collections import deque


N, M = map(int, input().split())
arr = deque([i for i in range(1, N + 1)])
target_number = list(map(int, input().split()))
cnt = 0

for i in range(M):
    target = target_number[i]
    if arr[0] == target:
        arr.popleft()
    else:
        temp = 0
        while True:
            if arr[0] == target:
                arr.popleft()
                cnt += temp
                break

            find_idx = arr.index(target)

            if find_idx > len(arr) / 2:
                arr.rotate(1)
                temp += 1
            else:
                arr.rotate(-1)
                temp += 1

            # case 2
            # if find_idx > len(arr) / 2:
            #     last_number = arr.pop()
            #     arr.appendleft(last_number)
            #     temp += 1
            # else:
            #     first_number = arr.popleft()
            #     arr.append(first_number)
            #     temp += 1

print(cnt)