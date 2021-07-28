# 과일 하나를 먹으면 길이는 1 늘어난다. i번째 과일의 높이는 hi이다.
# 자신의 길이보다 작거나 같은 높이에 있는 과일만 먹는다.
# 과일을 먹어 늘릴 수 있는 최대의 길이는?

# 과일들을 정렬해준다.
# 과일들을 순회하면서 초기 크기값보다 작거나 같으면, 크기의 값을 1씩 늘려나간다.
# 크기의 값보다 큰 과일(높이가 더 높은)을 만난다면, 반복문을 빠져나오고 그 시점까지의 크기 값을 출력한다.

fruits, bird_size = map(int, input().split())
fruit_height = sorted(list(map(int, input().split())))

for i in fruit_height:
    if i > bird_size: break
    bird_size += 1

print(bird_size)