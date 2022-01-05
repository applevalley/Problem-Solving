def dfs(x):
    global checked

    if x == 99:
        checked = True
        return

    for possible_route in G[x]:
        dfs(possible_route)
        if checked:
            return 1

    return 0


for test_case in range(1, 11):
    single_case, number_of_route = map(str, input().split())
    G = [[] * 100 for _ in range(100)]
    routes = list(map(int, input().split()))
    checked = False

    for i in range(0, len(routes), 2):
        start, end = routes[i], routes[i + 1]
        G[start].append(end)

    print(f"#{single_case} {dfs(0)}" if dfs(0) == 1 else f"#{single_case} 0")