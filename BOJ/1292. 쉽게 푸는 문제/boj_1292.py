# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4 ... 와 같이 증가하는 수가 있다.
# 시작과 끝을 알려주는 정수 start와 end는 1에서 1000 사이이기에 위의 증가하는 수 배열은 1000까지 있을 것이다.

start, end = map(int, input().split())
number_arr = []
res = 0

# 증가하는 수 배열을 직접 만들어버렸다. 하지만 이것보다 더 좋은 방법이 있지 않을까?
# 최댓값이 1000정도이니까 통과가 되었지 시간 제한이 더 작았거나, 혹은 범위가 100만 단위 이상으로 커졌다면
# 시간초과의 문제도 있을지 모른다.

for i in range(1, 1001):
    num = [i] * i
    number_arr.extend(num)

for i in range(start - 1, end):
    res += number_arr[i]

print(res)