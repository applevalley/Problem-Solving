# S, D, H, C 총 4개의 무늬와 1 ~ 13까지 총 13개의 카드가 있다. 4 X 13 = 52장.
# 가지고 있는 카드 외에 몇 장이 더 필요한지 구해야 한다. 입력 데이터에 중복된 요소가 들어오면 ERROR를 출력.
# 문제에서 카드의 무늬 순서가 정해졌기 때문에 [13,13,13,13] 리스트를 만들어 무늬 순서에 맞게 차감하면 될 것 같다. 딕셔너리로도 되지 않을까?

import sys
sys.stdin = open('card_game.txt')

T = int(input())

for test_case in range(1,T+1):
    shape_list = ['S', 'D', 'H', 'C']
    card_list = [13, 13, 13, 13]  # S, D, H, C
    cards = input()
    cnt, test1 = 0, 0
    res = ''
    # print(len(cards))
    card_count = len(cards) // 3     # 문자열을 3으로 나눈 몫으로 케이스 안에서의 총 카드 수를 판별
    # print(card_count)

    # 카드의 무늬에 맞게 card_list를 1씩 차감
    for j in range(0,len(cards),3):
        # print(cards[j], end = " ")
        for k in range(len(shape_list)):
            if cards[j] == shape_list[k]:
                card_list[k] -= 1
    for _ in card_list:           # card_list를 출력하면 [12, 12, 11, 13]으로 나와서 대괄호 없애주려고 만들었음!
        res += str(_) + ' '
    # print(res)

    # 카드가 같은 경우 에러를 출력
    # 테스트 케이스 (8/10)에서 직감했다. 카드는 꼭 4장이 아닐 수 있다는 것을...
    for i in range(0,len(cards)-3,3):      # step에 3을 주면 cards 문자열에서 무늬(S,D,H,C)인 부분에서 시작하게 된다
        test1 += 1
        for j in range(test1, card_count): # 카드가 꼭 4장은 아닐 것이기에 위에서 문자열을 3으로 나눈, 다시 말해 카드의 장수만큼 반복
            if cards[i:i+3] == cards[(3*j):(3*j)+3]:   # 문자열을 3개씩 끊어서 비교한다. S01과 S03 이렇게!
                cnt += 1                               # 카드가 ABCD 총 4장이라면, A와 B,C,D를 검사하고, B와 C,D, C와 D.
                break                                  # 이렇게 중복을 검사한다.
        if cnt == 1:
            print("#{} {}".format(test_case, 'ERROR')) # 중복이라면 ERROR를 출력하고 break!
            break

    if cnt == 1: continue;     # 이 부분을 안 써줬더니 ERROR여도 카드 수가 출력된다 ㅠㅠ 물어봐야겠다.
    print("#{} {}".format(test_case, res))
