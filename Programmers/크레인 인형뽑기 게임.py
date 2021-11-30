def solution(board, moves):
    answer = 0
    get_prizes = []

    for i in range(len(moves)):
        line = [[j, moves[i] - 1] for j in range(len(board)) if board[j][moves[i] - 1]]
        if not line: continue

        get_prizes.append(board[line[0][0]][line[0][1]])
        board[line[0][0]][line[0][1]] = 0

        if len(get_prizes) >= 2:
            if get_prizes[-1] == get_prizes[-2]:
                get_prizes = get_prizes[:-2]
                answer += 2

    return answer