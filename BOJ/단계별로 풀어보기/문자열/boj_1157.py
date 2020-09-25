word = input()
word = word.upper()
temp = []
ans = []
for i in range(len(word)):
    cnt = 0
    if word[i] in temp: continue
    else:
        temp.append(word[i])
        for j in range(i, len(word)):
            if word[j] == word[i]:
                cnt += 1
    ans.append(cnt)

print(temp)
print(ans)

max = 0
for i in range(len(ans)):
    if ans[i] > max:
        max = ans[i]
        max_idx = i
res = 0
for j in range(len(ans)):
    if ans[j] == ans[max_idx]:
        res += 1

if res > 1:
    print('?')
else:
    print(temp[max_idx])
# print(chr(65), chr(97))
# print(chr(66), chr(98))
# print(chr(90), chr(122))
# print(ord('z'), ord('Z'))