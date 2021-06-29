# 2차원으로 된 배열상의 점 N개가 주어졌을 때, 좌표를 x가 증가하는 순으로, 같은 경우 y좌표가 증가하는 순으로 정렬해보자!
# x좌표를 기준으로 정렬하되, 경우에 따라 y좌표도 기준이 될 수 있기에 둘 다 key로 정렬해준다!
# 내장 함수를 사용할 것이기에 매우 빠른 시간으로 답을 구할 수 있다.
# 최대 입력 데이터 N은 10만개까지 올 수 있기 때문에 input() 입력이 아닌 sys 라이브러리를 이용했다!
# 실제로 4000ms대에서 300ms대까지 속도의 개선이 가능했다.

import sys

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr.sort(key = lambda x: (x[0], x[1]))   # 정렬의 기준

for _ in arr:
    print(*_)