import sys
sys.stdin = open('1289.txt')

# 물론 모든 비트를 바꾸는것도 쉽게 해결할 수 있는 방법이지만 불필요한 연산이 너무 많아진다.
# 이런걸 절약하려는 생각이 필요하다!
def trans(x):
    global cnt
    if int(num[x]) == bits[x]:
        pass
    else:
        if num[x] == '1':
            for i in range(x, len(bits)):
                bits[i] = 1
        else:
            for i in range(x, len(bits)):
                bits[i] = 0
        cnt += 1

for test_case in range(1, int(input())+1):
    num = list(input())
    cnt = 0
    bits = [0] * len(num)

    for i in range(len(num)):
        trans(i)
    print("#{} {}".format(test_case, cnt))



def convert(value, start):
    for i in range(start, len(arr)):
        arr1[i] = value
T = 10
for tc in range(T):
    arr = list(map(int, input()))
    arr1 = [0] * len(arr)
    cnt = 0

    if arr[0] == 1:  # 1일때는 1로 모두 채움
        cnt += 1
        arr1 = [1] * len(arr)

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]: continue
        # 앞뒤가 다르면 다른 비트로 채우기
        if arr[i] == 1
            convert(0, i+1)
        else:
            convert(1, i+1)
        cnt += 1
    print("#{} {}".format(tc, cnt))