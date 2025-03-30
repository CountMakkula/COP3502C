#Pakudex class file
#Import libraries
from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuriList = []

    #Gets current size of Pakudex
    def get_size(self):
        return len(self.pakuriList)

    #Gets max capacity of Pakudex
    def get_capacity(self):
        return self.capacity

    #Returns list of current pakuri names
    def get_species_array(self):
        returnList = []
        if len(self.pakuriList) == 0:
            return None
        for pakuri in self.pakuriList:
            returnList.append(pakuri.species)
        return returnList

    #Returns specific pakuri stats
    def get_stats(self, species):
        for pakuri in self.pakuriList:
            if pakuri.species == species:
                return [pakuri.attack, pakuri.defense, pakuri.speed]
        return None

    #Sorts the Pakudex alphabetically
    def sort_pakuri(self):
        self.pakuriList.sort()

    #Adds a new pakuri
    def add_pakuri(self, species):
        if len(self.pakuriList) == self.capacity:
            return False
        for pakuri in self.pakuriList:
            if pakuri.species == species:
                return False
        newPakuri = Pakuri(species)
        self.pakuriList.append(newPakuri)
        return True

    #Evolves a pakuri
    def evolve_species(self, species):
        for pakuri in self.pakuriList:
            if pakuri.species == species:
                pakuri.evolve()
                return True
        return False