'''
쉬운 문제더라도 조건을 잘 확인하자!!!
해당 문제는 배열을 정렬해 내부 요소의 순서를 바꾸면 안되는 문제였다.
'''
def solution(arr):
    if len(arr) == 1:
        return [-1]

    arr.pop(arr.index(min(arr)))

    return arr