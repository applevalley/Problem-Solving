#
# def product(words, r):
#     words = sorted(words)
#
#     def generate(chosen):
#         if len(chosen) == r:
#             # print(chosen)
#             password = ''.join(chosen)
#             check.append(password)
#             return
#
#         start = words.index(chosen[-1]) + 1 if chosen else 0
#         for next in range(start, len(words)):
#             chosen.append(words[next])
#             generate(chosen)
#             chosen.pop()
#     generate([])
#     # for i in range(len(words)):
#     #     if r == 1:
#     #         yield [words[i]]
#     #     else:
#     #         for next in product(words[i + 1:], r - 1):
#     #             yield [words[i]] + next
#
# L, C = map(int, input().split())
# words = list(map(str, input().split()))
# length = C
# check = []
# ans = []
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# product(words, L)
# check.sort()
# for i in check:
#     for j in i:
#         if j in vowels and i not in ans:
#             ans.append(i)
#
# for i in ans:
#     print(i)
# # ans_list = list(product(words, L))
# # for i in ans_list:
# #     print(*i)
# # a c i s t w



import itertools

L, C = map(int, input().split())
words = list(map(str, input().split()))
temp = list(itertools.combinations(words, L))
vowels = ['a', 'e', 'i', 'o', 'u']
password = []

for i in temp:
    vo = 0
    not_vo = 0
    for j in i:
        if j in vowels:
            vo += 1
        else:
            not_vo += 1

    if vo >= 1 and not_vo >= 2:
        password.append(i)

password = [sorted(i) for i in password]
password.sort()

for i in password:
    print(''.join(i).strip())
# password = [sorted(i) for i in list(itertools.combinations(words, L))]
# password.sort()
#
# for i in password:
#     print(''.join(i))