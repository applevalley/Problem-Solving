import sys
sys.stdin = open('color.txt')

# 101x101 배열에서 좌측 하단부터 시작한다는게 포인트!

arr = [[0]*101 for _ in range(101)]
res = []
N = int(input())

for k in range(1,N+1):
    r1, r2, c1, c2 = list(map(int, input().split()))
    print(r1, r2, c1, c2)

    for i in range(r2, r2+c2): # 세로
        for j in range(r1, r1+c1): # 가로
            arr[100-i][j] = k

for k in range(1,N+1):
    ans = 0
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[100-x][y] == k:
                ans += 1

    res.append(ans)

for i in arr:
    print(*i)
for i in res:
    print(i)