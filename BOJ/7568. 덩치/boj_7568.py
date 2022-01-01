'''
두 명의 사람 A, B에 있어 A의 키와 몸무게가 B의 키와 몸무게보다 크다면 "A의 덩치가 B보다 크다"라고 말할 수 있다.
키와 몸무게 둘 다 우위에 있지 않는 경우는 순위를 가를 수 없고, 이 경우 공동 순위를 준다.
입력이 들어온 순서대로 순위를 매기자!

사람의 수 N이 최대 50이기 때문에 O(N^2)로 모든 사람들을 다 순회하며 1번부터 N번까지 모든 사람에 대한 등수를 구해도 충분해보인다!
'''


N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    ambiguous_count = 0     # 순위를 매길 수 없는 경우(공동 k위)를 나타내기 위해
    place = N               # 기본적으로 N등에서 시작

    for j in range(N):
        if i == j: continue     # 자기 자신은 비교의 대상에 포함되지 않는다.

        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:     # 덩치가 더 큰 경우, 순위를 1 차감
            place -= 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:   # 덩치가 더 작은 경우는 건너뛴다.
            pass
        else:                                                               # 그를 제외한 모든 경우, 순위를 매길 수 없다.
            ambiguous_count += 1

    place -= ambiguous_count          # 전체 순위에서 else문 안에서 더해진 변수의 값을 빼주면 최종 순위가 된다.
    print(place, end=' ')




