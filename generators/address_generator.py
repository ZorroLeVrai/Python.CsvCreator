from . import generator_constants as cst
import random as rd

class Address:
    def __init__(self, id, street_number: int, street_name: str, town: str, zipcode: str, last_name: str):
        self.id = id
        self.street_number = street_number
        self.street_name = street_name
        self.town = town
        self.zipcode = zipcode
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.street_number} {self.street_name} {self.zipcode} {self.town}"
    

class AddressGenerator:
    def __init__(self):
        self.towns = list(map(lambda item:[(item[0], item[1]), item[2]], cst.villes))
        self.town_info = list(map(lambda item: item[0], self.towns))
        self.weight = list(map(lambda item: item[1], self.towns))
        self.next_id = 1

    def generate_town(self):
        [town_name, town_zips_str] = rd.choices(self.town_info, weights=self.weight, k=1)[0]
        town_zips = town_zips_str.split("-")
        town_zip_code = rd.choice(town_zips)
        return (town_name, town_zip_code)


    def generate_address(self):
        street_number = rd.randint(1, 128)
        street_name = rd.choice(cst.street_list)
        (town_name, town_zip_code) = self.generate_town()
        last_name = rd.choice(cst.last_names)
        new_address = Address(self.next_id, street_number, street_name, town_name, town_zip_code, last_name)
        self.next_id += 1
        return new_address
