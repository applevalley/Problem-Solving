def solution(numbers):
    answer = sum([i for i in range(10) if i not in numbers])
    return answer