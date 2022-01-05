import sys
sys.stdin = open('forth_input.txt')

T = int(input())

for test_case in range(1, T+1):
    stack = []
    calc = ['+', '-', '*', '/', '.']
    words = list(map(str, input().split()))

    for i in range(len(words)):
        if words[i] not in calc:      # 숫자인 모든 경우에 대해
            stack.append(words[i])
        elif words[i] in calc:        # 숫자가 아닌 부호일 때
            cnt = 0
            if len(stack) < 2:       # 부호가 왔을 때 스택의 len이 1이라면?
                if words[i] == '.':  # .이 온다면 스택에서 뽑아내 출력하면 됩니다.
                    cnt = stack[-1]
                    stack.pop()
                    print("#{} {}".format(test_case, cnt))
                    break
                else:                # 하지만 다른 부호가 온다면 연산할 인자가 2개가 아닌 1개가 있는 상황이이에 error
                    print("#{} {}".format(test_case, 'error'))
                    break
            else:                   # 스택의 len이 2 이상인 경우: 부호를 통한 연산이 가능합니다.
                if words[i] == '+':
                    cnt = int(stack[-2]) + int(stack[-1])
                elif words[i] == '-':
                    cnt = int(stack[-2]) - int(stack[-1])
                elif words[i] == '*':
                    cnt = int(stack[-2]) * int(stack[-1])
                elif words[i] == '/':
                    cnt = int(stack[-2]) // int(stack[-1])
                    if cnt <= 0:
                        print("#{} {}".format(test_case, 'error'))     # 나눈 결과가 0보다 작아지는 경우 error
                        break
                elif words[i] == '.':                            # 숫자가 2개 이상 stack에 남아있는데 .이 와버리는 경우 error
                    print("#{} {}".format(test_case, 'error'))
                    break
            stack.pop()           # 연산에 사용된 두 숫자를 pop한 뒤
            stack.pop()
            stack.append(cnt)     # 연산한 결과인 cnt를 stack에 append합니다.
