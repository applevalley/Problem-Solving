'''
부분집합을 만들어주자! 가능한 모든 수를 사전 순으로 출력한다.
'''

import sys
sys.setrecursionlimit(3000)

def comb(n, k):
    if k == 6:
        for i in range(x):
            if pick[i]:
                print(numbers[i], end=' ')
        print()
        return

    for i in range(n, x):
        pick[i] = 1
        comb(i + 1, k + 1)
        pick[i] = 0

while True:
    numbers = list(map(int, input().split()))
    x = numbers[0]

    if x == 0: break

    numbers = numbers[1:]
    pick = [0] * x

    comb(0, 0)
    print()