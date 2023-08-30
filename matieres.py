import csv

csv_file_path = "fichiers_csv/matieres.csv"

matieres = ["Français", "Histoire Géographie", "Anglais", "Mathématiques", "SVT", "Physique Chimie", "EPS"]
lv2 = ["Espagnol", "Allemand", "Italien", "Portugais", "Arabe"]

data = [["id", "libelle_matiere"]]
for id, matiere in enumerate([*matieres, *lv2]):
    data.append([id + 1, matiere])

# Write data to the CSV file
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully.")