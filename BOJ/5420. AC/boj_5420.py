'''
함수 R과 D가 있다.
R은 배열 안의 숫자 순서를 뒤집고, D는 첫 숫자를 버린다.
빈 배열에서 D를 사용하면 에러가 발생한다. RD같이 붙여서 여러번 수행할 수 있다.
연산을 통한 최종 결과는?

덱을 사용해서 reverse 메서드와 popleft 메서드를 이용하려고 했는데 시간초과가 난다....
입력 문제인가 해서 sys 입력을 받으려 했더니 저런 모양이 되어버렸다.
reverse 메서드가 O(N)의 복잡도를 가지는 것이 시간 초과의 원인같다. 뒤집는 연산을 어떻게 구현할까?

---
0과 1로 구분되는 스위치를 하나 줬다!!
우선 입력을 받을 때 RR과 같은 경우를 ''로 바꿔주어 불필요한 과정을 줄여주었다.
그리고 p를 순회할 때, R을 만날 때마다 뒤집기를 해주면 시간 초과가 난다는 것을 알게 되었기에, 스위치를 활용했다.
초기 값을 1으로 두고, R인 경우 0이 되고 또 R이 오면 1이 되게끔 해주었다.
이렇게 되면 1인 경우 정방향이기에 D가 왔을 때 popleft 메서드를 호출하고, 0인 경우 뒤집힌 상태이기에 pop 메서드를 호출하면 된다!
R을 O(1)로 해결해버릴 수 있게 되었다. 와우 놀라워라

이렇게 p를 전부 순회한 뒤 스위치의 값이 0이라면(뒤집힌 상태) 그때서야 덱을 한번 뒤집어준다.
---
'''

from collections import deque
import sys

for test_case in range(int(input())):
    p = sys.stdin.readline().rstrip().replace('RR', '')
    n = int(input())
    arr = sys.stdin.readline().rstrip().replace('[', ',').replace(']', ',').split(',')[1:-1]
    Q = deque(list(map(str, arr)))
    status = 1

    for i in p:
        if i == 'R':
            status = (status + 1) % 2
        else:
            if not len(Q) or Q[0] == '':
                print('error')
                break

            if status:
                x = Q.popleft()
            else:
                x = Q.pop()
    else:
        if not status:
            Q.reverse()

        print('[' + ','.join(list(Q)) + ']')

