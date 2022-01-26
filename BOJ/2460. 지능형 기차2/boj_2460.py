max_value = 0
people_inside_train = 0

for i in range(10):
    get_out, get_in = map(int, input().split())

    if people_inside_train < get_out:
        people_inside_train = 0
    else:
        people_inside_train += (get_in - get_out)

    max_value = max(max_value, people_inside_train)

print(max_value)