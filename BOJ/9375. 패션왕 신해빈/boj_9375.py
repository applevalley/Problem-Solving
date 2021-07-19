# 의상들이 주어졌을 때 아무것도 입지 않는 경우를 제외하고 몇 가지 케이스가 나올까?
# 의상의 수는 최대 30개까지 올 수 있다.

# 같은 의상은 한 가지만 입게 된다.
# 한 분류의 의상을 입거나, 입지 않는다는 2가지의 선택지가 존재한다.
# 따라서 상의라는 분류의 의상이 3개가 있을 때, 여기에서 오는 경우의 수는 총 4가지이다.(N + 1)
# 이는 다른 분류의 의상들도 전부 마찬가지여서, 각 분류의 의상 N에 대해 (N + 1)을 쭉 곱한 뒤, 1(알몸)을 빼준 값이 전체 경우의 수가 된다!

# 갑자기 궁금해진 부분
# 선글라스 하나만 쓴거하고 알몸하고 뭐가 다른걸까..?
# 오히려 선글라스나 터번 하나만 쓴 알몸이 더 위험한 사람같아보이는데...

import sys
for test_case in range(int(sys.stdin.readline())):
    closet = dict()
    cnt = 1

    for i in range(int(sys.stdin.readline())):
        cloth, cloth_type = map(str, sys.stdin.readline().split())
        if cloth_type not in closet:
            closet[cloth_type] = [cloth]
        else:
            closet[cloth_type].append(cloth)

    for i in closet:
        cnt *= (len(closet[i]) + 1)

    print(cnt - 1)                     # 아무것도 안 입는 경우 한가지를 제외