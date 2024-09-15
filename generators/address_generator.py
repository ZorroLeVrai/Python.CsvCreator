class Address:
    def __init__(self, street_number: int, street_name: str, town: str, zipcode: str):
        self.street_number = street_number
        self.street_name = street_name
        self.town = town
        self.zipcode = zipcode

    def __str__(self) -> str:
        return f"{self.street_number} {self.street_name} {self.zipcode} {self.town}"