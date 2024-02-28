import sys

input = sys.stdin.readline

N = int(input())
commuter_list = [input().split() for _ in range(N)]
book = dict()

for data in commuter_list:
    book[data[0]] = True if data[1] == "enter" else False
else:
    worker_list = sorted([i for i in book if book[i]], reverse=True)
    for i in worker_list:
        print(i)