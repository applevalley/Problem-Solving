import sys; sys.stdin = open('10973.txt')

def check_perm(numbers):
    global chk
    for i in range(1, N):
        if numbers[i - 1] > numbers[i]:
            chk = True
            target_idx = i

    if chk == False:
        print(-1)
        return

    for j in range(N):
        if numbers[j] < numbers[target_idx - 1]:
            idx_for_swap = j

    numbers[target_idx - 1], numbers[idx_for_swap] = numbers[idx_for_swap], numbers[target_idx - 1]

    numbers[target_idx:] = numbers[target_idx:][::-1]

    for i in numbers:
        print(i, end=' ')

N = int(input())
numbers = list(map(int, input().split()))

chk = False

check_perm(numbers)

