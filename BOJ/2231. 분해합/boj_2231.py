'''
최대가 100만이라 단순히 1부터 100만까지 돌리면 된다고 생각했지만...
'''

N = int(input())

for i in range(max(0, N - 100), N):
    if sum(map(int, list(str(i)))) + i == N:
        print(i)
        break
else:
    print(0)
#
# N = int(input())
#
# for i in range(N + 1):
#     number = sum([int(j) for j in str(i)]) + i
#     if number == N:
#         print(i)
#         break
# else:
#     print(0)