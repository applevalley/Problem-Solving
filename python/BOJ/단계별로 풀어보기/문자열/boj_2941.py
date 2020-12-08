# word = input()
# cnt = 0
# croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
# for i in range(len(word) - 2):
#     if word[i:i + 3] == 'dz=':
#         word = word[0:i] + word[i+3:]
#         cnt += 1
#
# for i in range(len(word)):
#     for j in range(i+2, i+3):
#         if word[i:j] in croatia:
#             cnt += 1
#
# print(word)
# print(cnt)

word = input()
cnt, temp = 0, 0
croatia = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

while word:
    for i in range(len(word)):
        if i + 3 <= len(word) or i + 2 <= len(word):
            if word[0:3] in croatia:
                cnt += 1
                word = word[3:]
            elif word[0:2] in croatia:
                cnt += 1
                word = word[2:]
            else:
                cnt += 1
                word = word[1:]
        else:
            if word == '': break

            cnt += 1
            word = word[1:]

print(cnt)
# for i in range(len(word) - 2):
#     if word[i:i + 3] == 'dz=':
#         # word = word[0:i] + word[i+3:]
#         cnt += 1
#     else:
#
#
# for i in range(len(word)):
#     for j in range(i+2, i+3):
#         if word[i:j] in croatia:
#             temp += 1
#
# print(cnt + temp + (len(word) - (2 * temp)))
