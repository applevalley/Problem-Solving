notes = list(map(int, input().split()))
ascend, descend = 1, 1

for i in range(7):
    if notes[i] < notes[i + 1]:
        ascend += 1
    elif notes[i] > notes[i + 1]:
        descend += 1

if ascend == 8:
    print("ascending")
elif descend == 8:
    print("descending")
else:
    print("mixed")