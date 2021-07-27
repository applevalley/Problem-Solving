# n일동안 코인을 거래해 수익을 최대로 내려고 한다. 일차에 따른 가격이 주어진다.

# 쌀 때 사서 비싸게 팔자.

# 우선 두 갈래로 나뉜다. 지금 돈을 들고 있는가? 아니면 코인을 사서 가지고 있는가?
# 돈을 가진 경우, 당일보다 내일 더 시세가 비싸다면 오늘 코인을 사고, 싸다면 오늘은 사지 않는다.
# 코인을 가진 경우, 당일보다 내일 더 시세가 비싸면 오늘은 팔지 않고, 싸다면 오늘 판매한다.


n, W = map(int, input().split())
coin_chart = list(int(input()) for _ in range(n))
coin = 0
money = W

for i in range(n):
    if i == n - 1:
        money += (coin * coin_chart[i])
        break

    if not coin:
        if coin_chart[i] > coin_chart[i + 1]:
            continue
        else:
            coin += (money // coin_chart[i])
            money -= (coin * coin_chart[i])

    elif coin:
        if coin_chart[i] < coin_chart[i + 1]:
            continue
        else:
            money += (coin * coin_chart[i])
            coin = 0

print(money)