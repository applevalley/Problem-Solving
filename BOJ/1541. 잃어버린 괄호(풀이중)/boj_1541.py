# 풀이중! 아직 통과하지 못함

# 양수와 + - () 로만 식을 만든 뒤 괄호를 전부 지웠다.
# 괄호를 다시 쳐서 식의 값을 최소로 만드려면?

# 처음과 마지막 문자는 숫자이다. 이 문자열의 최대 길이는 50 이하이다.
# 두 개 이상의 연산자는 올 수 없고, 각 숫자의 최대 자릿수는 5자리이다.

# 어떻게 해야 최소의 값을 만들 수 있을까?
# - 연산자의 뒤에 괄호를 하는 방법이 있을 수 있다.
# 예제인 55-50+40의 경우 55-(50+40)으로 -35가 되어 작은 값이 된다.

# 입력은 문자열로 온다. 나중에 괄호를 씌우고 나면 어떻게 계산할 수 있을까?
# 단순히 int()로 변환하는 것으로는 연산할 수 없다. eval() 내장함수를 이용해보자!

# calc_string = list(input())  # 입력받은 문자열에 괄호를 넣기 편하게 리스트로 변환해주었다.
# bracket = [0, 0]   # 괄호의 개수를 카운팅하기 위해 만든 리스트
#
# for i in range(len(calc_string)):
#     if calc_string[i] == '-':                  # 만약 - 연산자가 온 경우
#         if bracket[0] == bracket[1]:           # 양측 괄호의 개수가 같다면
#             calc_string.insert(i + 1, '(')     # i + 1(- 연산자의 다음)번 인덱스에 여는 괄호를 끼워넣는다
#             bracket[0] += 1                    # 숫자 올려주기
#         else:                                  # 괄호의 개수가 다른 경우(여는 괄호가 있는 경우)
#             calc_string.insert(i, ')')         # i(- 연산자의 이전)번 인덱스에 닫는 괄호를 넣는다
#             bracket[1] += 1                    # 숫자 올려주기
#
#
#     print(i, calc_string[i])
# if bracket[0] != bracket[1]:                   # 수식의 마지막 - 연산자의 경우 위의 조건문으로는 닫는 괄호가 없게 된다.
#     calc_string.append(')')                    # 숫자가 맞지 않는 채로 수식이 끝난 경우 닫는 괄호를 하나 추가해준다.
#
# calc_string = ''.join(calc_string)             # 리스트로 요소들이 나뉜 형태이기에 join() 함수로 다시 문자열 형태로 변환한다.
# print(calc_string)
# print(eval(calc_string))                       # eval() 함수로 연산을 해보자!
#

# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# 0을 다른 수 앞에 넣을 수 없다.


words = input()
calc_string = ''
bracket = [0, 0]

for i in words:
    if i == '-' and bracket[0] == bracket[1]:
        calc_string += i
        calc_string += '('
        bracket[0] += 1

    elif i == '-' and bracket[0] != bracket[1]:
        calc_string += ')'
        calc_string += i
        bracket[1] += 1

    else:
        calc_string += i

if bracket[0] != bracket[1]:
    calc_string += ')'

print(eval(calc_string))
