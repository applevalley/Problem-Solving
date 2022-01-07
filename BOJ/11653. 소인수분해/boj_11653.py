def divide(x):
    number = 2

    while number <= x:
        if x % number == 0:
            print(number)
            x = x / number
        else:
            number += 1

N = int(input())
divide(N)