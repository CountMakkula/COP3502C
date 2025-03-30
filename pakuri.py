#Pakuri class file
class Pakuri:
    #Initializes class
    def __init__(self, species):
        self.species = species
        self.attack = len(species)*7 + 9
        self.defense = len(species)*5 + 17
        self.speed = len(species)*6 + 13

    #Returns species
    def get_species(self):
        return self.species

    #Returns attack
    def get_attack(self):
        return self.attack

    #Returns defense
    def get_defense(self):
        return self.defense

    #Returns speed
    def get_speed(self):
        return self.speed

    #Sets new attack value (for whatever reason; it's literally never used lol)
    def set_attack(self, new_attack):
        self.attack = new_attack

    #Evolves pakuri
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

    #Redefines less than operator to be used on pakuri species name
    def __lt__(self, other):
        return self.species < other.species