import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poke_list = []
poke_dict = {}

for i in range(N):
    poke_name = input().strip()
    poke_list.append(poke_name)
    poke_dict[poke_name] = i + 1

for i in range(M):
    question = input().strip()
    if question.isalpha():
        print(poke_dict[question])
    else:
        print(poke_list[i - 1])

# pokemon = [input().strip() for _ in range(N)]

# for i in range(M):
#     question = input().strip()
#     if question.isalpha():
#         print(pokemon.index(question) + 1)
#     else:
#         print(pokemon[int(question) - 1])