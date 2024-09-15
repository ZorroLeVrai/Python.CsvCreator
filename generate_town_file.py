import pandas as pd
import random as rd

file_path = "villes_simple.csv"
df_villes = pd.read_csv("villes_simple.csv")

villes = []
for row in df_villes.itertuples(index=True):
    ville_nom = row.ville_nom
    zip_codes = row.ville_code_postal  #.split("-")
    poids = row.ville_population_2012
    villes.append((ville_nom, zip_codes, poids))
    # for _ in range(poids // 10000):
    #     zipe_code = rd.choice(zip_codes)
    #     villes.append((ville_nom, zipe_code))

print(villes)
    