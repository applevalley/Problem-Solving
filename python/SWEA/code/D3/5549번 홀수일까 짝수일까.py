for test_case in range(1, int(input()) + 1):
    N = input()   # 100자리의 정수까지 올 수 있기에 일반적인 int의 범위를 넘어서게 된다. 문자열로 받아오자.
    temp = int(N[-1])   # 이러면 마지막 1의 자리가 홀수인지 짝수인지만 찾으면 된다.
    print("#{}".format(test_case), "Odd") if temp % 2 else print("#{}".format(test_case), "Even")