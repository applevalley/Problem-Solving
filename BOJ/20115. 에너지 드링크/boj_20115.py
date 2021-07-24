# 서로 다른 두 드링크를 골라 한 드링크를 다른 드링크에 전부 붓는다. 다만 붓는 과정에서 절반을 흘린다.
# 다 부은 에너지 드링크는 버린다.
# 이 과정을 하나가 남을 때까지 반복한다. 드링크의 최댓값은?

# 최댓값을 구해야 하기에 매 선택마다 가장 작은 값의 드링크를 다른 드링크에 붓는게 손실이 적다. 매번마다 절반을 흘려보내기 때문이다.
# 절반을 흘린 드링크를 다른 드링크에 합쳐야 하는데, 이 때 아무 드링크에나 섞어버리면 해당 드링크가 선택되었을 때 절반을 흘려보내는 과정에서 불필요한 손실이 더해진다.
# 따라서 아무 드링크에나 합치는 것보다 합칠 드링크를 정해놓고 그 드링크 하나에만 계속 다른 드링크를 섞는 것이 더 최적의 해에 가깝다는 것을 알 수 있다.
# 계속 증가할 드링크로는 주어진 배열 안에서 가장 큰 드링크를 고르는 것이 합당하다.

# 따라서 오름차순으로 정렬한 뒤 배열의 크기가 1이 될 때까지 계속 더해나가게 된다! 가장 작은 요소를 반으로 나누어 가장 큰 요소에 더해준다.
# 최대 데이터는 10만개이고, 위의 흐름을 따라 구성한다면 O(N) 정도로 구현이 가능할 것으로 보인다.


import sys
from collections import deque
N = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
cnt = 0
size.sort()
Q = deque()
Q.extend(size)

while len(Q) > 1:
    smallest = Q.popleft()
    biggest = Q.pop()

    new_biggest = (smallest / 2) + biggest
    Q.append(new_biggest)

print(int(Q[0])) if Q[0] == int(Q[0]) else print(Q[0])