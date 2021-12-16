'''
처음에는 1부터 스테이지 n까지 모든 경우에 있어 유저들의 정보를 한 번씩 순회하려 하였지만...
최대 데이터를 기준으로 했을 때 500 x 100000을 고려하면 시간 초과가 발생할 우려가 있었다.
그렇기에 모든 경우에서 stages를 순회할 필요가 없었다. 따라서 stages배열을 정렬해줬다! 그리고 이를 deque에 넣어줬다.
이렇게 했을 때, popleft()로 해당 스테이지를 통과하지 못한 유저 수를 변수에 담아 실패율을 구하는 연산을 O(1)로 해낼 수 있었다.

그 후 [스테이지 번호, 스테이지 미 클리어 유저 수 / 스테이지 도달한 유저 수 ]와 같은 식으로 모든 스테이지에서 스테이지와 실패율을 구했다!
스테이지 번호를 같이 묶은 이유는 추후 정렬을 편하게 하기 위해서였다.
람다를 이용해 x[1], x[0]같이 조건을 준 뒤 실패율이 "높은" 순으로 정렬해야 했기에 reverse=True 를 사용했는데....
이 경우 실패율이 같을 때 문제에서의 조건과 반대로 높은 stage 순으로 정렬되어버렸다.
그래서 실패율을 구해 리스트 fail_rate에 저장할 때 (1 - 실패율)이라는 편법(?)을 사용했다.
이렇게 하면 수치가 0에 가까울수록 실패율이 높다는 것을 의미하게 되고, 실패율이 같을 때 낮은 순으로 정렬하기도 용이하기 때문이다.

deque을 통해 최대한 전체 복잡도를 O(N)에 가깝게 하고자 하였으나.. 더 좋고, 깔끔한 방법이 분명히 있을 것이다.
'''

from collections import deque

def solution(N, stages):
    answer = []
    fail_rate = []

    Q = deque(sorted(stages))
    for i in range(1, N + 1):
        remain_user = len(Q)
        cnt = 0

        if not Q:
            fail_rate.append([i, 1])
            continue

        while Q:
            x = Q.popleft()
            if x == i:
                cnt += 1
            else:
                Q.appendleft(x)
                break

        fail_rate.append([i, (1 - (cnt / remain_user))])

    fail_rate.sort(key=lambda x: (x[1], x[0]))
    answer = [i[0] for i in fail_rate]

    return answer