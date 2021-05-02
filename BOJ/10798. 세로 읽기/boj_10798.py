words = [input() for _ in range(5)]
max_values = [len(i) for i in words]

for i in range(max(max_values)):
    for j in range(5):
        if len(words[j]) <= i: continue
        print(words[j][i], end='')
