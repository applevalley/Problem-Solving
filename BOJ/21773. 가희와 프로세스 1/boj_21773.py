import sys
import heapq


class Data:
    def __init__(self, p_id, time, priority):
        self.p_id = p_id
        self.time = time
        self.priority = priority

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.p_id < other.p_id
        else:
            return self.priority > other.priority


input = sys.stdin.readline
N, M = map(int, input().split())
time_count = N
hq = []

for _ in range(M):
    p_id, time, priority = map(int, input().split())
    heapq.heappush(hq, Data(p_id, time, priority))

while time_count:
    element = heapq.heappop(hq)
    print(element.p_id)
    if element.time - 1:
        heapq.heappush(hq, Data(element.p_id, element.time - 1, element.priority - 1))

    time_count -= 1