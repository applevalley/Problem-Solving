# 날마다 j개의 사탕을 포장한다. 크기가 다른 상자 N개가 있는데, 최소한의 상자를 써야 한다.
# 상자에는 가로, 세로 길이가 있어, 가로 x 세로만큼의 사탕을 포장할 수 있다.

# 상자들 중 최대한 면적이 큰 상자에 우선적으로 사탕을 담아야 상자의 수를 최소화할 수 있다.
# 따라서 상자들을 가로 x 세로의 합으로 내림차순 정렬한 뒤, 그 합을 사탕 수에서 차감해나간다.


import sys
for test_case in range(int(sys.stdin.readline().rstrip())):
    candy, box = map(int, sys.stdin.readline().split())
    boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(box)]
    cnt = 0

    boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

    for i in boxes:
        candy -= (i[0] * i[1])
        cnt += 1

        if candy <= 0:
            break

    print(cnt)