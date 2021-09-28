# 완전제곱수를 구하자!
# 완전제곱수란 자연수의 곱으로 이루어진 수를 말한다.

M = int(input())  # M에서 N까지의 자연수 범위 내에서 완전 제곱수를 찾아야 한다.
N = int(input())

# 데이터의 최댓값이 10000이기에 두번째 반복문의 range를 101까지로 줬다. (100 x 100 = 10000)
# 사실 조금 더 속도를 빠르게 하기 위해서는 range를 101이 아닌 N까지 줘버리면 된다!
numbers = [i for i in range(M, N + 1) for j in range(1, 101) if i == (j * j)]

if numbers:
    print(sum(numbers), min(numbers), sep='\n')
else:
    print(-1)