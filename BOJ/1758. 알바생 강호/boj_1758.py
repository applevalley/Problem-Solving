# 원래 주려고 생각한 돈에서 등수를 뺀 값을 주기에 원래 주려고 한 돈이 큰 순서로 정렬해 순서를 매기는 것이 최댓값에 가까워짐!

import sys
N = int(sys.stdin.readline())
people = [int(sys.stdin.readline()) for _ in range(N)]
cnt = 0
order = 1
tips = 0
people.sort(reverse=True)

for i in people:
    tips = i - (order - 1)
    if tips < 0: continue

    cnt += tips
    order += 1

print(cnt)