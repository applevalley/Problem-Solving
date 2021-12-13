'''
정수 배열 numbers 안에서 서로 다른 idx의 두 수를 뽑아 더한 값을 answer에 저장한다! 그 후 모든 수를 정렬한 배열을 반환한다.
서로 다른 두 idx의 값을 비교해야 하기에, O(N^2)의 복잡도가 발생하지만.. 정수 배열 numbers의 길이는 최대 100이다. 100을 가정해도 10000이기에 충분하다.

2중 반복문의 내부에서 numbers[i] + numbers[j]가 answer 안에 있는지 비교한 뒤 없으면 넣어주는 식으로 해도 되지만,
answer 안에 있는지 비교하는 과정에서 O(len(answer))만큼의 연산이 발생할 것이다.
단순히 전부 다 넣은 뒤, 배열 answer를 set으로 바꾸고, 다시 그것을 sorted 메서드를 통해 리스트로 바꿔주면 된다!
'''

def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(set(answer))