from cityname import CityName
from petname import PetName


class GenerateBandName:
    def __init__(self):
        self.band_name = ""
        self.city_name = ""
        self.pet_name = ""

        # creaete object of the cityname
        self.city_name = CityName()
        # create object of the petname
        self.pet_name = PetName()

    def take_input(self) -> None:
        self.take_city_name = self.city_name.get_city_name()
        self.take_pet_name = self.pet_name.get_pet_name()

    def generate_band_name(self):

        self.band_name = self.city_name.set_city_name() + self.pet_name.set_pet_name()
        print(f"Band Name is : {self.band_name}")


if __name__ == "__main__":

    band_name_generate = GenerateBandName()
    band_name_generate.take_input()
    band_name_generate.generate_band_name()
