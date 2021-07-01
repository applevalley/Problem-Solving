# 정수를 저장하는 큐를 구현하고, 입력에 대한 명령을 처리하자
# 명령의 수는 최대 2백만개까지 주어진다.
# N의 최대 데이터값이 200만이고, 시간 제한이 3초인 것을 가정했을 때 O(n log n)이하의 시간 복잡도가 보장되게끔 풀어내야 할것이다.
# 가장 처음 든 생각은 각 명령에 대한 함수를 구현하고, 이를 단순히 n개만큼 수행하는 것이다. 시간초과가 날까?

import sys
from collections import deque

def move(order):
    target = order_set.index(order)         # 명령어들을 배열에 넣어두고, 입력된 명령들로부터 인덱스를 찾아나갔다.
                                            # 생각해보면 불필요한 과정이었다. 명령의 앞 글자와 같이 구분되는 특징이 있기 때문이다.
    if target == 1:
        if Queue:
            x = Queue.popleft()
            print(x)
        else:
            print(-1)

    elif target == 2:
        print(len(Queue))

    elif target == 3:
        print(0) if Queue else print(1)

    elif target == 4:
        if Queue:
            print(Queue[0])
        else:
            print(-1)

    else:
        if Queue:
            print(Queue[-1])
        else:
            print(-1)

def push(number):
    Queue.append(number)

Queue = deque()
order_set = ['push', 'pop', 'size', 'empty', 'front', 'back']
N = int(input())

for i in range(N):
    order = sys.stdin.readline().rstrip()

    if order[:4] == 'push':
        push(int(order[5:]))
    
    else:
        move(order)