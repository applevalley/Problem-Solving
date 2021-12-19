serial_number = list(map(int, input().split()))
check_number = sum([i ** 2 for i in serial_number]) % 10
print(check_number)