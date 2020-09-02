T = int(input())

for test_case in range(1, T + 1):
    shape_list = ['S', 'D', 'H', 'C']
    card_list = [13, 13, 13, 13]  # S, D, H, C
    cards = input()
    cnt, test1 = 0, 0
    res = ''
    # print(len(cards))
    card_count = len(cards) // 3
    # print(card_count)

    # 카드의 무늬에 맞게 card_list를 1씩 차감
    for j in range(0, len(cards), 3):
        # print(cards[j], end = " ")
        for k in range(len(shape_list)):
            if cards[j] == shape_list[k]:
                card_list[k] -= 1
    for _ in card_list:  # 대괄호 없애기
        res += str(_) + ' '
    # print(res)

    # 카드가 같은 경우 에러를 출력
    for i in range(0, len(cards) - 3, 3):
        test1 += 1
        for j in range(test1, card_count):
            if cards[i:i + 3] == cards[(3 * j):(3 * j) + 3]:
                cnt += 1
                break
        if cnt == 1:
            print("#{} {}".format(test_case, 'ERROR'))
            break

    if cnt == 1: continue;
    print("#{} {}".format(test_case, res))