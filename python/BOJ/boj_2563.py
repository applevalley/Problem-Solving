'''
3
3 7
15 7
5 2
'''

arr = [[0] * 100 for _ in range(100)]
cnt = 0
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            if arr[j][k] == 0:
                arr[j][k] = 1
            else:
                arr[j][k] += 1
                cnt += 1

print((100 * T) - cnt)