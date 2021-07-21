# 서류 성적, 면접 성적이 다른 지원자들보다 전부 떨어지는 지원자는 절대 선발될 수 없다.
# 최대 몇 명이 뽑힐 수 있을까?

# 어떤 지원자 A의 성적이 어떤 지원자 B의 성적에 대배 전부 뒤떨어진다면 선발되지 않는다.
# 따라서 둘 중 하나의 성적을 기준으로 정렬한다. (어느 것이든 크게 문제되지는 않는다)
# 그리고 난 뒤 순회하며 기준이 아닌 나머지 요소를 비교해나간다.


import sys
for test_case in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    score = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cnt = 1                          # 정렬하면 첫 요소(사람)은 자동으로 뽑히기 때문
    score.sort(key=lambda x: x[0])
    target = score[0][1]

    for i in range(1, N):
        if score[i][1] < target:
            target = score[i][1]
            cnt += 1

    print(cnt)