alpha = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
numbers = []
words = input()

for i in words:
    numbers.append(alpha[ord(i) - 65])

while len(numbers) > 1:
    calc = []
    for i in range(0, len(numbers), 2):
        if i == (len(numbers) - 1):
            calc.append(numbers[i])
            break
        first, second = numbers[i], numbers[i + 1]
        calc.append((first + second) % 10)
    numbers = calc

print("I'm a winner!") if numbers[0] % 2 else print("You're the winner?")