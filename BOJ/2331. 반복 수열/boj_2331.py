A, P = map(int, input().split())
repeat_sequence = [A]

while True:
    latest_value = repeat_sequence[-1]
    new_value = sum([int(i) ** P for i in str(latest_value)])
    if new_value in repeat_sequence:
        target = repeat_sequence.index(new_value)
        print(len(repeat_sequence[:target]))
        break

    repeat_sequence.append(new_value)