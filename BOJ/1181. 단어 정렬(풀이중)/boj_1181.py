# N = int(input())
# words = set()
#
# for i in range(N):
#     single_word = input()
#     words.add(single_word)
#
# word_list = list(words)
#
# print(word_list)
# for i in range(len(word_list) - 1):
#     target_word = word_list[i]
#     for j in range(i + 1, len(word_list)):
#         compare_word = word_list[j]
#         if len(target_word) > len(compare_word):
#             word_list[i], word_list[j] = word_list[j], word_list[i]
#         elif len(target_word) == len(compare_word):
#             for k in range(len(target_word)):
#                 target = ord(target_word[k])
#                 compare = ord(compare_word[k])
#                 if target > compare:
#                     word_list[i], word_list[j] = word_list[j], word_list[i]
#                     break
#                 elif target < compare:
#                     break
#
# for i in word_list:
#     print(i)


N = int(input())
word_list = set([input() for _ in range(N)])

except_duplication_list = list(word_list)
except_duplication_list.extend([i for i in word_list if i not in except_duplication_list])
except_duplication_list.sort(key=lambda x: (len(x), sorted(x)))

for _ in except_duplication_list:
    print(_)