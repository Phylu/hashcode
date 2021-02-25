import sys
from file_reader import read, write

class InputFile:
    def __init__(self, inputFile):
        """Create an input file

        Args:
            inputFile (string): filename of the input file including the path
        """
        input = read(inputFile)
        firstLine = input[0].split(" ")
        self.duration = int(firstLine[0])
        self.intersectionCount = int(firstLine[1])
        self.streetCount = int(firstLine[2])
        self.carCount = int(firstLine[3])
        self.pointsPerCar = int(firstLine[4])

        self.streets = map(Street, input[1:self.streetCount + 1])
        self.cars = map(Car, input[self.streetCount + 1:])

    def __str__(self):
        return "Duration: {}\nIntersections: {}\nStreets: {}\nCars: {}\nPoints: {}\n".format(self.duration, self.intersectionCount, self.streetCount, self.carCount, self.pointsPerCar)

class Street:
    def __init__(self, data):
        data = data.split(" ")
        self.start = int(data[0])
        self.end = int(data[1])
        self.name = data[2]
        self.time = int(data[3])

class Car:
    def __init__(self, data):
        data = data.split(" ")
        self.streetCount = int(data[0])
        self.streets = data[1:]

class OutputFile:
    def __init__(self, intersectionSchedule):
        """Create an output file

        Args:
            intersectionSchedule (list): schedule of intersections
        """
        self.intersectionSchedule = intersectionSchedule

    def write(self, outputFile):
        """Write the output file to the disk

        Args:
            outputFile (string): filename of the output file
        """
        
        #print(self.intersectionSchedule)

        # First line is the number of intersections that have a schedule
        output = [len(self.intersectionSchedule)]

        for intersection, streets in self.intersectionSchedule.items():
            output.append(intersection)
            output.append(len(streets))
            for street in streets:
                # Name of the Street, Schedule
                output.append(street)

        write(outputFile, output)