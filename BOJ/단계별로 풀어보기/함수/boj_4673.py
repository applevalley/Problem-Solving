def calc():

    sum_list = []
    res = []
    for i in range(1, 10001):
        sum_list.append(i + sum([int(j) for j in str(i)]))

    e = list(range(1, 10001))

    for i in range(1,10001):
        if i not in sum_list:
            res.append(i)

    for i in res:
        print(i)

calc()
