#

import sys

N = int(input())
word_list = list(set(sys.stdin.readline().rstrip() for _ in range(N)))
word_list.sort()
word_list.sort(key=lambda x: len(x))

for i in word_list:
    print(i)







