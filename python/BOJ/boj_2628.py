import sys
sys.stdin = open('paper.txt')
# 종이가 가로로 잘라진다면 잘라지는 줄의 숫자와 세로 길이,
# 세로로 잘라진다면 잘라지는 줄의 숫자와 가로 길이간의 차를 구하다 보면
# 가로, 세로 각각의 경우에서의 최대 값이 나온다.
# 얘들을 곱하면 면적을 얻을 수 있다.
width, height = map(int, input().split())
arr = [[0]*width for _ in range(height)]
garo_length, sero_length = [0], [0]

number = int(input())
for i in range(number):
    direction, line = map(int, input().split())
    if direction == 0:
        garo_length.append(line)
    else:
        sero_length.append(line)
        cnt_for_height = 0

sero_length.append(width)
garo_length.append(height)
garo_length.sort()
sero_length.sort()

gmax = 0
for i in range(len(garo_length),0,-1):
    if garo_length[i-1] - garo_length[i-2] > gmax:
        gmax = garo_length[i-1] - garo_length[i-2]

hmax = 0
for i in range(len(sero_length),0,-1):
    if sero_length[i-1] - sero_length[i-2] > hmax:
        hmax = sero_length[i-1] - sero_length[i-2]

print(garo_length)
print(sero_length)
print(gmax, hmax)
print(gmax * hmax)