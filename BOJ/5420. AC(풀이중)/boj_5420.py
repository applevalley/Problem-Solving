'''
함수 R과 D가 있다.
R은 배열 안의 숫자 순서를 뒤집고, D는 첫 숫자를 버린다.
빈 배열에서 D를 사용하면 에러가 발생한다. RD같이 붙여서 여러번 수행할 수 있다.
연산을 통한 최종 결과는?

덱을 사용해서 reverse 메서드와 popleft 메서드를 이용하려고 했는데 시간초과가 난다....
입력 문제인가 해서 sys 입력을 받으려 했더니 저런 모양이 되어버렸다.
reverse 메서드가 O(N)의 복잡도를 가지는 것이 시간 초과의 원인같다. 뒤집는 연산을 어떻게 구현할까?
'''

from collections import deque
import sys

for test_case in range(int(input())):
    p = sys.stdin.readline().split()[0].replace('RR', '')
    n = int(input())
    arr = sys.stdin.readline().split()[0].replace('[', ',').replace(']', ',').split(',')[1:-1]
    Q = deque()

    if arr != ['']:
        for i in arr:
            Q.append(int(i))

    for i in p:
        if i == 'R':
            Q.reverse()
        else:
            if len(Q) == 0:
                print('error')
                break
            Q.popleft()
    else:
        print('[', end='')
        while Q:
            x = Q.popleft()
            print(x, end='')
            if Q:
                print(',', end='')
        print(']')