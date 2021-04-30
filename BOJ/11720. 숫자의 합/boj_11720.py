N = int(input())
numbers = int(input())
number_list = list(''.join(str(numbers)))
temp = 0

for i in number_list:
    temp += int(i)

print(temp)