'''
N개의 정수로 구성된 1차원 배열에 특정 정수 v가 몇 개 들어있을까?
결국 배열 전체를 한 번 순회해야 할 필요가 있다. O(N)!
N의 최댓값은 100, v는 -100 <= v <= 100 사이에 있다.
'''

N = int(input())
arr = list(map(int, input().split()))
print(arr.count(int(input())))