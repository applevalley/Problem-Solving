# +, -, 괄호를 가지고 식을 만든 뒤 괄호를 전부 지웠다.
# 괄호를 다시 적절히 넣어서 수식의 값을 최소로 만들자!

# 어떻게 해야 수식의 값이 최소가 될까?
# 가장 처음 만나는 - 기호부터 수식의 끝까지 전부 괄호로 묶는 것은 어떨까?
# 그랬더니 괄호로 묶어준 수식의 값이 음수가 되는 경우 괄호 앞의 마이너스 기호를 만나 플러스가 된 것같은 결과가 생겼다. 생각한 건 이게 아닌데...
# 수식의 값을 최대한 적게 만들기 위해서는, 음의 값을 최대한 크게 만들어줘야한다.
# - 기호가 들어온 다음부터, 다음 -기호가 올 때까지 묶어주면 어떨까?



calc = list(input())
switch = True
temp = ''
ans = ''

for i in ''.join(calc):
    if not temp and i == '0': continue   # 0이 여러개 올 수도 있을 것이라고는 생각도 못했었다... 구문에러의 원인을 여기서 잡아냈다.

    if i == '-' or i == '+':
        if len(temp) > 1 and temp[0] == '0':
            temp = temp[1:]
        ans += temp + i
        temp = ''
    else:
        temp += i
else:
    if len(temp) > 1 and temp[0] == '0':
        temp = temp[1:]
    ans += temp

calc = list(ans)
for i in range(len(calc)):
    if calc[i] == '-':
        if switch == False:
            calc.pop(i)
            calc.insert(i, '+')
            continue

        calc.insert(i + 1, '(')
        switch = False
if switch == False:
    calc.append(')')

print(eval(''.join(calc)))

#
# calc = list(input())
# switch = True
# temp = ''
# ans = ''
#
# for i in range(len(calc)):
#     if calc[i] == '-':
#         temp += '-'
#         if temp != '0' and temp[0] == '0':
#             temp = temp[1:]
#         ans += temp
#         temp = ''
#
#         if switch == False:
#             ans += ')'
#             switch = True
#         else:
#             ans += '('
#             switch = False
#     elif calc[i].isdigit():
#         temp += calc[i]
#     else:
#         temp += calc[i]
#
# if temp:
#     if temp != '0' and temp[0] == '0':
#         temp = temp[1:]
#     ans += temp
#     if switch == False:
#         ans += ')'
#
# print(ans)
# print(eval(ans))