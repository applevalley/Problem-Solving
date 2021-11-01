import sys
sys.setrecursionlimit(100000)

def GCD(x, y):
    if not y:
        return x
    else:
        return GCD(y, x % y)

N = int(input())
number_n = list(map(int, input().split()))
M = int(input())
number_m = list(map(int, input().split()))

a, b = 1, 1

for i in number_n:
    a *= i

for j in number_m:
    b *= j


result = GCD(a, b)

if len(str(result)) > 9:
    print(str(result)[-9:])
else:
    print(result)