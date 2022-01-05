# 나올 수 있는 경우
# 짝이 맞는 경우
# 스택이 비게 되고 괄호 짝이 맞는 경우 - 1
# 짝이 안맞는 경우(여는 괄호가 더 많음) - 스택이 차있는 상태 - 0
# 짝이 안맞는 경우(닫는 괄호가 더 많음) - 스택이 빈 상태에서 pop을 시도함 - top이 -1보다 작아짐 - 0
# 괄호 개수가 맞더라도 { ( } ) 이런 경우는 안 된다
# 저거를 어떻게 구현할까
#

import sys
sys.stdin = open('4866.txt')

a = int(input())

for test_case in range(1, a + 1):
    push_list = ['(', '{', '[']
    pop_list = [')', '}', ']']
    stack = []
    list1 = []
    top = -1
    cnt = 0
    arr = list(input())
    for i in arr:
        if i in push_list:
            stack.append(i)
            top += 1
        elif i in pop_list:
            if top == -1:
                cnt = 1
                break
            if i == ')':
                if stack[-1] == '(':
                    del stack[-1]
                    top -= 1
                else:
                    list1.append(i)

            elif i == '}':
                if stack[-1] == '{':
                    del stack[-1]
                    top -= 1
                else:
                    list1.append(i)

            elif i == ']':
                if stack[-1] == '[':
                    del stack[-1]
                    top -= 1
                else:
                    list1.append(i)

    if cnt == 1:
        print("#{} {}".format(test_case, '0'))
        continue
    if list1:
        print("#{} {}".format(test_case, '0'))
        continue
    if not stack:
        print("#{} {}".format(test_case, '1'))
    else:
        print("#{} {}".format(test_case, '0'))

#
#
# a = int(input())
#
# for test_case in range(1,a+1):
#     push_list = ['(','{','[']
#     pop_list = [')','}',']']
#     stack = []
#     top = -1
#     cnt = 0
#     res = 0
#     arr = list(input())
#     for i in arr:
#         if i in push_list:
#             stack.append(i)
#             top += 1
#         elif i in pop_list:
#             if top == -1:
#                 cnt = 1
#                 break
#             if i == ')':
#                 if '(' in stack:
#                     stack.pop()
#                     top -=1
#                 else:
#                     pass
#             elif i == '}':
#                 if '{' in stack:
#                     stack.pop()
#                     top -=1
#                 else:
#                     pass
#             else:
#                 if '[' in stack:
#                     stack.pop()
#                     top -=1
#                 else:
#                     pass
#             # stack.pop()
#             # top -= 1
#         elif i not in push_list and i not in pop_list:
#             res += 1
#     if res == len(arr):
#         print("#{} {}".format(test_case, '0'))
#         continue
#     if cnt == 1:
#         print("#{} {}".format(test_case, '0'))
#         continue
#     if not stack:
#         print("#{} {}".format(test_case, '1'))
#     else:
#         print("#{} {}".format(test_case, '0'))

    # a = int(input())
    #
    # for test_case in range(1, a + 1):
    #     push_list = ['(', '{', '[']
    #     pop_list = [')', '}', ']']
    #     stack = []
    #     list1 = []
    #     top = -1
    #     cnt = 0
    #     res = 0
    #     arr = list(input())
    #     for i in arr:
    #         if i in push_list:
    #             stack.append(i)
    #             top += 1
    #         elif i in pop_list:
    #             if top == -1:
    #                 cnt = 1
    #                 break
    #             if i == ')':
    #                 if '(' in stack:
    #                     stack.pop(stack.index('('))
    #                     top -= 1
    #                 else:
    #                     list1.append(i)
    #
    #             elif i == '}':
    #                 if '{' in stack:
    #                     stack.pop(stack.index('{'))
    #                     top -= 1
    #                 else:
    #                     list1.append(i)
    #
    #             else:
    #                 if '[' in stack:
    #                     stack.pop(stack.index('['))
    #                     top -= 1
    #                 else:
    #                     list1.append(i)
    #
    #         elif i not in push_list and i not in pop_list:
    #             res += 1
    #
    #     if res == len(arr):
    #         print("#{} {}".format(test_case, '0'))
    #         continue
    #     if cnt == 1:
    #         print("#{} {}".format(test_case, '0'))
    #         continue
    #     if list1:
    #         print("#{} {}".format(test_case, '0'))
    #         continue
    #     if not stack:
    #         print("#{} {}".format(test_case, '1'))
    #     else:
    #         print("#{} {}".format(test_case, '0'))
