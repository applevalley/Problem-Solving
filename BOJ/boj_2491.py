N = int(input())
number = list(map(int, input().split()))
cnt, temp = 1, 1
list1 = []

for i in range(1,N):
    if number[i] >= number[i-1]:
        cnt += 1
    else:
        cnt = 1

    list1.append(cnt)

for j in range(1, N):
    if number[j] <= number[j-1]:
        temp += 1
    else:
        temp = 1
    list1.append(temp)

if N == 1:
    print(1)
else:
    print(max(list1))
