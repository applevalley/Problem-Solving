# import sys
# sys.stdin = open('test_input (1).txt')

# for test_case in range(1, 11):
#     N = int(input())
#     target = input()
#     words = list(input())
#     res = 0
#
#     print(words)
#     for i in range(len(words) - len(target) + 1):
#         str_for_target = ''
#         for j in range(len(target)):
#             str_for_target += words[j]           # 주어진 문자열을 len(target)만큼 분리해 target과 같은지 확인한다.
#         if str_for_target == target:
#             res += 1
#     print("#{} {}".format(test_case, res))

# 보충수업 코드

def find(text, pattern):
    global ans
    for i in range(len(text)-len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:           # 위에서 내가 생각했던 아이디어가 더 깔끔하게 구현되어있다! 이것이 경험의 차이.
                break
            else: cnt += 1
        if cnt >= len(pattern):
            ans += 1


T = 10
for tc in range(T):
    ans = 0
    no = input()
    pattern = input()
    text = input()
    find(text, pattern)
    print("#{} {}".format(tc, ans))