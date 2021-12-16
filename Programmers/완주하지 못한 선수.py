'''
파이썬에서 해시 함수를 어떻게 사용할 수 있는지 잘 이해하지 못한 채 코드를 구성했다.
최대 데이터가 10만이기에, 단순히 딕셔너리에 키를 하나씩 넣고, in 메서드로 중복된 값이 존재한다면 값을 추가로 1 더 올려주는 식으로
참여 인원들을 정리하고, 완주한 사람(키)의 값을 딕셔너리에서 1씩 빼주는 식으로 계산하였다.
그 후 딕셔너리를 다시 순회하며 값이 1인(완주하지 못한) 사람을 찾아 반환했다.

이렇게 O(N)에 가까운 복잡도로 해결할 수 있었다.
'''


def solution(participant, completion):
    answer = ''
    enter = dict()

    for i in participant:
        if i in enter:
            enter[i] += 1
        else:
            enter[i] = 1

    for i in completion:
        enter[i] -= 1

    answer = list(i for i in enter if enter[i] > 0)[0]

    return answer



'''
다른 사람들의 풀이를 보며 해시를 이렇게 사용할 수 있다는 것을 느꼈다!
아이디어 자체는 크게 다르지 않았던 것 같다.
'''

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer