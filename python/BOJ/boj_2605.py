N = int(input())
students = list(range(1,N+1))
order = list(map(int, input().split()))
line = []

for i in range(N):
    line.append(students[i])
    if order[i] != 0:
        for j in range(order[i]):
            line[i-j], line[i-j-1] = line[i-j-1], line[i-j]

for i in line:
    print(i, end=' ')