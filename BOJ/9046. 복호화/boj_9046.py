alpha = [ chr(i) for i in range(97, 123) ]

N = int(input())
for i in range(N):
    bet = [0] * 26
    word = input()

    for j in word:
        if j == ' ': continue
        bet[alpha.index(j)] += 1

    most = max(bet)
    if bet.count(most) == 1:
        print(alpha[bet.index(most)])
    else:
        print('?')




