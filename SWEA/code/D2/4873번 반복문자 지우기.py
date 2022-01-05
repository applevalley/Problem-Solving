# 반복된 문자를 지운다
# 반복된 문자가 나오면 문자열 안에서 반복된 문자를 지우고 다시 반복한다
# 반복된 문자가 없을 때까지
# 어떻게 지울 수 있을까?
# pop할 수 있을텐데 문제는 문자 자체로 지정해주면 제일 앞에 있는걸 지우기에 조건이 맞지 않는다.
# 그럼 남는게 del말고

import sys
sys.stdin = open('4873.txt')


N = int(input())
cnt = 0
i = 0

for test_case in range(1, N + 1):
    words = list(input())
    print(words)
    cnt = 0
    i = 0
    length = len(words)

    while cnt == 0:
        if words[i] == words[i + 1]:
            del words[i:i+2]
            print(words)
        i += 1

        if i == length - 1:
            cnt += 1
            continue

        if length != len(words):
            length = len(words)
            i = 0

            if length == 0 or length == 1:
                cnt += 1
                continue
    print("#{} {}".format(test_case, len(words)))