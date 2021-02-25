from collections import Iterable

def read(inputFile):
    """Read an input file

    Args:
        inputFile (string): name of the input file

    Returns:
        list: content of the input file
    """
    with open(inputFile) as file:
        return file.readlines()


def write(outputFile, lines):
    """Write an output file

    Args:
        outputFile (string): name of the output file
        lines (list): content of the output file
    """
    with open(outputFile, 'w') as file:
        for line in lines:
            if isinstance(line, Iterable):
                line = " ".join(map(str, line))
            file.write(str(line) + '\n')