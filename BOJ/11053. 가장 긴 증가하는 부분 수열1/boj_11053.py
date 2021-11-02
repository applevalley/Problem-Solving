'''
가장 큰 증가하는 부분 수열을 구하자!
데이터의 최대 길이가 1000개이고, 시간 제한이 1초라면 단순히 O(N^2)로도 구할 수 있다.
'''

N = int(input())
numbers = list(map(int, input().split()))
dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))