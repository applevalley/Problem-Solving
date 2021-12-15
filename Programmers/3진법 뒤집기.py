'''
자연수 n을 3진법 수로 변환한 뒤, 그 수를 뒤집고, 다시 10진법 수로 바꾸자!

'''


def solution(n):
    answer = 0
    ternary = ''

    while n > 0:
        n, reminder = divmod(n, 3)
        ternary += str(reminder)

    for i in range(len(ternary)):
        if int(ternary[-(i + 1)]):
            answer += (int(ternary[-(i + 1)]) * (3 ** i))

    return answer