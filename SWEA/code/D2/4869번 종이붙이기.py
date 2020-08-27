#

import sys
sys.stdin = open('4869.txt')

def paper(n):
    if n >= 2 and len(memo) <= n:
        memo.append(paper(n-1) + (paper(n-2)*2))
    return memo[n]
memo = [1,3]

n = int(input())

for test_case in range(1,n+1):
    space = int(input())
    ans = (space//10)-1
    print("#{} {}".format(test_case, paper(ans)))


