list1 = list(range(65, 91))
list2 = []
list3 = []
for i in list1:
    list2.append(chr(i))

for j in range(2, 10):
    if j == 7 or j == 9:
        for k in range(4,5):
            list3.append(list2[0:k])
        list2 = list2[k:]
    else:
        for k in range(3,4):
            list3.append(list2[0:k])
        list2 = list2[k:]

word = input()
cnt = 0

for i in range(len(word)):
    for j in range(len(list3)):
        if word[i] in list3[j]:
            cnt += j + 2
    cnt += 1
print(cnt)
