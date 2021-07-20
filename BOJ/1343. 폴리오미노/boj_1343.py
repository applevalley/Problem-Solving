# AAAA와 BB가 있다.
# .와 X로 덮여있는 배열이 주어졌을 때, .를 제외한 X를 전부 AAAA나 BB로 덮어줘야 한다.
# X가 모두 덮여진 배열의 형태는 어떤 모습일까? 전부 덮을 수 없는 경우 -1을 출력하자.
# 사전순으로 앞서는 답을 출력해야 한다. 따라서 X가 4개 연속으로 있다면 BB/BB가 아닌 AAAA가 되어야 한다.

# replace() 메서드를 이용해 XXXX를 AAAA로 바꿔주고, 바꾸어진 배열에서 다시 replace() 메서드를 이용한다.
# 이번에는 XX를 BB로 바꾸어준다. 만약 여기서 X가 남아있다면 X가 홀수만큼 있는 것이기에 -1을 출력해주어야 한다.

import sys

board = sys.stdin.readline().rstrip()
check = False
splited = board.split('.')

for i in splited:
    if i.isalpha() and len(i) % 2 != 0:
        check = True
        break

new_board = board.replace('XXXX', 'AAAA')
new_board = new_board.replace('XX', 'BB')

print(-1) if check else print(new_board)