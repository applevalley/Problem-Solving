for test_case in range(int(input())):
    n = int(input())
    cnt = 0

    for a in range(1, 4):
        if a == n: cnt += 1
        for b in range(1, 4):
            if (a + b) == n: cnt += 1
            for c in range(1, 4):
                if (a + b + c) == n: cnt += 1
                for d in range(1, 4):
                    if (a + b + c + d) == n: cnt += 1
                    for e in range(1, 4):
                        if (a + b + c + d + e) == n: cnt += 1
                        for f in range(1, 4):
                            if (a + b + c + d + e + f) == n: cnt += 1
                            for g in range(1, 4):
                                if (a + b + c + d + e + f + g) == n: cnt += 1
                                for h in range(1, 4):
                                    if (a + b + c + d + e + f + g + h) == n: cnt += 1
                                    for i in range(1, 4):
                                        if (a + b + c + d + e + f + g + h + i) == n: cnt += 1
                                        for j in range(1, 4):
                                            if (a + b + c + d + e + f + g + h + i + j) == n: cnt += 1
    print(cnt)