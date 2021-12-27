'''
확장자들의 개수를 세어주어야 한다!
collections 모듈 내의 Counter 클래스를 사용해보았다.
요소의 개수를 세어야 할 때, Counter를 통해 O(N)의 복잡도로 개수를 세어줄 수 있다!
편리하구나 편리해
'''

import sys
from collections import Counter

N = int(input())

extension = [sys.stdin.readline().strip().split(".")[1] for _ in range(N)]
accumulated_and_sorted_list = sorted([[i, j] for i, j in zip(Counter(extension).keys(), Counter(extension).values())], key=lambda x: x[0])

for _ in accumulated_and_sorted_list:
    print(*_)