
word = list(input())
print(word)
cnt = 0

for i in range(len(word)):
    if word[i] == ' ':
        if i == 0 or i == len(word) - 1: pass
        else: cnt += 1
if word == [' ']:
    print(0)
else:
    print(cnt + 1)
