class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        if owner and not isinstance(owner, Owner):
            raise TypeError("owner must be an instance of Owner Class")
        self.owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise TypeError("pet_type must be in accepted PET_TYPES")
        self.pet_type = pet_type

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        owner_pets = self.pets()
        return sorted(owner_pets, key=lambda pet:pet.name)