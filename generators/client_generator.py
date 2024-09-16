import pandas as pd
from .person_generator import PersonGenerator
import generators.generator_tools as tools
from datetime import date

class Client:
    def __init__(self, client_id: int, first_name: str, last_name: str, address_id: str, birthday: date, client_code: str):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.address_id = address_id
        self.birthday = birthday
        self.client_code = client_code

    def to_data(self, headers: list[str]):
        return list(map(lambda header:getattr(self, header), headers))


class ClientDataFrameGenerator:
    client_headers = ["code_client", "prenom", "nom", "date_naissance", "adresse_id"]
    client_data_fields = ["client_code", "first_name", "last_name", "birthday", "address_id"]

    def __init__(self, oldest_client: date, youngest_client: date):
        self.person_generator = PersonGenerator(oldest_client, youngest_client)
        self.client_data: list[Client] = []
        self.client_code_generator = tools.unique_id_generator(lambda :tools.generate_random_code("LLddddddd"))

    def generate_persons(self, nb_person_to_generate: int, address_id: int):
        for _ in range(nb_person_to_generate):
            new_person = self.person_generator.create_person()
            client_code = self.client_code_generator()
            self.client_data.append(Client(new_person.person_id,
                                     new_person.first_name,
                                     new_person.last_name,
                                     address_id,
                                     new_person.birthday,
                                     client_code))

    def create_data_frame(self):
        client_row_data = list(map(lambda client:client.to_data(self.client_data_fields), self.client_data))
        return pd.DataFrame(client_row_data, columns=self.client_headers)
