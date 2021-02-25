from .models import InputFile, OutputFile

class Example2021:

    @staticmethod
    def __str__():
        """Convert class name to string

        Returns:
            string: class name
        """
        return "example_2021"

    def __init__(self, strategy, inputFile):
        """Create a hashcode simulation

        Args:
            strategy (object): strategy to use for this simulation
            inputFile (string): filename of the input file
        """
        self.strategy = strategy()
        self.inputFile = InputFile(inputFile)
        self.outputFileName = inputFile.split('/')[-1]

    def run(self):
        """Run the hashcode simulation based on the current input file
        """
        numberOfTeams, pizzas = self.strategy.run(self.inputFile)
        self.outputFile = OutputFile(numberOfTeams, pizzas)
        self.outputFile.write('/'.join([Example2021.__str__(), 'output', self.outputFileName]))