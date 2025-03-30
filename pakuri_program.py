#Main Pakudex file
#Import libraries
from pakudex import Pakudex

def Menu():
    print("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n")
    Option = int(input("What would you like to do? "))
    #List pakuri
    if Option == 1:
        ListPakuri()
    #Show pakuri
    elif Option == 2:
        ShowPakuri()
    #Add pakuri
    elif Option == 3:
        AddPakuri()
    #Evolve pakuri
    elif Option == 4:
        EvolvePakuri()
    #Sort pakuri
    elif Option == 5:
        SortPakuri()
    #Exit
    elif Option == 6:
        print("Thanks for using Pakudex! Bye!")
    #Invalid command
    else:
        print("Unrecognized menu selection!")
        Menu()

#List pakuri function
def ListPakuri():
    pakuriList = NewPakudex.get_species_array()
    i = 0
    if pakuriList is None:
        print("No Pakuri in Pakudex yet!")
    else:
        print("Pakuri In Pakudex:")
        for pokemon in pakuriList:
            i += 1
            print(f"{i}. {pokemon}")
    Menu()

#Show pakuri function
def ShowPakuri():
    name = input("Enter the name of the species to display: ")
    stats = NewPakudex.get_stats(name)
    if stats is None:
        print("Error: No such Pakuri!")
    else:
        print(f"\nSpecies: {name}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed:{stats[2]}")
    Menu()

#Add pakuri function
def AddPakuri():
    if NewPakudex.get_size() == NewPakudex.get_capacity():
        print("Error: Pakudex is full!")
        Menu()
    name = input("Enter the name of the species to add: ")
    check = NewPakudex.add_pakuri(name)
    if check:
        print(f"Pakuri species {name} successfully added!")
    else:
        print("Error: Pakudex already contains this species!")
    Menu()

#Evolve pakuri function
def EvolvePakuri():
    name = input("Enter the name of the species to evolve: ")
    check = NewPakudex.evolve_species(name)
    if check:
        print(f"{name} has evolved!")
    else:
        print("Error: No such Pakuri!")
    Menu()

#Sort pakuri function
def SortPakuri():
    NewPakudex.sort_pakuri()
    print("Pakuri have been sorted!")
    Menu()

#Main function
if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    Capacity = input("Enter max capacity of the Pakudex: ")
    try:
        Capacity = int(Capacity)
    except:
        Capacity = Capacity
    while type(Capacity) != int or Capacity < 1:
        print("Please enter a valid size.")
        Capacity = input("Enter max capacity of the Pakudex: ")
        try:
            Capacity = int(Capacity)
        except:
            Capacity = Capacity
    print(f"The Pakudex can hold {Capacity} species of Pakuri.")
    NewPakudex = Pakudex(Capacity)
    Menu()
