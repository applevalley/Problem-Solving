'''
명령어 D S L R이 있는 계산기
이 계산기는 0 ~ 10000 미만의 10진수를 저장할 수 있는 레지스터가 하나 있다.
D는 n을 2배로, S는 n - 1을, L과 R은 각각 n 자릿수를 하나씩 좌/우로 회전해 저장한다.
A에서 B가 되게끔 하는 최소한의 명령어는?
A가 0일 때, S 연산의 결과는 9999이다.

deque을 이용해보자!
명령어들을 큐에 하나씩 넣고, 비교해나간다..
바뀌어가는 a가 b와 같게 되면, 탈출하게 만들자.
시간 제한이 6초인걸 보면.. 보통 문제는 아닌거같다.
'''

from collections import deque

def go_D(x):
    double_number = int(x) * 2
    if double_number > 9999:
        double_number %= 10000
    return double_number

def go_S(x):
    if x == 0:
        return 9999
    else:
        return x - 1

def go_L(x):
    return ((x % 1000) * 10 + (x // 1000))

def go_R(x):
    return ((x % 10) * 1000 + (x // 10))

def calculator(A, move_list):
    Q = deque()
    Q.append([A, move_list])
    visited = set()
    visited.add(A)

    while Q:
        A, move_list = Q.popleft()
        if A == B:
            return move_list

        temp_number = go_D(A)
        if temp_number not in visited:
            visited.add(temp_number)
            Q.append([temp_number, move_list + "D"])

        temp_number = go_S(A)
        if temp_number not in visited:
            visited.add(temp_number)
            Q.append([temp_number, move_list + "S"])

        temp_number = go_L(A)
        if temp_number not in visited:
            visited.add(temp_number)
            Q.append([temp_number, move_list + "L"])

        temp_number = go_R(A)
        if temp_number not in visited:
            visited.add(temp_number)
            Q.append([temp_number, move_list + "R"])


for test_case in range(int(input())):
    A, B = map(int, input().split())

    print(calculator(A, ''))