import sys; sys.stdin = open("pow.txt")

def pow(x, y):
    global cnt
    if y == 0: return
    cnt *= x
    pow(x, y - 1)

for test_case in range(1, 11):
    n = int(input())
    a, b = map(int, input().split())
    cnt = 1

    pow(a, b)

    print("#{} {}".format(n, cnt))