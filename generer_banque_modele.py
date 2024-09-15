import pandas as pd
import generators.generator_tools as tools
import generators.person_generator as perg
import generators.address_generator as adrg
from datetime import date

oldest_person = date(1960,1,1)
youngest_person = date(2020,1,1)

def create_csv(dataframe, file_name):
    dataframe.to_csv(file_name, index=False)
    print(f"Fichier {file_name} généré correctement")


def generate_address_dataframe(nb_address_to_generate):
    address_headers = ["id", "numero_rue", "nom_rue", "code_ville", "nom_ville", "nom_famille"]
    address_generator = adrg.AddressGenerator()
    address_data = []
    for _ in range(nb_address_to_generate):
        new_address = address_generator.generate_address()
        address_data.append([new_address.id, new_address.street_number, new_address.street_name, new_address.zipcode, new_address.town, new_address.last_name])
    return pd.DataFrame(address_data, columns=address_headers)


def generate_person_dataframe(nb_person_to_generate):
    person_headers = ["id", "prénom", "nom", "date_naissance", "code_client"]
    personGenerator = perg.PersonGenerator(oldest_person, youngest_person)
    personCodeGenerator = tools.unique_id_generator(lambda :tools.generate_random_code("LLddddddd"))
    person_data = []
    for _ in range(nb_person_to_generate):
        new_person = personGenerator.generate_person()
        person_code = personCodeGenerator()
        person_data.append([new_person.id, new_person.first_name, new_person.last_name, new_person.birthday, person_code])
    return pd.DataFrame(person_data, columns=person_headers)


def generate_accounts():
    pass


df_address = generate_address_dataframe(500)
df_persons = generate_person_dataframe(1000)
create_csv(df_address, "./adresses.csv")
create_csv(df_persons, "./personnes.csv")
