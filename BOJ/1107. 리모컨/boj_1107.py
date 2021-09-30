# 채널의 시작점은 100이다.
# 누를 수 있는 버튼은 0~9, +, -이며 +를 누르면 채널 1 증가, -는 1 감소한다.
# 채널은 무한대이고, 0에서 -를 눌러도 음수값이 되지는 않는다.
# 고장난 버튼이 주어졌을 때 100번 채널에서 목표 채널 N까지 몇번을 눌러야 갈 수 있을까?

# 목표 채널에 도달하는 경우는 2가지가 있다.
# +나 -를 계속 반복하거나, 고장난 버튼을 제외하고 나머지 버튼으로 목표 채널에 도달하는 경우가 있다.(도달할 수 없는 경우 최대한 가까운 채널로 간 뒤 +나 -로 조절할 수 있다)
# 두 경우를 전부 비교해보고, 그 중 값이 작은 경우가 답이 될 것으로 보인다.

def press_buttons(N):
    for_lower = N - 1
    for_higher = N + 1
    while for_lower >= 0:
        temp = str(for_lower)
        check = False
        for i in temp:
            if int(i) in broken_buttons:
                break
        else:
            check = True

        if not check:
            for_lower -= 1
        else:
            break

    while for_higher <= 999999:
        temp = str(for_higher)
        check = False
        for i in temp:
            if int(i) in broken_buttons:
                break
        else:
            check = True

        if not check:
            for_higher += 1
        else:
            break

    if abs(N - for_lower) <= abs((N - for_higher)):
        if for_lower >= 0:
            return for_lower
        else:
            return for_higher
    else:
        return for_higher


N = int(input())
broken_count = int(input())
broken_buttons = []
healthy_check = False

if broken_count:
    broken_buttons = list(map(int, input().split()))

just_up_or_down = abs(N - 100)

if broken_buttons:
    find_close_channel = abs(N - int(press_buttons(N))) + len(str(press_buttons(N)))

    for i in str(N):
        if int(i) in broken_buttons:
            break
    else:
        healthy_check = True

    if healthy_check == True:
        if abs(100 - N) > len(str(N)):
            print(len(str(N)))
        else:
            print(abs(100 - N))
    else:
        print(min(just_up_or_down, find_close_channel))
else:
    if N == 100:
        print(0)
    else:
        print(min(just_up_or_down, len(str(N))))


