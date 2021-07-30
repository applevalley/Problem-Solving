# 0으로 시작하지 않는 N자리의 수가 주어진다면, K개의 숫자를 지워서 얻을 수 있는 가장 큰 수는 무엇일까?
# 가장 큰 수가 되어야 하기에, 주어진 수의 각 자리중 가장 큰 숫자가 제일 앞에 위치해야 한다.
# 가장 큰 숫자를 찾았다면, 그 수보다 앞 자리의 숫자들을 지워나가게 된다.
# 여기서 지워야 하는 자릿수가 주어진 K보다 큰 경우, 해당 수는 기준이 될 수 없다.
# 따라서 이런 경우에는 두번째로 작은 수가 기준이 된다.

# 이렇게 가장 앞 자리의 숫자를 확정했다면, 지워야 할 숫자가 K개가 될 때까지 위의 과정을 반복한다.
# 선택된 수가 N자리의 숫자 안에 여러개 포함된 경우 가장 먼저 만나게 되는(왼쪽의) 수가 기준이 될 것이고,
# 앞에 같은 숫자가 있다면 해당 경우는 건너뛴다.

# (17723)이라는 숫자가 있고 2개를 지워야 한다면, 가장 큰 수인 7을 기준으로 앞에 위치한 1을 지운다.
# 숫자는 7723이 되었고, 가장 큰 수인 7은 첫 번째 자리에 고정된다.
# 그 다음 과정에서도 남은 723중 가장 큰 수인 7을 찾게 되는데, 7 앞에는 지울 수 있는 숫자가 없다.(이전의 7은 첫 자리에 고정됨)
# 따라서 7을 다시 두 번째 자리에 고정해 77이라는 숫자가 확정된다.
# 남은 숫자는 23이고, 한 자리를 더 지워야 한다. 23중 가장 큰 수는 3이고, 앞의 2를 지운다.
# 3을 마지막 자리에 채우면 773이라는 답이 나온다.

# 시간...초과...

# import sys
#
# N, K = map(int, sys.stdin.readline().split())
# word = sys.stdin.readline().rstrip()
# biggest_number = ''
# cnt = K
# temp = 0
#
# while cnt:
#     sorted_number = sorted(word, reverse=True)
#     target_number = word.find(sorted_number[temp])
#     if target_number > 0:
#         if target_number <= cnt:
#             cnt -= target_number
#             biggest_number += word[target_number]
#             if len(word) > target_number:
#                 word = word[target_number + 1:]
#             temp = 0
#         else:
#             temp += 1
#     else:
#         biggest_number += word[target_number]
#         if len(word) != 1:
#             word = word[1:]
#         temp = 0
#
# biggest_number += word
#
# print(biggest_number)


# 결국 풀이를 찾아봤다.
# 스택을 사용하는게 기존의 풀이보다 더 빠르고 간편했다..!
# 접근에 있어 핵심적인 부분은 위와 크게 다르지 않았다.
# 주어진 문자열(숫자)를 순회하며 스택 가장 위에 위치한 수들과 비교해가며 작은 수라면 스택에서 꺼낸다.
# 꺼내는 과정은 K번만큼 이루어진다.

import sys

N, K = map(int, sys.stdin.readline().split())
word = sys.stdin.readline().rstrip()
cnt, stack = K, []

for i in range(N):
    while cnt > 0 and stack and stack[-1] < word[i]:
        stack.pop()
        cnt -= 1
    stack.append(word[i])

print(''.join(stack[:N - K]))