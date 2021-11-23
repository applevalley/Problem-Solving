#
# def check(string):
#     first_check_list = ['p', 'i', 'k', 'a', 'c', 'h', 'u']
#     first_false_check = [i for i in string if i not in first_check_list]
#     if first_false_check:
#         return "NO"
#
#     temp = ''
#     second_check_list = ['pi', 'ka', 'chu']
#     for i in string:
#         temp += i
#         if temp in second_check_list:
#             temp = ''
#         elif len(temp) >= 3 and temp not in second_check_list:
#             return "NO"
#     else:
#         if temp:
#             return "NO"
#
#     return "YES"
#
# string = input()
#
# print(check(string))

a = input()
a = a.replace("pi", "1")
a = a.replace("ka", "1")
a = a.replace("chu", "1")

print(a)