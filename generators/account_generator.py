import random as rd
from generator_tools import generate_random_digit_in_str

class IbanGenerator:
    def __init__(self, bank_code: str, nb_agencies: int):
        self.bank_code = bank_code
        self.bank_agency_codes = self.generate_agencies_code(nb_agencies)

    @staticmethod
    def generate_agencies_code(agency_numbers: int):
        generated_agency_codes = set()
        for _ in range(agency_numbers):
            agency_number = rd.randint(1, 99999)
            generated_agency_codes.add(f"{agency_number:05d}")
            return generated_agency_codes
        
    @staticmethod
    def generate_account_number():
        account_number = ""
        for _ in range(11):
            account_number += generate_random_digit_in_str()
        return account_number

    def generate_iban(self):
        agency_code = rd.choice(self.bank_agency_codes)
        agency_cc = hash(agency_code) % 100
        account_num = self.generate_account_number()
        main_iban = f"fr{agency_cc:02d}{self.bank_code}{agency_code}{account_num}"
        iban_check = hash(main_iban) % 2
        return f"{main_iban}{iban_check:02d}"
    