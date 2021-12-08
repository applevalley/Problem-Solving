dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def chess(arr, count):
    global king_x, king_y, stone_x, stone_y

    new_king_x, new_king_y = king_x + dx[count], king_y + dy[count]
    if 0 <= new_king_x < 8 and 0 <= new_king_y < 8:
        if new_king_x == stone_x and new_king_y == stone_y:
            new_stone_x, new_stone_y = stone_x + dx[count], stone_y + dy[count]
            if 0 <= new_stone_x < 8 and 0 <= new_stone_y < 8:
                king_x, king_y = new_king_x, new_king_y
                stone_x, stone_y = new_stone_x, new_stone_y
        else:
            king_x, king_y = new_king_x, new_king_y

    return arr


king, stone, move_count = map(str, input().split())
arr = [[0] * 8 for _ in range(8)]
move_set = ["T", "B", "L", "R", "LT", "LB", "RT", "RB"]

king_x, king_y = abs(int(king[1]) - 8), (ord(king[0]) - 65)
stone_x, stone_y = abs(int(stone[1]) - 8), (ord(stone[0]) - 65)

for i in range(int(move_count)):
    order_count = move_set.index(input())
    chess(arr, order_count)

final_king_point = "".join(chr(65 + king_y) + str(abs(king_x - 8)))
final_stone_point = "".join(chr(65 + stone_y) + str(abs(stone_x - 8)))

print(final_king_point)
print(final_stone_point)