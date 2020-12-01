all_dwarfs = []
height = 0
cnt = 0

for i in range(9):
    dwarf = int(input())
    all_dwarfs.append(dwarf)
    height += dwarf

for i in range(8):
    for j in range(i + 1, 9):
        if height - (all_dwarfs[i] + all_dwarfs[j]) == 100:
            all_dwarfs.remove(all_dwarfs[i])
            all_dwarfs.remove(all_dwarfs[j - 1])
            break
    if len(all_dwarfs) == 7:
        break

all_dwarfs.sort()

for i in all_dwarfs:
    print(i)