def solution(absolutes, signs):
    plus = [absolutes[i] for i in range(len(absolutes)) if signs[i]]
    minus = [-absolutes[i] for i in range(len(absolutes)) if not signs[i]]

    return (sum(plus) + sum(minus))