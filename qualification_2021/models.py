import sys
from file_reader import read, write

class InputFile:
    def __init__(self, inputFile):
        """Create an input file

        Args:
            inputFile (string): filename of the input file including the path
        """
        input = read(inputFile)
        firstLineArray = input[0].split(" ")
        self.numberOfPizzas = int(firstLineArray[0])
        self.teamList = firstLineArray[1:]
        self.pizzaList = input[1:]

    def teamsByNumber(self,numberOfMembers):
        """Get the number of teams for a certain number of members

        Args:
            numberOfMembers (int): how many members are in the team

        Returns:
            int: how many teams there are of this size
        """
        if numberOfMembers not in [2, 3, 4]:
            print("Team size not allowed")
            sys.exit()
        return int(self.teamList[numberOfMembers - 2])

class OutputFile:
    def __init__(self, numberOfTeams, teamPizzaList):
        """Create an output file

        Args:
            numberOfTeams (int): number of teams that pizzas will be delivered
            teamPizzaList (list): list of the pizzas for all the teams
        """
        self.numberOfTeams = numberOfTeams
        self.teamPizzaList = teamPizzaList

    def write(self, outputFile):
        """Write the output file to the disk

        Args:
            outputFile (string): filename of the output file
        """
        output = [self.numberOfTeams] + self.teamPizzaList
        write(outputFile, output)