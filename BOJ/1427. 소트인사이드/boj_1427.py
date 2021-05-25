# 숫자를 문자의 형태로 바꾼 뒤, list로 만들어 하나씩 쪼개버렸다.
# 그 뒤 .sort로 원본 데이터를 변경하되, reverse=True 속성으로 오름차순을 내림차순으로 바꿔버렸다.
# 출력하면 끝!

N = int(input())

seperate = list(str(N))
seperate.sort(reverse=True)
ans = "".join(seperate)



# 하지만 너무 성의없게 풀었다는 생각이 들었다.
# 바로 내장함수 sort를 이용해버리지 말고 정렬을 추가로 구현하면 어떨까?

to_str = str(N)                          # 숫자를 문자로 바꾼 것은 동일하다.
joined = ",".join(to_str)                # 문자열의 각 요소에 ,를 넣었다. 2,1,4,3의 형태가 된다.
splited = joined.split(",")              # 이걸 ,를 기준으로 쪼개면 [2, 1, 4, 3]이 될 것이다.

# 신나는 버블 소트의 시간
for i in range(len(splited) - 1):
    for j in range(i + 1, len(splited)):
        if int(splited[i]) < int(splited[j]):                # 앞 요소가 뒤 요소보다 작은 경우 순서를 바꿔줄 것이다.
            splited[i], splited[j] = splited[j], splited[i]

res = "".join(splited)                   # [4, 3, 2, 1]의 배열을 하나의 문자열로 합쳐준다!
print(res)