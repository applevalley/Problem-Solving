# 육각형으로 이루어진 벌집이 있다. 1부터 N번 방까지 최소 개수의 방을 지난다고 할 때 몇 개의 방을 지나갈까?
# 육각형을 구현해서 움직인다는 것은 사실상 불가능한 일이라고 생각했다.
# 구현도 어렵겠지만 이동은 어떻게 할 것이며, 최대 데이터는 10억까지 들어오는데 시간 제한 안에 탐색이 가능할까?
# 규칙을 찾아보는 것이 우선이라는 생각이 들었다.
# 1부터 시작해, 6각형으로 한겹씩 쌓여나간다. 이를 통해서 특정 수열이 있다는 것을 생각해볼 수 있다.
# 1(1 + (6 * 0)) -> 7(1 + (6 * 1)) -> 19(7 + (6 * 2)) -> 37(19 + (6 * 3)) ... 이런 식이다.
# (6 * i)의 i를 증가시켜가면서 입력받은 자연수 n이 수열의 범위 안에 있는지 확인해볼 수 있다.
# 이를테면, 주어진 값이 25라면, 이는 19보다는 크지만 37보다는 작다. 20 ~ 37 범위 안에 있는 것이다.
# 첫 시작점 1을 포함하기 때문에, 25까지 도달하기 위한 최소 방문 방 수는 4개가 될 것이다.


n = int(input())
multiple_value = 0
ans = 1
check = False

while not check:
    ans += (6 * multiple_value)

    if n <= ans:
        check = True
    else:
        multiple_value += 1

print(multiple_value + 1)
