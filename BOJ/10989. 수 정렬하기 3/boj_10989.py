import sys

N = int(sys.stdin.readline().rstrip())
counting_sort_list = [0] * 10001

for i in range(N):
    number = int(sys.stdin.readline().rstrip())
    counting_sort_list[number] += 1

for i in range(len(counting_sort_list)):
    for j in range(counting_sort_list[i]):
        print(i)