from datetime import date, timedelta
import csv
import random

csv_file_path = "fichiers_csv/eleves_notes.csv"
nb_pupils = 10000
fille = "Fille"
garcon = "Garçon"

# Sample lists of first names, last names, and classes
first_names_female = ["Jade", "Louise", "Ambre", "Alba", "Emma", "Rose", "Alice", "Romy", "Anna", "Lina", "Léna", "Mia", "Lou", "Julia", "Chloé", "Alma", "Agathe", "Iris", "Inaya", "Charlie", "Juliette", "Léa", "Victoire", "Luna",
                      "Giulia", "Adèle", "Jeanne", "Nina", "Eva", "Olivia", "Zoé", "Léonie", "Romane", "Victoria", "Nour", "Lya", "Inès", "Lucie", "Lyana", "Lola", "Alix", "Charlotte", "Mila", "Sofia", "Louna", "Margaux", "Ava", "Elena", "Emy", "Mya"]
first_names_male = ["Gabriel", "Léo", "Raphaël", "Maël", "Louis", "Noah", "Jules", "Arthur", "Adam", "Lucas", "Liam", "Sacha", "Isaac", "Gabin", "Eden", "Hugo", "Naël", "Aaron", "Mohamed", "Léon", "Paul", "Noé", "Marceau", "Ethan",
                    "Nathan", "Théo", "Tom", "Nino", "Marius", "Ayden", "Malo", "Mathis", "Gaspard", "Martin", "Lyam", "Victor", "Rayan", "Elio", "Timéo", "Eliott", "Milo", "Robin", "Tiago", "Valentin", "Ibrahim", "Axel", "Augustin", "Amir", "Enzo", "Imran"]
last_names = ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent", "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel", "Fournier", "Girard", "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent", "Muller", "Lefevre", "Faure", "Andre", "Mercier", "Blanc", "Guerin", "Boyer", "Garnier", "Chevalier", "Francois", "Legrand", "Gauthier", "Garcia", "Perrin", "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Gautier",
              "Masson", "Marchand", "Duval", "Denis", "Dumont", "Marie", "Lemaire", "Noel", "Meyer", "Dufour", "Meunier", "Brun", "Blanchard", "Giraud", "Joly", "Riviere", "Lucas", "Brunet", "Gaillard", "Barbier", "Arnaud", "Martinez", "Gerard", "Roche", "Renard", "Schmitt", "Roy", "Leroux", "Colin", "Vidal", "Caron", "Picard", "Roger", "Fabre", "Aubert", "Lemoine", "Renaud", "Dumas", "Lacroix", "Olivier", "Philippe", "Bourgeois", "Pierre", "Benoit", "Rey", "Leclerc", "Payet", "Rolland", "Leclercq", "Guillaume", "Lecomte"]

# Generate random data for the CSV file
data = [["id", "prénom", "nom", "note"]]
for index in range(nb_pupils):
    id = index + 1
    gender = random.choice([fille, garcon])
    first_name = random.choice(
        first_names_female) if gender == fille else random.choice(first_names_male)
    last_name = random.choice(last_names)
    note = round(random.uniform(0, 20), 2)
    data.append([id, first_name, last_name, note])

# Write data to the CSV file
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully.")
