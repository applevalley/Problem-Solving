import sys
sys.stdin = open('6190.txt')

# 접근은 비슷했지만 내 코드는 출력이 초과되었다.. 아마 str로 입력을 받고, int로 다시 변환해 순회했던 것이 원인이었던 것 같다.
# 시간에 대해 생각해볼 수 있는 좋은 기회가 되었다.

def solve(x):
    a = str(x)
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = -1

    for i in range(N-1):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            if solve(num):
                if ans < num:
                    ans = num
    print("#{} {}".format(test_case, ans))