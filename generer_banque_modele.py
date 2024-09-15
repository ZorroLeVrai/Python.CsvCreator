import pandas as pd
import generators.generator_tools as tools
import generators.person_generator as perg
from datetime import date

nb_person_to_generate = 1000
oldest_person = date(1960,1,1)
youngest_person = date(2020,1,1)
person_headers = ["id", "prénom", "nom", "date_naissance", "code_client"]

def create_csv(dataframe, file_name):
    dataframe.to_csv(file_name, index=False)
    print(f"Fichier {file_name} généré correctement")

def generate_addresses():
    pass

def generate_person_file():
    personGenerator = perg.PersonGenerator(oldest_person, youngest_person)
    personCodeGenerator = tools.unique_id_generator(lambda :tools.generate_random_code("LLddddddd"))
    data = []
    for _ in range(nb_person_to_generate):
        new_person = personGenerator.generate_person()
        person_code = personCodeGenerator()
        data.append([new_person.id, new_person.first_name, new_person.last_name, new_person.birthday, person_code])

    return pd.DataFrame(data, columns=person_headers)


def generate_accounts():
    pass


df_persons = generate_person_file()
create_csv(df_persons, "./person.csv")
