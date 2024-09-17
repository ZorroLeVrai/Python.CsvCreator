import string
import random as rd
import os
from datetime import date, timedelta
from enum import Enum

path_generation = "./fichiers_csv"
Gender = Enum("Gender", ["Male", "Female"])

def create_path(file_name):
    return os.path.join(path_generation, file_name)

def generate_random_digit_in_str():
    return str(rd.randint(0, 9))

def generate_random_letter(is_upper):
    if is_upper:
        return rd.choice(string.ascii_uppercase)
    return rd.choice(string.ascii_lowercase)

def generate_random_code(format: str) -> str:
    result = ""
    for format_item in format:
        match format_item:
            case "l":
                result += generate_random_letter(False)
            case "L":
                result += generate_random_letter(True)
            case "d" | "D":
                result += generate_random_digit_in_str()
            case _:
                raise ValueError(f"The format {format_item} is unknown")
    
    return result


def unique_id_generator(func):
    unique_ids = set()

    def get_unique_id():
        while True:
            unique_id = func()
            if unique_id not in unique_ids:
                unique_ids.add(unique_id)
                return unique_id

    return get_unique_id


def get_random_date_generator(start_date: date, end_date: date):
    nb_days = (end_date - start_date).days
    if (nb_days < 0):
        raise ValueError(f"end_date should not be before start_date (start_date:{start_date}, end_date:{end_date})")
    
    def generate_date():
        rand_nb_days = rd.randint(0, nb_days)
        return start_date + timedelta(days=rand_nb_days)

    return generate_date


def get_random_date(start_date: date, end_date: date):
    nb_days = (end_date - start_date).days
    rand_nb_days = rd.randint(0, nb_days)
    return start_date + timedelta(days=rand_nb_days)
