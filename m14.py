def GetWinner(filename):
    MaxLvl = 0
    Winner = ""

    with open(filename, 'r') as file:
        for line in file:
            Parts = line.strip().split(',')
            Trainer = Parts[0]
            Pakuri = Parts[1:]

            for species in Pakuri:
                name, level = species.rsplit('-', 1)
                level = int(level)

                if level > MaxLvl:
                    MaxLvl = level
                    Winner = Trainer

    return Winner

def WriteWinnerFile(winner, filename):
    with open(filename, 'w') as file:
        file.write(winner)

def WriteSpeciesFile(inputFilename, outputFilename):
    SpeciesSet = set()

    with open(inputFilename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')[1:]
            for pakuri in parts:
                name, _ = pakuri.rsplit('-', 1)
                SpeciesSet.add(name)

    SortedSpecies = sorted(SpeciesSet)

    with open(outputFilename, 'w') as file:
        for species in SortedSpecies:
            file.write(species + '\n')

def main():
    ContestFile = 'contest.txt'
    WinnersFile = 'winners.txt'
    SpeciesFile = 'pakuri.txt'

    winner = GetWinner(ContestFile)
    WriteWinnerFile(winner, WinnersFile)
    WriteSpeciesFile(ContestFile, SpeciesFile)

if __name__ == "__main__":
    main()