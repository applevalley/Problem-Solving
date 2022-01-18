import math

N, K = map(int, input().split())
scores = sorted([int(float(input()) * 10) for _ in range(N)])

if K:
    trimmed_mean = round(sum(scores[K:-K]) / len(scores[K:-K]), 1)
    adjusted_mean = round(sum([sum([scores[K] for i in range(K)]), sum(scores[K: -K]), sum([scores[-(K + 1)] for i in range(K)])]) / N, 1)
    print("%0.2f" % float(trimmed_mean / 10))
    print("%0.2f" % float(adjusted_mean / 10))
else:
    print("%0.2f" % ((sum(scores) / N) / 10))
    print("%0.2f" % ((sum(scores) / N) / 10))
