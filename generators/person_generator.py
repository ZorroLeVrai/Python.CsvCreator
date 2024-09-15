from .generator_tools import Gender, get_random_date_generator
from . import generator_constants as cst
from datetime import date, timedelta
import random as rd


class Person:
    def __init__(self, id, first_name, last_name, gender, birthday):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday


class PersonGenerator:
    def __init__(self, oldest_person_birthday: date, yougest_person_birthday: date):
        self.birthday_generator = get_random_date_generator(oldest_person_birthday, yougest_person_birthday)
        self.next_id = 1

    @staticmethod
    def generate_first_name(gender: Gender):
        if gender == Gender.Female:
            return rd.choice(cst.first_names_female)
        return rd.choice(cst.first_names_male)

    def generate_person(self):
        id = self.next_id
        gender = rd.choice(list(Gender))
        first_name = self.generate_first_name(gender)
        last_name = rd.choice(cst.last_names)
        birthday = self.birthday_generator()
        self.next_id += 1
        return Person(id, first_name, last_name, gender, birthday)
