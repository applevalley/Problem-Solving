def expression_to_postfix(expr):
    postfix = ""
    stack = []
    for i in expr:
        if i.isdigit():
            postfix += i
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while True:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        postfix += (stack.pop())
            elif i in ['*', '+', '(']:
                if value_for_opeator[stack[-1]] < value_for_opeator[i]:
                    stack.append(i)
                else:
                    postfix += (stack.pop())
                    stack.append(i)

    return postfix


def postfix_to_calc(expr):
    stack = []
    for i in expr:
        if i.isdigit():
            stack.append(i)
        else:
            first_number_to_calculate = stack.pop()
            second_number_to_calculate = stack.pop()
            if i == '*':
                calculated_number = int(first_number_to_calculate) * int(second_number_to_calculate)
            else:
                calculated_number = int(first_number_to_calculate) + int(second_number_to_calculate)
            stack.append(calculated_number)

    return stack[0]


for test_case in range(1, 11):
    length = int(input())
    expression = input()
    value_for_opeator = {'*': 3, '+': 2, '(': 1}
    postfix = expression_to_postfix(expression)
    value = postfix_to_calc(postfix)

    print(f"#{test_case} {value}")