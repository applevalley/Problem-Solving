import sys
sys.stdin = open('tour.txt')


# 전체 인원을 두 그룹으로 나누어서 가위바위보를 돌리고, 승자만 남겨가는 것이 중요
# 어떻게 하면 좋을까
# N // 2?
# 재귀로 한다고?
# len이 N만큼인 스택을 만들고 가장 아래 depth에서부터 둘씩 돌리고 승자를 스택에 넣어서 그 안에서 또 돌리는 재귀를 짜보면 어떨까?

# def getmin(low, high):   # 매개변수 -> 문제의 크기를 나타내는 값
#
#     if low == high:
#         return arr[lo]
#     else:
#         mic = (lo + hi) // 2
#         l = getmin(lo,mid)
#         r = getmin(mid+1, hi)
#         ret = getmin(lo, hi-1)
#
# print(getmin(0, N-1))


# def rock(x,y):
#     print(x, y)
#     if x == y:
#         return games[x]
#     else:
#         mid = (x+y)//2
#         s = rock(x, mid)
#         e = rock(mid+1, y)
#         return min(s,e)

# def rock(x,y):
#     if games[x] == 1:     # 가위
#         if games[y] == 1: # 비김
#             del_list.append(y)   # x의 번호가 더 작기에 패자를 제거할 리스트에 추가
#         elif games[y] == 2: # 바위 - y 승
#             del_list.append(x)
#         elif games[y] == 3: # 보 - x 승
#             del_list.append(y)
#
#     elif games[x] == 2:   # 바위
#         if games[y] == 1: # 가위 - x 승
#             del_list.append(y)
#         elif games[y] == 2: # 비김
#             del_list.append(y)
#         elif games[y] == 3: # 보 - y 승
#             del_list.append(x)
#
#     elif games[x] == 3:   # 보
#         if games[y] == 1: # 가위 - y 승
#             del_list.append(x)
#         elif games[y] == 2: # 바위 - x 승
#             del_list.append(y)
#         elif games[y] == 3: # 비김
#             del_list.append(y)
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     games = list(map(int, input().split()))
#     par = []
#
#     for i in range(1, N+1):
#         par.append(i)
#
#     for i in range(N//2):
#         length = len(par)
#         del_list = []
#         for j in range(0, length, 2):
#             if j == length -1:
#                 pass
#             else:
#                 rock(j, j+1)
#         for k in range(len(del_list), 0, -1):
#             par.pop(del_list[k-1])
#             games.pop(del_list[k-1])
#
#     print("#{} {}".format(test_case, par[0]))


# def rock(x,y):
#     if games[x] == 1:     # 가위
#         if games[y] == 1: # 비김
#             del_list.append(y)   # x의 번호가 더 작기에 패자를 제거할 리스트에 추가
#         elif games[y] == 2: # 바위 - y 승
#             del_list.append(x)
#         elif games[y] == 3: # 보 - x 승
#             del_list.append(y)
#
#     elif games[x] == 2:   # 바위
#         if games[y] == 1: # 가위 - x 승
#             del_list.append(y)
#         elif games[y] == 2: # 비김
#             del_list.append(y)
#         elif games[y] == 3: # 보 - y 승
#             del_list.append(x)
#
#     elif games[x] == 3:   # 보
#         if games[y] == 1: # 가위 - y 승
#             del_list.append(x)
#         elif games[y] == 2: # 바위 - x 승
#             del_list.append(y)
#         elif games[y] == 3: # 비김
#             del_list.append(y)
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     games = list(map(int, input().split()))
#     par = []
#
#     for i in range(1, N+1):
#         par.append(i)
#
#     for i in range((N//2)+1):
#         length = len(par)
#         del_list = []
#         for j in range(0, length//2, 2):
#             if j == length -1:
#                 pass
#             else:
#                 rock(j, j+1)
#         for j in range((length//2)+1, length, 2):
#             if j == length -1:
#                 pass
#             else:
#                 rock(j, j+1)
#         for k in range(len(del_list), 0, -1):
#             par.pop(del_list[k-1])
#             games.pop(del_list[k-1])
#
#     print("#{} {}".format(test_case, par[0]))


def rock(x,y):
    if (games[x-1] == 1 and games[y-1] == 3) or (games[x-1] == 1 and games[y-1] == 1):
        return x
    elif (games[x-1] == 2 and games[y-1] == 1) or (games[x-1] == 2 and games[y-1] == 2):
        return x
    elif (games[x-1] == 3 and games[y-1] == 2) or (games[x-1] == 3 and games[y-1] == 3):
        return x
    return y

def loop(s,e):
    if s == e:
        return s

    first = loop(s, (s+e)//2)
    second = loop((s+e)//2+1, e)
    return rock(first, second)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    games = list(map(int, input().split()))
    s = 1
    e = N
    print("#{} {}".format(test_case, loop(s,e)))