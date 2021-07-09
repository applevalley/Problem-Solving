import sys

k = int(sys.stdin.readline().rstrip())
numbers = []

for i in range(k):
    single_number = int(sys.stdin.readline().rstrip())
    if single_number == 0:
        numbers.pop()
    else:
        numbers.append(single_number)

print(sum(numbers))