while True:
    reversed_string = input()
    if reversed_string == 'END': break
    for i in reversed_string[::-1]:
        print(i, end='')
    print()