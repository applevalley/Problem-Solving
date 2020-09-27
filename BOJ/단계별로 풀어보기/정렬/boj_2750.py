N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

for i in range(N):
    for j in range(N-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

for _ in num:
    print(_)