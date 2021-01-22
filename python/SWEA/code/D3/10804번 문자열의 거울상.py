def change(x):
    if x == 'b':
        x = 'd'
    elif x == 'd':
        x = 'b'
    elif x == 'p':
        x = 'q'
    elif x == 'q':
        x = 'p'
    return x

for test_case in range(1, int(input()) + 1):
    my_string = ''
    word = input()

    for letter in word[::-1]:
        my_string += change(letter)

    print('#{} {}'.format(test_case, my_string))