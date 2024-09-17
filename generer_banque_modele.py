import pandas as pd
import random as rd
import generators.generator_tools as tools
import generators.client_generator as clig
import generators.address_generator as adrg
import generators.account_generator as accg
from datetime import date

oldest_client = date(1960,1,1)
youngest_client = date(2020,1,1)
bnp_country_code = "FR"
bnp_bank_code = "30004"
bnp_nb_agencies = 209

def create_csv(dataframe: pd.DataFrame, file_name: str):
    dataframe.to_csv(file_name, index=False)
    print(f"Fichier {file_name} généré correctement")


def create_address_generator(nb_address_to_generate: int):
    address_df_generator = adrg.AddressDataFrameGenerator()
    address_df_generator.generate_addresses(nb_address_to_generate)
    return address_df_generator


def get_random_clients_to_create():
    return rd.choices(list(range(1,8)), [0.3, 0.1, 0.1, 0.4, 0.05, 0.04, 0.01], k=1)[0]

def get_random_accounts_to_create():
    return rd.choices(list(range(1,6)), [0.45, 0.35, 0.11, 0.06, 0.03], k=1)[0]


address_generator = create_address_generator(5000)
client_df_generator = clig.ClientDataFrameGenerator(oldest_client, youngest_client)
account_df_generator = accg.AccountDataFrameGenerator(bnp_country_code, bnp_bank_code, bnp_nb_agencies)
#generate clients
for address_item in address_generator.address_data:
    nb_clients = get_random_clients_to_create()
    client_df_generator.generate_persons(nb_clients, address_item.address_id)
#generate accounts
for client in client_df_generator.client_data:
    nb_accounts = get_random_accounts_to_create()
    account_df_generator.generate_accounts(nb_accounts, client.client_code)
#generate dataframes
df_addresses = address_generator.create_data_frame()
df_clients = client_df_generator.create_data_frame()
df_accounts = account_df_generator.create_data_frame()

create_csv(df_addresses, tools.create_path("adresses.csv"))
create_csv(df_clients, tools.create_path("clients.csv"))
create_csv(df_accounts, tools.create_path("accounts.csv"))
