# 큰 배열 안에 분수들이 있다.
# 지그재그로 이어지는 순서에만 집중해 분수들의 값이 눈에 들어오지 않았다. 당연히 규칙을 알아낼 수 없었다...
# 첫 탐색은 1/1이고, 1개의 요소를 탐색한다. 그 다음 탐색에서는 2개의 요소를 탐색한다.
# 이와 같이 n번째 탐색까지 나아가는데, n이 홀수인 경우 분모는 1부터 n까지 커지고, 분자는 n부터 1까지 작아진다.
# n이 짝수인 경우는 분모와 분자가 반대가 된다.

N = int(input())
temp = 0
check = 1
odd_counter = 1

while True:
    cnt = temp
    temp += check

    if N <= temp:
        break
    else:
        check += 1
        odd_counter += 1

if odd_counter % 2:
    mother = N - cnt
    son = (temp - N) + 1
else:
    mother = (temp - N) + 1
    son = N - cnt

print(f'{son}/{mother}')