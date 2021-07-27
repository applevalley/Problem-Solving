# 0과 1로만 된 문자열에서 모든 숫자를 같게 만들자.
# 연속된 하나 이상의 숫자를 잡고 전부 뒤집는다. 모든 숫자가 같게 되는 행동의 최솟값은?

# 0과 1을 하나의 묶음으로 본다.
# 문자열 S를 전부 순회하면서 0과 1의 묶음 수를 세고, 더 적은 묶음의 수를 출력한다.
# 문자열 S는 최대 100만이고, 시간 제한은 2초이다.
# 위의 흐름이라면 O(N)으로 해결이 가능하다.

import sys
S = sys.stdin.readline().rstrip()
zero_check = 0
one_check = 0

if S[0] == '0':
    zero_check += 1
else:
    one_check += 1

standard = S[0]
for i in range(1, len(S)):
    if S[i] != standard:
        if S[i] == '1':
            one_check += 1
        else:
            zero_check += 1
        standard = S[i]

print(min(zero_check, one_check))