colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
values = [[0, 1], [1, 10], [2, 100], [3, 1000], [4, 10000], [5, 100000], [6, 1000000], [7, 10000000], [8, 100000000], [9, 1000000000]]
answer = ''

for i in range(3):
    single_color = input()
    target_idx = colors.index(single_color)

    if i == 2:
        answer = int(answer) * values[target_idx][1]
    else:
        answer += str(values[target_idx][0])

print(answer)