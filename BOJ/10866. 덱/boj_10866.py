import sys
from collections import deque


def deque_order(order):
    if order[-1].isdigit():
        if order.split(" ")[0] == "push_back":
            Q.append(order.split(" ")[1])
        else:
            Q.appendleft(order.split(" ")[1])
    else:
        if order == "front":
            if not Q:
                print(-1)
            else:
                print(Q[0])
        elif order == "back":
            if not Q:
                print(-1)
            else:
                print(Q[-1])
        elif order == "size":
            print(len(Q))
        elif order == "empty":
            if not Q:
                print(1)
            else:
                print(0)
        elif order == "pop_front":
            if not Q:
                print(-1)
            else:
                print(Q.popleft())
        elif order == "pop_back":
            if not Q:
                print(-1)
            else:
                print(Q.pop())


N = int(input())
Q = deque()

for _ in range(N):
    order = sys.stdin.readline().rstrip()
    deque_order(order)
