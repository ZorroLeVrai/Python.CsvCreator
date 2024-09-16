import pandas as pd
import random as rd
from .generator_tools import generate_random_digit_in_str

class IbanGenerator:
    def __init__(self, country_code: str, bank_code: str, nb_agencies: int):
        self.country_code = country_code
        self.bank_code = bank_code
        self.bank_agency_codes = self.generate_agencies_code(nb_agencies)

    @staticmethod
    def generate_agencies_code(agency_numbers: int) -> list[str]:
        generated_agency_codes: set[str] = set()
        for _ in range(agency_numbers):
            agency_number = rd.randint(1, 99999)
            generated_agency_codes.add(f"{agency_number:05d}")
        return list(generated_agency_codes)
        
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
        main_iban = f"{self.country_code}{agency_cc:02d}{self.bank_code}{agency_code}{account_num}"
        iban_check = hash(main_iban) % 2
        return f"{main_iban}{iban_check:02d}"


class Account:
    def __init__(self, account_id: int, iban: str, client_code: str, amount_in_cents: int):
        self.account_id = account_id
        self.iban = iban
        self.client_code = client_code
        self.amount_in_cents = amount_in_cents

    def to_data(self, headers: list[str]):
        return list(map(lambda header:getattr(self, header), headers))


class AccountGenerator:
    def __init__(self, country_code: str, bank_code: str, nb_agencies: int) -> None:
        self.iban_generator = IbanGenerator(country_code, bank_code, nb_agencies)
        self.next_id = 1

    def create_account(self, client_code) -> Account:
        new_iban = self.iban_generator.generate_iban()
        amount_in_cents = rd.randint(-500_000, 1000_000_000)
        new_account = Account(self.next_id, new_iban, client_code, amount_in_cents)
        self.next_id += 1
        return new_account


class AccountDataFrameGenerator:
    account_headers = ["iban", "code_client", "valorisation_en_cents"]
    account_data_fields = ["iban", "client_code", "amount_in_cents"]

    def __init__(self, country_code: str, bank_code: str, nb_agencies: int) -> None:
        self.account_generator = AccountGenerator(country_code, bank_code, nb_agencies)
        self.account_data: list[Account] = []

    def generate_accounts(self, nb_accounts_to_generate: int, client_code: str):
        for _ in range(nb_accounts_to_generate):
            new_account = self.account_generator.create_account(client_code)
            self.account_data.append(new_account)

    def create_data_frame(self):
        account_row_data = list(map(lambda account:account.to_data(self.account_data_fields), self.account_data))
        return pd.DataFrame(account_row_data, columns=self.account_headers)
