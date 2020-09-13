cnt, ans = 0, 0
arr = []
for i in range(10):
    arr.append(int(input()) % 42)
# print(arr)
for i in range(10):
    cnt = 0
    for j in range(i + 1, 10):
        if arr[i] == arr[j]:
            cnt += 1         # 같은 숫자가 여러 번 오더라도 결국 1번으로 처리해줘야 한다.
    if cnt != 0:
        ans += 1
print(10 - ans)

# 첫 오답 코드
cnt = 0
arr = []
for i in range(10):
    arr.append(int(input()) % 42)

cnt = len(arr)
for i in range(10):
    for j in range(i + 1, 10):
        if arr[i] == arr[j]:
            cnt -= 1     # 이렇게 해버리면 같은 숫자가 10개 들어왔을 때 cnt가 -45이 되어버린다..
print(cnt)