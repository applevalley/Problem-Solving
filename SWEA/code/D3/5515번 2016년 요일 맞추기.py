# 1월 1일은 금요일이다. m월 m일은 무슨 요일일까?
# 함수를 짜서 달과 일을 입력하면, 요일이 나오게 하면 될 것 같다.
# 어떻게?
# 달:일의 딕셔너리를 구성하고, 월의 수에 따라 딕셔너리의 value값을 변수에 반복해 저장한다.
# 그렇게 입력받은 누적된 일 값을 7로 % 해서 나오는 나머지로 계산해보면 어떨까?

def date(x,y):
    cnt = 0
    res = 0
    if x > 1:
        for i in range(1,x):
            cnt += calender[i]
        cnt += y
    elif x == 1:
        cnt += y
    res = (cnt % 7)+3        # 4 5 6 7 8 9
    if res > 6:
        res -= 7
    return res


T = int(input())

calender = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for test_case in range(1,T+1):
    month, day = map(int, input().split())
    print("#{} {}".format(test_case,date(month, day)))
