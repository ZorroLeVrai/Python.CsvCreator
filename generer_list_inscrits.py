from datetime import date, timedelta
import fichiers_csv.generators.generator_tools as tools
import csv
import random

nb_persons = 5000
nb_football_players = 1000
nb_tennis_players = 1000
fille = "Fille"
garcon = "Garçon"

# Sample lists of first names, last names, and classes
first_names_female = ["Jade", "Louise", "Ambre", "Alba", "Emma", "Rose", "Alice", "Romy", "Anna", "Lina", "Léna", "Mia", "Lou", "Julia", "Chloé", "Alma", "Agathe", "Iris", "Inaya", "Charlie", "Juliette", "Léa", "Victoire", "Luna", "Giulia", "Adèle", "Jeanne", "Nina", "Eva", "Olivia", "Zoé", "Léonie", "Romane", "Victoria", "Nour", "Lya", "Inès", "Lucie", "Lyana", "Lola", "Alix", "Charlotte", "Mila", "Sofia", "Louna", "Margaux", "Ava", "Elena", "Emy", "Mya"]
first_names_male = ["Gabriel", "Léo", "Raphaël", "Maël", "Louis", "Noah", "Jules", "Arthur", "Adam", "Lucas", "Liam", "Sacha", "Isaac", "Gabin", "Eden", "Hugo", "Naël", "Aaron", "Mohamed", "Léon", "Paul", "Noé", "Marceau", "Ethan", "Nathan", "Théo", "Tom", "Nino", "Marius", "Ayden", "Malo", "Mathis", "Gaspard", "Martin", "Lyam", "Victor", "Rayan", "Elio", "Timéo", "Eliott", "Milo", "Robin", "Tiago", "Valentin", "Ibrahim", "Axel", "Augustin", "Amir", "Enzo", "Imran"]
last_names = ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent", "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel", "Fournier", "Girard", "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent", "Muller", "Lefevre", "Faure", "Andre", "Mercier", "Blanc", "Guerin", "Boyer", "Garnier", "Chevalier", "Francois", "Legrand", "Gauthier", "Garcia", "Perrin", "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Gautier", "Masson", "Marchand", "Duval", "Denis", "Dumont", "Marie", "Lemaire", "Noel", "Meyer", "Dufour", "Meunier", "Brun", "Blanchard", "Giraud", "Joly", "Riviere", "Lucas", "Brunet", "Gaillard", "Barbier", "Arnaud", "Martinez", "Gerard", "Roche", "Renard", "Schmitt", "Roy", "Leroux", "Colin", "Vidal", "Caron", "Picard", "Roger", "Fabre", "Aubert", "Lemoine", "Renaud", "Dumas", "Lacroix", "Olivier", "Philippe", "Bourgeois", "Pierre", "Benoit", "Rey", "Leclerc", "Payet", "Rolland", "Leclercq", "Guillaume", "Lecomte"]

oldest_person = date(1960,1,1)
youngest_person = date(2020,1,1)

# Generate random data for the CSV file
#person_list = [["id", "prénom", "nom", "genre", "date_naissance"]]
person_list = []
birthday_generator = tools.get_random_date_generator(oldest_person, youngest_person)
for index in range(nb_persons):
    id = index + 1
    gender = random.choice([fille, garcon])
    date_of_birth = birthday_generator()
    first_name = random.choice(first_names_female) if gender == fille else random.choice(first_names_male)
    last_name = random.choice(last_names)
    person_list.append([id, first_name, last_name, gender, date_of_birth])

def create_person_list(csv_file_path, nb_selected):
    list_header = ["id", "prénom", "nom", "date_naissance"]
    person_ids = set()
    #create football players
    for index in range(nb_selected):
        person_ids.add(random.randint(0, nb_persons))
    
    output_list = [list_header]
    index = 0
    for id in person_ids:
        index += 1
        person = person_list[id]
        output_list.append([index, person[1], person[2], person[4]])

    # Write data to the CSV file
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(output_list)


create_person_list("fichiers_csv/football_players.csv", nb_football_players)
create_person_list("fichiers_csv/tennis_players.csv", nb_tennis_players)

print(f"CSV files created successfully.")
