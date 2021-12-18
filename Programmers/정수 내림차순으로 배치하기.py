def solution(n):
    answer = 0
    separate_numbers = [i for i in str(n)]
    separate_numbers.sort(reverse=True)

    return int(''.join(separate_numbers))