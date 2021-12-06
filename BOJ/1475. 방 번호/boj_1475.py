'''
번호 N이 주어졌을 때, 이를 나타낼 수 있는 0~9까지의 번호 세트가 가장 적게 들어가려면? 6은 뒤집어 9, 9는 뒤집어서 6이 될 수 있다.
고려되는 경우는 다음과 같다.
6과 9가 가장 많은 경우, 그렇지 않은 경우
6, 9외의 다른 숫자가 가장 많이 발견된다면, 그 횟수만큼의 번호 세트가 필요하다.
다만 6이나 9가 가장 많다면? 6과 9는 서로 변환될 수 있다.
126966인 경우, 단순히 숫자당 횟수만 세면 3세트가 필요할 것처럼 보이지만 2세트에서 9를 6으로 바꿔준다면 3개의 6을 만들 수 있다.
물론 1269696인 경우는 3세트가 필요하다.
이러한 성질을 이용하기 위해, 6의 횟수와 9의 횟수를 더한 뒤, 이것을 2로 나눈 값을 ceil 연산하고, 이 수와 6, 9 이외의 횟수에서의 최댓값과 비교한다.
ceil 연산한 수가 다른 수에서의 최댓값과 같거나 크다면, ceil 연산한 수를 출력해준다.

연산 횟수는 대략 10 x len(N)에 비례할 것이다.
'''

import math

N = input()
max_value = 0

for i in range(10):
    if i == 6 or i == 9: continue
    count = N.count(str(i))
    max_value = max(max_value, count)

six_or_nine_count = math.ceil((N.count('6') + N.count('9')) / 2)
print(six_or_nine_count) if six_or_nine_count >= max_value else print(max_value)