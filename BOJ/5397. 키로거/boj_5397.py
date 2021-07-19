# 백스페이스 -가 있고 앞에 문자가 있다면 해당 문자를 지운다
# 화살표 입력 < > 가 온다면 해당 방향으로 위치를 한 칸 옮긴다
# 입력 문자열 L의 길이는 최대 100만개이고, 시간 제한은 1초
# 중간에 끼워넣고 삭제하는 과정에서 생기는 연산을 어떻게 O(1) 단위로 줄여내는지가 중요하다
# deque같은건 어떨까? 그나마 연산을 조금 줄일 수 있지 않을까?

# 단순히 입력이 오는 경우 - 그대로 추가
# 커서의 이동이 있는 경우 - 좌우를 계산해서 카운팅하기
# 동작하지 않는 예시
# 채워진 문자가 없는데 커서 이동만 있는 경우
# 커서가 가장 왼쪽인데 삭제 명령이 들어온 경우 (커서의 좌측 위치 값이 채워지는 비밀번호 문자열의 길이보다 더 크면 생략)
# 커서의 위치 값이 0일 때 오른쪽으로의 이동 명령이 들어온 경우(이미 커서가 가장 오른쪽이기 때문에 여기서 오른쪽으로 한 칸을 보내도 의미가 없다)
# 연산에 주의해야 할 예시
# 커서값이 0이 아닐 때(음수일 때) 삽입이나 삭제 명령이 주어지는 경우

# deque을 이용한 풀이

# import sys
# from collections import deque
#
# for test_case in range(int(sys.stdin.readline().rstrip())):
#     encrypted = list(sys.stdin.readline().rstrip())
#     real_password = deque()
#     move = ['<', '>']
#     counter = 0
#
#     for i in encrypted:
#         if i in move and not real_password: continue    # 채워진 문자는 없고, 커서의 이동만 있을 때
#         elif i in move and real_password:               # 채워진 문자가 있는 상황에서의 커서 이동
#             if i == '<':
#                 if not abs(counter) >= len(real_password):
#                     counter -= 1
#
#             else:
#                 counter += 1
#                 if counter > 0:                         # 카운터가 0 이상인 경우는 아무리 오른쪽으로 이동시켜도 위치가 변하지 않는다.
#                     counter = 0                         # 카운터를 0으로 고정시켜야 이후 왼쪽으로 n칸 이동해야 할 때 정확히 움직인다.
#             continue                                    # 여기서 끊어주어야 뒤의 조건문을 불필요하게 방문하지 않는다
#
#         if i.isalpha() == True or i.isdigit() == True:  # 문자나 숫자가 왔을 때
#             if counter < 0:                             # 커서의 값이 -인 경우(왼쪽으로 n칸 이동해있을 경우)
#                 real_password.insert(len(real_password) - abs(counter), i)
#             else:                                       # 커서의 값이 0 이상이라면, 가장 오른쪽임을 의미한다.
#                 real_password.append(i)                 # 따라서 바로 입력이 가능하다.
#
#         if i == '-':                                    # 삭제 명령이 왔을 때
#             if not real_password: continue
#
#             if counter < 0:                             # 커서의 값이 -인 경우(왼쪽으로 n칸 이동해있을 경우)
#                 if abs(counter) == len(real_password): continue    # 커서의 절대값이 문자의 전체 길이와 동일하다면, 커서는 가장 왼쪽이고, 지울 수 있는 앞의 문자가 없는 상황이다.
#
#                 del real_password[(counter) - 1]         # 해당 인덱스값을 삭제한다
#
#             else:                                       # 커서의 값이 0 이상이라면, 가장 오른쪽에 위치해있다.
#                 real_password.pop()                     # 가장 오른쪽의 값을 뽑아낸다.
#
#     print(''.join(real_password))



# 스택을 이용한 풀이가 훨씬 더 빠르고 간편했다...
# 단순히 append, pop 메서드를 반복해나가면 O(N)의 연산을 수행해 시간 초과가 날 것을 우려했는데,
# 두 스택에 대해 커서의 이동에 따라 가장 마지막 요소를 pop해서 반대쪽 스택에 append해주는 식으로 진행하면
# 모든 경우에 대해 O(1) 수준으로 진행할 수 있다는 부분을 생각하지 못했었다.

# 스택을 이용한 풀이

import sys
for test_case in range(int(sys.stdin.readline())):
    words = list(sys.stdin.readline().rstrip())

    left_side = []
    right_side = []

    for i in words:
        if i == '-':
            if left_side:
                left_side.pop()
        elif i == '<':
            if left_side:
                right_side.append(left_side.pop())
        elif i == '>':
            if right_side:
                left_side.append(right_side.pop())
        else:
            left_side.append(i)

    left_words = ''.join(left_side)
    right_words = ''.join(right_side[::-1])

    print(''.join([left_words, right_words]))

