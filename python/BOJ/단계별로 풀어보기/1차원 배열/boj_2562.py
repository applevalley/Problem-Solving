arr = []
for i in range(9):
    arr.append(int(input()))

max = arr[0]
max_idx = 0   # 얘를 안 써줬더니 런타임 에러가 났다. max를 배열의 첫 값으로 주고 시작했기에 max가 가장 큰 값일 경우 max_idx를 인식하지 못한다.
for i in range(1,len(arr)):
    if arr[i] > max:
        max = arr[i]
        max_idx = i


print(max)
print(max_idx+1)