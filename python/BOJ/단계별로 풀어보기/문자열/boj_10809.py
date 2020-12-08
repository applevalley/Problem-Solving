temp = list(range(97,123))
alpha = []
for i in temp:
    alpha.append(chr(i))
bet = [-1] * 26

S = input()

for i in range(len(S)):
    if S[i] in alpha:
        if bet[alpha.index(S[i])] != -1: pass
        else:
            bet[alpha.index(S[i])] = i

for i in bet:
    print(i, end=' ')


# 1, 0, -1, -1, 2, -1, -1, -1, -1, 4, 3, -1, -1, 7, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
# 1, 0, -1, -1, 2, -1, -1, -1, -1, 4, 3, -1, -1, 7, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
