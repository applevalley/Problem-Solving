# 1부터 N까지의 사람들 중에서 순서대로 K번째 사람을 제거해야 한다. K보다 작은 순서라면, 다음 사람으로 넘어간다.
# N명의 사람들이 모두 제거될 때까지 반복하는데, 1명이 남을 때까지 계속 K번째 사람을 찾아서 제거해야 한다.
# 리스트보다는 deque를 사용하는게 더 빠르다고 생각했다. deque의 popleft나 append는 O(1)이 걸리지만, 리스트에서는 O(1)로 넣고 빼는 연산이 불가능하다.
# [data][::-1]로 첫 번째 사람을 pop()으로 꺼낼 수는 있지만, 다시 리스트에 넣어주려면 가장 마지막, 뒤집힌 리스트에서는 0번 idx에 넣어야 하고, append로는 안 된다.
# 그렇다면 insert(0, data)를 사용해야 하는데, 여기선 O(N)이 걸린다. 따라서 deque의 사용이 더 빠르다.

# deque 이용 풀이

# from collections import deque

# N, K = map(int, input().split())
# members = deque(i for i in range(1, N + 1))
# answer = []
# cnt = 0
#
# print("<", end='')
# while len(members) > 1:
#
#     x = members.popleft()
#     cnt += 1
#     if cnt == K:
#         answer.append(x)
#         cnt = 0
#     else:
#         members.append(x)
# else:
#     answer.extend(members)
#
# print(*answer, end='', sep=', ')
# print(">")

# 리스트를 사용한 풀이 - 역시 이게 조금 더 느렸다.
# N, K = map(int, input().split())
# members = [i for i in range(1, N + 1)][::-1]
# answer = []
# cnt = 0
#
# print("<", end='')
# while len(members) > 1:
#     x = members.pop()
#     cnt += 1
#     if cnt == K:
#         answer.append(x)
#         cnt = 0
#     else:
#         members.insert(0, x)
# else:
#     answer.extend(members)
#
# print(*answer, end='', sep=', ')
# print(">")

# sys를 이용한 입출력을 사용했음에도 유의미한 변화가 없었다.
# K번째 사람을 찾기까지 매번 1부터 K까지 순회한 것이 문제였던듯 하다.

N, K = map(int, input().split())
members = [i for i in range(1, N + 1)]
answer = []
cnt = 0

while members:
    cnt = (cnt + K - 1) % len(members)
    answer.append(members.pop(cnt))

print(f"<{', '.join(map(str, answer))}>")
print("<" + ', '.join(map(str, answer)) + ">")
