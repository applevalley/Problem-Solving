

# 회의들은 N개, 그러나 회의실은 단 하나
# 각 회의들은 각자 시작 시간과 끝나는 시간이 있다.
# 한 회의실에서 모든 회의가 이루어지기에 진행할 수 없는(겹치는) 회의들이 존재한다.
# 따라서 특정 회의들은 버려진다는 것을 생각해낼 수 있다!

# 우선 끝나는 시간을 기준으로 회의들을 정렬할 필요가 있다.
# 다만 끝나는 시간이 동일할 때가 있다. 이럴 때를 생각해서 두번째 조건으로 시작 시간 순서로 정렬을 해야 한다!
# (3, 3), (1, 3) 이렇게 시작 시간 순서로 추가적인 정렬을 하지 않는다면 오류가 생긴다.
# 위의 반례의 경우 답은 2가 되지만, 시작 시간 정렬을 하지 않는다면 1이 되어버릴 것이다.


# 회의의 수 N은 10만개까지 올 수 있고, 시간 제한은 2초이다.
# 10만개정도면 O(N)으로 충분하지 않을까?

import sys
N = int(sys.stdin.readline().rstrip())
meet = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sorted_meet = sorted(meet, key=lambda x: (x[1], x[0]))
print(meet)
print(sorted_meet)
cnt = 1

end_point = sorted_meet[0][1]
for j in range(1, len(sorted_meet)):
    if end_point <= sorted_meet[j][0]:
        end_point = sorted_meet[j][1]
        cnt += 1

print(cnt)


# 실수한 부분
# 위의 풀이가 바로 생각나지 않아 2중 반복문으로 작성을 해버렸다.
# 테스트케이스나 웹 상의 다른 예제들을 통과했지만, O(N^2)이기에 당연히 시간 초과가 났다.

# for i in range(len(sorted_meet)):
#     end_point = sorted_meet[i][1]
#     temp = 1
#     for j in range(i + 1, len(sorted_meet)):
#         if end_point <= sorted_meet[j][0]:
#             end_point = sorted_meet[j][1]
#             temp += 1
#
#     cnt = max(cnt, temp)