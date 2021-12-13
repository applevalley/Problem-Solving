'''
배열 arr[i: j + 1]까지 자르고 정렬한 뒤 k번째 수를 구한다.
입력으로는 배열 arr, [i, j, k] 형태의 2차원 배열 command가 주어진다.
command 안의 요소의 개수만큼의 결괏값을 배열에 담아 반환하자!

arr의 길이는 최대 100, command의 길이는 최대 50이다.
데이터의 크기가 크지 않기에 모든 케이스에 대해 단순한 슬라이싱 이후 정렬을 통해 배열을 만들고, 그 중에서 k번째 값을 뽑아내면 된다!
'''

def solution(array, commands):
    answer = []

    kth_number = [sorted(array[(i - 1): j])[k - 1] for i, j, k in commands]
    answer = kth_number
    return answer