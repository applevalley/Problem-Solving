def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)


N = int(input())

print(fibo(N))

