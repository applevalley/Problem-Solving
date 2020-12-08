num = [0] * 10
sum = 1

for i in range(3):
    sum *= int(input())
to_str = str(sum)

for i in to_str:
    num[int(i)] += 1

for i in num:
    print(i)