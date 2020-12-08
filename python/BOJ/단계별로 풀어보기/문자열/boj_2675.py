for tc in range(int(input())):
    temp = input()
    res = []

    for i in range(len(temp[2:])):
        res.append(temp[i+2] * int(temp[0]))

    for i in res:
        print(i, end='')
    print()