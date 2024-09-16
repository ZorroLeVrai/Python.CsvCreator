import pandas as pd
import random as rd
from . import generator_constants as cst


class Address:
    def __init__(self, id: int, street_number: int, street_name: str, town: str, zipcode: str, last_name: str):
        self.address_id = id
        self.street_number = street_number
        self.street_name = street_name
        self.town = town
        self.zipcode = zipcode
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.street_number} {self.street_name} {self.zipcode} {self.town}"
    
    def to_data(self, headers: list[str]):
        return list(map(lambda header:getattr(self, header), headers))
    

class AddressGenerator:
    max_street_number = 128

    def __init__(self):
        # cst.villes = [(town_name, list_of_zip_codes), town_population]
        # self.town_info = (town_name, list_of_zip_codes)
        self.town_info = list(map(lambda item: (item[0], item[1]), cst.villes))
        # self.weight = town_population
        self.weight = list(map(lambda item: item[2], cst.villes))
        self.next_id = 1

    def generate_town(self):
        [town_name, town_zips_str] = rd.choices(self.town_info, weights=self.weight, k=1)[0]
        town_zips = town_zips_str.split("-")
        town_zip_code = rd.choice(town_zips)
        return (town_name, town_zip_code)


    def create_address(self) -> Address:
        street_number = rd.randint(1, self.max_street_number)
        street_name = rd.choice(cst.street_list)
        (town_name, town_zip_code) = self.generate_town()
        last_name = rd.choice(cst.last_names)
        new_address = Address(self.next_id, street_number, street_name, town_name, town_zip_code, last_name)
        self.next_id += 1
        return new_address


class AddressDataFrameGenerator:
    address_headers = ["adresse_id", "numero_rue", "nom_rue", "code_ville", "nom_ville", "nom_famille"]
    address_data_fields = ["address_id", "street_number", "street_name", "zipcode", "town", "last_name"]

    def __init__(self):
        self.address_generator = AddressGenerator()
        self.address_data: list[Address] = []

    def generate_addresses(self, nb_address_to_generate: int):
        for _ in range(nb_address_to_generate):
            new_address = self.address_generator.create_address()
            self.address_data.append(new_address)

    def create_data_frame(self):
        address_row_data = list(map(lambda address:address.to_data(self.address_data_fields), self.address_data))
        return pd.DataFrame(address_row_data, columns=self.address_headers)
