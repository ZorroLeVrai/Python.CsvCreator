import csv
import random

csv_file_path = "fichiers_csv/notes.csv"
nb_pupils = 5000

index = 0

def choose_lv2():
    rand = random.random()
    if rand <= 0.75:
        return 8
    if rand <= 0.92:
        return 9
    if rand <= 0.96:
        return 10
    if rand < 0.99:
        return 11
    
    return 12

def choose_lv3(lv2):
    while True:
        lv3 = random.randint(8,12)
        if lv3 == lv2:
            continue
        return lv3

data = [["id", "id_eleve", "id_matiere", "note"]]
for id_eleve in range(1, 5001):
    matieres = [*range(1,8)]
    rand = random.random()
    lv2 = 0
    if rand < 0.9:
        lv2 = choose_lv2()
        matieres.append(lv2)
    if rand < 0.1:
        lv3 = choose_lv3(lv2)
        matieres.append(lv3)

    for id_matiere in matieres:
        index = index + 1
        note = (1 + round(39*random.random())) / 2
        data.append([index, id_eleve, id_matiere, note])

# Write data to the CSV file
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully.")
