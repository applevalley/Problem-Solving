x, y, w, h = map(int, input().split())
minimum_distance_for_axis_x = min((x - 0), (w - x))
minimum_distance_for_axis_y = min((y - 0), (h - y))
answer = min(minimum_distance_for_axis_x, minimum_distance_for_axis_y)

print(answer)