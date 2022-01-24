while True:
    x, y, z = map(int, input().split())
    triangle = sorted([x, y, z])
    if sum(triangle) == 0:
        break

    if triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2:
        print("right")
    else:
        print("wrong")