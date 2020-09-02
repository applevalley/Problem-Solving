import sys
sys.stdin = open('seto.txt')


def sero(x):
    word_sum = ''
    global max

    for i in range(max):
        for j in range(5):
            if len(words[j]) <= i: continue
            else:
                word_sum += words[j][i]
    return word_sum

T = int(input())

for test_case in range(1, T+1):
    words = [list(input()) for _ in range(5)]

    max = 0
    for i in range(5):
        if max < len(words[i]):
            max = len(words[i])

    print("#{} {}".format(test_case,sero(5)))