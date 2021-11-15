woolim = list(map(int, input().split()))
startlink = list(map(int, input().split()))
check = False

score_woolim, score_startlink = 0, 0

for i in range(9):
    score_woolim += woolim[i]
    score_startlink += startlink[i]

    if score_woolim >= score_startlink:
        check = True


if check == True and score_woolim < score_startlink:
    print("Yes")
else:
    print("No")