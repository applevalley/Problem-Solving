import sys

for test_case in range(int(sys.stdin.readline().rstrip())):
    arr = sorted(map(int, sys.stdin.readline().split()))
    print(arr[-3])
