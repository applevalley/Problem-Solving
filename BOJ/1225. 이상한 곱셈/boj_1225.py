# A / B는 최대 10,000자리..... O(N^2)로 하나씩 구해 더하면 시간초과

A, B = map(str, input().split())
value_to_multiply = sum([int(i) for i in A])
answer = sum([value_to_multiply * int(i) for i in B])
print(answer)