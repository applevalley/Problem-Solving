# N개의 정수를 한 번만 출력하게 하면서 오름차순으로 정렬해보자!
# frozenset을 이용하면 시간이 더 줄어들 것 같았지만 차이는 없었다. 

import sys

N = int(sys.stdin.readline())
words = frozenset(sorted(list(map(int, sys.stdin.readline().split()))))
print(*sorted(words))

