'''
첫 번째 수가 주어지고, 임의의 두 번째 수를 만든다. 세 번째부터의 수는 n - 2번째 수에서 n - 1번째 수를 뺀 값이다.
이 값이 음수가 되면 해당 수를 버리고, 더 이상 수를 만들지 않는다.
이렇게 만들어지는 수들의 최대 개수를 찾고, 해당 수들을 출력하자.

n - 2에서 n - 1번을 빼는 형태이기 때문에, 필연적으로 n - 1은 n - 2 / 2보다는 클 것이다.
1번 = 100, 2번 = 30이라고 해보자. 규칙을 따라보자면...
100 30 70 <- 2번째보다 3번째 수가 커지기 때문에 반드시 여기서 끝나버린다!
1번 = 100, 2번 = 70 이라면....
100 70 30 40 <- 2번째보다 3번째 수가 작아지기에 경우에 따라 3개를 넘어서는 수열이 만들어질 수 있음

'''

initial_number = int(input())
max_value = 0
answer = []
for i in range(initial_number // 2, initial_number + 1):
    temp_list = [initial_number, i]

    while True:
        nth_number = temp_list[-2] - temp_list[-1]
        if nth_number < 0:
            if max_value < len(temp_list):
                answer = temp_list

            max_value = max(max_value, len(temp_list))
            break

        temp_list.append(nth_number)


print(max_value)
print(*answer)