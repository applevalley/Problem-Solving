N = int(input())
cnt= 0
for i in range(N):
    temp = input()
    word = []
    ans = 0
    for j in range(len(temp)):
        if temp[j] in word:
            if temp[j] == word[-1]:
                continue
            else:
                ans += 1
        else:
            word.append(temp[j])
    if ans != 0: cnt += 1
print(N - cnt)