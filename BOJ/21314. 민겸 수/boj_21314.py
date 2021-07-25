# 10^N 꼴의 10진수는 N + 1개의 M으로, 5 * 10^N 꼴의 10진수는 N개의 M뒤에 1개의 K를 붙인 문자열로 나타낸다.
# 1은 10^0이기에, 0 + 1개의 M으로 나타내 M이 되고, 5는 5 * 10^0이기에 0개의 M뒤에 1개의 K를 붙여 K가 된다.
# 10은 1+1으로 MM, 50은 5 * 10^1으로 MK이다.
# 이런 수를 이어붙여 만든 것이 민겸 수이다. 이를 10진수로 변환하려면 1개 이상의 숫자로 분리한 뒤, 각각을 10진수로 변환해 순서대로 이어붙인다.
# MKKMMK는 50/5/500 으로 505500이 되기도, 1/5/5/10/5로 155105가 되기도 한다.
# 이렇듯 하나의 민겸 수가 10진수로 변환될 때의 최댓값과 최솟값은?

# 어떻게 끊어내는 것이 최대가 될까?
# MK, MMK 과 같이 크게 묶어내는 것이 타당해보인다. MKK같이 K가 연달아 온다면 (MK)K와 같이 최대한 끊어낸다.
# 5....0의 형태로 만들고, M이 남으면 전부 1로 바꾼다.

# 반대로 최소로 만드려면?
# 하나씩 끊어내는 방법이 있을것같다. MKK의 경우, (MK)K로 끊어내면 50/5가 되지만 M/K/K로 나눈다면 1/5/5가 된다.
# 여기서 주의할 것은 M이 연속되는 경우 M들을 한 묶음으로 처리해야 한다는 것이다.
# MMMk의 경우 하나씩 자르면 1/1/1/5가 되지만, M들을 하나로 처리하면 100/5가 되기에 이어붙이면 더 적은 수가 된다.

# 문자열을 입력받고, 최대/최소의 경우를 각 함수의 인자로 전달해 처리해주자!


def max_value(arr):
    temp = ''
    ans = ''

    for i in arr:
        temp += i
        if i == 'K':
            m_count = temp.count('M')
            ans += str(5 * (10 ** m_count))
            temp = ''

    if temp:
        m_count = temp.count('M')
        ans += ('1' * m_count)
    return ans

def min_value(arr):
    temp = ''
    ans = ''

    for i in arr:
        temp += i
        if i == 'K':
            m_count = temp.count('M')
            if m_count:
                ans += str(10 ** (m_count - 1))

            ans += '5'
            temp = ''

    if temp:
        m_count = temp.count('M')
        ans += str(10 ** (m_count - 1))
    return ans

import sys
minK_number = sys.stdin.readline().rstrip()

print(max_value(minK_number))
print(min_value(minK_number))