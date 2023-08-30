import csv

csv_file_path = "fichiers_csv/niveaux.csv"

matieres = ["6ème", "5ème", "4ème", "3ème", "Seconde", "Première", "Terminale"]

data = [["id", "niveau"]]
for id, matiere in enumerate(matieres):
    data.append([id+1, matiere])

# Write data to the CSV file
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully.")