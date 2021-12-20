for test_case in range(int(input())):
    crying_sounds = list(map(str, input().split()))
    sound_excepts_fox = []

    while True:
        animal = input()
        if animal != "what does the fox say?":
            animal_sounds = animal.split(" ")
            sound_excepts_fox.append(animal_sounds[-1])
        else:
            print(*[i for i in crying_sounds if i not in sound_excepts_fox])
            break