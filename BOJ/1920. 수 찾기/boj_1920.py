def binary_search(numbers, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        return binary_search(numbers, target, start, mid - 1)
    else:
        return binary_search(numbers, target, mid + 1, end)

N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

M = int(input())
targets = list(map(int, input().split()))

for i in targets:
    ans = binary_search(numbers, i, 0, N - 1)

    if ans == None:
        print(0)
    else:
        print(1)