# 10수인 두 정수를 2진수로 변환했을 때, 두 숫자를 같게 만드는데 필요한 최소의 연산 횟수를 비트 우정지수라고 한다.
# 임의의 자릿수를 0이나 1로 바꾸거나, 서로 다른 두 자리의 숫자 위치를 바꾸는 동작으로 우정 지수를 구할 수 있다.
# 두 이진수의 비트 우정지수를 구하자!

# 10진수를 2진수로 변경하는 과정이 필요할 것 같았는데, 단순히 우정지수만 구해주면 되는 문제였다.
# 두 수를 같게 만들어야 하기에, A와 B중 기준이 되는 A가 존재하게 된다. B를 A와 동일하게 만들어야 하기 때문이다.
# 만약 0을 1로 바꿔준다고 했을 때, 기준인 A에는 1이 3개, B에는 5개가 있다면 2번만큼의 동작은 반드시 존재한다.
# B를 A와 동일하게 만들어야 하기에 A보다 더 많은 2개의 1을 0으로 전환해야 하기 때문이다.
# 1의 숫자가 동일해졌다면, 2진수 내 1의 위치를 확인한다. 이미 같은 자리에 1이 있다면, 굳이 이동시킬 필요가 없다.

# 생각해보니 집합을 통해 조금 더 간추려서 풀어볼 수 있겠다는 생각이 들었다.
# 두 2진수의 위치를 집합에 따로 저장한다.
# 크기가 더 큰 집합을 기준으로, 해당 집합의 요소가 반대 집합에 속해있지 않은 만큼의 수를 구한다.
# 이 수에는 1의 개수가 차이가 나 1을 0으로 바꿔줘야 하는 경우, 1의 개수는 같아졌지만 위치가 달라 바꿔줘야 하는 경우의 연산 수가 모두 들어있다.

# 최대 100만자리의 2진수가 들어올 수 있다.
# 시간 제한이 1초인 것으로 보아 O(N^2)에 가까운 복잡도가 나온다면 무조건 시간초과가 난다.

import sys
for test_case in range(int(sys.stdin.readline().rstrip())):
    first, second = map(str, sys.stdin.readline().split())
    first_info = {i for i in range(len(first)) if first[i] == '1'}
    second_info = {i for i in range(len(second)) if second[i] == '1'}
    cnt = 0

    print(first_info, second_info)
    if len(first_info) > len(second_info):
        standard = first_info
        target = second_info
    else:
        standard = second_info
        target = first_info

    for i in standard:
        if i not in target:
            cnt += 1

    print(cnt)
