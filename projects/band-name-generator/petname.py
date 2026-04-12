class PetName:
    def __init__(self):
        self.pet_name = ""

    def get_pet_name(self):
        self.pet_name = input("Please Enter Pet name ")

    def set_pet_name(self):
        return self.pet_name
