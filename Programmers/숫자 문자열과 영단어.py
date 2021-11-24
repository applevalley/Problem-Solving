'''
영어 단어로 된 자릿수를 숫자로 바꿔주자!
0부터 9까지의 키와 값 쌍을 정의하고, 0~9까지 10번의 횟수에 대해 replace() 메서드를 사용하자.
'''


def solution(s):
    word_to_num = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                   9: 'nine'}

    for i in range(10):
        s = s.replace(word_to_num[i], str(i))

    return int(s)