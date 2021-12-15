'''
예산은 정해져 있고, 최대한 많은 부서의 물품을 구매해야 한다.
제한된 예산 안에서 "최대한" 많은 부서에 지원을 해주려면 어떻게 해야 할까?
신청한 금액이 적은 순으로 정렬을 해주면 가능하다.
'''


def solution(d, budget):
    answer, cnt = 0, 0

    if sum(d) <= budget:
        return len(d)

    d.sort()

    for i in d:
        cnt += i
        if cnt > budget: break

        answer += 1

    return answer