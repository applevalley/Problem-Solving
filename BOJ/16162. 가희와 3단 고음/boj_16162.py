N, A, D = map(int, input().split())
sounds = list(map(int, input().split()))
cnt = 0
note = 0
checked = False

for i in sounds:
    if i == A and not checked:
        checked = True
        cnt += 1
        note = i

    if checked and i == note + D:
        cnt += 1
        note += D

print(cnt)