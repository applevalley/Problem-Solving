from collections import Counter

N = int(input())

for i in range(N):
    first_word, second_word = map(str, input().split())
    if Counter(first_word) == Counter(second_word):
        print(f"{first_word} & {second_word} are anagrams.")
    else:
        print(f"{first_word} & {second_word} are NOT anagrams.")