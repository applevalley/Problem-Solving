N, M = map(int, input().split())
heard = set()
seen = set()

for i in range(0, N):
    heard.add(input())

for i in range(0, M):
    seen.add(input())

answer = list(heard & seen)
answer.sort()

print(len(answer))
for i in answer:
    print(i)
# print(len(heard & seen))
# for i in heard & seen:
#     print(i)