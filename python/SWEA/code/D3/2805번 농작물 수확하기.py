# 배열은 N x N 크기이다. 정사각혈 마름모 형태로만 접근해야 한다.
# 여러 방법이 있겠지만, 가장 먼저 생각난 방법은 마름모를 절반으로 나누어서 2번 연산하는 것이었다.
# 마름모의 맨 위 지점(한 칸만 있는)부터 중간까지(길이가 N인)를 구해 저장하고, 나머지도 동일하게 구해 저장한다.
# 불필요한 연산들이 들어가지만.. 2번 나누는 과정, 그리고 구해서 리스트에 저장한 값들을 2중 for 안에서 숫자들을 뽑아 계산한 부분은
# 충분히 코드를 줄일 수 있을 것이다. 물론 접근하는 방법 자체도 새롭게 만들 수 있을 것 같다.
# 중간 지점, arr[0][N//2]에서 아래로 내려가면서 계산할 수 있게 while 안에 for를 쓰는 것은 어떨까?
# 길이가 N이 되는 지점에서 다시 y가(arr[x][y]) 감소하게 짜야 한다는 것이 생각해볼 점이지만 지금 작성한 코드보다는 더 빠를거같다.

import sys
sys.stdin = open('farm.txt')

T = int(input())

for test_case in range(1, T+1):
    arr = []
    list1 = []
    res = 0
    number = int(input())

    for i in range(number):
        space = input()
        arr.append(space)

    cnt = number//2
    for x in range(0,(number//2)+1):
        if cnt == 0:
            list1.append(arr[x][:])
        else:
            list1.append(arr[x][cnt:-cnt])
            cnt -= 1

    cnt = 1
    for x in range((number//2)+1, number):
        if cnt == number//2:
            list1.append(arr[x][cnt])
        else:
            list1.append(arr[x][cnt:-cnt])
            cnt += 1
    print(list1)
    for x in list1:
        for y in x:
            res += int(y)

    print("#{} {}".format(test_case,res))