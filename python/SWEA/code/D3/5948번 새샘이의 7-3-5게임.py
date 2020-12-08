# 숫자는 7개, 더할 숫자는 3개이다.
# 그렇다면 3중 for문을 돌려서 합을 전부 구해낸 후 5번째로 큰 값을 찾으면 해결할 수 있지 않을까?

T = int(input())

for test_case in range(1,T+1):
    arr = list(map(int, input().split()))
    sum_list = []
    # 여기서부터 3중 for
    for i in range(len(arr)-2):               # 0 1 2 3 4
        for j in range(i+1, len(arr)-1):      # 1 2 3 4 5
            for k in range(j+1, len(arr)):    # 2 3 4 5 6
                ans = arr[i] + arr[j] + arr[k]
                # 합이 중복되는 경우가 있을 수도 있다!
                if ans in sum_list:
                    pass
                else:
                    sum_list.append(ans)
    # 정렬해요 버블 버블
    for j in range(len(sum_list)):
        for i in range(len(sum_list)-1):
            if sum_list[i] < sum_list[i+1]:
                sum_list[i], sum_list[i+1] = sum_list[i+1], sum_list[i]
    print("#{} {}".format(test_case, sum_list[4]))