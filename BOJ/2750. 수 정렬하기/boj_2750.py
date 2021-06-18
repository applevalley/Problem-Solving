# N개의 수가 주어졌을 때, 오름차순으로 정렬하자

# 시간 제한은 1초이고, 입력 데이터 N의 최대 개수는 1000이다.
# O(n^2)의 복잡도를 가지는 선택정렬이나 삽입정렬을 이용해도 문제가 없다.

# 선택정렬의 경우
# 데이터가 무작위로 여러 개가 있을 때, 이 중 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸고,
# 그 다음으로 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복한다면?

N = int(input())
numbers = [int(input()) for _ in range(N)]

for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[min_index] > numbers[j]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

for i in numbers:
    print(i)

# 삽입정렬의 경우
# 선택 정렬은 문제 풀이에 있어서는 느린 편이다. 그렇다면 데이터를 하나씩 확인하면서 적절한 위치에 삽입하는 방식은 어떨까?
# 선택 정렬에 비해 실행 시간에 있어서 더 효율적이다. 필요한 상황에서만 위치를 바꾸기에 원본 데이터가 정렬된 형태에 가깝다면 효율적이다.
# 이런 경우 최선의 상황에서는 O(N)의 복잡도까지 가질 수 있다.
# 특정한 데이터가 적절한 위치에 삽입되기 전, 그 앞까지의 데이터는 모두 정렬되어있다고 가정한다.
# 선택 정렬은 데이터의 상태에 상관없이 일단 모든 원소를 비교한 뒤 위치를 바꾸지만 삽입 정렬은 그렇게 하지 않는다.

N = int(input())
numbers = [int(input()) for _ in range(N)]

for i in range(1, len(numbers)):
    for j in range(i, 0, -1):
        if numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
        else:
            break

for i in numbers:
    print(i)