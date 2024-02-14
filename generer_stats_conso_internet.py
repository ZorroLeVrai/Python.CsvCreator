import csv
import random
from datetime import date, timedelta

fichier_utilisateurs = "fichiers_csv/utilisateurs.csv"
fichier_reseaux_sociaux = "fichiers_csv/reseaux_sociaux.csv"

nb_personnes = 10000


def get_next_id():
    id = 1
    while True:
        yield id
        id += 1


def generate_ip():
    nums = []
    for _ in range(4):
        nums.append(str(random.randint(0, 255)))

    return ".".join(nums)


def get_time(avg):
    time = round(random.gauss(avg, avg/4), 1)
    return time if time > 0 else 0


def create_file(file_name, data):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


# Sample lists of first names, last names, and classes
first_names_female = ["Jade", "Louise", "Ambre", "Alba", "Emma", "Rose", "Alice", "Romy", "Anna", "Lina", "Léna", "Mia", "Lou", "Julia", "Chloé", "Alma", "Agathe", "Iris", "Inaya", "Charlie", "Juliette", "Léa", "Victoire", "Luna",
                      "Giulia", "Adèle", "Jeanne", "Nina", "Eva", "Olivia", "Zoé", "Léonie", "Romane", "Victoria", "Nour", "Lya", "Inès", "Lucie", "Lyana", "Lola", "Alix", "Charlotte", "Mila", "Sofia", "Louna", "Margaux", "Ava", "Elena", "Emy", "Mya"]
first_names_male = ["Gabriel", "Léo", "Raphaël", "Maël", "Louis", "Noah", "Jules", "Arthur", "Adam", "Lucas", "Liam", "Sacha", "Isaac", "Gabin", "Eden", "Hugo", "Naël", "Aaron", "Mohamed", "Léon", "Paul", "Noé", "Marceau", "Ethan",
                    "Nathan", "Théo", "Tom", "Nino", "Marius", "Ayden", "Malo", "Mathis", "Gaspard", "Martin", "Lyam", "Victor", "Rayan", "Elio", "Timéo", "Eliott", "Milo", "Robin", "Tiago", "Valentin", "Ibrahim", "Axel", "Augustin", "Amir", "Enzo", "Imran"]
last_names = ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent", "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel", "Fournier", "Girard", "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent", "Muller", "Lefevre", "Faure", "Andre", "Mercier", "Blanc", "Guerin", "Boyer", "Garnier", "Chevalier", "Francois", "Legrand", "Gauthier", "Garcia", "Perrin", "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Gautier",
              "Masson", "Marchand", "Duval", "Denis", "Dumont", "Marie", "Lemaire", "Noel", "Meyer", "Dufour", "Meunier", "Brun", "Blanchard", "Giraud", "Joly", "Riviere", "Lucas", "Brunet", "Gaillard", "Barbier", "Arnaud", "Martinez", "Gerard", "Roche", "Renard", "Schmitt", "Roy", "Leroux", "Colin", "Vidal", "Caron", "Picard", "Roger", "Fabre", "Aubert", "Lemoine", "Renaud", "Dumas", "Lacroix", "Olivier", "Philippe", "Bourgeois", "Pierre", "Benoit", "Rey", "Leclerc", "Payet", "Rolland", "Leclercq", "Guillaume", "Lecomte"]
social_networks = [("YouTube", 500), ("Instagram", 300), ("WhatsApp", 300), ("TikTok", 300), ("X", 150), ("Snapchat", 250),
                   ("Facebook", 150), ("Facebook Messenger", 150), ("WeChat", 100), ("QQ", 50), ("LinkedIn", 150), ("Pinterest", 100), ("Twitch", 100)]


oldest_person = date(1990, 1, 1)
days_delta = 365*15

person_data = [["id", "prénom", "nom", "date de naissance", "adresse IP"]]
time_spent_data = [["id", "adresse IP", "site", "temps passé"]]
id_generator = get_next_id()
for id_personne in range(1, nb_personnes+1):
    first_name = random.choice(first_names_female + first_names_male)
    last_male = random.choice(last_names)
    birth_date = oldest_person + timedelta(days=random.randint(1, days_delta))
    ip_address = generate_ip()
    person_data.append(
        [id_personne, first_name, last_male, birth_date, ip_address])
    nb_sites = random.randint(1, 8)
    for sn_name, sn_avg_time in random.sample(social_networks, nb_sites):
        id_data = next(id_generator)
        time_spent = get_time(sn_avg_time)
        time_spent_data.append([id_data, ip_address, sn_name, time_spent])

# Write data to the CSV file
create_file(fichier_utilisateurs, person_data)
create_file(fichier_reseaux_sociaux, time_spent_data)

print(f"files created successfully.")
