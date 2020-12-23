import sys; sys.stdin = open("mo.txt")

N = int(input())
for test_case in range(1, N + 1):
    vowel = ['a', 'e', 'i', 'o', 'u']
    word = list(input())
    print("#{}".format(test_case), end=' ')
    for i in word:
        if i not in vowel:
            print(i, end='')
    print()