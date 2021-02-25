from .models import InputFile, OutputFile

class Qualification2021:

    @staticmethod
    def __str__():
        """Convert class name to string

        Returns:
            string: class name
        """
        return "qualification_2021"

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

        intersectionSchedule = self.strategy.run(self.inputFile)
        self.outputFile = OutputFile(intersectionSchedule)
        self.outputFile.write('/'.join([Qualification2021.__str__(), 'output', self.outputFileName]))